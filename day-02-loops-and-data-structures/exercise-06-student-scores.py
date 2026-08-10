'''
Exercise : Student Scores
Name: Pawan Shrestha
Day: 2'''

student_scores = {
    "Pawan": 85,
    "Reeta": 90,
    "Arbin": 78,
    "Sita": 55,
    "Prateek": 48
}

#Calculations
# Print every student and score.
for student, score in student_scores.items():
    print(f"{student}: {score}")
# Create a dictionary containing only students who scored at least 60.
passed_students={student: score for student, score in student_scores.items() if score >=60}

# Find the student with the highest score.
highest_score_student=max(student_scores, key=student_scores.get)
# Calculate the average score.
average_score=sum(student_scores.values()) / len(student_scores)

#Display the results
print(f"Students who scored at least 60: {passed_students}")
print(f"Student with the highest score: {highest_score_student} with score {student_scores[highest_score_student]}")
print(f"Average Score: {average_score:.2f}")
