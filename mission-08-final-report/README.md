# Mission 8 - Final report and submission

## 1. Task / objective
Review the whole repository, make the root README useful for someone visiting for the first time, check that every mission was committed and pushed, and submit the repository link.

## 2. Work completed
- Went through the repository and compared it with the required structure.
- Updated the root README (topics explored, how to run the number converter, what I learned).
- Checked every mission README against the required format and the final checklist.
- Searched the files for private details to make sure nothing personal was published.

### Repository structure check
All the required paths are present:

| Required path | Present? |
|---|---|
| `README.md` | Yes |
| `mission-00-setup/README.md` | Yes |
| `mission-01-computer-basics/README.md` | Yes |
| `mission-02-terminal/README.md` | Yes (with the `terminal-practice/` files) |
| `mission-03-operating-system/README.md` | Yes |
| `mission-04-programs/README.md` + `hello.py` | Yes |
| `mission-05-numbers-data/README.md` + `number_converter.py` | Yes |
| `mission-06-git-github/README.md` | Yes |
| `mission-07-networking/README.md` | Yes |
| `mission-08-final-report/README.md` | Yes (this file) |
| `evidence/` | Yes (empty, I kept the command outputs inside each mission README instead) |

### Status of each mission

| Mission | Status | Commit message |
|---|---|---|
| 0 | Done | Set up Digital Detective mission structure |
| 1 | Done | Complete computer basics and IPOS mission (plus a later fix: Add difficulties and resolutions to Mission 1 README) |
| 2 | Done | Complete Terminal and file management mission |
| 3 | Done | Document operating system and file management |
| 4 | Done | Compare compilers and interpreters |
| 5 | Done | Build number converter and practise data representation |
| 6 | Done. Pull Request #1 is open and not merged | Complete Git and GitHub collaboration mission |
| 7 | Done | Explain networking concepts and website communication |
| 8 | Done | Complete final report and verify assignment submission |

### Corrections made
- After committing Mission 1, I saw the difficulties section was too short, so I fixed it in a second commit.
- I made sure the Mission 6 files were committed on `main` and not on the `update-about` branch.
- I searched the files for personal details. The only path in the repository is in Mission 3 and my username there is replaced with `[redacted]`.

### Final verification
- The converter was tested again with 7, 42 and 300 and printed correct binary and hex values (111 / 0x7, 101010 / 0x2a and 100101100 / 0x12c).
- I checked that every mission README follows the required format with the same headings.

### Final checklist
- [x] All mission folders are present and each has its own README.md.
- [x] Every mission README records the task, commands/tools used, understanding and difficulties.
- [x] Every mission has its own meaningful commit and all of them are pushed.
- [x] IPOS, hardware, software and computer-system examples are included.
- [x] Terminal operations, file management, flags and pipes are explained.
- [x] Operating system, processes, paths, storage and permissions are covered.
- [x] Compiler and interpreter are compared.
- [x] Number conversions include working and Python verification.
- [x] `number_converter.py` runs successfully with at least three test values.
- [x] Git commit history, branch and Pull Request activity are visible.
- [x] LAN, MAN, WAN, DNS, router, protocols and client-server are explained.
- [x] The root README explains the project and how to run the converter.
- [x] Personal information has been removed from outputs.
- [x] All final changes are committed and pushed to GitHub.

## 3. Commands / tools used
- `git ls-files` - list every file Git is tracking, to check the structure
- `git grep` - search the tracked files for private details
- `git log` - check the commit history
- `python3 number_converter.py` - test the converter again
- GitHub website - check that the repository is public and the files are visible

## 4. My understanding
Going through the whole repository showed me how the missions connect: the Terminal and file work from Mission 2 is what I used to look at the operating system in Mission 3, the Python from Missions 4 and 5 ran in the same Terminal, and Git and GitHub from Missions 0 and 6 kept all of it saved with a history. The commit history shows the order I worked in, and each commit matches one mission.

## 5. Difficulties faced
- After switching branches for the Pull Request, my root `README.md` still showed the "My Learning" change on `main`, even though that change was meant to stay on the `update-about` branch.
- It was hard to be sure that no private detail had been published, because many commands print my username and paths.
- Pull Request #1 is still open, so my local `main` does not have the My Learning section.

## 6. How I resolved them
- I checked `git status` and `git branch` before every commit and only added the files for the mission I was committing, so the extra change did not get committed with the wrong mission.
- I searched all tracked files with `git grep` for my username, paths and network details and replaced them with `[redacted]` where needed.
- I decided to leave the Pull Request open, because merging is only needed if the instructor asks for it.

## 7. Evidence / files
- The repository: https://github.com/osman095/digital-detective-8483
- All mission READMEs, `hello.py`, `number_converter.py` and the `terminal-practice` files
- Pull Request #1 (open) on GitHub

## 8. Commit details
Commit message: "Complete final report and verify assignment submission"
Pushed to GitHub and checked that the file shows up there.
