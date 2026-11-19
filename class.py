class Student:
    name = "ram"
    age = 20


s1 = Student()
s2 = Student()
s2.name = "chandana"

print(s1.name)
print(Student.name)
print(s2.name)
print(Student.name)


class College:
    name = "gopalan"
    loc = "Hoodi"
    
    @classmethod
    def disp(cls): # cls:address of the class
        print(cls.name, cls.loc)
    
    

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print(self.name, self.age, self.dept)

    def change_name(self, new_name):
        self.name = new_name


college = College("deeksha", 20, "cse")
college.display()
s2_college = College("gopalan", 22, "ece")
s2_college.display()

s1 = College("raju", 20, "cse")
s2 = College("deeksha", 25, "ece")

print("before")
s2.display()
s2.change_name("ram")
print("after")
s2.display()

s1.disp()
