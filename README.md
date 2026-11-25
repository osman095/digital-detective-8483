# The Digital Detective - Diwali Assignment

This is my Diwali independent learning assignment. The idea is to explore how my own computer works, practise the Terminal, and use Git and GitHub to upload my work. It is split into missions and I did them one by one in order.

## Mission index

- [Mission 0 - Setup](mission-00-setup/README.md)
- [Mission 1 - Computer basics and IPOS](mission-01-computer-basics/README.md)
- [Mission 2 - Terminal](mission-02-terminal/README.md)
- [Mission 3 - Operating system](mission-03-operating-system/README.md)
- [Mission 4 - How programs run](mission-04-programs/README.md)
- [Mission 5 - Numbers and data](mission-05-numbers-data/README.md)
- [Mission 6 - Git and GitHub](mission-06-git-github/README.md)
- [Mission 7 - Networking](mission-07-networking/README.md)
- [Mission 8 - Final report](mission-08-final-report/README.md)

Every mission was finished, written up and committed separately before I started the next one, so the commit history shows the order I worked in.

## Topics explored

- How a computer works: input, processing, output and storage (IPOS), hardware and software
- Terminal commands, file management, flags and pipes, and package managers
- The operating system: processes, paths, storage and file permissions
- How programs run: compiler vs interpreter, running a Python file
- Binary, decimal and hex conversions, text encoding and a small Python converter
- Git and GitHub: commits, a branch and a Pull Request
- Networks: LAN, MAN, WAN, DNS, routers and what happens when a website opens

## Running the number converter

You need Python 3 installed. From the root of this repository run:

```
cd mission-05-numbers-data
python3 number_converter.py
```

Then type a positive whole number when it asks. It shows the binary and hexadecimal version of that number, for example 13 gives `0b1101` and `0xd`.

## What I learned

I learned that most of what a computer does comes down to simple steps that I can check myself in the Terminal. Commands often print nothing when they work, so I have to look at the result. Numbers and text are stored in binary, and my hand calculations matched Python's. Git keeps a history of my work and a branch with a Pull Request lets changes be looked at before they go into `main`. I also learned why DNS and packets matter when a website opens. Pull Request #1 (adding a "My Learning" section) is still open and not merged.
