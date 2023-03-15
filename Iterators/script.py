'''
New Teacher in Town
You are a new teacher at Pine Valley Elementary School!

This project will help you practice and further master the learned material from the Iterables and Iterators lesson
by utilizing the information learned to set up and organize your new classroom and roster of students.
'''

from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools
#task1
student_roster_iter = student_roster.__iter__()
for i in range(10):
  student = next(student_roster_iter)
  print(student)

#task4
classX = ClassroomOrganizer()
print(classX.studentCombo())

#task5
stemClass = itertools.chain(classX.get_students_with_subject("Math"), classX.get_students_with_subject("Science"))
print(list(itertools.combinations(stemClass, 4)))