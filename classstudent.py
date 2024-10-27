class Student():
    name = ""
    age = 14
    grade = 8
    teacher_name = "Alex"
    school = "ISA"

    def __init__(self):
        print("new object of student class")

    def show_details(self):
        print("The student details are ")
        print(self.name,self.age,self.grade,self.teacher_name,self.school)

    def change_details(self):
        print("Enter the name of the student: ")
        self.name = input()


Alp = Student()
Alp.show_details()
Alp.change_details()
Alp.show_details()

Jake = Student()
Jake.change_details()
Jake.show_details()