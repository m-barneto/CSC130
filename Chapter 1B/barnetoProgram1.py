def is_valid_choice(input):
    return input == "a" or input == "d" or input == "e"


courses = []
while True:
    choice = input("Enter A to add course, D to drop course, and E to exit: ").lower()
    while not is_valid_choice(choice):
        print("Invalid choice.")
        choice = input("Enter A to add course, D to drop course, and E to exit: ").lower()
    if choice == "a":
        course = input("Enter course to add: ").upper()
        if course in courses:
            print("You are already registered in that course.")
        else:
            courses.append(course)
            courses.sort()
            print("Course added.")
            print("Courses registered:", courses)
    elif choice == "d":
        course = input("Enter course to drop: ").upper()
        if course in courses:
            courses.remove(course)
            print("Course dropped.")
            print("Courses registered:", courses)
        else:
            print("You are not registered for that course.")
    else:
        break

    print()
