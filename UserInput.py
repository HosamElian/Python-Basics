fName = input("Please enter you frist name: ")
mName = input("Please enter you Middle name: ")
lName = input("Please enter you last name: ")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f" Hello Mr.{fName} {mName:.1s} {lName}")