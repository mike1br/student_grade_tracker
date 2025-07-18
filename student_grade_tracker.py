class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []


    def __str__(self):
        if self.grades:
            avg = round(self.get_average())
            return f"Student Name: [{self.name}], ID: [{self.student_id}], Average Grade: [{avg}]"
        else:
            return f"Student Name: [{self.name}], ID: [{self.student_id}], No grades yet"
     
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")


    def get_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def has_passed(self):
        return self.get_average() >= 60
    

    
    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'


    def reset_grades(self):
        self.grade.clear()
        print(f"Grades have been reset for {self.name}.")

student1 = Student(“Quincy”, "12345")
student2 = Student(“Ivan”, "678910")

student1.add_grade(90)
student1.add_grade(85)
student1.add_grade(88)

student2.add_grade(55)
student2.add_grade(60)
student2.add_grade(42)

print(student1)
print("Passed:", student1.has_passed())
print("Letter Grade:", student1.get_letter_grade())
print()


print(student2)
print("Passed:", student2.has_passed())
print("Letter Grade:", student2.get_letter_grade())
print()
