class A:          #single inheritence
    a = 10


class B(A):
    b = 20


class C(B):
    c = 30


class D(C):
    d = 40


ob1 = D()
print(ob1.a, ob1.b, ob1.c, ob1.d)


class Bank:
    bname = 'SBI'
    bloc = 'DDS'

    def __init__(self, name, phno, eid):
        self.name = name
        self.phno = phno
        self.eid = eid

    def display(self):
        print(self.name, self.phno, self.eid)


c1 = Bank("deeksha", 4435777788, 'gachandana089.com')
c1.display()


class Bank_details(Bank):
    founder = 'ABC'

    def __init__(self, name, phno, eid, add, pan):
        super().__init__(name, phno, eid)
        self.add = add
        self.pan = pan

    def display(self):
        super().display()
        print(self.add, self.pan)


c1 = Bank_details("deeksha", 6545567899, "chandana089@gmail.com", "dds", "dsknsdshi")
c1.display()


class school:  # hierarchical and multiple inheritance
    sname = "ABC"
    sloc = "ecity"


class College(school):
    cname = "GCEM"
    cloc = "hoodi"


class University(school):
    uname = "jain"
    uloc = "german"


class Masters(College, University):
    @classmethod
    def display(cls):
        print(cls.sname, cls.sloc, cls.cname, cls.cloc, cls.uname, cls.uloc)


master = Masters()
master.display()

# Polymorphism: method overloading and operator overloading
class Demo:
    @staticmethod
    def sam(*values):
        if not values:
            print("why are you late")
        elif len(values) == 2:
            print(values[0] + values[1])
        elif len(values) == 3:
            print(values[0] * values[1] * values[2])
        else:
            raise TypeError("sam() accepts zero, two, or three arguments")


demo = Demo()
demo.sam()
demo.sam(10, 20)
demo.sam(10, 20, 30)


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


print(Number(10) + Number(20))
# Operator overloading

class demo:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return demo(self.value + other.value)


a = demo(100)
b = demo(200)
c = a + b
print(c.value)

print("-----concatenation--------")
s1 = demo("hlo")
s2 = demo("good morning")
result = s1 + s2
print(result.value, type(result.value))

#encapsulation

class Bank:
    __deposit = 1000000
    def __init__(self, name, phone, acno):
        self.name = name
        self.phone = phone
        self.__acno = acno


b = Bank("ram", 3598765689, 3445859)
print(b.name, b.phone, b._Bank__acno)#syntax to access private members
print(b._Bank__deposit)  # Access a private class attribute via name mangling
print(Bank._Bank__deposit)  # Access a private class attribute via name mangling

class BankAccount:  # getter and setter methods
    def __init__(self, name, balance):
        self.name = name
        self._bal = balance

    def get_bal(self):
        return self._bal

    def set_bal(self, amount):
        self._bal = amount

    def deposit(self, amount):
        self.set_bal(self.get_bal() + amount)

    def withdraw(self, amount):
        if amount <= self.get_bal():
            self.set_bal(self.get_bal() - amount)
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


account = BankAccount("Ram", 1000)
print("Before:", account.get_bal())
account.deposit(1000)
print("After deposit:", account.get_bal())
account.withdraw(200)
print("After withdrawal:", account.get_bal())

#abstract

from abc import ABC, abstractmethod

class Student(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def write(self):
        pass


class school(Student):
    def study(self):
        print(self.name, "studying")

    def write(self):
        print(self.name, "writing")


s1 = school("Ram")
s2 = school("studying")
s1.study()
s2.study()
