# Is key value pair object
# Key can be any object type thing but not list
# value can be any object type
# must key be unique or it will take last value of key with same name
# not orderd but acces by key

user = {
   "name" : "hosam",
   "age" : 39,
   "country" : "egypt",
   (1, 2, 3, 4) : "tuple" 
}
print(user)

# get item
print(user["name"])
print(user.get("name"))

# print keys or values
print(user.keys())
print(user.values())

# 2D dictionary
languages = {
    "one" : {
        "name" : "html",
        "progress" : "80%"
    },
    "two" : {
        "name" : "CSS",
        "progress" : "90%"
    },
    "three" : {
        "name" : "js",
        "progress" : "95%"
    }
}

# print item in 2D Dictionary
print(languages["one"]["name"])

# clear
languages.clear()
print(languages)

# update

languages["name"] = "programming language"
languages.update({"play": "football"})

a = languages.copy()

# setdefault
a = {
    "name" : "Hosam"
}

print(a)
a.setdefault("name", "mahmoud")
print(a)

# popitem => return last add item
print(a.popitem())

# get all item => all item even if added after line of coping
# retun data in list of tuple

a = languages.items()
print(a)

# create dictionary
a = "name", "age", "type"
b = "hosam"
print(dict.fromkeys(a, b))