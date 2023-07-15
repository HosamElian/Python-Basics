
# string
email = "hosamemm@gmail.com"

Name = input("Please enter You name: ").strip().capitalize()
email = input("Please enter You email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1 :]
print(f"Hello {Name}!!")
print(f"Your username is: {username}  and your domain: {domain}")