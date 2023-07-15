# regular expression is wild card to match what you want to test
# \w => match word
# \W => match non word

# \d => match Digit
# \D => match non Digit

# \s => match space
# \S => match non space

# [A-Z] from A - Z cap.
# [a-z] from A - Z small
# [0-9] from 0 - 9
# [\.] special character .

# ^xxx start of word
# xxxx$ end of word

# [A]+ one or more from char
# [A]* zero or more from char

# () group of condition
# | or
# \ esc for special char 
# x? if x exits it's ok=1 else ok too=0 

# match mail
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+

# match Password like this xxxx@xxxx

# [A-z0-9\.]+@[A-z0-9\.]

import re

my_search = re.search("[A-Z]", "Hosam Elian")
print(my_search)
print(my_search.span())
print(my_search.string)
print(my_search.group())

print("=" * 50)

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", "hosamemm@gmail.com")
if is_email:
    print("valid")
else:
    print("not email")

print("=" * 50)

# findall return all match or []
# email_input = input("Please Enter your Email")
# search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.[A-z]+", email_input)

# email_list = []

# if search != []:

#     email_list.append(search)
#     print("valid")
# else:
#     print("invalid")


# split (regular expression, string, time or split for matchs)
myStr = "I Love Python"

search = re.split(r"\s", myStr)
print(search)

# sub (expression, replaceType, stringTochange, replaceCount)
search1 = re.sub(r"\s", "-", myStr, 2)

print(search1)