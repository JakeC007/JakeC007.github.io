---
layout: post
title: Efficient File Monitoring and ClamAV Scanning for Your Downloads Folder
subtitle: Set Up a Daemon-ized Bash Script to Automate File Scanning and Ensure Real-Time Protection 
tags: [how-to]
---
Keep your downloads folder safe (on your unix machine)!

I developed a Bash script  that automatically monitors my Downloads folder, updates ClamAV, and scans any new or modified files. This setup is great for ensuring that potentially harmful files are detected before I interact with them. The script can then be set up in the background as a chronjob or as a daemon.

Here’s a quick guide on how I wrote this script, how it works, and how you can set it up on your own system to keep your Downloads folder safe.


### Overview of the Script

The script is designed to:

1. **Monitor a designated folder** (in my case, the Downloads folder) for changes.
2. **Update `ClamAV`** to the latest virus definitions.
3. **Scan the folder** for any malicious files whenever changes are detected.
4. **Generate a report** of any issues or threats detected during the scan.

This automated process means that I don’t have to manually scan files or worry about accidentally opening a malicious one.


### Prerequisites

Before you set up the script, you'll need to ensure that a few essential packages are installed on your system. These include:

- `ClamAV`: The antivirus software to detect malware.
- `inotify-tools`: A set of command-line tools that monitor changes to files and directories.
  

To install these packages, you can run the following commands (assuming you're using a Debian-based system):

```bash
sudo apt update
sudo apt install clamav clamav-daemon inotify-tools
```


### The Script

Here’s the core of the script that monitors the Downloads folder, updates ClamAV, and scans for threats:

```bash
#!/bin/bash

# Configuration
WATCH_DIR="/path/to/your/folder"
LOG_FILE="/var/log/clamav_scan.log"
REPORT_FILE="/var/log/clamav_report.log"

# Function to run ClamAV scan (orginal)
#run_clamscan() {
#    echo "$(date): Running ClamAV scan..." | tee -a "$LOG_FILE"
#    clamscan -r --bell --log="$REPORT_FILE" "$WATCH_DIR"
#}

# Function to run ClamAV scan
run_clamscan() {
    echo "$(date): Running ClamAV scan..." | tee -a "$LOG_FILE"

    # Run clamscan and capture the output
    SCAN_OUTPUT=$(clamscan -r --bell --log="$REPORT_FILE" "$WATCH_DIR")

    # Check if any infected files are found
    if echo "$SCAN_OUTPUT" | grep -q "Infected files: 0"; then
        echo "$(date): No infected files found." | tee -a "$LOG_FILE"
    else
        # If infected files found, log the scan result to the report file
        echo "$SCAN_OUTPUT" >> "$REPORT_FILE"
        echo "$(date): Infected files detected! Check the report for details." | tee -a "$LOG_FILE"
    fi
}

# Function to update ClamAV database
update_clamav() {
    echo "$(date): Updating ClamAV database..." | tee -a "$LOG_FILE"
    freshclam
}

# Monitoring function
monitor_changes() {
    echo "$(date): Monitoring $WATCH_DIR for changes..." | tee -a "$LOG_FILE"
    inotifywait -m -r -e modify,create,delete "$WATCH_DIR" | while read -r path action file; do
        echo "$(date): Change detected in $path$file ($action)" | tee -a "$LOG_FILE"
        update_clamav
        run_clamscan
    done
}

# Run the monitoring function in the background
monitor_changes &
```

### How to Set It Up

#### 1. Modify the Script

- **Set the directory to monitor**: Change the `WATCH_DIR` variable to point to your Downloads folder. For example:
  
  ```bash
  WATCH_DIR="/home/yourusername/Downloads"
  ```

#### 2. Make the Script Executable

Once the script is ready, you'll need to make it executable. Open a terminal and navigate to the folder containing the script, then run:

```bash
chmod +x your_script.sh
```

#### 3. Run It Manually (Optional)

If you'd like to run the script manually before setting it up as a daemon or cron job, you can simply execute it from the terminal:

```bash
./your_script.sh
```

### Running the Script Automatically

You have two options to run the script automatically:

#### Option 1: Set it up as a **Cron Job**

A cron job is ideal if you want the script to run periodically. For instance, you could set it to run every 5 minutes.

1. Open the crontab configuration by typing:

   ```bash
   crontab -e
   ```

2. Add the following line to run the script every 5 minutes:

   ```
   */5 * * * * /path/to/your_script.sh
   ```

3. Save and close the file. The cron job will now automatically execute the script every 5 minutes.

#### Option 2: Set it up as a **`Systemd` Service**

A `systemd` service can run the script as a background service (daemon), ensuring it continuously monitors the Downloads folder for changes.

1. **Create a systemd service file**:  
   Create a file named `/etc/systemd/system/clamav_monitor.service` and add the following content:

   ```ini
   [Unit]
   Description=ClamAV Folder Monitor
   After=network.target
   
   [Service]
   ExecStart=/path/to/your_script.sh
   Restart=always
   User=root
   
   [Install]
   WantedBy=multi-user.target
   ```

2. **Reload systemd**:  
   After creating the service file, reload the systemd configuration to apply the new service.

   ```bash
   sudo systemctl daemon-reload
   ```

3. **Enable and start the service**:  
   Enable the service so it starts on boot and start it immediately.

   ```bash
   sudo systemctl enable clamav_monitor
   sudo systemctl start clamav_monitor
   ```

4. **Check the service status**:  
   To make sure everything is working, check the status of the service:

   ```bash
   sudo systemctl status clamav_monitor
   ```



