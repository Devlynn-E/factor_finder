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

    

statement_gen("factor finder", "*")

instructions = input("would you like instructions? <y> for yes, <n> for no ")

instructions_yes = ["y"]

if instructions in instructions_yes:
    print("\ninput an integer between 1 and 200 (inclusive)")

num_check(int(input("what is your number (1-200): ")))


