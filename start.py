from Model1_Exam.students.students import *
from Model1_Exam.repository.repo_students import *
from Model1_Exam.service.service import *
from Model1_Exam.ui.ui import *


file_repo = FileRepository()
service = StudentService(file_repo)
ui = Ui(service)

ui.load()
ui.start()

