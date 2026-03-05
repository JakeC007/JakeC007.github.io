---
layout: post
title: openai command not found
subtitle: Notes from the front
tags: [how-to, code, UNIX nonsense]
---



## `openai ` command not found

I have been working on fine tuning GPT3 for a research project recently. Things have been going smoothly until I opened up my terminal today and tried to finetune a new model with the standard `openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL> `. I got the following error message 



> $ openai: command not found



This proved to be very strange since I was fine tuning and testing models without a hitch for a few weeks now. 

A quick check with pip (`pip3 show openai`) indicated that the package was still there so I figured that this was likely a path issue. 



### Trying To Fix The Path

I tried adding both the utils location and local bin location of the openai package to my terminal path 



> \$ PATH=<NEWPATH>:$PATH



And then checking that the path was correctly modified 



> \$ echo $PATH



The path was correctly modified, but I still got the same error of c*ommand not found*. 



### Getting `openai` To Run Again

After poking around a bit more I found that if I ran `./openai`  in the local bin folder it would execute. e.g.,



> ~/.local/bin$ ./openai 



This was a big relief because I could finetune my model, However, I found navigating to the `~.\local\bin` directory cumbersome. I missed being able to just use `openai` without any extra steps. I figured that a quick use of `alias ` would solve my issue and I could all `openai` again from any directory. 



> \$ alias openai=~/.local/bin/openai



And I was right! 



### The Fix

To fix this permanently, I needed to edit my shell's config file. Note if you aren't using Bash, below are the location of other common shells:

- Zsh shell: `~/.zshrc`

- Fish shell: `~/.config/fish/config.fish`

Just swap `~/.bashrc` with what is applicable for you.



I opened my shell's config file:

> \$ sudo nano ~/.bashrc



and added the following code 

```cmake
#Custom aliases
alias openai='~/.local/bin/openai'
```



Back in the terminal, I loaded my new settings into my current terminal. (Note: the new alias would have automatically loaded the next time I opened the terminal).



> \$ source ~/.bashrc



Confirmed that I had correctly added the alias.



> \$ alias



And the output confirmed that I was good to go! Since then, I have had no issues.



### TLDR 

If you are getting an error message in your terminal that says *openai: command not found* AND you have confirmed that 

- you are in the correct venv (if applicable) 
- openai is installed via `pip3 show openai`

Then the following fix may work for you:

1. Find where the openai program is stored 
   1. It is likely `~.\local\bin`
   2. If it isn't there try triggering a delete in pip via `pip uninstall openai`
      1. Before you delete it will list all of the locations that openai exists. This is how you can quickly find where the openai program exists outside of the scripts/utils folder in `~/.../Python3.X/.../openai`
2. Try `~/.local/bin/openai`
3. If it works, create an alias in the terminal `alias openai=~/.local/bin/openai`
4. If that works, save the alias to your shell config file see section "The Fix" for how to do that