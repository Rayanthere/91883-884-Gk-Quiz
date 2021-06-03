#This is a simple quiz
#initial score
Q1 = 'Avengers Endgame'
Q2 = 'Elon Musk'
Q3 = '1963 Ferrari 250 GTO'
Q4 = 'Iron Man'
Q5 = 'Pineapple'

score = 0

status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>")

#What if the user is not ready
if status == 'No' or status == 'no' or status == 'n' or status == 'N' : 
    print("See you next time.")
    
#what if the user is ready
if status == 'yes' or status == 'Yes' or status == 'y' or status == 'Y' or status == 'a' or status == 'A':
    print("Welcome to the quiz.")

#set of questions that are asked
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    print("                                      ")
    
    ans=input("What is the most famous Sci-Fi movie in the world?\n \na.Avengers Endgame\nb.Outside the wire\nc.Raising Dion\n \nYour answer : ")
  
    if ans == 'avengers endgame' or ans == 'Avengers Endgame' or ans =='A' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
        
    else:
        print("Oops incorrect the correct answer is :" ,Q1)
        if score <=0:
            score = 0
            print("Your score is",score)



    print("\nQuestion: 2|score:{}".format(score))

    ans=input("Who is the richests man alive on earth?\na.Bill Gates\nb.Elon Musk\nc.Jeff Bezos \nYour answer : ")
    if ans == 'elon musk' or ans == 'Elon Musk' or ans =='B' or ans == 'b':
        print("Correct")
        score+=1
        print("Your score is",score)

        
    else:
        print("Oops incorrect the correct answer is :" ,Q2)
        if score <=0:
            score = 0
            print("Your score is",score)



    print("\nQuestion: 3|score:{}".format(score))

    ans=input("What is the most expensive car ?\na.1963 Ferrari 250 GTO\nb.Bugatti La Voiture Noire\nc.Pagani Zonda HP Barchetta \nYour answer : ")
    if ans == '1963 Ferrari 250 GTO' or ans == '1963 ferrari 250 gto' or ans =='A' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)

        
    else:
        print("Oops incorrect the correct answer is :" ,Q3)
        if score <=0:
            score = 0
            print("Your score is",score)


    print("\nQuestion: 4|score:{}".format(score))

    ans=input("Who is the smartest guy in Avenger Endgame ?\na.Captain America\nb.Hulk\nc.Iron Man \nYour answer : ")
    if ans == 'Iron Man' or ans == 'iron man' or ans =='C' or ans == 'c':
        print("Correct")
        score+=1
        print("Your score is",score)

        
    else:
        print("Oops incorrect the correct answer is :" ,Q4)
        if score <=0:
            score = 0
            print("Your score is",score)




    print("\nQuestion: 5|score:{}".format(score))

    ans=input("What food is delicious but a pain to eat?\na.Mango\nb.Pineapple\nc.Grapes \nYour answer : ")
    if ans == 'Pineapple' or ans == 'pineapple' or ans =='A' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)

        
    else:
        print("Oops incorrect the correct answer is :" ,Q5)
        if score <=0:
            score = 0
            print("Your score is",score)





            






