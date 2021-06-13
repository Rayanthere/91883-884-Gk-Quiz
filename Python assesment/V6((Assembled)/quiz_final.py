from random import shuffle
import datetime
import time
x=datetime.datetime.now()


#Creating dictionary for question and the right answer
general=[
['What is the most common colour of toilet paper in France?',
 {'answer': 'b','options' : 'a)blue:b)Pink:c)black:d)white'}],

['The average person does what thirteen times a day?',
 {'answer' : 'a','options' : 'a)laugh:b)smile:c)cry:d)sleep'}],

['What is the correct term for a question mark immediately followed by an exclamation mark?',
 {'answer' : 'd','options' : 'a)idk:b)whaaaaaa:c)confused:d)Interrobang'}],

['What is the most famous Sci-Fi movie in the world?',
 {'answer' : 'c','options' : 'a)Raising Dion:b)Outside the wire:c)Avengers Endgame:d)Strangers'}],

['Who is the richests man alive on earth?',
 {'answer' : 'a','options' : 'a)Elon Musk:b)Bill Gates:c)Jeff Bezos:d)Me(Rayan)'}],

['What is the name of a swimming stroke which is also name of an insect?',
 {'answer' : 'd','options' : 'a)Ants:b)Cockroaches:c)Unicorns:d)Butterfly'}],

['What is the most expensive car ',
 {'answer': 'a','options' : 'a)1963 Ferrari 250 GTO:b)Bugatti La Voiture Noire:c)Pagani Zonda HP Barchetta:d)Prius'}],

['Who is the smartest guy in Avenger Endgame ?',
 {'answer' : 'c','options' : 'a)Captain America:b)Doctor Strange:c)Iron Man:d)Black Widow'}],

['What food is delicious but a pain to eat?',
 {'answer' : 'b','options' : 'a)Mango:b)Pineapple:c)apple:d)orange'}],

['1What skill is beneficial in swimming?',
 {'answer' : 'd','options' : 'a)Running:b)Passing:c)Throwing:d)Breathing Techniques'}],

]
shuffle(general)


index=0
score=0
optnum=0

#Using functions to greet the user.
def rounds():
    global r , total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds do you want to play there are a total of 10 round at max. : "))
            if 0<r<=10:
                break
            else:
                print("Please enter the rounds in 1-10 only")
        except:
            print('Please enter rounds in numbers only (The max is 10)')


    total=r


def greet():
    while True:
        name = input("What's your name? : ")
        if name.replace(' ','').isalpha():
            break
        print("--------------------------------")
        print("Please enter characters A-Z only")
        print("--------------------------------")



#Asking the user to enter their age by using try and except.
def age():
    while True:
        age = input("How old are you? : ")
        if age.isnumeric():
            break
        print("This is not a valid data type.Please enter your age in numbers.")




def rules():
    ready=input("press y to read the rules or \npress any other key to continue : ").lower()
    if ready=="y" or ready == "yes":
        print("============================================================")
        print("The basic rules are as follows \n1. Enter the answer in a,b,c,d.\n2. press a,b,c,d if you don't know the answer.\n3. You are not allowed to use help of internet\n4. You can work with people but then the score will be your and the person you playing with.\nThe following options are just help for you.\nRead the question and the options multiple times.\nPress enter after your input.")
        print("============================================================")
    else:
       print("You can play without the rules")

#Asking the user if they are ready for the quiz
def status():
    ready=input("Are you ready for the quiz?: press y to continue or any other key to enter to exit : ").lower()
    if ready=="y" or ready == "yes":
        print("lets continue")
        print("------------------------------------------------------------")
        print("Please answer the questions with the the alphabets (a,b,c,d)")
        print("------------------------------------------------------------")
    else:
        print("======================")
        print("Consider playing later")
        print("======================")
        exit()

    
print("-------------------------------------------------------------------------------")
print("--------------------Welcome to the general knowledge quiz !!-------------------")
print("-------------------------------------------------------------------------------")
print("                  ======================================\n                  The time is",x,"\n                  This quiz has been created by rayan\n                  ======================================\n")


greet()
age()
rules()
status()
rounds()

               
while r>0:
    data = general[0]
    i = data[0]
    data = data[1]
    answer = data["answer"]
    options = data['options'].replace(':','\n')

    print(i)
    print(options)
    while True:
        useranswer = input("Enter your answer here please : ")
        if useranswer == 'a' or useranswer == 'b' or useranswer == 'c' or useranswer == 'd':
            if useranswer == answer:
                print("=====================")
                print("Your answer is right!")
                print("=====================")
                score += 1

                print("Your score is",score)
            else:
                print("====================")
                print("Your answer is wrong")
                print("The answer is",answer)
                print("====================")

            del general[0]
            r-=1
            break
        else:
            print("------------------------------------------------------------")
            print("Please answer the questions with the the alphabets (a,b,c,d)")
            print("------------------------------------------------------------")
    
            

#This last part shows your total of the quiz and the percentage of the quiz.
print("========================================================================")
print("You have succesfully completed Rayan's General Knowledge quiz!")
print("Have any problems please contact this mail 19478@students.mrgs.school.nz")
print("Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing")
print("========================================================================")
time.sleep(9)
exit()

