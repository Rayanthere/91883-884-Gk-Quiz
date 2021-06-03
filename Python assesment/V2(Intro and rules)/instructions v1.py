ready=input("press y to read the rules or press x to continue without rules : ").lower()
if ready=="y" or ready == "yes":
    print("The basic rules are as follows \n1. Enter the answer in a,b,c,d.\n2. press a,b,c,d if you don't know the answer.\n3. You are not allowed to use help of internet\n4. You can work with people but then the score will be your and the person you playing with.\nThe following options are just help for you.\nRead the question and the options multiple times.\nPress enter after your input.")
elif ready=="no" or ready == "x":
    print("You can play without the rules")
    exit()
