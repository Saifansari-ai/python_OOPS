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
             pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
 

    
chat = chatbook()