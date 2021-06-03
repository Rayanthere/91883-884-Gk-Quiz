#the following code is to ask rhe user their user details

print("*********************Welcome to the General knowledge Quiz**********************")
print("This quiz is been developed by Rayan")

while True:
    name = input("What is your name : ")
    if name.replace(' ','').isalpha():
        break
    print("Please enter your name in letters only")

while True:  
    age = input("What is your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("Please enter your age in numbers only")


    
