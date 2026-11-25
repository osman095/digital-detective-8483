# Mission 5 - Numbers and data

## 1. Task / objective
Convert between decimal, binary and hexadecimal, check the answers with Python, build a small number converter program and explain how text is stored.

## 2. Work completed
- Did the seven conversions by hand and showed the steps.
- Checked them using Python's built-in functions.
- Wrote `number_converter.py` and tested it with four numbers.
- Answered the questions about how text is stored.

### Task 5.1 - Conversions by hand

| Question | My working and answer |
|---|---|
| Decimal 13 to binary | Keep dividing by 2 and write the remainders: 13 ÷ 2 = 6 r **1**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1**. Read the remainders from bottom to top: **1101** |
| Decimal 25 to binary | 25 ÷ 2 = 12 r **1**, 12 ÷ 2 = 6 r **0**, 6 ÷ 2 = 3 r **0**, 3 ÷ 2 = 1 r **1**, 1 ÷ 2 = 0 r **1**. Bottom to top: **11001** |
| Binary 1010 to decimal | Place values are 8, 4, 2, 1. (1×8) + (0×4) + (1×2) + (0×1) = 8 + 2 = **10** |
| Binary 1101 to decimal | (1×8) + (1×4) + (0×2) + (1×1) = 8 + 4 + 1 = **13** |
| Hex A to decimal | In hex A = 10, so the answer is **10** |
| Hex 1F to decimal | 1F means 1 sixteen and F (15) ones: (1×16) + 15 = **31** |
| Binary 1111 to hex | 1111 is one group of 4 bits: 8 + 4 + 2 + 1 = 15, and 15 is F in hex. So **F** |

### Task 5.2 - Verifying with Python
I opened Python and tried the built-in functions. `bin()` and `hex()` change a number to binary and hex text, and `int(text, base)` changes text in a base back to a normal number.

| Expression I tested | Result | Matches my manual answer? |
|---|---|---|
| `bin(13)` | `0b1101` | Yes (1101) |
| `bin(25)` | `0b11001` | Yes (11001) |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `0xf` | Yes (F) |

### Task 5.3 - My number converter
`number_converter.py` asks for a decimal number, turns the typed text into an integer with `int()`, and shows the binary and hex versions:

```python
num = int(input("Enter a positive decimal number: "))

binary = bin(num)
hexa = hex(num)

print("Binary:", binary)
print("Hexadecimal:", hexa)

print("Binary (no prefix):", binary[2:])
print("Hex (no prefix):", hexa[2:].upper())
```

Run with `python3 number_converter.py`. Test results:

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | 0b1101 | 0xd |
| 100 | 0b1100100 | 0x64 |
| 255 | 0b11111111 | 0xff |
| 1024 | 0b10000000000 | 0x400 |

What the functions do: `input()` reads what the user types, but always as text. `int()` turns that text into a real number. `bin()` returns the binary form as text starting with `0b`, and `hex()` returns the hex form starting with `0x`. I cut off the first two characters with `[2:]` to also show the numbers without the prefix.

### Task 5.4 - How is text stored?
- **ASCII codes:** uppercase `A` is 65 and lowercase `a` is 97 (I checked with `ord('A')` and `ord('a')`).
- **Why an encoding standard is needed:** a computer only stores numbers (bits), so every letter has to be given a number. If everyone used their own numbers, text from one computer would show as wrong characters on another one, so a shared standard like ASCII or UTF-8 is needed.
- **Not in basic ASCII:** the rupee sign `₹`. Python gave `ord('₹')` as 8377, which is too big for ASCII (0 to 127), and in UTF-8 it takes three bytes (`\xe2\x82\xb9`).

## 3. Commands / tools used
- `python3` interactive mode and `python3 number_converter.py` - to run the checks and the program
- `bin()` - decimal number to binary text
- `hex()` - decimal number to hex text
- `int(text, base)` - text in base 2 or 16 to a decimal number
- `input()` - read what the user types
- `ord()` - get the code number of a character
- `.encode('utf-8')` - see the bytes used for a character
- A text editor to write the converter

## 4. My understanding
A bit is 0 or 1 and 8 bits make a byte. Binary uses base 2, hex uses base 16, and each hex digit stands for exactly 4 bits, which is why 1111 becomes F so easily. Converting by hand using remainders (decimal to binary) and place values (binary to decimal) gave the same answers as Python every time. Text is stored as numbers too, and the encoding standard decides which number is which character. UTF-8 can store many more characters than basic ASCII, like `₹`, by using more than one byte.

## 5. Difficulties faced
- At first it was easy to read the remainders in the wrong order when converting to binary.
- `bin()` and `hex()` put `0b` and `0x` in front, and hex came out in small letters, so it did not look like my hand answers.
- When I tried `bin("13")` without converting it, Python gave `TypeError: 'str' object cannot be interpreted as an integer`.
- When I typed `abc` into my converter it crashed with `ValueError: invalid literal for int() with base 10: 'abc'`.

## 6. How I resolved them
- I remembered to read the remainders from bottom to top, and checked each with Python.
- I understood the prefixes just show the base, and I added a version without them using `[2:]` and `.upper()` for hex.
- The TypeError showed me that `input()` gives text, so I need `int()` first. My program already does that.
- I did not add error handling, because the task asked for positive numbers only, so my converter only works for valid whole numbers. I wrote that as a limit of the program.

## 7. Evidence / files
- `number_converter.py`
- The tables and outputs above

## 8. Commit details
Commit message: "Build number converter and practise data representation"
Pushed to GitHub and checked that the files show up there.
