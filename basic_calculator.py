import os
from time import sleep
def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
def add(a,b):
    y= a+b
    return y
def sub(a,b):
    y= a-b
    return y
def mul(a,b):
    y= a*b
    return y
def div(a,b):
    if b == 0:
        print("Division by zero not possible")
        return 'infinity'
    else:    
        y = a/b
    return y    
def rem(a,b):
    if b == 0:
        print("Division by zero is not possible")
        return 'infinity'
    else:    
        y = a%b
    return y    
c=1    
while c > 0:
    sleep(3)
    screen_clear()
    print("\t\t\tBASIC CALCULATOR\n\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for finding remainder\n0 to exit")
    c = int(input("\nEnter your choice: "))
    if c == 1:
        print('Sum is:',add(float(input('A: ')),float(input('B: '))))
    elif c == 2:
        print('Diff is:',sub(float(input('A: ')),float(input('B: '))))
    elif c == 3:
        print('Product is:',mul(float(input('A: ')),float(input('B: '))))
    elif c == 4:
        print('Result is ',div(float(input('A: ')),float(input('B: '))))
    elif c == 5:
        print('Remainder is ',rem(float(input('A: ')),float(input('B: '))))
    elif c == 0:
        break    
    else:
        print('Wrong input!!!')

    