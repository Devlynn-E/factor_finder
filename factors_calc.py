def statement_gen(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def num_check(question):

    valid = False
    while not valid:

        error = "please input an integer that is more than ""(or equal to) 1"

        try:

            response = int(input(question))

            if response >= 1:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)

    valid = False
    while not valid:

        error = "please input a number above zero"

        try:

            num = int(input("enter the number: "))

            if num >= 1:
                valid = True

            else:
                print(error)
                print()

        except ValueError:
            print(error)


def get_factors(to_factor):

    # me when


statement_gen("factor finder", "*")

instructions = input("would you like instructions? <y> for yes, <n> for no ")

instructions_yes = ["y"]

if instructions in instructions_yes:
    print("\ninput an integer between 1 and 200 (inclusive)")

keep_going = ""
while keep_going == "":

    comment = ""

    var_to_factor = num_check("number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "one is UNITY! It only had one factor. Itself."

    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    statement_gen(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or <any> to stop")
    print()

print("\nThank you for using the factors calculator")
