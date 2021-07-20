#Universities listesinde sırasıyla her üniversite için (liste içinde liste) şunlar var:
#Üniversitenin kodu, ismi, puanı, kontenjanı
#Students listesinde sırasıyla her öğrenci için (liste içinde liste) şunlar var:
#Öğrencinin id'si, ismi, soyismi, kitapçığı, doğrusu, yanlışı, boşu, neti, puanı, 1. tercihinin ismi, 2. tercihinin ismi, yerleştiği yer
class Student: #I created a Student class.
    def __init__(self, id, name, lastName):
        self.__id=id #Id is private, name and lastName are global.
        self.name=name
        self.lastName=lastName
    def getid(self): #Getter for id
        return self.id

    def setid(self,id): #Setter for id
        self.id=id

menuChoice = 0 #I assigned the "menuChoice" variable in order to use it.
while menuChoice != -1: #If "menuChoice == -1" the program stops running.
    ##----------FIRST OPTION----------
    if menuChoice == 1: #If I chose "1":
        studentFile = open("student.txt", "r", encoding="utf-8") #I am opening the file for using it.
        students = {} #I created a "students" dictionary.
        for line in studentFile: #It is looking for every line in the students.txt file.
            studentF = line.split()
            id = studentF[0] #I assigned the first element to id, second element to name and third element to last name.
            name = studentF[1]
            lastName = studentF[2]
            students[id] = Student(id, name, lastName) #Id is the key.

        try: #I have gotten an error while I was trying to print "Not found" so I used a try-expect.
            student_id = input("Enter a student id (It must be a six-digit integer): ") #The input for getting the student's id.
            if student_id.isdigit():
                if (int(student_id) / 100000) >= 1:
                    s = students.get(student_id)
                    print(s.name, s.lastName)
                else:
                    print("The input is not six-digit. Please write a six-digit integer.")
            else:
                print("The input is string. Please write a integer.")

        except:
            print("Not found") #It prints "Not found" if a student doesn't exist with the given id.

    ##---------SECOND OPTION---------
    universityFile = open("university.txt", "r", encoding="utf-8") #I am opening the file for using it.
    universityF = universityFile.readlines() #It reads every line in university.txt file.

    universities = [] #I created a "universities" list.
    universityFile = open("university.txt", "r", encoding="utf-8")
    for element in universityFile:
        universities_split = element.split(",") #It is splitting all of the elements by commas.
        universities.append(universities_split) #It is adding the elements into the list that we splitted a line before.

    basePointList = [] #I created a list that includes all base points of the universities.
    for everyLine in universityF:
        universityNumber, universityNameAndDepartment, basePoint, quota = everyLine.strip().split(",") #It splits the elements by commas and defining them.
        basePointList.append(basePoint) #It adds the basePoint elements to the basePointList.

    basePointList.sort(reverse = True) #It sorts the base points in the list from the biggest to the smallest.
    if menuChoice == 2: #If I chose "2":
        for i in range(len(basePointList)):
            for j in range(len(universities)):
                if basePointList[i] == universities[j][2]: #If i'th point in the basePointList equals to the j'th point in the universities list:
                    print(universities[j][1], basePointList[i]) #It prints the university's name first and its point second.
        a = max(basePointList)
        for k in range(len(universities)):
            if a == universities[k][2]:
                print(a, universities[k][1])

    ##---------THIRD OPTION----------####
    keys = [] #I created a keys list for keeping keys in it.
    keyFile = open("key.txt", "r", encoding="utf-8") #I opened the keys.txt file for using it.
    for element in keyFile:
        keys.append(element) #It adds keys in the key.txt file to the keys list.
    AList=keys[0] #It is assigning the first key to the A key.
    BList=keys[1] #It is assigning the second key to the B key.

    answerFile = open("answers.txt", "r", encoding="utf-8") #I opened the answers.txt file for using it.
    answers = [] #I created a answers list for adding every element in answers.txt file in it.
    for element in answerFile:
        answers_split = element.split() #It splits the elements.
        answers.append(answers_split) #It adds the elements.

    students = [] #I created a students list for adding every element in student.txt file in it.
    studentFile = open("student.txt", "r", encoding="utf-8")
    for element in studentFile:
        student_split = element.split() #It splits the elements.
        students.append(student_split) #It adds the elements.

    for i in range(len(students)):
        for k in range(len(answers)):
            if answers[k][0]==students[i][0]: #If the id in the answers list and students list are the same:
                students[i].append(answers[k][1]) #It adds the book type into the students list.

    for i in range(len(students)):
        for k in range(len(answers)):
            if answers[k][0] == students[i][0] and answers[k][1] == "B": #If ids are the same in the lists and the book type is B:
                correct = 0
                incorrect = 0
                blank = 0
                counter1=0
                for j in answers[k][2]: #It is looking at every char in the student's answer.
                    if j == BList[counter1]: #If it's same in the answer and in the key:
                        correct = correct + 1
                    elif j == "*": #If that question left blank:
                        blank = blank + 1
                    else:
                        incorrect = incorrect + 1
                    counter1=counter1+1 #It increases the counter so every answer is handled.
                students[i].append(correct)
                students[i].append(incorrect)
                students[i].append(blank)
                net = correct - (incorrect / 4) #4 incorrect answers are deleting a correct answer.
                score = net * 15 #It finds the score.

                students[i].append(net) #It adds the "net" to the students list.
                students[i].append(score) #It adds the "score" to the students list.
            elif answers[k][0] == students[i][0] and answers[k][1] == "A": #It does same things for the "A" book type.
                correct = 0
                incorrect = 0
                blank = 0
                counter2 = 0
                for j2 in answers[k][2]:
                    if j2 == AList[counter2]:
                        correct = correct + 1
                    elif j2 == "*":
                        blank = blank + 1
                    else:
                        incorrect = incorrect + 1
                    counter2 = counter2 + 1
                students[i].append(correct)
                students[i].append(incorrect)
                students[i].append(blank)
                net = correct - (incorrect / 4)
                score = net * 15

                students[i].append(net)
                students[i].append(score)

    codeList = [] #I am creating a list for universities' codes.
    universityNameAndDepartmentList = [] #I am creating a list for universities' names and their departments.

    universityFile = open("university.txt", "r", encoding="utf-8")
    universityF = universityFile.readlines()
    for line in universityF:
        code, universityNameAndDepartment, point, capacity = line.strip().split(",") #It splits the elements by commas and defining them.
        codeList.append(code) #It adds the universities' codes to to codeList.
        universityNameAndDepartmentList.append(universityNameAndDepartment) #It adds the universities' names and departments to the list.

    for i in range(len(students)):
        students[i].append(answers[i][3]) #It adds the first university choice's code to the students list.
        students[i].append(answers[i][4]) #It adds the second university choice's code to the students list.

    for i in range(len(students)):
        for j in range(len(codeList)):
            if students[i][9] == codeList[j]: #If a student's first choice is j'th in codeList:
                students[i].append(universityNameAndDepartmentList[j]) #It adds the j'th university name to the students list.
        for k in range(len(codeList)):
            if students[i][10] == codeList[k]: #If a student's second choice is k'th in codeList:
                students[i].append(universityNameAndDepartmentList[k]) #It adds the k'th university name to the students list.

    for i in range(len(students)):
        del students[i][9] #It deletes the first choice's code.
        del students[i][9] #It deletes the second choice's code.(The first one is deleted so the second one becomes the ninth element.)
    if menuChoice == 3: #If I chose "3":
        resultFile=open("results.txt", "w", encoding="utf-8")
        for i in students: #It writes the students list to the results.txt file.
            resultFile.write(str(i))
            resultFile.write("\n")
        resultFile.close()
    #-------FOURTH OPTION----------
    if menuChoice == 4: #If I chose "4":
        n = len(students) #There is a bubble sort.
        for i in range(n-1):
            for j in range(0,n-i-1):
                if students[j][8] < students[j+1][8]: #If j'th score is less than j+1'th score:
                    students[j], students[j+1] = students[j+1], students[j] #j'th and j+1'th students change places.
        for k in range(len(students)):
            print(students[k][8], students[k][0], students[k][1], students[k][2]) #Prints students' score, id, name, last name.

    #---------FIFTH OPTION-----------
    for i in range(len(students)):
        for j in range(len(universities)):
            if students[i][8] >= int(universities[j][2]): #If student's score is higher than the universities'.
                if students[i][9] == universities[j][1]: #If i'th student's first choice is at j'th at the list.
                    if int(universities[j][3]) > 0: #If the quota is more than 0:
                        students[i].append(universities[j][1]) #It adds the university's name to the i'th student's list.
                        universities[j][3] = int(universities[j][3]) - 1 #It decreases the quota.
                    else: #If student wasn't able to get into the his/her first choice, it does the same things for second choice.
                        if students[i][10] == universities[j][1]:
                            if int(universities[j][3]) > 0:
                                students[i].append((universities[j][1]))
                                universities[j][3] = int(universities[j][3]) - 1
                            else:
                                students[i].append("x")#If there is no quota it adds a x. X means student wasn't be able to placed anywhere.
        else:
            students[i].append("x") #If student's score is not higher than or equal to the universities' scores it adds a x.
    if menuChoice == 5: #If I chose "5":
        for i in range(len(universities)):
            print(universities[i][1]) #It prints the universities's names.
            print("------------------------------------------")
            for k in range(len(students)):
                if students[k][11] == universities[i][1]: #If student was be able to placed anywhere:
                    print(students[k][1], students[k][2]) #It prints the student's name and last name.

    ##-------------SIXTH OPTION------------------
    if menuChoice == 6: #If I chose "6":
        print("Who were not be able to placed anywhere:")
        print("---------------------------------------")
        for k in range(len(students)):
            if students[k][11] == "x": #Is student wasn't be able to placed anywhere (that means "x"):
                print(students[k][1], students[k][2]) #It prints the student's name and last name.

    ##-------------SEVENTH OPTION----------------
    departments = []
    departments2 = []
    departments3 = []
    if menuChoice == 7: #If I chose "7":
        for i in range(len(universities)):
            splitted=universities[i][1].split("University ") #It splits the lines before and after "Üniversitesi"
            departments.append(splitted) #It adds the splitted elements to the first list.
            for j in departments[i]:
                splitted2=j.split(",") #It splits the lists by comma.
            departments2.append(splitted2) #It adds the splitted elemets to the second list.
        for i in departments2:
            if not i in departments3: #If a department haven't written before:
                departments3.append(i) #It adds it to the third list.
        for i in range(len(departments3)):
            for j in departments3[i]:
                print(j) #It prints the unique departments.

    menuChoice = int(input("Write '1' for searching for a student with a given id.\nWrite '2' for listing universities with maximum base points.\nWrite '3' for result.txt\nWrite '4' for student informations sorted by score.\nWrite '5' for students who placed in universities\nWrite '6' for students who were not be able to placed anywhere.\nWrite '7' for all the departments\nWrite '-1' for exit.\nYour choice: "))
studentFile.close()
answerFile.close()
keyFile.close()
universityFile.close()