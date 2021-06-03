from random import shuffle

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
status()

general=[
['What is the most common colour of toilet paper in France?',
 {'answer': 'b','options' : 'a)blue:b)Pink:c)black:d)white'}],

['The average person does what thirteen times a day?',
 {'answer' : 'a','options' : 'a)laugh:b)smile:c)cry:d)sleep'}],

['What is the correct term for a question mark immediately followed by an exclamation mark?',
 {'answer' : 'd','options' : 'a)idk:b)whaaaaaa:c)confused:d)Interrobang'}],

['Select one skill that is required for passing the ball in Hockey',
 {'answer' : 'c','options' : 'a)Speaking:b)Kicking:c)Dribbling:d)Jogging'}],

['What is one of the basic rule of basketball?',
 {'answer' : 'a','options' : 'a)No running with the ball:b)No Speaking with the ball:c)No passing with the ball:'}],

['What is the name of a swimming stroke which is also name of an insect?',
 {'answer' : 'd','options' : 'a)Ants:b)Cockroaches:c)Unicorns:d)Butterfly'}],

['For how long can you hold the ball in Netball?',
 {'answer': 'a','options' : 'a)3 seconds:b)50 seconds:c)10 seconds:d)100 seconds'}],

['How long is the interval betweeen each game in Badminton?',
 {'answer' : 'c','options' : 'a)30 mins:b)1 hour:c)1 min:d)2 mins'}],

['How many times does the ball bounce per side in tennis?',
 {'answer' : 'b','options' : 'a)2 time:b)1 time:c)3 times:d)4 times'}],

['1What skill is beneficial in swimming?',
 {'answer' : 'd','options' : 'a)Running:b)Passing:c)Throwing:d)Breathing Techniques'}],

]
shuffle(general)

index=0
score=0
optnum=0

while len(general)>0:
    data = general[0]
    q = data[0]
    data = data[1]
    answer = data['answer']
    options = data['options'].replace(':','\n')

    print(q)
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
    
