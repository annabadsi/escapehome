from abc import ABC, abstractmethod

class Protocol(ABC):
    
    def __init__(self, id, type):
        self.id = id
        self.type = type
        super().__init__()
    
    @abstractmethod
    def execute(self, args):
        pass 

    
    