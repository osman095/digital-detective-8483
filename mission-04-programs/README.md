# Mission 4 - How programs run

## 1. Task / objective
Run a simple Python program and compare how a compiler and an interpreter translate or run programs.

## 2. Work completed
- Made `hello.py` with a one-line program and ran it from Terminal using Python 3.
- Filled in the compiler vs interpreter comparison table.
- Wrote a short explanation of the difference in my own words.

### Task 4.1 - Create and run a Python program
`hello.py` has one line:

```python
print("Hello from Python")
```

I ran it with `python3 hello.py` and the message appeared in the Terminal:

```
Hello from Python
```

### Task 4.2 - Compiler vs interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | The whole program is translated before it runs, as a separate step | The program is read and carried out line by line while it runs |
| Typical output | A separate executable (machine code) file that can run on its own | No separate file needed, the output appears directly as the program runs |
| One example | C compiler (`gcc`) | Python (`python3`) |
| One advantage | The finished program usually runs faster and can be run without the compiler | It is easy to test, I can edit a file and run it again straight away |

A compiler translates all of the source code into machine code first, and then I run the result, so errors in the whole program are found before it starts. An interpreter reads the code and runs it as it goes, so it stops when it reaches a problem. That is why I could change `hello.py` and run it again immediately with no extra step. In real life it is not so strict, Python for example turns the code into an in-between form first and then runs it, so many languages use a bit of both.

## 3. Commands / tools used
- `python3 --version` - to check the Python version (3.10.18)
- `python3 hello.py` - to run my program with the Python interpreter
- A text editor - to write the file
- `ls` - to check that the file was there

## 4. My understanding
Computers only understand machine code, so the code I write has to be translated. A compiler does the translation for the whole program ahead of time, and an interpreter does it while the program runs. Python is mostly called an interpreted language, and `python3` is the interpreter that read my `hello.py` and ran it. I noticed that I never made a separate output file for `hello.py`, which fits with it being interpreted.

## 5. Difficulties faced
- I was not sure at first if I should type `python` or `python3`.
- When I mistyped the file name once (I ran `hellp.py`), Python gave an error that said it can't open the file.
- It was hard to put the difference in my own words because Python also does some translation before running, so it is not purely "no compile".

## 6. How I resolved them
- I checked both with `--version`. They both showed Python 3.10.18 on my computer, but I used `python3` since the assignment says Python 3.
- I read the error and saw `No such file or directory` with the wrong name, so I corrected the spelling and it ran.
- I explained it with the simple version first (compiler before, interpreter during) and added a line saying that real implementations can combine both, which the assignment also mentions.

## 7. Evidence / files
- `hello.py`
- Output shown above

## 8. Commit details
Commit message: "Compare compilers and interpreters"
Pushed to GitHub and checked that the files show up there.
