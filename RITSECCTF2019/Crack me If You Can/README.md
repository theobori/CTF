# Crack me If You Can // Writeup

## Problem

*Rev up your GPUs...*

*nc ctfchallenges.ritsec.club 8080*

*Flag format RS{ }*

Author: Sp1kedshell

## Solution

Connect to the given ip with netcat : `nc ctfchallenges.ritsec.club 8080`

It returned a hash and i put it in `hash.hash` :

**hash** : `$6$F6fotlsVBaJJBf2/$hfHlysK77xU.OJ1CD.iI7Pf9bYbYm20gscrHWtYC8zax3eITnWQjTRFeBhaQeJxVFZ7CKYAN9Nmk2mjKlhAma/`

It looks like **sha512crypt** , so let's try to get the plaintext with hashcat : 
`hashcat -a 0 -m 1800 hash.hash 10-million-password-list-top-1000000.txt`

**FLAG**: `synergy`
