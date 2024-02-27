
class Student:

    def set_name(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name, self.age
    

student1 = Student()
student1.set_name("Manish", 21)
print(student1.get_name())