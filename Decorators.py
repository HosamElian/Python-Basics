# Decorator: higher order function
# enhance function behavior

def decoratorFunction(func):
    
    def nestedFunction():
        print("before")
        func()
        print("after")
    return nestedFunction

# new
@decoratorFunction
def sayHello():
    print("Hello from say hello function")

sayHello()

# # old
# deco = decoratorFunction(sayHello)
# deco()

print("=" * 50)

# function with parameter

def decoratorFunctionWithParameter(func):
    
    def nestedFunction(num1, num2):
        print("before")
        func(num1, num2)
        print("after")
    return nestedFunction

@decoratorFunctionWithParameter
def Calculate(num1, num2):
    print(num1 + num2)

Calculate(1, 2)

# best practice => anynumber of argus
def decoratorFunctionWithParameter(func):
    
    def nestedFunction(*numbers):
        print("before")
        func(*numbers)
        print("after")
    return nestedFunction

# speed test
def speedTest(func):

    def nestedFunction():
        start = time()

        func()

        end = time()

        print(f"function run for {end - start} ")
    return nestedFunction
