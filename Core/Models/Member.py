from User import User

class Member(User):
    
    def __init__(self , username , medicines): # medicines is a list of medicines it will be empty at first
        
        super().__init__(username)
        
    def role(self):
        
        return "Member"
    
    def add_medicine(self , medicines):
        
        # choose from the list of medicines the admin has
        pass
    
    def remove_medicine(self , medicine):
        
        # choose from the list of medicines you have
        pass