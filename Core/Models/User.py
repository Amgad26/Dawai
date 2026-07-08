from abc import ABC , abstractmethod
import uuid

class User(ABC):
    
    def __init__(self , username):
        
        self.id = str(uuid.uuid4())
        self.username = username
    
    @abstractmethod
    def role(self):
        
        pass