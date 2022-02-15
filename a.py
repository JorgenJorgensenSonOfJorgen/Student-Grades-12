import random

#we want to allow them to randomize student grades (test mode) or they can input their own grades.
def startup():
    grades = []
    lowest = 100
    highest = 0
    #sum of all grades
    sum = 0
    honours = 0
    cmd = input('random or input?')
    if cmd == 'random':
        for i in range(50):
            grade = random.randint(0,100)
            grades.append(grade)
            if grade > highest:
                highest = grade
            if grade < lowest:
                lowest = grade
            if grade > 80:
                honours +=1
            sum += grade

    elif cmd == 'input':
        count = 0
        print('Enter your grade. Enter quit to retry.')
        while count < 50:
            grade = input()
            try:
                grade = int(grade)
                #if this fails, get them to input a new thing
                if 0<= grade <= 100:
                    grades.append(grade)
                    if grade > highest:
                        highest == grade
                    if grade < lowest:
                        lowest = grade
                    if grade > 80:
                        honours +=1
                    sum += grade
                    count += 1
                else:
                    print('Please Enter a number from 0 to 100')
            except:
                #allow user to stop inputting
                if grade == 'quit':
                    return startup()
                else:
                    print('You Entered a non-integer, please try again')
    else:
        print('Please choose sir . . .')
        return startup()
    average = sum/50
    menu(highest, lowest, average, honours, grades)
    
def menu(highest, lowest, average, honours, grades):
    cmd = input('Enter "New Grades", "Display All Grades", "Stats", "Count Honours", or "Exit".')
    if cmd == 'New Grades':
        return startup()
    elif cmd == 'Exit':
        return
    else:
        if cmd == 'Display All Grades':
            for i in grades:
                print(str(i) + '%')
        elif cmd == 'Stats':
            print("Highest Grade: {}%".format(highest))
            print("Lowest Grade: {}%".format(lowest))
            print("Average Grade: {}%".format(average))
        elif cmd == 'Count Honours':
            print("Number of grades over 80% is {}.".format(honours))
        else:
            print('invalid command')
        return menu(highest, lowest, average, honours, grades)

startup()