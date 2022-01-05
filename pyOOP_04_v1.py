class Person():

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + " , " + str(self.age)

    
class Employee(Person):

    def __init__(self, first, last, age, empno):
        self.firstname = first
        self.lastname = last
        self.age = age
        self.empno = empno

    def __str__(self):
        return self.firstname + " " + self.lastname + " , " + str(self.age) + ", " + str(self.empno)   

def main():
    # print (issubclass(Employee,Person))
    # print (issubclass(Employee, object))
    # print (issubclass(Person, object))

    x = Person("Ashwin", "Pajankar", 31)
    print(x)

    y = Employee ("James", "Bond", 32, 1007)
    print(y)

if __name__ == "__main__":
    main()