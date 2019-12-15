# iso_32 // Writeup

## Problem

*a 32bit elf crackme
try to solve it :)*

## Solution

In `main` , we can see it calls **`__f_func`** function after calling **`f`**.

By disassembling the ELF we see , there is a **`__s_fun`** function and that return `Great !!`.

So there are differents solutions , i have patched it using **IDA** , 
