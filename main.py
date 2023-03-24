print("Exam Grade Calculator")

exam = input("Name of Exam: ")
max_score = int(input("Max. Possible Score: "))
score = int(input("Your Score: "))
grade = (score / max_score) * 100
grade = round(grade, 2)

if grade >= 90:
  print("You got", grade,"% which is A+")
elif grade >= 80:
  print("You got", grade,"% which is A-")
elif grade >= 70:
  print("You got", grade,"% which is B")
elif grade >= 60:
  print("You got", grade,"% which is C")
elif grade >= 50:
  print("You got", grade,"% which is D")
else:
  print("You got", grade,"% which is U")