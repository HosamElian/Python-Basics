import os
path = "test.txt"
# cwd = os.getcwd()

# # main currenct working directory
# print(cwd)
# # abs path
# print(os.path.abspath(__file__)) 
# # # current file
# print(os.path.dirname(__file__))
# # change current working dir
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# # dir of opened file
# print(os.path.abspath(os.path.dirname(__file__)))

# r"xz" => mean it's row string dot change and special char

## by default 'r'=> reading    

the_file = open(f"{path}")

# file date
print(the_file)
print(the_file.name)
print(the_file.mode)
print(the_file.encoding)

# read line file  (numOfData)
print(the_file.readline())


# read lines in file  (numOfData)
print(the_file.readlines())

# close file
the_file.close()


# by default 'w'=> write on exist
the_file = open(path, 'w')
the_file.write("Hello world\n")
myList = ["hosam", "ahmed", "mahmoud"]

the_file.writelines(myList)
# close file
the_file.close()


# by default 'a'=> append at end
the_file = open(path, 'w')
the_file.write("Hello world\n")
# myList = ["hosam", "ahmed", "mahmoud"]

# the_file.writelines(myList)
# close file
the_file.close()


# by default 'w'=> write on exist
the_file = open(path, 'w')
the_file.write("Hello world")
myList = ["hosam", "ahmed", "mahmoud"]

#functions
the_file = open(path, 'w')

# truncate 5 lines
the_file.truncate(5)

# set cursor position
the_file.seek(20)
# get cursor position
print(the_file.tell())

# close file
the_file.close()


# remove File
os.remove(path)