try:
    username =input("Enter your name: ")
except EOFError:   
    name = "mary"
print("Hello : " + username + "! Have a great day! ")