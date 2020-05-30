def countd(n) :
    i=0
    while n != 0 :
        i = i + 1
        n = int(n / 10)
    return i

def arms(n) :
    new = 0
    a = countd(n)
    p = n
    while n != 0:
        r = n % 10
        new = new + r**a
        n = int(n / 10)
    if new == p :
        return 1
    else :
        return 0

if __name__ == "__main__" :
    k = int(input("Enter first number in range\n"))
    l = int(input("Enter second number of range\n"))
    count = 0
    while k <= l :
        if arms(k) == 1 :
            print(k," is armstrong number")
            print("\n")
            count = count + 1
        k = k + 1
    if count == 0 :
        print("No Armstrong numbers in given range \n")


