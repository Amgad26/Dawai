class Address:
    
    def __init__(self , country , governorate , city , street , extra = ""):
        
        self.country = country
        self.governorate = governorate
        self.city = city
        self.street = street
        self.extra = extra
        
    def get_full_address(self):
        
        address = f"{self.country} - {self.governorate} - {self.city} - {self.street}"
        
        if self.extra:
            
            address += f" - {self.extra}"
            
        return address
         
    