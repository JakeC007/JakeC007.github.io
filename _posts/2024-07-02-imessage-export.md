---
layout: post
title: How I Got Message-Book To Work
subtitle: A Guide For Tech Novices
tags: [how-to]
---
Below are the steps I took to get MacOS ready to run `message-book` -- bkettle's excellent iMessage --> PDF book program. 

I was running this whole thing on someone else's Mac who does not code so I had no preinstalled programs to rely upon. Since I had to work from a clean install, I thought the steps I took may be helpful for people with less coding experience. 

**NB:** If you see `$` in a command to type in that just indicates that this is a command for the terminal and you should not type it.

## 1. Get Rust
1. Hit `cmd + spacebar` to open Spotlight Search.
2. Type in "Terminal" and press `Enter` to open the Terminal application.
3. Copy and paste the following command into the terminal, then press `Enter`: 
   ```sh
   $ curl https://sh.rustup.rs -sSf | sh
   ```
4. Close the terminal window after the installation completes.

## 2. Get the iMessage-exporter Tool
1. Open the terminal again by repeating steps 1 and 2 from the "Get Rust" section.
2. Copy and paste the following command into the terminal, then press `Enter`:
   ```sh
   $ cargo install imessage-exporter
   ```
3. If prompted to install command line developer tools, click "Install".
4. After the installation completes, rerun the same command from step 2 to ensure everything is set up correctly:
   ```sh
   $ cargo install imessage-exporter
   ```

## 3. Grant Full Disk Access to Terminal
1. Open "System Settings" by clicking the Apple logo in the top-left corner of the screen and selecting "System Settings".
2. Go to "Privacy & Security".
3. Find "Full Disk Access" and click on it.
4. Toggle the switch next to "Terminal" to "on".
5. Quit the terminal and then reopen it for the changes to take effect.

## 4. Copy the Chat Database
To get your iMessage data, you need to copy the chat database file from its location.
1. Open the terminal.
2. Copy and paste the following command into the terminal, then press `Enter` to make a copy of your chat database:
   ```sh
   $ cp ~/Library/Messages/chat.db ~/path/to/your/backup_folder
   ```
   Make sure to replace `~/path/to/your/backup_folder` with the actual path to the folder where you want to save the backup.

## 5. Set Up the Message-book Program
1. Download the repository from [this link](https://github.com/bkettle/message-book).
2. Open the terminal and navigate to the root of the downloaded repository. Use the `cd` command to change directories, for example:
   ```sh
   $ cd ~/Downloads/message-book
   ```
3. Once in the correct directory, run the following command to see the help options:
   ```sh
   $ cargo run -- --help
   ```

## 6. Run the Program
The program instructions say that the way to run the file is:
> Usage: message-book [OPTIONS] <RECIPIENT>

This means you need to put your options first and then the phone number of the recipient at the end without any flags before it. Here is an example of how to run the program:
```sh
$ cargo run -- -o '~/path/to/output_dir' -c '~/path/to/folder_with_copy/chat.db' '+13125551234'
```
Replace `~/path/to/output_dir` with the path to your output directory, `~/path/to/folder_with_copy/chat.db` with the path to your chat database copy, and `+13125551234` with the recipient's phone number.

If you encounter permission issues accessing `chat.db`, you can run the command as a `sudo` command (which gives it higher privileges):
```sh
$ sudo cargo run -- -o '~/path/to/output_dir' -c 'path/to/folder_with_copy/chat.db' '+13125551234'
```

## Get LaTeX to Compile
After running the program, your `output_dir` should contain many files, mostly ending with `.tex` and one called `Makefile`.

If you haven't installed LaTeX yet, download it from [this link](https://www.latex-project.org/get/).

### How to Compile the LaTeX Files
1. Open the terminal and navigate to your `output_dir` folder using the `cd` command.
2. Run the following command to compile the LaTeX files:
   ```sh
   $ make
   ```
3. Once the compilation is complete, you should have a PDF file that you can view and enjoy.
