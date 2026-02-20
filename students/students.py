class Student:
    def __init__(self, id: int, name: str, attendance: int, grade: int):
        self.id = id
        self.name = name
        self.attendance = attendance
        self.grade = grade

    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + str(self.attendance) + ", " + str(self.grade) + "\n"