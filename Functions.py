# def functionName(parameter):
#     body
# functionName(arguments)

# no parameter no return
def HelloMsg():
    print("Hello Hossam")

HelloMsg()
print("=" * 50)

# parameter no return
def HelloMsgWithParameter(name):
    print(f"Hello {name}")

HelloMsgWithParameter("hosam Elian")
print("=" * 50)

# parameter And return
def HelloMsgWithParameterAndReturn(name):
    return f"retrun {name}"
value = HelloMsgWithParameterAndReturn("hosam Elian")

print(value)
print("=" * 50)

# default value must be last parameter
# if its first one any parameter after it should have default value too
def HelloMsgWithParameterAndReturn(name = "unknown"):
    print(f"{name}")
HelloMsgWithParameterAndReturn("hosam Elian")

print("=" * 50)

# packing and unpacking  
# *Args => any number of argus as tuple 
# **Args => any number of argus as dictionary 
# if *[1, 2, 3, 4] => 1, 2, 3, 4
myList = [1, 2, 3, 4]
print(myList)
print(*myList)

print("=" * 50)

name = "hosam"
tup = ("don net", "Mysql", "SQL Server")
dic = {"skill":"JS", "skill-2": "Html", "skill-4":"CSS"} # call - 2

def skillsWithTupleAndDictionary(name, *skills, **skillsWithProgress): # tuple
    print(f"Hello {name} - You skills Without progress:")
    for skill in skills:
        print(f"{skill}")
    print(f"Hello {name} - You skills With progress:")
    for key, value in skillsWithProgress.items():
        print(f"{key} => {value}")

# Calling ways
skillsWithTupleAndDictionary("hossam") # call - 1
print("=" * 50)

skillsWithTupleAndDictionary("hossam", *tup) # call - 2
print("=" * 50)

skillsWithTupleAndDictionary("hossam", **dic) # call - 3
print("=" * 50)

skillsWithTupleAndDictionary("hossam", tup, skill="Html", skill2="CSS", skill3="JS") # call - 4
print("=" * 50)

skillsWithTupleAndDictionary("hossam", *tup, **dic) # call - 5
print("=" * 50)

x = 1
def changeGlobalValue():
    global x
    x = 2
    print(f"value for x is {x}")

print(f"value for x is {x}")
changeGlobalValue()
print(f"value for x is  after gloabal change {x}")

print("=" * 50)

def wordCuttingRecursion(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return wordCuttingRecursion(word[1:])
    return word[0] + wordCuttingRecursion(word[1:])

print(wordCuttingRecursion("wwwwwwwwooorddd"))

print("=" * 50)

# lambda  function

def printHello(name):
    print(f"Hello {name}")
hello = lambda name : print(f"Hello {name}")

printHello("Hosam")
hello("Hosam")

print(printHello.__name__)
print(hello.__name__)
print("=" * 50)


# ======================= BuildIn Functions =======================
print("======================= BuildIn Functions =======================")


x = [1, 2, 3, 4]

if all(x): # must all are true
    print("All x items are true")
else:
    print("Not All x items are true")

print("=" * 50)

if any(x): # at leaste one are true
    print("there items in  x are true")
else:
    print("Not item in x are true")

# get binary of number
print(bin(100))

# Get var place in memory
x = 1
print(id(x))
# sum
numberWillAddOnList = 40
a = [10, 20, 30]
print(sum(a))
print(sum(a,numberWillAddOnList))

# round to up if more than 0.5
print(round(150.50, 2)) # 150 and get 2 number after mark
print(round(150.52)) # 151

# range(start, end, step)
print(list(range(10)))
print("Hello", "Hossam", sep="_") # change separator from space to _

# abs()
print(abs(100))
print(abs(-100))

# pow(base, exp, mod) base = 2, exp = 2, mod= after get the value of (2**2) % mod
print(pow(2, 2))

# min(item, item or iterator) get min
print(min(list(range(10))))

# max(item, item or iterator) get max
print(max(list(range(10))))

# slice(start, stop, step)
name = "hosam"
print(name[slice(2)])

# map(function, iterator) 
def formatedText(text):
    return f" - {text} -"
myList = ["Ahmed", "Mahmoud", "Elian"]
for name in map(formatedText, myList):
    print(name)

for name in map(lambda text : f" - {text} -", myList):
    print(name)

print("=" * 50)

# filter(function, iterator)
myList = [10, 20, 30, 40]
def compare(num):
    if num> 10:
        return num
for num in filter(lambda num : num > 10, myList):
    print(num)

print("=" * 50)

# reduce(function, iterator)

from functools import reduce
print(reduce((lambda num1, num2: num1 + num2), [1, 2, 3, 4]))

print("=" * 50)

# enumerate(list, counterStart) => add conter to my list by default like this (0, "HTML"), ....
for counter, skill in enumerate(["HTML", "CSS", "JS"]):
    print(f"{counter} - {skill}")

print("=" * 50)

# help => show help about something
# print(help(print))

print("=" * 50)

# reverse => reverse iterable
name = "hosam"
for n in reversed(name):
    print(n)

print("=" * 50)

# random number
import random
print(f"float random {random.random()}")
print(f"int random {random.randint(100, 200)}")

print("=" * 50)

# print all data in object
print(dir(random))

print("=" * 50)

# colored nice text

import pyfiglet, termcolor
print(termcolor.colored(pyfiglet.figlet_format("Hossam Elian"), "yellow"))

print("=" * 50)
