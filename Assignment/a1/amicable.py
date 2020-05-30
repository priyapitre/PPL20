def sumofdivisors(n) :
    i = 1; new = 0
    while i < n :
        if n%i == 0 :
            new = new + i
        i = i + 1
    return new

if __name__ == "__main__" :
    num1 = 1; num2 = 1
    while num1 <= 10 :
        m = sumofdivisors(num2)
        if m != num2 :
            p = sumofdivisors(m)
            if p == num2 :
                print(num2," and ",m," is pair of amicable numbers \n")
                num1 = num1 + 1
                num2 = m
        num2+=1
