intNumber = 10
floatVersion = float(intNumber)
complexVersion = complex(intNumber)

print(type(intNumber))
print(type(floatVersion))
print(type(complexVersion))

# list
# myList[start:end:steps]

myList = ["one", "two", "three", 20, 102.32, "four", "five", True]

print(myList) #"one", "two", "three", 20, 102.32, "four", "five", True
print(myList[0]) # one
print(myList[-1]) # True
start = 0
end = 8
steps = 1
print(myList[1:5:steps]) # "two", "three", 20, 102.32, 
print(myList[1:]) # "two", "three", 20, 102.32, "four", "five", True
print(myList[:4]) # "one", "two", "three", 20, 102.32,

myList[0:2] = [] # ---empty first and second item in list-- "three", 20, 102.32, "four", "five", True  
myList.append("object")
myList.append(["hosam", "ahmed", "mohamed"]) # will add list as item
print(myList)

a = [1, 2, 3, 4, 9]
b = [5, 6, 7, 8]
a.extend(b) # will extend my old list to with added list
print(a)

a.remove(9) # will reomve first item it meet
print(a)

c = [10, 1000, -20, 6]
c.sort(reverse=True) # will sort them but if reverse to sort then in reverse Note: dont mix numbers and alpha
print(c)
c.sort(reverse=False) # will sort them but if reverse to sort then in reverse
print(c)

d = ["hosam", 2, 5, "all"]
d.reverse()
print(d)

# clear items
f = d.copy()
d.clear()
print(d)

# index
print(f.index(2))

# insert(atIndex, value)
f.insert(0, "hosam")


# count 
print(f.count("hosam"))

print(f)

# pop 
print(f.pop(-1))