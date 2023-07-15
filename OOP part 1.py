# Class method
# 1- Class => take decorator (@classmethod) and cls as first parameter and used by ClassName.MethodName()
# 2- instance  => take self as first parameter and used by ClassName.MethodName()
# 3- Static => () take decorator (@staticmethod) used by ClassName.MethodName()
# 4- magic => () used by ClassName.MethodName()
    # like :
    #  __init__(self) => initialize
    #  __str__(self)  => human readable output
    #  __len__(self)  => return lenght of CNTR

class Member:
    # attribute for class
    notAllowedNames = ["mo", "so", "ko"]
    userNumbers = 0

    def __init__(self, firstName, middleName, lastName, gender):
       # attribute for instance
        self.fname = firstName
        self.mname = middleName
        self.lname = lastName
        self.gender = gender
        Member.userNumbers += 1

    def __str__(self):
        return f"This class are used to store user data"

    def __len__(self):
        return len(self.fname)

    # Instance method
    def getFullName(self):
        if self.fname in Member.notAllowedNames:
            raise ValueError("Not allowed name")
        else:
            return f"{self.fname} {self.mname}  {self.lname}"
    
    # instance method
    def nameWithTitle(self):
        if(self.gender.lower() =="male"):
            return f"Hello Mr. {self.fname}"
            
        else: 
            return f"Hello Mrs. {self.fname}"
    
    # instance method
    def deleteUser(self):
        Member.userNumbers -= 1
        return f"{self.fname} Has been deleted !"    

    # static method
    @staticmethod
    def sayHello():
        return "Hello"

    # Class method
    @classmethod
    def showUsersCount(cls):
        return f"We Have {cls.userNumbers} Users in Our Systems."

# call
a = Member("Ahmed", "Mahmoud", "Elian", "Male")
h = Member("Hosam", "Mahmoud", "Elian", "Male")
y = Member("yasmin", "Mahmoud", "Elian", "Female")

print("=" * 50)

# get class function
print(dir(Member))
print("=" * 50)

# get Parent class 
print(a.__class__)
print("=" * 50)

# get class info
print(a.fname)
print(h.fname)
print("=" * 50)


# use function
print(a.getFullName())
print(h.getFullName())
print(h.nameWithTitle())
print(y.nameWithTitle())
print(Member.userNumbers)
print(y.deleteUser())
print(Member.showUsersCount())
print(h)
print(len(h))
print("=" * 50)

# print(dir(dir))