import uuid

class User():
    
    def __init__(self ,  username , address , role = "Member"): # medicines is a list of medicines it will be empty at first
        
        self.id = str(uuid.uuid4())
        self.username = username
        self.address = self.address
        self.role = self.role
        self.medicines = []
        
    def get_role(self):
        
        return self.role
    
    def change_address(self , new_address):
        
        self.address = new_address
    
    def add_medicine(self , medicines):
        
        # choose from the list of medicines the admin has
        pass
    
    def remove_medicine(self , medicine):
        
        # choose from the list of medicines you have
        pass