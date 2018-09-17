# BUILD A GRADEBOOK (WEEK 4, DAY 3)
#PROJECT #4
#CODE ACADEMY
#PROGRAMMING WITH PYTHON
#Dean Jones, Aug.01, 2018

# Build a Gradebook
# In this project, you will act as a student and create a gradebook to keep track of some
# of the subjects you've taken and grades you have received in them. To complete the project,
# you will need to understand how to create and combine lists, and how to add elements.
# On the way, you'll refresh your knowledge of basic Python syntax. If you get stuck or confused,
# remember that your Slack community is there to help!

# This project is not graded and you do not need to submit it anywhere.
# If you would like to check your results, the solution code can be found here.


#FUNCTION: ADD SUBJECT
def add_subject(subject, grade):
  subjects.append(subject)
  grades.append(grade)

#FUNCTION: CREATE LISTS (COMBINE)(subjects and grades)
def list_subjects_and_grades(list_subjects, list_grades):
  #return zip(list_subjects, list_grades)		#***WARNING, causes empty list
  return list(zip(list_subjects, list_grades))

#FUNCTION: PRINT GRADES
def print_grades(message, list_grades):
  #print(message, list(zip_grades))
	print(message, list_grades)

#--------------------

#old grades
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#LISTS
subjects = ['physics', 'calculus', 'poetry', 'history']
grades = list((98, 97, 85, 88))		#alternate method
#grades = [98, 97, 85, 88]

#(see ADD SUBJECT)
#APPEND (new subject and grade)
#subjects.append("computer science")
#grades.append(100)

#add subject
add_subject('computer science', 100)  #100% wow!
add_subject('visual art', 93)

#ZIP (subjects with grades)
gradebook = list_subjects_and_grades(subjects, grades)


#gradebook = zip(subjects, grades)
print_grades("Gradebook: ", list(gradebook))
#print("gradebook: ", list(gradebook))

#FULL GRADES (this semester and last)
full_gradebook = last_semester_gradebook + gradebook

#print("full gradebook: ", list(full_gradebook))
print_grades("Full Grades: ", full_gradebook)
