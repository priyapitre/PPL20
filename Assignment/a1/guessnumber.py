def numdigits(n) :
    i = 0
    while n != 0 :
        i = i + 1
        n = int(n / 10)
    return i

import random
if __name__ == "__main__" :
    a = random.randrange(1000)
    b = numdigits(a)
    print(b," digit number.\n")
    c = int(input("Enter a number to compare \n"))
    k = 0
    while 1 :
        if c > a :
            print(c," is greater than number to be guessed \n")
            break
        elif c < a :
            print(c," is less than number to be guessed \n","Enter another upper bound \n")
            c = int(input())
        else :
            k = 1
            print(c," is the correct number \n")
            break
    if k == 0 :
        up = c
        low = 10**(b-1)
        num = 0
        while 1 :
            print("Your number lies between ",low," and ",up,"\n")
            num = int(input("Enter a number to lower the range \n"))
            if num < a :
                low = num
            elif num > a :
                up = num
            else :
                print(num," is the correct number \n")
                break

