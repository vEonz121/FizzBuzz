import time
import os
import sys
import colorama
from colorama import Fore
command = 'clear'
if os.name in ('nt', 'dos'):
    command = 'cls'
os.system(command)
print()
while True:
    fizz = "\033[48;2;86;58;205m"+"Fizz"+"\033[0m"
    buzz = "\033[48;2;250;69;69m"+"Buzz"+"\033[0m"
    
    def clearLine():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

    def tileIt(text,ANS):
        fizz = "\033[48;2;86;58;205m"+"Fizz    "+"\033[0m"
        buzz = "\033[48;2;250;69;69m"+"Buzz    "+"\033[0m"
        fizzbuzz = "\033[48;2;86;58;205m"+"Fizz"+"\033[0m"+"\033[48;2;250;69;69m"+"Buzz"+"\033[0m"
        if ANS == "":
            spaceString=""
            spaces = 8 - len(text)
            for i in range(spaces):
                spaceString+=" "
            return str(f"\033[48;2;255;255;255m{Fore.BLACK +str(text)}{spaceString}\033[0m")
        else:
            if text.lower() == "fizz":
                return fizz
            if text.lower() == "buzz":
                return buzz
            if text.lower() =="fizzbuzz":
                return fizzbuzz


    i = 0
    reANS =""
    print(f"{fizz}{buzz} lets fkin goo!!! \n")
    print(f"\033[48;2;255;255;255m{Fore.BLACK + 'How To Play:'}\033[0m",end='')
    print(f"\033[48;2;255;255;255m                                             \033[0m") 
    print(f"\033[48;2;255;255;255m                                                         \033[0m")
    print(f"\033[48;2;255;255;255m{Fore.BLACK + 'Type the next number in the sequence and hit enter.      '}\033[0m")
    print(f"\033[48;2;255;255;255m{Fore.BLACK + 'If its a multiple of 3 you must type '}\033[0m{fizz}\033[48;2;255;255;255m{Fore.BLACK + '.'}               \033[0m")
    print(f"\033[48;2;255;255;255m{Fore.BLACK + 'If its a multiple of 5 you must type '}\033[0m{buzz}\033[48;2;255;255;255m{Fore.BLACK + '.'}               \033[0m")
    print(f"\033[48;2;255;255;255m{Fore.BLACK + 'If its a multiple of both 3 and 5 you must type '}\033[0m{fizz}{buzz}\033[48;2;255;255;255m{Fore.BLACK + '.'}\033[0m")
    print(f"\033[48;2;255;255;255m                                                         \033[0m")
    
    print(f"\n\033[48;2;48;160;0m{Fore.WHITE + 'START!  '}\033[0m")

    print(tileIt(str(i),reANS))

    clock = time.time()
    while True:
        
        output =""
        reANS =""
        
        i +=1
        
        if (i % 3 == 0):
            output += "fizz"
            reANS+=fizz
        if (i % 5 == 0):
            output += "buzz"
            reANS+=buzz
        
        if(output == ""):
            output = str(i)
            

        try:
            ans = input("")
        except:
            i -= 1
            continue
                

        if ans == output:
            clearLine()
            print(tileIt(output,reANS))
            continue
        
        else:
            clearLine()
            sec = round((time.time() - clock), 2)
            sec = sec % (24 * 3600)
            h = sec // 3600
            sec %= 3600
            minutes = sec // 60
            sec %= 60
            
            t = str("%d:%02d:%02d" % (h, minutes, sec))

            print(f"\033[48;2;38;38;38m{Fore.WHITE + 'END!    '}\033[0m\n")
            print(f"Game Over :( \nYour score is {i-1}\nTime Taken: {t}")
            break
    
    
    res = input("Try again ? (y/n): ")
    if res.lower() == "y":
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
        pass
    else:
        print("Bye!")
        break