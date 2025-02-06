try:
    username =input("Enter your name: ")
    print("Hello : " + username + "! Have a great day! ")
except EOFError:   
    print("No input recieved! ")