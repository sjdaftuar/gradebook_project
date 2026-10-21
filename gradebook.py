all_grades={"data science":[88, 100, 95], "latin":[94,82,99], "chemistry":[86, 98, 91]}

def main(): # main method!
    print(all_grades)
    add_grade("english", 93)
    print(all_grades)

def add_grade(subject, grade) : # to add a new grade to all_grades
    new_subject = False
    for i in range (len(all_grades)) :
        if list(all_grades)[i] == subject :
            new_subject = True
    if new_subject == True :
        all_grades[len(all_grades)] = subject
    all_grades[subject]=grade

if __name__ == "__main__": # i guess the main method needs to run 
    main()