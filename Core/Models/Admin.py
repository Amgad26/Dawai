from User import User
class Admin(User):
    
    def __init__(self , username , password , address):
        
        super().__init__(username , address , role = "Admin")
        self.password = password
        
    def get_role(self):
        
        return self.role
    
    def verify_password(self , password):
    
        # just hash the password and compare it with the stored password in the database
        pass
        
    def change_password(self , new_password):
        
        # if the hashed new password is the same as the old password then alert the user that the password has been changed
        # else change the password
        pass