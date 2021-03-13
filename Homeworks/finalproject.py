# Hakan İleri

#Knowledge questions

def knowledgeCompetition(): #create knowledge competition function
    q1 = input("\nCapital city of Turkey: ")#Ankara
    q2 = input("\nLife history written by oneself: ")#Autobiography 
    q3 = input("\nOne who knows everything: ")#Omniscient
    q4 = input("\nThe person who collects coins: ")#Numismatist 
    q5 = input("\nPerson who writes with both hands: ")#Ambidextrous 
    q6 = input("\nPerson who walks in sleep: ")#Somnambulist 
    q7 = input("\nWorld Trade Organization came into existence in……")#1995
    q8 = input("\nLargest and the deepest ocean of the world is ")#Pacific
    q9 = input("\nWho discovered Penicillin? ")#Alexander Fleming
    q10 = input("\nIn what year was the Chernobyl disaster? ")#1986

    points = 0 #create variable for total points
    #Check each answer and give 10 points if the answer is correct
    if q1.lower() == "ankara":
        points+=10
    if q2.lower() == "autobiography":
        points+=10
    if q3.lower() == "omniscient":
        points+=10
    if q4.lower() == "numismatist":
        points+=10        
    if q5.lower() == "ambidextrous":
        points+=10
    if q6.lower() == "somnambulist":
        points+=10
    if q7 == "1995":
        points+=10
    if q8.lower() == "pacific":
        points+=10 
    if q9.lower() == "alexander fleming":
        points+=10
    if q10 == "1986":
        points+=10
    #Print if the user is succesful or not
    if points>50:
        print("Congratulations! Your grade is ",points, end=".")
    else:
        print("Better luck next time! Your grade is",points, end=".")
    condition = input("\nEnter 'Y' to start again. ")    
    if condition.lower() == "y":
        knowledgeCompetition()
knowledgeCompetition()