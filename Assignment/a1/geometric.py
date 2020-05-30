if __name__ == "__main__" :
    a = float(input("Enter first term of GP \n"))
    r = float(input("Enter common ratio of GP \n"))
    l = []
    i = 1
    l.append(a)
    while i < 10 :
        a = a * r
        l.append(a)
        i = i + 1
    print("10 terms of GP are as follows \n")
    print(l,"\n")
