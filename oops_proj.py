class chatbook:
    
    __user_id = 0 #static value
    
    def __init__(self):
        self.id = chatbook.__user_id #class is accessing it
        chatbook.__user_id += 1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False

    @staticmethod
    def get_id(): #No need to give any self
        return chatbook.__user_id

    @staticmethod
    def set_id(value): #No need to give any self
        chatbook.__user_id = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value    
    
    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           """)
        
        if user_input == "1":
            self.signup()

        elif user_input == "2":
            self.signin()

        elif user_input == "3":
            self.write_post()
            
        elif user_input == "4":
            self.send_message()
            
        else:
            exit()

    def signup(self):
        email = input("Enter your email here: ")
        pwd = input("Set up your password here: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()


    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/ username here: ")
            pwd = input("Enter your password here: ")

            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!")
                self.loggedin = True
            else:
                print("Please input the correct credentials")
        
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin == True:
            txt = input("Enter your post here: ")
            print(f"Following Content has been posted: {txt}")
        else:
            print("Please signin first to make a Post on ChatBook.")

        print("\n")
        self.menu()    

    def send_message(self):
        if self.loggedin == True:
            friend = input("Whom to send the message? ")
            mssg = input(f"Enter the message you want to send to {friend}")
            print(f"Your Message: {mssg} ,has been sent to {friend}")
        
        else:
            print("Please signin first")
        
        print("\n")
        self.menu()  

obj = chatbook()
