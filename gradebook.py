all_grades={"data science":[88, 100, 95], "latin":[94,82,99], "chemistry":[86, 98, 91]}

def main(): # main method!
    add_grade("english", 96)
    print_average("data science")
    print_grades("data science")

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

if __name__ == "__main__": # i guess the main method needs to run 
    main()