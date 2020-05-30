def sumreci(n) :
    i = 1; new = 0
    while i <= n :
        if n%i == 0 :
            new = new + 1/i
        i = i + 1
    return new

def numdivisors(n) :
    i = 1; count = 0
    while i <= n :
        if n%i == 0 :
            count = count + 1
        i = i + 1
    return count

if __name__ == "__main__" :
    i = 1; l = 1
    while i <= 10 :
        p = sumreci(l)
        q = numdivisors(l)
        if q/p == int(q/p) :
            print(l," is a harmonic number \n")
            i = i + 1
        l = l + 1
