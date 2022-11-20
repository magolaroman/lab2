from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any
@property
def name():
    x=name.split()
    x[0]==first_name
    x[1]==second_name
    print(x[0], x[1])



@dataclass
class PersonalInfo:
    
    """Data class with personal information"""

    id: int
    name: str
    first_name:str
    second_name:str
    adress: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float
  

class Enrollment:
    @staticmethod
    def enroll(Course, Student):
        """If there are places for the course add student name to list of students on the course and course title to list of courses"""
        if (
            Course.limit > len(Course.students)
            and Student._personal_info.name not in Course.students
        ):
            Course.students.append(Student._personal_info.name)
            Student.courses.append(Course.title)
            print(
                f"Student {Student._personal_info.name} as been added to the course {Course.title}"
            )
        else:
            print("Too many students or this student is already in the course")

    @staticmethod
    def unenroll(Course,  Student):
        """Remove students from the course and course title from students courses"""
        Course.students.remove(Student._personal_info.name)
        Student.courses.remove(Course.title)
        print(f"{Student._personal_info.name} remove from course {Course.title}")


class Department:
    def __init__(self, title: str):
        self.title = title
        self.students: List[Student] = []
        self.professors: List[Lector] = []
        self.courses: List[Course] = []
        self.requests: List[str] = []
        self.ill_person: List[str] = []

    def get_ill_person(self):
        """Return a list of ill person"""
        return self.ill_person

    def get_requests(self):
        """Return a list of requests"""
        return self.requests






class Staff(ABC):
    def __init__(self, _pesonal_info: PersonalInfo):
        self._persoanl_info = _pesonal_info

    @abstractmethod
    def ask_sick_leave(self, department: Department) -> bool:
        pass

    @abstractmethod
    def send_request(self, department: Department) -> bool:
        pass

class Seminar:
    def __init__(
        self,
        id: int,
        title: str,
        deadline: datetime,
        assignments: List[dict],
        status: Any,
        related_course: str,):
        pass

    def implement_item(item_name: str) -> str:
        pass

class Course:
  """"""
  def __init__(self,title:str,start_date:datetime,end_date:datetime,description:str,lectures:list[str],assignments:list[str], limit:int, ):
    self.title=title
    self.start_date=start_date
    self.limit = limit
    self.end_date=end_date
    self.description=description
    self.lectures=lectures
    self.assignments=assignments 
    self.students = []
    self.seminars: List[int] = []

    
  # Returns a list of students from the course
  def check_students(self):
      """Returns the list of students enrolled in the course"""
      return self.students
  
 

class Student(Staff):
  """"""
  def __init__(self, name:str, 
               address:str,
               phone_number:str,
               email:str,
               student_number:int) -> None:
    self.name = name
    self.address = address
    self.phone_number = phone_number
    self.email = email
    self.student_number = student_number
    self.average_mark = 0.0
    self.courses: List[Course] = []
    self.course_progress = []
    self._personal_info=PersonalInfo(None, name, None, None, None, None, None, None, None, None)
  def taken_courses(self) -> List[Course]:
    return self.courses
  def enroll(self, course: Course) -> None:
    """Enroling student to a course"""
    self.courses.append(course)


  def ask_sick_leave(self, department: Department):
      """Add student name to list of ill person and allow not to go to class"""
      department.ill_person.append(f"student {self._personal_info.first_name} is ill")
      print(f"{self._personal_info.first_name} you can not go to class today")

  def send_request(self, department: Department):
      """Add student request to list of requests"""
      reques = input("Write your request:")
      department.requests.append(
          f"Student {self._personal_info.first_name} want to {reques}")

  def unenroll(self, course_title):
    """Unenrollign student from a course"""
    self.courses = list(filter(lambda x: x.title == course_title, self.courses))
    print(f'Student {self.name} unenrolled from {course_title}')

  
class PostGraduateStudent(Staff):
  """"""
  def __init__(self, name:str,
               address:str,
               phone_number:str,
               email:str,
               student_number:int,
               phd_status:str) -> None:
    self.name = name
    self.address = address
    self.phone_number = phone_number
    self.email = email
    self.student_number = student_number
    self.average_mark = 0.0
    self.courses: List[Course] = []
    self.course_progress = []
    self.phd_status=phd_status
  def taken_courses(self) -> List[Course]:
    return self.courses
  def enroll(self, course: Course) -> None:
    """Enroling student to a course"""
    self.courses.append(course)


  def ask_sick_leave(self, department: Department):
      """Add student name to list of ill person and allow not to go to class"""
      department.ill_person.append(f"student {self._personal_info.first_name} is ill")
      print(f"{self._personal_info.first_name} you can not go to class today")

  def send_request(self, department: Department):
      """Add student request to list of requests"""
      reques = input("Write your request:")
      department.requests.append(
          f"Student {self._personal_info.first_name} want to {reques}")

  def unenroll(self, course_title):
    """Unenrollign student from a course"""
    self.courses = list(filter(lambda x: x.title == course_title, self.courses))
    print(f'Student {self.name} unenrolled from {course_title}')

class CourseProgres:
  """Implement docstrin!!!"""
  def __init__(self, received_marks: dict,
               visited_lectures: int,
               notes:dict[str]):
    self.received_marks = received_marks
    self.visited_lectures = visited_lectures
    self.assignments = {}
    self.notes = notes
  def get_final_mark(self)->float:
    """Calculating a final mark for a student"""
    final_mark=sum(self.received_marks.values())/len(self.received_marks)
    return final_mark
  def get_progress_to_date(self, date: datetime):
    marks = [value["mark"] for key, value in self.assignments if date >= key]
    return sum(marks) / len(marks)


  
class Lector(Staff):
  def __init__(self,name:str,address:str,phone_number:str,email:str, salary: float, course: Course):
    self.name=name
    self.address=address
    self.phone_number=phone_number
    self.email=email
    self.salary=salary
    self.course = course
  def check_assignment(assignment: dict) -> None:
    if assignment["is_done"]:
      assignment["mark"] = 5.0


  def add_postgraduate_student(self, student: PostGraduateStudent):
      pass

  def ask_sick_leave(self, department: Department) -> bool:
      """Add professor name to list of ill person and allows not to conduct the lesson if he finds a replacement"""
      department.ill_person.append(
          f"Professor {self._personal_info.first_name} is ill")
      print(f"{self._personal_info.first_name} you must find a replacement")

  def send_request(self, department: Department) -> bool:
      """Add professor request to list of requests"""
      reques = input("Write your request:")
      department.requests.append(
          f"Professor {self._personal_info.first_name} want to {reques}")



assignment_1 = {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}
assignment_2 = {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}


student1=Student( 'Roman Magola','lviv','096833','Holovcko@gmail.com', 3,)
person1=PersonalInfo( 1, 'Roman Magola',None, None,'lviv','096833','Holovcko@gmail.com',1, None, None)
course1=Course('Patern',(1,9,2022),(1,12,2022),'nothing',['math','english','programming'],['programming','developing games','running'],11)
student_progress_1=({"english":151,"math":151,"programming":151},3,{'math':True,'english':False,'programming':True},{'good job':'job good','true':'false'})
print(student_progress_1)
professor1 = Lector("Oleh", None, None, None, None, course1)
department1 = Department("LNY department")
Enrollment.enroll(course1, student1)
Enrollment.unenroll(course1, student1)
Name.name(student1, person1)