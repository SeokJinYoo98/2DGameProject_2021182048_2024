from component import Component

class SpecialFunction(Component):
    def __init__(self, special_range=100, collTime=1):
        self.specialF_range = special_range
        self.specialF_colltime, self.specialF_elapsed = collTime
        self.status = None
        
    def update(self, frametime):
        if self.__check_colltime():
            self.specialF_elapsed -= frametime
        else:
            self.special_function()
            self.specialF_elapsed = self.specialF_colltime
            
    def set_status(self, status):
        self.status = status
                 
    def set_colltime(self, colltime):
        self.specialF_colltime = colltime
          
    def special_function(self):
        print("Special")
        pass
    
    def __check_colltime(self):
         return self.specialF_elapsed <= 0