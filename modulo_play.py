keep_going = ""
while keep_going == "":

    num_lollies = int(input("how many lollies? "))
    num_students = int(input("how many students? "))

    lollies_per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    if lollies_left == 1:
        lolly_pl = "lolly"
    else:
        lolly_pl = "lollies"

    print("\nYou have {} lollies and {} students".format(num_lollies, num_students))
    print("each student gets {} lollies".format(lollies_per_student))
    print("You have {} {} left".format(lollies_left, lolly_pl))
    print()

    keep_going = input("again <enter>? ")
    print()
