# Set not orderdand not indexing and not slicing
# can contain any immutable type but not  List or Dict
# items is unique if repeated it will remove second item
mySet = {"Hosam", "Mahmoud", 100}
print(mySet)

# clear
mySet.clear()

# union
a = {1, 2, 3}
b = {4, 5, 6}
d = {7, 8, 9}
c = a | b
print(c)
# or 
c = a.union(b, d)
print(c)
# or 
c.update({45,46, 47})
# or
c.update([49, 50])

# Add
c.add(10)
print(c)

# Copy
f = c.copy()
print(f)

# remove by value if itemnot exist throw error
f.remove(10)
print(f)

# discard = remove 
# discard not throw an error
f.discard(10)

# pop => random element
print(f.pop())

# difference => find item in set1 not in set2 == a-b
a = { 1, 2, 3, 4, "Hosam"}
b = {1, 3, 5}
print(a.difference(b))

# difference_update  => find item in set1 not in set2 == a-b
# then update ''c'' with founded item
c = { 1, 2, 3, 4, "Hosam"}
d = {1, 3, 5}
c.difference_update(b)
print(c)

# intersection == c & d
c = { 1, 2, 3, 4, "Hosam"}
d = {1, 3, 5}
c.intersection(b)
print(c)


# intersection_update == c & d 
# then update ''c'' with founded item
c = { 1, 2, 3, 4, "Hosam"}
d = {1, 3, 5}
c.intersection_update(b)
print(c)


# symmetric_difference == c ^ d item not found in both
c = { 1, 2, 3, 4, "Hosam"}
d = {1, 3, 5}
c.symmetric_difference(b)
print(c)

# symmetric_difference == c ^ d item not found in both 
# then update ''c'' with founded item
c = { 1, 2, 3, 4, "Hosam"}
d = {1, 3, 5}
c.symmetric_difference_update(b)
print(c)

#  issuperset a have all b items
a = { 1, 2, 3, 4, "Hosam"}
b = {1, 3, 5}
print(c.issuperset(d))


#  issubset a part of b
a = { 1, 2, 3, 4, "Hosam"}
b = {1, 3, 5}
print(c.issubset(d))

# isdisjoint a not contain any item of b
print(a.isdisjoint(b))
