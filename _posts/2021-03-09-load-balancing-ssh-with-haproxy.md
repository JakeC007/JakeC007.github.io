---
layout: post
title: Load-Balancing ssh with HAProxy
---

One of the many things I did last (2020) summer was set up a up [HAProxy](https://cbonte.github.io/HAProxy-dconv/2.2/intro.html#1) as a load-balancer for my CS department's incoming ssh connections. I completed this project with my CS Department's wonderful Sysadmin [Jeff Knerr](https://jeffknerr.github.io/). This page is a modified mirror of Jeff's page that describes our setup.



### Some Background

The Swarthmore CS department maintains our own servers (*i.e.,* dns, web, email, ldap, etc) and lab computers. Spread out over the various labs on campus we manage a touch over 100 lab computers--all of which that run linux. 

To access the lab computers remotely, students ssh in. This is an especially popular feature for students who either (1) aren't on campus or (2) want to work from elsewhere on campus. The former now especially relevant as our institution had eliminated in person computer lab access as a response to the pandemic.  

To make this easy for students, we one name (e.g., *lab.myschool.edu*) that students could ssh to, which would load-balance the ssh connections across our various lab computers. Additionally, if any computers happen to reboot or be down, we wanted them automatically (and quickly) removed from the load-balancing rotation, and put back into the rotation when they were up again.

### Our Setup

- One server (we use debian) runs HAProxy (v1.8.19) and has the hostname you want the students to use when connecting (e.g., `ssh lab.myschool.edu`)
- Nobody actually logs in to the HAProxy server except admins, so you don’t need to set up student accounts on the HAProxy server
- Set up HAProxy to bind to port 22 (see the `listen ssh` part of the config file below)
- Also set up sshd on the HAProxy server to run on a different port (we use `Port 9000` in `/etc/ssh/sshd_config`) so your admins can still get to it (`ssh -p 9000 lab.myschool.edu`)
- Set up the **same ssh host keys for all of the lab computers** you want in the load-balancing rotation, otherwise your users will get WARNING SSH HOST KEY CHANGED messages each time they get sent to a different computer
- You probably want to put all of these ssh host pub keys in a `/etc/ssh/ssh_known_hosts2` file, and distribute it to all of your lab computers

For example, here’s a simplified section of our `ssh_known_hosts2` file (with fake names and IP addresses), only showing one of the key types (ed25519) for each host:

```bash
lab,lab.myschool.edu,1.2.3.1 ssh-ed25519 AAAAO3Nzaer56DI1NTE5AAAAIJfPzJHRiiiwhrGposISykHMLvpcowKnjRbUxb028Klx root@hostA
hostA,hostA.myschool.edu,1.2.3.10 ssh-ed25519 AAAAO3Nzaer56DI1NTE5AAAAIJfPzJHRiiiwhrGposISykHMLvpcowKnjRbUxb028Klx root@hostA
hostB,hostB.myschool.edu,1.2.3.11 ssh-ed25519 AAAAO3Nzaer56DI1NTE5AAAAIJfPzJHRiiiwhrGposISykHMLvpcowKnjRbUxb028Klx root@hostA
hostC,hostC.myschool.edu,1.2.3.12 ssh-ed25519 AAAAO3Nzaer56DI1NTE5AAAAIJfPzJHRiiiwhrGposISykHMLvpcowKnjRbUxb028Klx root@hostA
```



So each lab computer (hostA, hostB, hostC) has the same `ssh_host_ed25519_key` and `ssh_host_ed25519_key.pub` files (in `/etc/ssh`). Do the same for any other host key types you use (rsa, ecdsa, etc). If a student ssh’s to any of those hosts, with any name or number (hostA, hostB.myschool.edu, 1.2.3.12), they should see the same ssh host key.

And here’s a simplified version of our `/etc/haproxy/haproxy.cfg` file (from a server running Debian 10 (Buster)):

```bash
global
	log /dev/log	local0
	log /dev/log	local1 notice
	chroot /var/lib/HAProxy
	stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
	stats timeout 30m
	maxconn 2500
	user HAProxy
	group HAProxy
	daemon

defaults
	log	global
	mode	tcp
	timeout connect 10s
	timeout client 36h
	timeout server 36h
	option	dontlognull
	errorfile 400 /etc/haproxy/errors/400.http
	errorfile 403 /etc/haproxy/errors/403.http
	errorfile 408 /etc/haproxy/errors/408.http
	errorfile 500 /etc/haproxy/errors/500.http
	errorfile 502 /etc/haproxy/errors/502.http
	errorfile 503 /etc/haproxy/errors/503.http
	errorfile 504 /etc/haproxy/errors/504.http

listen ssh 
	bind *:22
	balance leastconn
	mode tcp
        
	option tcp-check	
	tcp-check expect rstring SSH-2.0-OpenSSH.*
		
	server hostA  1.2.3.10:22 check inter 10s fall 2 rise 1
	server hostB  1.2.3.11:22 check inter 10s fall 2 rise 1
	server hostC  1.2.3.12:22 check inter 10s fall 2 rise 1
# lots more hosts here (we currently have 42 hosts in here)

listen stats
	mode http
	maxconn 15
	bind *:443 ssl crt /etc/letsencrypt/live/lab.myschool.edu/haproxy.pem
	stats enable
	stats show-node
	stats uri /stats
	stats refresh 10s
	stats auth adminname:adminpassword
	stats hide-version
```



Some things to note in the above config:

* We set the timeouts to 36 hours, since students sometimes set up long-running (overnight) jobs, and we figured they would check back in on them after 12-24 hours
* For each server line, the `check inter 10s fall 2 rise 1` part controls how HAProxy checks (every 10 sec) for offline (2 failed checks) and online (1 successful check) hosts
* The `tcp-check` line means it is looking for a string that starts with SSH-2.0-OpenSSH when checking if the ssh service is up on each host. Try `telnet hostname 22` to see what your sshd prints.
* Not shown here, we also use [zabbix](https://www.zabbix.com/) (`system.run[netstat -a -n | grep ESTABLISHED | wc -l]`) and [grafana](https://grafana.com/) to make a pretty dashboard showing connections to HAProxy vs time, so we can see how the service is used during the week



### The Results

Two semesters in and the load balancing server is doing great. Students have used the service continuously, with sometimes close to 150 current connections distributed over 40 computers! (That's a lot for our tiny CS department).

I setup the HAProxy server (at the behest of Jeff) to replace a round-robin DNS that was trying to load-balance across 10 machines. That worked, but was the number of hosts we could use was too few. Moreover, it was slow to respond to unreachable hosts (we had to notice the host was down, then change the dns records to remove the host, then worry about cached dns data). 



### Should You Adopt This Set Up?

Maybe. Here is a list of pros and cons that we assembled:

| Pro                                                          | Con                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Single hostname for students to remember (`lab.myschool.edu`) | One single point of failure if our HAProxy server goes down (but students can still ssh directly to any lab computer) |
| Hosts quickly and automatically taken out of the rotation if offline, added back when online | All computers need to have the same ssh host keys (not too hard if you already manage them with ansible) |
| ssh load-sharing across 40+ computers                        |                                                              |
| Easy to monitor (see stats example below)                    |                                                              |



### Helpful Guides and Documentation

There were several crucial documents that we followed to get this up and running. First and foremost was the [HAProxy documentation](https://cbonte.github.io/HAProxy-dconv/2.2/intro.html#1). We also consulted [Eugene Petrenko’s blog post on Load Balancing SSH](https://jonnyzzz.com/blog/2017/05/24/ssh-HAProxy/) and [Evan Carmi’s blog post on Setup HAProxy stats over HTTPS](https://evancarmi.com/writing/setup-HAProxy-stats-over-https/). 