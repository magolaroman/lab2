from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any


@property
class Name():
    """Class to split name from Group dataclass"""
    def name(Student, PersonalInfo):
        x=Student.name.split()
        x[0]==PersonalInfo.first_name
        x[1]==PersonalInfo.second_name
        print(x[0], x[1])
   
@dataclass
class Group:
    id: int
    title: str
    student_list: list
    department_id: int

@dataclass
class PersonalInfo:
    """Data class with personal information"""

    id: int
   # name: str
    first_name:str
    second_name:str
    #adress: str
    #phone_number: str
    #email: str
    #position: int
    #rank: str
    salary: float
 



class Department:
    def __init__(self, id:int, title: str):
        self.id=id
        self.title = title
        self.students: List[Student] = []
        self.professors: List[Professor] = []
        self.courses: List[Course] = []
        self.requests: List[str] = []
        self.ill_person: List[str] = []

    def get_ill_person(self):
        """Return a list of ill person"""
        return self.ill_person

    def get_requests(self):
        """Return a list of requests"""
        return self.requests






class Staff(PersonalInfo):

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

  

  @abstractmethod
  def add_student(Student):
    pass
  @abstractmethod
  def remove_student(Student):
      pass
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
    self._personal_info=PersonalInfo(None, name, None, None, )
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
  """"""
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


  
class Professor(Staff):
  """Professor class for creating a professor object with given attributes"""
  average_mark=0
  post_students: List[PostGraduateStudent]=[]
  def check_assignment(assignment: dict) -> None:
    if assignment["is_done"]:
      assignment["mark"] = 5.0
  @abstractmethod
  def fill_couse() -> None:
      pass
  @abstractmethod
  def create_course(self) ->Course:
      pass
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

class Math(Course):
    def __init__(self, title:str,
                 assignments: list[str],   students_limit: int):
        self.title = title
        self.limit = students_limit
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []
        
        #function for adding students into the list

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f"Student {student.name} has been added to the course {self.title}")
        else:
            print(f"Too many students in {self.title} course")

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f"student {student.name} are removed from the {self.title} !")
class Programming(Course):
    def __init__(self, title: str,
                 assignments: list[str],  students_limit: int):
        self.title = title
        self.limit = students_limit
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []
        
        #function for adding students into the list

    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f"Student {student.name} has been added to the course {self.title}")
        else:
            print(f"Too many students in {self.title} course")

        # function for removing students from list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f"student {student.name} are removed from the {self.title} !")
class Algorithms(Course):
    def __init__(self, title:str,
                 assignments: list[str],   students_limit: int):
        self.title = title
        self.limit = students_limit
        self.assignments = assignments
        self.students: Student = []
        self.seminars: List = []
        
        #function for adding students into the list
    def add_student(self, student: List):

        if self.limit > len(self.students):
            student.courses.append(self.title)
            self.students.append(student)
            Enrollment.enroll(student, self)
            print(f"Student {student.name} has been added to the course {self.title}")
        else:
            print(f"Too many students in {self.title} course")

        # function for removing students from tbe list

    def delete_student(self, student):
        student.unenroll(self.title)
        self.students.remove(student)
        print(f"student {student.name} are removed from the {self.title} !")

class MathProfessor(Professor):
    """Math professor method of professor class"""
    def create_course(self,  math:Math) -> Course:
        if math.title=='Math':
            Professor.create_course(self)
            print(f"{math.title} course created by {self.first_name} {self.second_name}")
            return f"{math.title} course created by {self.first_name} {self.second_name}"
        else:
            print(f"{math.title} is wrong course title")
            return f"{math.title} is wrong course title"


class ProgrammingProfessor(Professor):
    """Programming professor method of professor class"""
    def create_course(self,  prog:Programming) -> Course:
        if prog.title=='Programming':
            Professor.create_course(self)
            print(f"{prog.title} course created by {self.first_name} {self.second_name}")
            return f"{prog.title} course created by {self.first_name} {self.second_name}"
        else:
            print('{prog.title} is wrong course title')

class AlgorithmsProfessor(Professor):
    """Algorithms professor method of professor class"""
    def create_course(self,  algo:Algorithms) -> Course:
        if algo.title=='Algorithms':
            Professor.create_course(self)
            print(f"{algo.title} course created by {self.first_name} {self.second_name}")
            return f"{algo.title} course created by {self.first_name} {self.second_name}"
        else:
            print(f"{algo.title} is wrong course title")
class Enrollment:
    def __init__(self)-> None:
        self.student_course=defaultdict(list)
        self.course_student=defaultdict(list)
  
    def enroll(self,student_id, course_title, student_name)->None:
        self.course_student[student_id].append(course_title)        
        print(f'{student_name}  has been added to the course {course_title}')
        return f'{student_name}  has been added to the course {course_title}'

    
    def unenroll( self,  student_id, course_title, student_name)->None:
        """Remove students from the course and course title from students courses"""
        if course_title in self.course_student and student_id in self.student_course:
            self.course_student[student_id].student_course(course_title)
            self.student_course[course_title].remove(student_id)
            print(f'{student_name} has been removed from course {course_title}')
        else:
            print("It is impossible to retrieve connection that does not exist!")
assignment2= {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}
student1=Student( 'Roman Magola','Lviv','096833','Magola@gmail.com', 3)
course1 = Algorithms('Algorithms', assignment2,  100)
enrl=Enrollment()
enrl.enroll(student1.student_number, course1.title, student1.name)