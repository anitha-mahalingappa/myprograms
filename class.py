import random
class students:
    def __init__(self):
        self.name = input(" please enter the student name:")
        self.age = input(" please enter the student Age:")
        self.gender = input(" please enter the student gender:")
        self.rollno = str(random.randrange(0,50))
    def student_details(self):
        print("new student name is : " + self.name + " age = "+ self.age + "gender: " + self.gender +  " assigned rollnumber :" + self.rollno)


class first_std(students):
    def __init__(self):
        super().__init__()
        self.sub = input(" please enter the student sub:")

    # def student_details(self):
    #     print("gender: "+ self.gender)

class sec_std(students):
    pass




A1 = students()
A1.student_details()
A2 = first_std()
A2.student_details()
A3 = sec_std()
A3.student_details()
# A4 = students()
# A4.student_details()


