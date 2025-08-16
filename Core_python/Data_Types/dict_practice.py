"""
Practice Problem: Dictionaries

Task:
    Write a function to:
   - Find the student with the highest score.
   - Calculate the average score.
   - Update the score of a particular student.
"""
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}
print(f"Student details are : {students}")
print()

# student with the highest score.
def highest_score(student_dict : dict):
    high_Score = max(student_dict.values())
    student_name = [name for name,value in student_dict.items() if value==high_Score][0]
    print(f"Student with high score {high_Score} is {student_name}")

#highest_score(students)

# Average score calculation
def avg_score(student_dict: dict):
    average_score = (sum(student_dict.values())/len(student_dict.values()))
    print(f"Average score is : {average_score}")

#avg_score(students)

# Updating the score of a particular student.
def updating_student_score(student_dict : dict, student_name: str, new_score : int):
    print(f"new score for {student_name} is {new_score}")
    student_dict[student_name]=new_score
    print(f"Details with updated score for {student_name} : {student_dict}")


updating_student_score(students, "Bob", 90)