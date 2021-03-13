#Hakan İleri

def listSorter(studentDict,studentList):#take students in dictionary and store their grades in sorted list
    for i in range(len(studentDict)):
        #calculate grade with given percentages
        grade = studentDict[i]["Midterm"]*0.3+studentDict[i]["Project"]*0.3+studentDict[i]["Final"]*0.4
        studentList.append([studentDict[i]["Name"],grade]) #append name and grade os student to list
        studentList.sort(key = lambda x: float(x[1]), reverse=True) #sort from highest grade to lowest grade
    return studentList

def listPrint(studentList):
    for i in range(len(studentList)):     
        print (studentList[i][0], " Grade Average: ", studentList[i][1]) #print sorted student list

def studentDictMaker(studentDict,studentCount):
    for i in range(studentCount): 
        name = input("Name of the student: ")
        midterm = float(input("Midterm grade: "))
        project = float(input("Project grade: "))
        final = float(input("Final grade: "))
        studentDict[i] = {'Name':name, 'Midterm':midterm, 'Project':project, 'Final':final}
    return studentDict    

studentDict = {} #create an empty dictionary to store information
studentList = [] #create an empty list 
studentCount= 5  #given in the question
studentDict = studentDictMaker(studentDict,studentCount) #call dictionary function
studentList = listSorter(studentDict,studentList) #call sort function
listPrint(studentList) #call print sorted list  