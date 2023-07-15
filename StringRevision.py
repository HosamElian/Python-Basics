a = "#######i love pyton#######"

print( a)
print(len(a))
# string.strip() remove char from word start and end
# if no parameter given its remove white space 
print(a.strip("#"))
# only delete from right 
print(a.rstrip("#"))
# only delete from left 
print(a.lstrip("#"))

print("------------------------------------------")
q = "I Love Python"

# print(q.rjust(10, "!"))
# print(q.ljust(10,"!"))

# string.title() capitalize char in start of every word and after numbers
print(a.title())
# capitalize like title() but not capitalize char after numbers
print(a.capitalize())

# zfill if i have 1, 11 ,111 => will change it to 001, 011, 111
b, c, d = "1", "11", "111"

print(b.zfill(3)) #001
print(c.zfill(3)) #011
print(d.zfill(3)) #111

mySting = "I love Python and Dot net"
print(mySting.split()) # takes first argus => split char, second => max number to split 

mySting = "I-love-Python-and-Dot-net"
print(mySting.split("-", 3))

name = "hosam"

print(name.center(9, "#")) #takes argus => take number of string char will return
                     # takes => what will it add before and after default==spaces

mySting = "I love Python and Dot net"
startIndex = 0
endIndex = len(mySting)
print(mySting.count("net", startIndex, endIndex))

print(mySting.swapcase())

mString  = "I am Hosam"
print(mString.startswith("I")) # true 
print(mString.startswith("I"), startIndex, 10) # true

print(mString.endswith("I")) # false 
print(mString.endswith("m"), startIndex, 10) # true

print(mString.index("m", startIndex, endIndex)) # if exsist return index else throw an exception
print(mString.find("m", startIndex, endIndex)) # if exsist return index else -1

w = """
First Line
Second Line
Third Line
"""
print(w.splitlines())

e = "First Line\tSecond Line\tThird Line"
print(e.expandtabs(2)) # number of spaces tab will add

#check string
print(e.islower())
print(e.isspace())
print(e.istitle())
print(e.isidentifier()) # check if sring can use as name for variable

r = "hhhhhhhaaaaaaaa"
t = "aaaaaaaaaassssss333"

print(r.isalpha()) # true if contain all char => true
print(t.isalpha()) # false becaue it's contain numbers


print(r.isalnum()) # true if contain all char
print(t.isalnum()) # true becaue it's contain numbers + char
numberofWordToReplace = 3
print(r.replace("h", "Hosam", numberofWordToReplace))

mylist = ["hosam", "Mahmoud", "Elian"]

print(" ".join(mylist))
print("-".join(mylist))
print(", ".join(mylist))


name = "Hosam"
age = 10
money = 10344.01546
# foramts
# old way
print("I'm %s my age is: %d and i have %.2f dollers"% (name, age, money))

# new way
print("I'm {:s} my age is: {:d} and i have {:.2f} dollers".format(name, age, money))

# in version 3.6+
print(f"I'm {name} my age is: {age} and i have {money} dollers")

# truncae

#old way
mySting = "I love people how can understand me and not try to win arrg"
print("My Message is %s" % mySting)
print("My Message is %.38s" % mySting)

# new way
print("My Message is {:s}".format(mySting) )
print("My Message is {:.38s}".format(mySting) )

#money format

print("My money is: {:_f}".format(money))
print("My money is: {:,f}".format(money))

e = "one"
r = "two"
t = "three"
print("Hello {2} {1} {0}".format(e, r, t))
print("Hello {2:s} {1:s} {0:s}".format(e, r, t))
