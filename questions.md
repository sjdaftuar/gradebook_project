1. the general purpose of my program is to provide a user with the ability to navigate a dictionary
of subjects with associated assessment grades. the user uses the menu to perform actions/changes/get info
about gradebook, and the functions exist to return said information to user

2. two possible expected users are students and school admin/teachers (who want to keep records).
the program targets these two by storing all current grades, separated by subject. the get_GPA()
and print_average() functions are particulary helpful for a student or teacher who wishes to see
how one (a student) is doing academically.

3. one non-negotiable of this project is the add_grade() function. not having it completely
defeats the purpose of this being a gradebook that can change. the get_GPA() funciton is nice
to have but is not necessary since it's an operation done on the grades, but doesn't
impact the existing grades or what will be inputed

4. 1 - have the menu options run continuously, so once the user does something they can do another thing
without restarting program (maybe like a while true?)
2 - the option to remove grades. this would help if, say, a grade changes (maybe a curve was added)