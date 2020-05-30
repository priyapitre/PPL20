def operation12(l1,l2,i) :
    k = l1.pop(i)
    print(k," moved from bank1 to bank2 \n")
    l2.append(k)
    return l1,l2

def operation21(l1,l2,i) :
    k = l2.pop(i)
    print(k," moved from bank2 to bank1 \n")
    l1.append(k)
    return l1,l2

if __name__ == "__main__" :
    bank1 = []; bank2 = []
    print("Enter components to be transported in priority order. \n")
    for i in range(0,3) :
        a  = input()
        bank1.append(a)
    print("bank1:",bank1,"\n bank2:",bank2,"\n")
    bank1,bank2 = operation12(bank1,bank2,1)
    print("Boat comes back to bank1. \n")
    bank1,bank2 = operation12(bank1,bank2,1)
    bank1,bank2 = operation21(bank1,bank2,0)
    bank1,bank2 = operation12(bank1,bank2,0)
    print("Boat comes back to bank1. \n")
    bank1,bank2 = operation12(bank1,bank2,0)
    print("Final output: \n bank1:",bank1,"\n bank2:",bank2)
