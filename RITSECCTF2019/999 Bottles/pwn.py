import os
import subprocess

ascii = '0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_abcdefghijklmnopqrstuvwxyz{}'
list_ascii = list(ascii)
valid_char = []

for file in os.listdir():

    if not 'c.out' in str(file):
        continue

    for char in list_ascii:

        run =  subprocess.Popen('echo %s | ./%s' % (str(char) , str(file)), shell=True, stdout=subprocess.PIPE).stdout

        byte_output = run.read()
        string_output = byte_output.decode()

        if 'OK' in string_output:
            valid_char.append(str(char))

print('\n' + str(''.join(valid_char)))
