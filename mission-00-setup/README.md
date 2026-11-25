# Mission 0 - Create your GitHub workspace

## 1. Task / objective
Make a public GitHub repository with the correct name and set up a folder for every mission, plus a root README.

## 2. Work completed
- Chose the repo name `digital-detective-8483` (assignment name + last 4 digits of my USN).
- Made a local folder with the same name.
- Created the mission folders (mission-00 to mission-08), a README.md in each one, an `evidence` folder, and an empty `number_converter.py` in mission-05.
- Wrote the root README with the mission index.
- Created a public repo on GitHub with the same name and connected my local folder to it.

## 3. Commands / tools used
- `git --version` and `python3 --version` - to check both tools are installed.
- `mkdir` - to create the folders.
- `touch` - to create the empty files.
- `git init` - to turn the folder into a git repository.
- `git remote add origin <url>` - to link the local folder to the GitHub repo.
- GitHub website - to create the repository.

**Tool versions:** Git 2.54.0, Python 3.10.18.

## 4. My understanding
A repository is a folder that git keeps track of, so every change is saved and I can go back to an older version. I organised the work by mission so each part is separate and easy to find. The remote called `origin` is just the GitHub copy of my folder. The names of the local folder and the GitHub repo should match so nothing gets confusing.

## 5. Difficulties faced
The GitHub command line tool (`gh`) is not installed on my computer, so I could not create the repo from the Terminal. I also was not completely sure about the exact repo name because the assignment only gave an example.

## 6. How I resolved them
I created the repo through the GitHub website instead, which worked fine. For the name I followed the format in the example (`digital-detective-` plus my last four USN digits).

## 7. Evidence / files
- `README.md` in the root folder
- Folders for all missions, each with a README.md
- `evidence/` folder (empty for now)

## 8. Commit details
Commit message: "Set up Digital Detective mission structure"
Pushed to GitHub and checked that the files show up there.
