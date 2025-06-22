class chatbook:
    
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""wellcome to the chatbook,do the following steps to use the chatbook:
          1.press 1 to signup
          2.press 2 to signin
          3.press 3 to post 
          4.press 4 to message a friend
          5.press anykey to exit
          """)
    
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.msg()
        else:
            exit()
 
    def signup(self):
        user = input("enter your email :")
        pwd = input("Create a password :")
        self.username = user
        self.password = pwd
        print("You have signup successfully!!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            user = input("enter your email/username here ->")
            pwd = input("Enter your password here ->")
            if self.username == user and self.password == pwd:
                print("You have logged in successfully!!")
                self.loggedin = True
            else:
                print("Invalid username or password")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your post here -> ")
            print(f"your post has been uploaded successfully and the content is {txt}")
        else:
            print("Please signin first by pressing 2 in the main menu")
            print("\n")
            self.menu()

    def msg(self):
        if self.loggedin == True:
            msg = input("Enter your message here ->")
            frnd = input("Whom to message ->")
            print(f"Your message {msg} has been sent to {frnd}")
        else:
            print("Please signin first by pressing 2 in the main menu")
            print("\n")
            self.menu()
        



user_1 = chatbook()