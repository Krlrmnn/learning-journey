student = {
    "name": "John",
    "age": 23,
    "language": "Python",
    "level": "Intermediate"
}

student["country"] = "Colombia"
student["active"] = "True"
student["age"] = 24
student_str = "\n".join([f"{key}: {value}" for key, value in student.items()])

print(student_str)