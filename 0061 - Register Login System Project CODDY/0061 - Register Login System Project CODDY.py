def maintain_set(a_set, number):
    # Your code here
    if number in a_set:
        return number * 2
    else:
        a_set.add(number)
        return a_set
    
class LoginSystem:
    def __init__(self):
        self.users = dict()
        self.logged_users = set()
        self.mapping = {
   "a" : "i", "b" : "l", "c" : "q", "d" : "f", "e" : "z", "f" : "s",
   "g" : "a", "h" : "g", "i" : "e", "j" : "p", "k" : "w", "l" : "o",
   "m" : "v", "n" : "u", "o" : "b", "p" : "j", "q" : "k", "r" : "n",
   "s" : "x", "t" : "d", "u" : "h", "v" : "y", "w" : "t", "x" : "m",
   "y" : "r", "z" : "c"
}
        
    def encrypt(self, password):
        titkositott_pw = ""
        for letter in password:
            if letter.lower() in self.mapping:
                titkositott_pw += self.mapping[letter.lower()]
        return titkositott_pw


    def register(self, username, password):
        if username in self.users:
            print("user already exists")
        else:
            self.users[username]=self.encrypt(password)
            print("user registered successfully")
    def login(self, username, password):
        if username in self.users:
            if self.users[username] == self.encrypt(password):
                self.logged_users.add(username)
                print("user logged in successfully")
            else:
                print("password doesn't match")
        else:
            print("user isn't in the system")
    
    def sign_out(self, username):
        if username in self.users:
            if username in self.logged_users:
                self.logged_users.remove(username)
                print("user signed out successfully")
            else:
                print("user is not logged in")
        else:
            print("user is not in the system")
