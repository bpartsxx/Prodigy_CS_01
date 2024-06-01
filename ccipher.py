
import sys
from termcolor import cprint 
from pyfiglet import figlet_format
from colorama import init
from itertools import cycle




def caesar_cipher(shift,text,mode):
    if mode=='d':
        shift=0-int(shift)
    else:
        shift=int(shift)
    lalphabet = 'abcdefghijklmnopqrstuvwxyz'
    ualphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphamodupper = ualphabet[shift:] + ualphabet[:shift]
    alphamodlower = lalphabet[shift:] + lalphabet[:shift]
    #print(alphamod)
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = ualphabet.find(char)
                new_char = alphamodupper[index]
            else:
                index = lalphabet.find(char)
                new_char = alphamodlower[index] 
        else:
            new_char = char  # Keep non-alphabetic characters the same

        result += new_char

    return result
        
            
    
    
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
cprint(figlet_format('CCipher1.0'),
       'red', 'on_black', attrs=['bold'])
print("Welcome to CCipher1.0 | Made by 6p@rtsXX | Prodigy CS-01\n")
print("==========================================================")

print("Usage Hint: Enter (e)ncrypt or (d)ecrypt followed by key seperated by space. \nFor example:\n> e 3\n\nPress Ctrl+C to exit.\n\n")

while(True):
    text=input("\nEnter text:\n=> ")
    inputlist=input("> ").split(" ")
    key=inputlist[1]
    mode=inputlist[0]
    #print(inputlist[0])
    if len(inputlist)==2:
        if inputlist[0]!='e' and inputlist[0]!='d':
            print("Incorrect syntax. Please refer to the format.")
            continue
        else:
            key=int(key)%26
            result=caesar_cipher(key,text,mode)
            print("Result: "+result)

            
    else:
        print("Please follow the format shown in the example.")
        continue


