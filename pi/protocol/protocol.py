from abc import ABC, abstractmethod


class Protocol(ABC):

    def __init__(self, protocol_id, protocol_type):
        self.id = protocol_id
        self.type = protocol_type
        super().__init__()

    @abstractmethod
    def execute(self, value, *address):
        pass
