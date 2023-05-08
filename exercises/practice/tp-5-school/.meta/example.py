from __future__ import annotations
from typing import Dict, List, Set


class Student:
    student_id: int
    name: str
    courses: set[Course]

    students: Dict[int, Student] = {}

    def __init__(self, id_number: int, name: str):
        if id_number in Student.students:
            raise ValueError(f"Student {id_number} already exists")
        Student.students[id_number] = self
        self.student_id = id_number
        self.name = name
        self.courses = set()

    @staticmethod
    def get_student(student_id: int) -> Student:
        student = Student.students.get(student_id)
        if not student:
            raise ValueError(f"Invalid Student Id: {student_id}")
        return student

    def __repr__(self):
        return f"{self.student_id}-{self.name}"

    def get_scores(self) -> Dict[Course, List[int]]:
        result = {}
        for course in self.courses:
            scores = course.get_scores(self.student_id)
            if scores:
                result[course] = scores
        return result


class Course:
    course_id: str
    description: str
    students: Set[Student]
    exams: Dict[Student, List[int]]

    courses: Dict[str, Course] = {}

    def __init__(self, course_id: str, description: str):
        if course_id in Course.courses:
            raise ValueError(f"Course {course_id} already exists")
        Course.courses[course_id] = self

        self.course_id = course_id
        self.description = description
        self.students = set()
        self.exams = {}

    def __repr__(self) -> str:
        return f"{self.course_id}-{self.description}"

    @staticmethod
    def get_course(course_id: str) -> Course:
        course = Course.courses.get(course_id)
        if not course:
            raise ValueError(f"Invalid Course: {course_id}")
        return course

    def enroll(self, student_id: int):
        student = Student.get_student(student_id)
        student.courses.add(self)
        self.students.add(student)
        self.exams[student] = []

    def add_exam(self, student_id: int, score: int):
        if score < 0 or score > 100:
            raise ValueError("Score should be between 0 and 100")

        self.exams[self.get_student(student_id)].append(score)

    def get_student(self, student_id: int) -> Student:
        student = Student.get_student(student_id)
        if student not in self.students:
            raise ValueError(f"Student {student} not enrolled in this course")
        return student

    def get_scores(self, student_id: int) -> List[int]:
        return self.exams[self.get_student(student_id)]
