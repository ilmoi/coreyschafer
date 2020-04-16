class Employee(object):

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

    def fullname(self):
        fullname = f'{self.first} {self.last}'
        return fullname

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # meant for developers
    def __repr__(self):
        return f"{self.__class__.__name__}({self.first}, {self.last}, {self.pay})"

    # meant for normal users
    def __str__(self):
        return f"{self.first} - {self.pay}"

############################################################################
# # testing raising amount

# ilja = Employee('ilja', 'moi', 50000)
# print(ilja.raise_amt)
# print(Employee.raise_amt)
#
# Employee.set_raise_amt(1.10)  # affects both
#
# print(ilja.raise_amt)
# print(Employee.raise_amt)
#
# ilja.set_raise_amt(1.20)  # also affects both, coz keyword cls
#
# print(ilja.raise_amt)
# print(Employee.raise_amt)

############################################################################
# # testing from string method
# new_emp_1 = Employee.from_string("John-Doe-80000")
# print(new_emp_1.first)

############################################################################
# testing subclasses

# class Developer(Employee):
#     raise_amt = 1.25
#
#     def __init__(self, first, last, pay, lang):
#         # Employee.__init__(self, first, last, pay)
#         super().__init__(first, last, pay)  # another way, which corey says is best
#         self.lang = lang
#
#
# class Manager(Employee):
#
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def rem_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print('--->', emp.fullname())
#
#
# emp1 = Employee('vadim', 'olek', 70000)
# emp1.apply_raise()
# print(emp1.pay)
#
# dev1 = Developer('ilja', 'moi', 70000, 'python')
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.lang)
#
# man1 = Manager('andrey', 'potato', 100000)
# man1.add_emp(dev1)
# man1.print_emps()

############################################################################
# testing repr and str


# emp1 = Employee('ilja', 'moi', 70000)
# # emp1
# print(emp1)
#
# print(repr(emp1))
# print(str(emp1))

############################################################################
# practicing getters/setters

# class Person(object):
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     # this is pythonic way of building a GETTER
#     # this also allows a method to be accessed like an attribute (no ())
#     @property  # we're going to use the property decorator
#     def email(self):
#         return self.first + self.last + '@gmail.com'
#
#     # now lets do a SETTER
#     # need to define this as a property first
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     # after which we can create a setter out of it
#     @fullname.setter
#     def fullname(self, name):
#         self.first, self.last = name.split(' ')
#
#     @fullname.deleter
#     def fullname(self):
#         print('this will delete the name!')
#         self.first = None
#         self.last = None
#
#
# john = Person('john', 'smith', 70000)
# john.first = 'jim'
#
# # GETTING - both should be updated
# print(john.first)
# print(john.email)
# print(john.fullname)
#
# # SETTING - first and last should be updated
# john.fullname = ('spider man')
# print(john.first)
# print(john.last)
#
# # DELETING - first and last should be emptry
# del john.fullname
# print(john.first)
# print(john.last)


class House(object):

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @price.deleter
    def price(self):
        self._price = None


dzirnavu = House(250)
print(dzirnavu.price)
dzirnavu.price = 500
print(dzirnavu.price)
del dzirnavu.price
print(dzirnavu.price)

# we're using the property decorator to create a getter anda a setter
# this allows existing code to continue using price as a variable, not get_price() or set_price()
# while it allows us to modify price internally to make it _price (hidden)
