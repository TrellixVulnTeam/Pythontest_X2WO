class Other():
    def override(self):
        print("Other override()")
    
    def implicit(self):
        print("Other implicit()")
    
    def altered(self):
        print("other altered()")
        
class Child():
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        self.other.override()
        
    def altered(self):
        print("Child, before other altered()")
        self.other.altered()
        print("Child, after other altered()")

son = Child()

son.implicit()
son.override()
son.altered()