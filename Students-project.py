Students = []
Grades = []
while True:
    print("1-Add a student")
    print("2-Show students And their grades")
    print("3-Highest grade")
    print("4-Average")
    print("5-Exit")
    Choice = int(input("Choose a number: "))
    if Choice == 1:
        New_name = input("student name: ")
        New_grade = float(input("Student grade: "))
        Students.append(New_name)
        Grades.append(New_grade)
        print("Student was added succesfully to the list")
    elif Choice == 2:
        print(Students)
        print(Grades)
    elif Choice == 3:
        Highest = max(Grades)
        position = Grades.index(Highest)
        print("The highest grade is:",Highest)
        print("And its from:",Students[position])
    elif Choice == 4:
        Avg = sum(Grades) / len(Grades)
        print("The average is: ",Avg)
    elif Choice == 5:
        print("Thank you")
        break
    else:
        print("Enter a valid number")


