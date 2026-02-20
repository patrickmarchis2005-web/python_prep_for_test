from Model1_Exam.repository.repo_students import NameNotFoundError


class StudentService:
    def __init__(self, repo):
        self._repo = repo

    def add(self, id: int, name: str, attendance: int, grade: int):
        self._repo.add(id, name, attendance, grade)

    def give_bonus(self, p, b):
        self._repo.give_bonus(p, b)

    def find_student(self, name: str) -> list:
        try:
            lst = self._repo.find_student(name)
            return lst
        except NameNotFoundError:
            raise NameNotFoundError("")

    def load(self):
        try:
            self._repo.load()
        except AttributeError:
            pass

    def save(self):
        try:
            self._repo.save()
        except AttributeError:
            pass

    @property
    def data(self):
        return self._repo.data

