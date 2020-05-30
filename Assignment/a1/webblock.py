import requests as reqs
a = input("Enter a website \n")
response = reqs.get(a)
print(response.status_code)
if response.status_code == 451 :
    print("Website you entered is blocked. \n")
else :
    print("Website you entered is not blocked. \n")
