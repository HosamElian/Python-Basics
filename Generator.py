# generator is funcction like normal function but use yield instead of return
# return iterator and support next()
# continue where you call it not from start

def myGenerator():

    yield 1
    yield 2
    yield 3
    yield 4

gene = myGenerator()
# type => generator
print(type(gene))
# next()
print(next(gene))

# support iteration
for num in myGenerator():
    print(num)