from Model1_Exam.students.students import Student


class RepositoryError(Exception):
    def __init__(self, msg = ""):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class IdError(RepositoryError):
    def __init__(self, msg):
        super().__init__(msg)


class NameNotFoundError(RepositoryError):
    def __init__(self, msg):
        super().__init__(msg)


class AttendanceError(RepositoryError):
    def __init__(self, msg):
        super().__init__(msg)


class GradeError(RepositoryError):
    def __init__(self, msg):
        super().__init__(msg)


class MemoryRepository:
    def __init__(self):
        self._data: dict = {}

    def add(self, id: int, name: str, attendance: int, grade: int):
        """
        Adds a new student to the repository.
        :param grade: grade of a student at that lab
        :param attendance: nr of attendances of the student at a lab
        :param name: the name of the student that will be added
        :return:
        """
        student = Student(id, name, attendance, grade)
        if id not in self._data.keys():
            self._data[id] = student

    def give_bonus(self, p: int, b: int):
        for student in self._data.values():
            if student.attendance >= p:
                student.grade += b
                if student.grade > 10:
                    student.grade = 10

    def find_student(self, name: str) -> list:
        # lst = []
        # ok = False
        # for student in self._data.values():
        #     if name in student.name:
        #         lst.append(student)
        #         ok = True
        # if ok:
        #     return lst
        # else:
        #     raise NameNotFoundError

        chars = []
        for chr in name:
            if chr not in chars:
                chars.append(chr)

        first_list = []
        for student in self._data.values():
            if chars[0].lower() in student.name:
                if student not in first_list:
                    first_list.append(student)
            elif chars[0].upper() in student.name:
                if student not in first_list:
                    first_list.append(student)

        chars.pop(0)
        for chr in chars:
            new_list = []
            for student in first_list:
                if chr.lower() in student.name:
                    new_list.append(student)
                elif chr.upper() in student.name:
                    new_list.append(student)
            first_list = new_list

        if len(first_list) == 0:
            raise NameNotFoundError("Doesn't exist any student with that name")
        else:
            return first_list

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        pass


class FileRepository(MemoryRepository):
    def __init__(self):
        super().__init__()

    def load(self):
        try:
            fin = open("students.txt", "rt", encoding="utf-8")
            lines = fin.readlines()
            for line in lines:
                tokens = line.split(",")
                name_parts = tokens[1].split(" ")
                name_parts.pop(0)
                name = " ".join(name_parts)
                tokens[2].strip()
                tokens[3].strip()
                self.add(int(tokens[0]), name, int(tokens[2]), int(tokens[3]))
            fin.close()
        except FileNotFoundError:
            pass

    def save(self):
        try:
            fout = open("students.txt", "wt", encoding="utf-8")
            for student in self._data.values():
                fout.write(str(student))
            fout.close()
        except FileNotFoundError:
            pass

    def add(self, id: int, name: str, attendance: int, grade: int):
        super().add(id, name, attendance, grade)

    def give_bonus(self, p: int, b: int):
        super().give_bonus(p, b)

    def find_student(self, name: str) -> list:
        try:
            lst = super().find_student(name)
            return lst
        except NameNotFoundError:
            raise NameNotFoundError("Doesn't exist any student with that name")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        pass
