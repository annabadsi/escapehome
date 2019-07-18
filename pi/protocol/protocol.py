from abc import ABC, abstractmethod
from time import sleep
import ast


class Protocol(ABC):

    def __init__(self, protocol_id, protocol_type):
        self.id = protocol_id
        self.type = protocol_type
        super().__init__()

    @staticmethod
    @abstractmethod
    def execute(device, action):
        pass

    @staticmethod
    @abstractmethod
    def send(*args, **kwargs):
        pass

    @staticmethod
    def wait(**kwargs):
        sleep(sleep_time)
