from random import shuffle

general=[
['What is the most common colour of toilet paper in France?',
 {'answer': 'b','options' : 'a)blue:b)Pink:c)black:d)white'}],

['The average person does what thirteen times a day?',
 {'answer' : 'a','options' : 'a)laugh:b)smile:c)cry:d)sleep'}],

['What is the correct term for a question mark immediately followed by an exclamation mark?',
 {'answer' : 'd','options' : 'a)idk:b)whaaaaaa:c)confused:d)Interrobang'}],

['Select one skill that is required for passing the ball in Hockey',
 {'answer' : 'c','options' : 'a)Speaking:b)Kicking:c)Dribbling:d)Jogging'}],
]
shuffle(general)

index=0
score=0
optnum=0

while len(general)>0:
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
            break
        else:
            print("------------------------------------------------------------")
            print("Please answer the questions with the the alphabets (a,b,c,d)")
            print("------------------------------------------------------------")


#Presenting the scores to the users.
print("==============================================================")
print("You have succesfully completed Rayan's General Knowledge quiz!")
print("Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing")
print("==============================================================")
exit()
    
