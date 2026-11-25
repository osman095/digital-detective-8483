# Mission 3 - Understand the operating system

## 1. Task / objective
Find out about my operating system, look at running processes, understand paths and file permissions, and explain what an operating system is responsible for.

## 2. Work completed
- Used Terminal to check my OS details, my account, my storage and a snapshot of system activity.
- Looked at the process list and found the PID column and some example processes.
- Gave an absolute and a relative path example from my assignment folder and read the permissions of a practice file.
- Filled in the table of OS responsibilities in my own words.

### Task 3.1 - Explore my operating system
Usernames and the device name are replaced with [redacted].

| Information explored | What it tells me | My observation (privacy-safe) |
|---|---|---|
| OS / system details (`uname -a`, `sw_vers`) | Which OS and version I am using and what kind of processor | macOS 27.2.1, Darwin kernel 27.2.0, `arm64` (so an Apple chip, not Intel) |
| Current account (`whoami`) | Which user account is running the commands | It printed my account name: [redacted] |
| Available and used storage (`df -h /`) | How big the disk is and how much is used or free | Size 460Gi, used 13Gi, available 228Gi, capacity 6% |
| System activity snapshot (`top -l 1 -n 0`) | How many processes are running and how busy the CPU and memory are | 595 processes in total, only 2 running and 593 sleeping. CPU about 84% idle. Memory showed 15G used |

### Task 3.2 - Understand processes
I used Terminal (`ps -eo pid,comm`) to see the process list. A few lines looked like this:

```
  PID COMM
    1 /sbin/launchd
  532 /usr/libexec/logd
  535 /usr/libexec/UserEventAgent
```

- **What is a process?** A process is a program that is currently running. When I open an app, the OS starts a process for it and gives it memory and CPU time.
- **What does the PID column represent?** PID is the process identifier, a unique number the OS gives to each running process so it can keep track of it and I can refer to it.
- **Two examples running on my computer:** `launchd` (PID 1, the first process that starts the others) and `Finder` (PID 1682, the app for browsing files). `logd` is also running in the background, which writes system logs.

### Task 3.3 - Paths and permissions
Absolute vs relative path:
- **Absolute path:** starts from the root `/` and gives the full location. Mine: `/Users/[redacted]/Documents/diwali hw/digital-detective-8483/mission-02-terminal/terminal-practice/notes.txt`
- **Relative path:** starts from the folder I am currently in. From my assignment folder: `mission-02-terminal/terminal-practice/notes.txt`

When I moved between folders with `cd`, the path shown by `pwd` changed each time to match where I was.

Permissions of a practice file (`ls -l` on `notes.txt`):

```
-rw-r--r--@ 1 [redacted]  staff  52 Nov 25 13:15 notes.txt
```

The first part `-rw-r--r--` shows the permissions. For the owner it is `rw-`, so the owner can read and write the file but cannot execute it. The group and everyone else have `r--`, so they can only read it. I did not change any permissions.

### Task 3.4 - OS responsibilities

| OS responsibility | My explanation | Example |
|---|---|---|
| Process management | Decides which programs run, when and for how long, and starts and stops them | Running Slack and Terminal at the same time and switching between them |
| Memory management | Gives each program some RAM and takes it back when the program closes | Closing an app frees its memory for other programs |
| Device management | Controls the hardware like the keyboard, screen and disk through drivers | Typing on the keyboard makes letters show on the screen |
| File management | Organises how files and folders are stored, named, found and protected | Saving a file in Documents and finding it again later |
| User interface / shell | The way I talk to the computer, either by clicking (GUI) or typing (shell) | Finder for clicking and Terminal for typing commands |
| Security and permissions | Controls who can read, write or run files and stops programs from interfering | The `rw-` / `r--` permissions on my file |

## 3. Commands / tools used
- `uname -a` - show the system and kernel details
- `sw_vers` - show the macOS version
- `whoami` - show the current account
- `df -h /` - show disk size, used and free space in readable units
- `top -l 1 -n 0` - take one snapshot of system activity
- `ps -eo pid,comm` - list running processes with their PIDs
- `grep` - pick certain lines out of the process list
- `pwd` and `ls -l` - show my location and the file's permissions

## 4. My understanding
The operating system sits between the hardware and the programs I use and manages everything for them: running programs, giving memory, controlling devices, organising files and keeping things secure. Each running program is a process with its own PID. Paths tell the computer where a file is, either from the very top (absolute) or from where I am (relative). The permission letters show who is allowed to read, write or run a file. I also noticed that most of the 595 processes were sleeping, so the computer is not working hard on all of them at once.

## 5. Difficulties faced
- The task said to open a browser or text editor and view the process list, but I did it in Terminal, so I was not sure if this was fine.
- The process list was really long and hard to read, and the names were long paths.
- My folder name `diwali hw` has a space in it, so paths with it needed quotes.
- The `top` snapshot showed 15G memory used and almost nothing unused, which looked like the computer was out of memory.

## 6. How I resolved them
- I used `ps` in Terminal, which still shows the process list with the PID column, and used `head` and `grep` to show only a few lines.
- I cut the output down so only a few processes are shown, and I replaced my username with [redacted].
- I put the path in quotes whenever it contained `diwali hw`.
- I read that the OS keeps spare memory busy (for example for caching and compressing), so low "unused" memory is normal and not a problem on its own.

## 7. Evidence / files
- Command outputs shown above (username and device name replaced with [redacted])
- `mission-02-terminal/terminal-practice/notes.txt` used for the permission example

## 8. Commit details
Commit message: "Document operating system and file management"
Pushed to GitHub and checked that the file shows up there.
