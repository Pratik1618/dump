class Student:
 def info(self):
    self.name = input("Enter your name: ")
    self.roll = int(input("Enter your roll no: "))
    self.id = int(input("Enter your ID: "))
 def display(self):
    print("Name:", self.name)
    print("Roll no:", self.roll)
    print("Student ID:", self.id)
obj = Student()
obj.info()
obj.display()