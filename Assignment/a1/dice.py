import random
if __name__ == "__main__" :
    i=1
    while i > 0 :
        print("Dice roll output is :")
        print(random.randrange(1,7))
        print("\n")
        a = input("Do you wish to roll it again? y or n\n")
        if a == 'n' :
            break
        i = i+1
