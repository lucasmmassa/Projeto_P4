from abc import ABC, abstractmethod

# abstract class to maintain the pattern of the managers
class Abstract_Manager(ABC):

    # abstract method
    def run_screen(self,screen):
        pass

    # abstract method
    def check_events(self,screen):
        pass