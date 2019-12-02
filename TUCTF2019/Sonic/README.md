# Sonic // Writeup

## Problem

*Gotta go fast*

*nc chal.tuctf.com 30100*

## Solution

On that problem there was differents ways to solve it. For example, you can send every plaintext for each shift key ( 0 -> 26 ).

Or you can decode the message with the same shift key and do it until you got the flag : 

```python
from pwn import * 
import codecs

while True:

    conn = remote('chal.tuctf.com' , 30100)
    full_message = str(conn.recv())[301:]

    LIST = list(full_message)

    search=0
    while search < len(LIST):
        if LIST[search] == '\n':
            for i in range(30):
                try:
                    del LIST[search]
                except:
                     pass
        search += 1
        
    encoded_message = ''.join(LIST)
    rot13_message = codecs.encode(str(encoded_message) , 'rot_13')
    conn.sendline(str(rot13_message))
    recv = conn.recv()

    if 'TUCTF' in recv:
        print(recv)
        break
        
    conn.close()
```

**FLAG**: `TUCTF{W04H_DUD3_S0_F4ST_S0N1C_4PPR0V3S}`
