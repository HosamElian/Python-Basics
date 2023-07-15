### while loop

# simple while loop
a = 0
while  a < 10:
    print(a)
    a += 1

print("loop is Done")

print("=" * 50)

# with list
myList = ["Hosam", "Ahmed", "Mahmoud", "Ali", "Sayed"]
a = 0
while a < len(myList):
    print(myList[a])
    a +=1
print("=" * 50)

# example
# tries = 4
# myPassword = "hosam123"
# inputPassword = input("Please Enter Your Password: ")
# while inputPassword != myPassword:
#     print(f"wrong password, {'Last' if tries == 1 else tries} Left")
#     inputPassword = input("Please Enter Your Password: ")
#     tries -=1
#     if tries == 0:
#         print("try again in 5 min")
#         break

# print("=" * 50)

# for Loop

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in myList:
    print(n)

print("=" * 50)
# even check
for n in myList:
    if(n % 2 == 0):
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

print("=" * 50)

# for With Dictionary

myskillDictionary = {
    "html" : "50",
    "css" : "40",
    "js" : "80",
    "dot net" : "90"
}
# print(myskillDictionary["html"])
# print(myskillDictionary.get("html"))
for skill in myskillDictionary:
    # print(f"{skill} => {myskillDictionary.get(skill)}") 
    print(f"{skill} => {myskillDictionary[skill]}") 
# or
print("##" * 50)
print(myskillDictionary.items())
for key, value in myskillDictionary.items():
    print(f"{key} => {value}") 

print("=" * 50)

# nested for with nested dictionary

peoples ={
    "Hosam" :{
    "html" : "50",
    "css" : "40",
    "js" : "80",
    "dot net" : "90"
    },
    "Ahmed" : {
    "html" : "50",
    "css" : "40",
    "js" : "80",
    },
    "Mahmooud" : {
    "dot net" : "90"
    } 
}
for person in peoples:
    print(f"{person} have skills in:-")
    for skill in peoples[person]:
        print(f"- {skill} => {peoples[person][skill]}")

# or
print("##" * 50)

for main_key, main_value in peoples.items():
    print(f"{main_key} have skills in:-")
    for child_key, chile_value in main_value.items():
        print(f"- {child_key} => {chile_value}")

print("=" * 50) 

print("Continue, Break, Pass")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in myList:
    if n == 3:
        continue # dont print and complete for loop
    if n == 9:
        break # go out of loop
    print(n)

for n in myList:
    pass # if i dont declar any use so i write pass to avoi error

print("=" * 50) 

# zip() => return objects contains all objects
# lenght of zip object is lowest lenght of objects

list1 = range(5)
list2 = ["a", "b"]
tuple1 = ("man", "women", "boy", "girl")
dic1 = {"name": "hosam", "age": 25, "country": "egypt" }

# loopZip = zip(list1, list2)
# for i in loopZip:
#     print(i)
for item1, item2, item3, item4 in zip(list1, list2, tuple1, dic1):
    print(f"_{item1}_{item2}_{item3}")
    print("Dic1 => key", item4, "Dic1 => value", dic1[item4])