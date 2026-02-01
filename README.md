# Hack Assembler

Python-based assembler for the **Nand2Tetris** course (Building a Modern Computer from First Principles).

## Function

It takes code written in the Hack Assembly language (`.asm` files) and translates it into binary machine code (`.hack` files) that can run on the Hack computer simulation.

It handles all the standard assembler tasks:
- parsing A-instructions and C-instructions
- translating mnemonics into binary bits
- managing the symbol table (labels and variables)

## How to Run

Run the assembler from the command line, passing your assembly file as an argument:

```bash
python hackassembler.py YourProgram.asm
```
It will generate a ```YourProgram.hack``` file in the same directory.
