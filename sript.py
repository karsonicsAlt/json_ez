import json

file = open("students.json") 
data = json.load(file)
print(data)

for student in data["Students"]:
    print(f"{student['FirstName']} {student['LastName']}")
    for studens in data["students"]:
        age_vid = 0
        age_vid += int(student["Age"])
        avg_age = age_vid/ len(data["Students"])
        print(avg_age)
