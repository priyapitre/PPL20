#This program opens files and does file operations and deals with
#exceptions related with them when it encounters them.
#Test this code on a text file given with code.

file_name = input("Enter name of file with extension to be opened \n")
mode = input("Enter mode in which file is to be opened\n")
try : 
    f1 = open(file_name,mode)
    print(f1.read())
    f1.write("Trial text is written to test the code\n")
except UnicodeDecodeError :
    print("Something went wrong, Check whether the opened file is readable? \n")
except FileNotFoundError :
    print("Something went wrong, Check whether filename and path is correct?\n")
except IsADirectoryError :
    print("Something went wrong, Cant open a directory.\n")
except PermissionError :
    print("Something went wrong, Check permissions of file to be opened.\n")
except :
    print("Cant predict what exacty went wrong.\n")
else :
    print("Your job of file management successfully done!\n")
