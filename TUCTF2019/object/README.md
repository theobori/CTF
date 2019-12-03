# object // Writeup

## Problem

## Solution

We have an object file and in this method we are going to compile it.

`run.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped`

To compile it : `gcc run.o -o run_binary`

After compiling, I disassembled and decompiled it with ghidra and i saw there was an interesting function : `checkPassword`;

