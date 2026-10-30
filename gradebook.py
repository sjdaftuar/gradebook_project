all_grades={"data science":[88, 100, 95], "latin":[94,82,99], "chemistry":[86, 98, 91]}

def main(): # main method! 
    print("\nwelcome to your gradebook!")
    # menu options
    choice = input("\nWould you like to \n"  \
        "a. print out each class and its average grade \n" \
        "b. print the average grade of a subject \n" \
        "c. print the average GPA \n" \
        "d. add a grade to a particular subject \n" \
        "please type 'a', 'b', 'c', or 'd' lowercase. \n\n")

    if choice == 'a' :
        print_all_averages()
    elif choice == 'b' :
        user_subject = input("what subject? ")
        print_average(user_subject)
    elif choice == 'c' :
        print(get_GPA(), "is the GPA")
    else : # if choice is d or if user inputs something other than a, b, c, d
        user_subject = input("what subject? ")
        user_grade = input("what grade should be added with that subject? ")
        add_grade(user_subject, user_grade)
        print("a grade of", user_grade, "has been added to", user_subject)

def add_grade(subject, grade) : # to add a new grade to all_grades
    new_subject = False
    for i in range (len(all_grades)) :
        if list(all_grades)[i] == subject :
            new_subject = True
    if new_subject == True :
        all_grades[len(all_grades)] = subject
    all_grades[subject]=grade

def print_average(subject) : # prints the average grade of a subject
    sum = 0
    for i in range (len(all_grades[subject])) :
        sum = sum + all_grades[subject][i]
    print(sum/len(all_grades[subject]))

def print_grades(subject) : # prints all the grades in a given subject
    for i in range (len(all_grades[subject])) :
        print(all_grades[subject][i])

def print_all_averages(): # prints the average in every subject
    averages = {}
    for subject in all_grades :
        average = 0
        for grade in all_grades[subject] :
            average += grade
        average = average/len(all_grades[subject])
        averages[subject] = average

    for subject in averages:
        print("average grade in", subject, "-", averages[subject])

def get_GPA(): # returns GPA on a 4.0 across all subjects
    averages = {}
    for subject in all_grades :
        average = 0
        for grade in all_grades[subject] :
            average += grade
        average = average/len(all_grades[subject])
        averages[subject] = average
    
    gpa_100 = 0 # represents numerical gpa on a 100pt scale
    for subject in averages:
        gpa_100 += averages[subject]
    gpa_100 = gpa_100/len(averages)

    gpa_4 = 0.0 # represents gpa on a 4.0 scale
    if gpa_100 >= 92.5 :
        gpa_4 = 4.0
    elif gpa_100 >= 89.5 :
        gpa_4 = 3.7
    elif gpa_100 >= 79.5 :
        gpa_4 = 3.0
    elif gpa_100 >= 69.5 :
        gpa_4 = 2.0
    elif gpa_100 >= 65.0 :
        gpa_4 = 1.0

    return gpa_4
       

if __name__ == "__main__": # i guess the main method needs to run 
    main()