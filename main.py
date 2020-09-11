# Boyuan Lai bjl5716
# solo
def getGradePoint(grade):
  if grade == "A": 
    return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0

def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = float(input("Enter your course 1 credit: "))
  point1 = float(getGradePoint(grade1))
  print (f"Grade point for course 1 is: {getGradePoint(grade1)}")

  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = float(input("Enter your course 2 credit: "))
  point2 = float(getGradePoint(grade2))
  print (f"Grade point for course 2 is: {getGradePoint(grade2)}")

  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = float(input("Enter your course 3 credit: "))
  point3 = float(getGradePoint(grade3))
  print (f"Grade point for course 3 is: {getGradePoint(grade3)}")

  GPA = ((point1*credit1)+(point2*credit2)+(point3*credit3))/(credit1+credit2+credit3)
  print (f"Your GPA is: {GPA}")
 
if __name__ == "__main__":
  run()