subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

subjects.append("gym")
grades.append(100)

gradebook = zip(grades, subjects)

gradebook.append(("visual arts", 93))

print(gradebook)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)
