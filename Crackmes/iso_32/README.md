# iso_32 // Writeup

## Problem

*a 32bit elf crackme
try to solve it :)*

## Solution

In `main` , we can see it calls **`__f_func`** function after calling **`f`**.

By disassembling the ELF we see , there is a **`__s_fun`** function and that return `Great !!`.

So there are differents solutions , i have patched it using **IDA** , thats look like this : 

![iso_32_screenshot_main](ida_iso_32.png) 

Or you can use **gdb** to break at `0x080491ad` (__f_func)  and jump to `0x08049182` (__s_func)

```
$./crackme 
enter the password:b0th
Great !!
```
