from .User import User

class Member(User):
    
    def __init__(self , username , addresses ,  medicines): # medicines is a list of medicines it will be empty at first
        
        super().__init__(username)
        self.addresses = []
        self.medicines = []
        
    def role(self):
        
        return "Member"
    
    def add_address(self , address_object):
        
        self.addresses.append(address_object)
    
    def add_medicine(self , medicines):
        
        # choose from the list of medicines the admin has
        pass
    
    def remove_medicine(self , medicine):
        
        # choose from the list of medicines you have
        pass