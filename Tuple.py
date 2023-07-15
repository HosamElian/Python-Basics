# tuple are same as list
# tuple are immutple => can't be aasign or remove or clear


myTupleOne = (1, 2, 3, 4, 5, 6)
print(myTupleOne)

myTupleTwo = 1, 2, 3, 4, 5, 6
print(myTupleTwo)

oneItemTupleOne = ("Hosam",)
oneItemTupleTwo = "Ahemd",

# tuple concatenation
tupleConcatenation = oneItemTupleOne + ("Ameen", "Mohamed") + oneItemTupleTwo
print(tupleConcatenation)

# Repeat
print("Hosam\t" * 6)
print(("Hosam", "Mahmoud") * 6)
print(["Hosam", "Mahmoud"] * 6)

# count
print(tupleConcatenation.count("Ameen"))

# index 
print(tupleConcatenation.index("Ameen"))

# tuple destruct

print("------------")
a = (1, 2, 3)
x, y, z = a
print(x)
print(y)
print(z)

# or 
a = (1, 2, "sa", 3)
x, y, _, z = a
print(x)
print(y)
print(z)