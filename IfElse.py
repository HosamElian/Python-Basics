name = "Hosam"
country = "kuwait"
course = "Python Course"
price = 100

if country == "egypt":
    print(f"Hello {name} because you from {country}")
    print(f"The course {course} Price is {price - 80}")
elif country == "kuwait":
    print(f"Hello {name} because you from {country}")
    print(f"The course {course} Price is {price - 50}")
else:
    print(f"Hello {name} because you from {country}")
    print(f"The course {course} Price is {price - 30}")