# Mission 6 - Git and GitHub

## 1. Task / objective
Understand version control, stage and commit changes, make a branch, open a Pull Request and explain how collaboration works with Git and GitHub.

## 2. Work completed
- Used `git status`, `git add`, `git commit` and `git log` on my project and wrote down what each one does.
- Made a branch called `update-about`, added a "My Learning" section to the root README, committed it and pushed the branch to GitHub.
- Opened Pull Request #1 from `update-about` into `main` on GitHub and looked at the changed file.
- Wrote a glossary of Git commands in my own words.

### Task 6.1 - Basic Git workflow

| Git operation | What it does in my own words |
|---|---|
| Check repository status (`git status`) | Shows which files I changed, which ones are ready to be committed and which branch I am on |
| Stage selected changes (`git add README.md`) | Picks the files whose changes I want to include in the next commit |
| Create a commit (`git commit -m "..."`) | Saves a snapshot of the staged changes in the history with a message |
| View commit history (`git log --oneline`) | Lists the earlier commits with their short ID, time and message |

Real output from my work on the branch:

```
$ git status
 M README.md

$ git add README.md
$ git status --short
M  README.md

$ git commit
[update-about 15dd2f7] Add My Learning section to README
 1 file changed, 8 insertions(+)
```

The difference between staging and committing: staging (`git add`) only chooses what will go into the next commit, so I can pick some files and leave others out. Committing (`git commit`) actually saves that chosen set in the history. After `git add` the status changed from ` M` to `M ` which shows the change was staged but not committed yet.

### Task 6.2 - Branch
I made the branch `update-about` with `git checkout -b update-about`. On it I added a "My Learning" section to the root `README.md` with three things I learned (Terminal output and `>` vs `>>`, number systems checked with Python, and processes and permissions). Then I checked the status, staged the README, committed it as "Add My Learning section to README" (`15dd2f7`) and published the branch with `git push -u origin update-about`.

### Task 6.3 - Pull Request
- I opened my repository on GitHub and used the compare page to compare `update-about` with `main`. GitHub showed "Able to merge", 1 commit and 1 file changed (8 added lines).
- I created Pull Request **#1**, "Add My Learning section to README", from `update-about` into `main`, with the description: "Added a 'My Learning' section to the root README with three things I have learned so far from the first missions."
- I looked at the changed file in the PR: only `README.md` changed, with 8 added lines and nothing removed.
- **Status: the PR is open and NOT merged.** The assignment says to merge only if the instructor asks for it, and I was not told to merge. Because of that I did not do the last step (switching to `main` and pulling the merged changes), so my local `main` still does not have the My Learning section.

What a branch and a Pull Request are, and why they help: a branch is a separate line of work, so I can try changes without touching the main version. A Pull Request is a request to bring the changes from one branch into another, and it shows exactly what changed so others can look at it and comment before it is merged. When several people work on the same project, this keeps everyone's work separate until it has been checked, so nobody breaks the main code or overwrites someone else's changes.

### Task 6.4 - Git command glossary

| Git operation | One-line explanation |
|---|---|
| Initialise a repository (`git init`) | Turns a normal folder into a Git repository so it starts tracking changes |
| Check status (`git status`) | Shows changed, staged and untracked files and the current branch |
| Stage changes (`git add`) | Selects changes to go in the next commit |
| Commit changes (`git commit`) | Saves the staged changes as a snapshot with a message |
| View history (`git log`) | Lists the past commits |
| Create or list branches (`git branch`, `git checkout -b`) | `git branch` lists branches and `git checkout -b name` makes a new one and switches to it |
| Switch branches (`git checkout main`) | Moves my working folder to another branch |
| Publish changes (`git push`) | Uploads my commits to GitHub |
| Retrieve remote changes (`git pull`) | Downloads new commits from GitHub and brings them into my local branch |

## 3. Commands / tools used
- `git status` - see what changed
- `git add` - stage a file
- `git commit` - save a commit
- `git log --oneline` - see history
- `git checkout -b update-about` - create and switch to a new branch
- `git checkout main` - switch back to the main branch
- `git push -u origin update-about` - publish the branch
- `git remote add origin` - connect my folder to GitHub (Mission 0)
- GitHub website - to compare branches and open the Pull Request

## 4. My understanding
Git keeps the history of my work as commits, and each commit is a saved version I can go back to. The staging area lets me choose exactly what goes into a commit. Branches let me work separately from `main`, and a Pull Request is how GitHub lets changes be reviewed before they are merged. I saw that pushing a branch does not change `main` at all, which is why my local and GitHub `main` still do not have the new section until the PR is merged.

## 5. Difficulties faced
- I could not create the Pull Request at first. One browser gave an error "Validation failed: must be a collaborator", because it was signed in with a different GitHub account than my own.
- I had to be careful to switch back to `main` before writing and committing this mission, so the Mission 6 files do not end up on the `update-about` branch.
- I was not sure whether I should merge the Pull Request.

## 6. How I resolved them
- I opened the compare link in the browser where I was signed in as my own account (`osman095`) and the Pull Request was created without a problem.
- I ran `git checkout main` and checked with `git branch` that `main` was the active branch before committing.
- I re-read the assignment, which says to merge only if the instructor asks, so I left the PR open and wrote its status here.

## 7. Evidence / files
- Pull Request #1 on GitHub (`update-about` into `main`, open)
- The commit `15dd2f7` on the `update-about` branch
- Command outputs shown above

## 8. Commit details
Commit message: "Complete Git and GitHub collaboration mission"
Pushed to GitHub and checked that the file shows up there.
