student_scores={
    "aman":78,
    "Kaushik":86,
    "Antik":81,
    "soham":76
}
#to print the grades of the students we need to create a empty dictionary
student_grade={}
for key in student_scores:
    #print(student_scores[key])
  score=student_scores[key]
  if score>90:
    student_grade[key]="outstanding"
  elif score>80:
      student_grade[key]="Very Good"
  else:
      student_grade[key]="avg"
print()      