# inheritance
class Food:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"Create Base class with name: {self.name} price: {self.price}")

    def eat(self):
        print("Eat from Base Class")

class Apple(Food):
   
    def __init__(self, name, price, amount):
        
        self.amount = amount
        super().__init__(name, price) # or Food.__init__(self, name, price)

        print(f"Create drived class with name: {self.name} price: {self.price} and amount {self.amount}")

a = Apple("Apple", 20, 100)
h = Food("orange", 20)

print("=" * 50)

# multiple inheritance

class BaseOne:
    def __init__(self):
        return"From BaseOne"
    
    def funOne(self):
        return"From BaseOne_funOne"

class BaseTwo:
    def __init__(self):
        return"From BaseTwo"
    
    def funTwo(self):
        return "From BaseTwo_funTwo"

class DrivedClass(BaseOne, BaseTwo):
    def __init__(self):
        pass


drivedClass = DrivedClass()

print(drivedClass.funOne())
print(drivedClass.funTwo())

print("=" * 50)

# polymorohism
# override
class A:

    # impelement Class method in childs
    def doSomeThing(self):
        print("ClassA -> doSomeThing")
        raise NotImplementedError("implement this method")


class B(A):
    def doSomeThing(self):
      print("ClassB -> doSomeThing")

b = B()
b.doSomeThing()

print("=" * 50)

# Encapsulation
# public => any place
# protected => class and sub-classes => no error if access
# private => class only ==> error if access unless using instnce._ClassName__privateProp

class C:
    def __init__(self, name):
        # public
        self.name = name
        # protected _name
        self._nameTwo = ""
        # private __name
        self.__nameThree = ""
    
    # function as prop
    @property
    def sayHello(self):
        print(f"hello {self.name}")

print("=" * 50)
derivadc = C("hosam")
derivadc.sayHello


print("=" * 50)

# Abstract

from abc import ABCMeta, abstractmethod
class abs(metaclass=ABCMeta):
    
    @abstractmethod
    def doSomething(self):
        pass