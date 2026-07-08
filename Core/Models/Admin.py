from .User import User

class Admin(User):
    
    def __init__(self , username , password):
        
        super().__init__(username)
        self.password = password
        
    def role(self):
        
        return "Admin"
    
    def verify_password(self , password):
    
        # just hash the password and compare it with the stored password in the database
        pass
        
    def change_password(self , new_password):
        
        # if the hashed new password is the same as the old password then alert the user that the password has been changed
        # else change the password
        pass