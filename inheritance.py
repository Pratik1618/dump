class Base:
 def info(self):
    self.name = input("Enter your name: ")
    self.roll = int(input("Enter your roll no.: "))
    self.id = int(input("Enter your ID: "))
class Child(Base):
 def display(self):
    print("Name:", self.name)
    print("Roll No.:", self.roll)
    print("Student ID:", self.id)
obj = Child()
obj.info()
obj.display()