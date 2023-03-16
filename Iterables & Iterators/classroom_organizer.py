#task2
from roster import student_roster
import itertools
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

#task4
  def studentCombo(self):
    return list(itertools.combinations(self.sorted_names,2))

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

#task3
myClass = ClassroomOrganizer()
myClass_iter = iter(myClass.sorted_names)
for s in range(10):
  print(next(myClass_iter))