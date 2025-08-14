class Student:
    def __init__(self, student_name, roll_number, marks):
        self.student_name = student_name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_sum(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        total_marks = self.calculate_sum()
        return total_marks / len(self.marks)

    def grade(self):
        per = self.calculate_percentage()
        if per >= 90:
            return "A+"
        elif per >= 80:
            return "A"
        elif per >= 70:
            return "B"
        elif per >= 60:
            return "C"
        elif per >= 50:
            return "D"
        else:
            return "Fail"

    def display_result(self):
        print(f"\nStudent Name: {self.student_name}")
        print(f"Roll Number: {self.roll_number}")
        print("Marks:")
        for subject, marks in self.marks.items():
            print(f"  {subject}: {marks}")
        print(f"Total Marks: {self.calculate_sum()}")
        print(f"Total Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.grade()}")
        print("-" * 30)


class ReportCardSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = {}
        num_subject = int(input("\nEnter number of subjects: "))
        for _ in range(num_subject):
            subject = input("Enter subject name: ")
            mark = float(input(f"Enter marks for {subject}: "))
            marks[subject] = mark
        student = Student(student_name, roll_number, marks)
        self.students.append(student)
        print("Student added successfully!")

    def view_result(self):
        if not self.students:
            print("No students found")
        else:
            for student in self.students:
                student.display_result()

    def run(self):
        while True:
            print("\n=== Student Report Card ====")
            print("1. Add Student")
            print("2. View Result")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_result()
            elif choice == "3":
                print("Goodbye ")
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    report = ReportCardSystem()
    report.run()
