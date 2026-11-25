# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
Use the command line to look around folders, make and manage practice files, understand flags and pipes, and explain what a package manager does.

## 2. Work completed
- Ran the basic commands inside my assignment repo and noted what each one did.
- Made a folder called `terminal-practice` inside this mission folder and did all the file practice only there.
- Made a text file, added a second line without removing the first, made a backup copy and renamed it.
- Compared `ls` with `ls -lah` and tried a pipe.
- Checked Homebrew (version and package list) without installing or removing anything.

### Task 2.1 - Basic Terminal operations

| Operation / command | What it does | What I observed |
|---|---|---|
| `pwd` | Shows the full path of the folder I am in | It printed the whole path ending in `digital-detective-8483` |
| `ls` | Lists files and folders in the current place | It showed README.md, evidence and all the mission folders |
| `ls -l` | Lists them in a detailed (long) format | Each line had permissions, owner, size, date and name. The folders start with `d` |
| `cd mission-02-terminal` then `cd ..` | Changes directory. `..` means the parent folder | `pwd` showed the path get longer with `cd mission-02-terminal` and shorter again after `cd ..` |
| `mkdir terminal-practice` | Creates a new folder | No message, but `pwd` and `ls` later showed the folder exists |
| `touch notes.txt` | Creates an empty file | Nothing printed, and the file was listed with size 0 |
| `cp notes.txt notes-copy.txt` | Copies a file under a different name | Now two files existed, `notes.txt` and `notes-copy.txt` |
| `mv notes-copy.txt notes-renamed.txt` | Moves or renames a file | The name `notes-copy.txt` disappeared and `notes-renamed.txt` showed up |
| `cat notes.txt` | Shows the contents of a file | It printed `hello from my first file` |

### Task 2.2 - Practising file changes safely
Inside `terminal-practice` I wrote one line into `notes.txt` and then added a second line, and `cat` showed both lines:

```
hello from my first file
line two, added at the end
```

Then I made a backup copy with `cp notes.txt notes-backup.txt` and renamed it with `mv notes-backup.txt notes-backup-old.txt`.

Answers:
- **Replacing vs adding to the end:** `>` replaces everything in the file with the new text, while `>>` keeps what is already there and adds the new text at the end. I used `>>` for the second line so the first line stayed.
- **Copying vs moving:** copying makes a second file and the original stays. Moving takes the file from one name or place to another, so the old name no longer exists.
- **What `pwd` gives:** it tells me exactly which folder I am working in, with the full path. That helps me not to create or delete files in the wrong place.
- **Why `ls` is useful:** it shows what is in the folder, so I can check a file was really created, renamed or copied.

### Task 2.3 - Flags and pipes
Normal `ls` only showed the three file names. `ls -lah` showed much more:

```
drwxr-xr-x@ 5 [redacted]  staff   160B Nov 25 13:15 .
drwxr-xr-x@ 4 [redacted]  staff   128B Nov 25 13:15 ..
-rw-r--r--@ 1 [redacted]  staff    52B Nov 25 13:15 notes-backup-old.txt
-rw-r--r--@ 1 [redacted]  staff     0B Nov 25 13:15 notes-renamed.txt
-rw-r--r--@ 1 [redacted]  staff    52B Nov 25 13:15 notes.txt
```

What the flags changed: `-l` gives the long, detailed format, `-a` also shows hidden items (the `.` and `..` entries appeared), and `-h` writes sizes in a human-readable way like `52B` instead of just numbers.

For the pipe I ran `ls -l | head -n 3`. The pipe `|` takes the output of the command on its left and sends it as the input of the command on its right. Here `ls -l` made the detailed listing and `head -n 3` only showed the first three lines of it.

### Task 2.4 - Package managers
Homebrew is already installed on my Mac. `brew --version` showed Homebrew 7.0.9 and `brew list` shows the packages it manages. I counted them with `brew list | wc -l` and got 216. I did not install or uninstall anything.

A package manager is useful because it installs, updates and removes software with one command, and it also takes care of the other software that program needs. Without it I would have to download each program and its parts by hand and keep track of the versions myself.

## 3. Commands / tools used
- `pwd` - show the current folder path
- `ls`, `ls -l`, `ls -lah` - list files (simple, detailed, detailed with hidden files and readable sizes)
- `cd` - change folder
- `mkdir` - make a folder
- `touch` - make an empty file
- `cp` - copy a file
- `mv` - move or rename a file
- `cat` - show a file's contents
- `echo` with `>` and `>>` - write text into a file (replace / add at the end)
- `head -n 3` and the pipe `|` - show only the first lines of another command's output
- `brew --version`, `brew list`, `wc -l` - check Homebrew and count its packages

## 4. My understanding
The Terminal lets me do the same things I do in Finder but by typing, and it is more exact because I can see the path and the result of each command. Most commands do not print anything when they work, so I had to check with `ls` or `cat` to be sure. Flags change how a command behaves, like `-l` and `-a` for `ls`. A pipe lets me join small commands together so the output of one becomes the input of the next. Package managers like Homebrew save time because they handle installing and updating for me.

## 5. Difficulties faced
- Commands like `mkdir`, `touch` and `cp` showed nothing on the screen, so at first it was not clear if they worked.
- The task list does not include a command to put text inside a file, so I had to find out how to write text from the Terminal.
- In the `ls -l` output there was an `@` after the permission letters which I did not expect.
- My renamed copy (`notes-renamed.txt`) turned out to be 0 bytes, not the same as `notes.txt`.

## 6. How I resolved them
- I used `ls` and `cat` after each command to see the result instead of expecting a message.
- I used `echo "text" > file` for the first line and `echo "text" >> file` for the second line. I was careful with `>` because it would replace the file's contents.
- I understood the `@` is a marker that the file has extra attributes attached, and it does not change the basic read and write permissions.
- The 0 bytes made sense when I thought about the order: I made that copy right after `touch`, when `notes.txt` was still empty, and I only wrote text into `notes.txt` after that. A copy only has what the file had at the time it was copied.

## 7. Evidence / files
- `terminal-practice/` folder with `notes.txt`, `notes-renamed.txt` and `notes-backup-old.txt`
- Command outputs shown above (my username was replaced with [redacted])

## 8. Commit details
Commit message: "Complete Terminal and file management mission"
Pushed to GitHub and checked that the files show up there.
