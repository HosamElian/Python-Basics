# DocString: use to document func, class, module
# type:

#  single line
'''single line Documentaion'''

#  multiple line
"""
multiple line Docstring 
"""


def sayHello():
    '''My docString to say why we create this'''
    print("hello")

# to it
print(sayHello.__doc__)
help(sayHello)