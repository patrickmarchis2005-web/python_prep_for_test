from Model1_Exam.repository.repo_students import NameNotFoundError
from Model1_Exam.service.service import StudentService


class Ui:
    def __init__(self, service: StudentService):
        self._service = service

    def menu(self):
        print("1. Add a new student to the list")
        print("2. Display all students")
        print("3. Give bonus")
        print("4. Display all students with given name")
        print("5. Exit")

    def load(self):
        self._service.load()

    def option(self):
        while True:
            try:
                option = int(input(">").strip())
                if option < 1 or option > 5:
                    raise ValueError
                break
            except ValueError:
                print("Invalid option. Please try again.")
        return option

    def start(self):
        while True:
            self.menu()
            option = self.option()

            if option == 1:
                while True:
                    try:
                        id = int(input("Enter student id: "))
                        first_name = input("Enter student's first name: ")
                        last_name = input("Enter student's last name: ")
                        attendance = int(input("Enter student's attendance: "))
                        grade = int(input("Enter student's grade: "))
                        break
                    except ValueError:
                        print("Invalid input. Try again.")

                if id<0:
                    print("Invalid input. Try again.")
                    continue
                elif len(first_name)<3 or len(last_name)<3:
                    print("Invalid input. Try again.")
                    continue
                elif attendance<0:
                    print("Invalid input. Try again.")
                    continue
                elif grade<0 or grade>10:
                    print("Invalid input. Try again.")
                    continue

                name = first_name.upper() + " " + last_name.upper()
                self._service.add(id, name, attendance, grade)

            elif option == 2:
                data = self._service.data.values()
                for student in data:
                    print(str(student))

            elif option == 3:
                while True:
                    try:
                        p = int(input("Minimum attendances required: "))
                        b = int(input("Bonus points to be added: "))
                        break
                    except ValueError:
                        print("Invalid input. Try again.")
                self._service.give_bonus(p, b)

            elif option == 4:
                while True:
                    try:
                        name = input("Enter student name: ")
                        break
                    except TypeError:
                        print("Invalid input. Try again.")

                try:
                    lst = self._service.find_student(name)
                    for student in lst:
                        print(str(student))
                except NameNotFoundError:
                    print("Does not exist any student with that name")

            elif option == 5:
                try:
                    self._service.save()
                except AttributeError:
                    pass
                break


