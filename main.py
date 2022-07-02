class Student(object):
  def __init__(self, name, age, gender, year = None):
    self.name = name
    self.age = age
    self.gender = gender
    self.year = year or {}
  def setYear(self, course, year):
    self.year[course] = year
  def getYear(self, course):
    return self.year[course]
  def getGPA(self):
    return sum(self.year.values())/len(self.year)
student = Student('Fahim', 12, 'Male', {'math':3.3})
print(student.getGPA())