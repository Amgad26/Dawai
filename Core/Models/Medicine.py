import uuid

class Medicine:
    
    def __init__(self , name , price , dose , form , description = ""):
    
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.dose = dose
        self.form = form
        self.description = description

    def get_full_description(self):
        
        desc = f"{self.name} | {self.dose} | {self.form} | {self.price:.2f} EGP"
        
        if self.description:
            
            desc += f"\n{self.description}"
            
        return desc