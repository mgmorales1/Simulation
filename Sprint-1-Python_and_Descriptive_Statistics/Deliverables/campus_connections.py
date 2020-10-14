""" 
This script uses enorllment data to understand how densely connected is the Rollins campus
    
CMS 380, Fall 2020
Maria Morales
"""

# import csv module to process delimited text files
import csv
# Imports the functions from method_definitions.py to be used for distribution calculation
from method_definitions import *

# Set up matplotlib and configure it to be used on Mimir 
import matplotlib
matplotlib.use('Agg') # Required because we are using a remote environment
from matplotlib import pyplot as plt

# Create a dictionary to store the cids for each student
courses_per_student = {}

# Second dictionary to store the students in each course 
students_per_course = {}

# Create a list to store the total number of students in each course 
class_size = []

# open the enrollments.csv file
f = open('enrollments.csv', 'r')

# Create a csv reader to process the file
reader = csv.reader(f)

# Use the for loop to iterate through all lines in the file
for line in reader:
    r_number = line[0]
    cid = line[1]
    
    # If this is the frist time we've seen the student r_number, make an entry for it in the dictionary
    if r_number not in courses_per_student:
        courses_per_student[r_number] = [] # Makes a brand new empyt lists of courses associated with this student
        
    # If this is the first time we've seen the course ID, make an entry for it in the  dictionary
    if cid not in students_per_course:
        students_per_course[cid] = [] # Makes a brand new empty list of students associated with this course
    
    # Append the course id so that it adds to the list of courses associated with that student
    courses_per_student[r_number].append(cid)
    # Append the student ID so that it adds to the list of students associated with that course
    students_per_course[cid].append(r_number)

# Count the total number of students in each course and append it to the list
for cid in students_per_course:
    class_size.append(len(students_per_course[cid]))


print('The mean class size: ',calc_mean(class_size))
print('The median class size: ', calc_median(class_size))

# Create a new figure for the histogram
plt.figure()

# Plot a histogram of the data of total students per course 
plt.hist(class_size, 20)

# Set title and axes labels 
plt.title('Class size distribution')
plt.xlabel('Class size')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('class_size_histogram.pdf', bbox_inches='tight')

# Create a new figure for the  boxplot
plt.figure()

# Plot the boxplot of the data of total students per course
plt.boxplot(class_size)

# Set title
plt.title('Class size')

# Save the figure to a file
plt.savefig('class_size_boxplot.pdf', bbox_inches='tight')

# INTERACTIONS
# This part of the script is used to determine how many  unique students does each  Rollins student interact with in classes

# Number of unique student ids for the student
student_interactions = []
# Total number of unique student interactions
total_interactions = []

# For each student look up their  list of courses
for r_number in courses_per_student:
    course_list = courses_per_student[r_number]
    # Acess each course
    for course in course_list:
        student_list = students_per_course[course]
        
        # Iterate through the students in each course and keep track of unique student ids 
        for student in student_list:
            if student not in student_interactions:
                student_interactions.append(student)
                
    total_interactions.append(len(student_interactions) - 1)
    student_interactions.clear()
    

print('The average number of unique student interactions: ', calc_mean(total_interactions))

# Create a new figure for the histogram
plt.figure()

# Plot a histogram of the unique student interactions
plt.hist(total_interactions, 20)

# Set title and axes labels 
plt.title('Unique student interactions')
plt.xlabel('Unique students')
plt.ylabel('Count')

# Save the figure to a file
plt.savefig('unique_student_histogram.pdf', bbox_inches='tight')

# Create a new figure for the  boxplot
plt.figure()

# Plot the boxplot of the unique student interactions
plt.boxplot(total_interactions)

# Set title
plt.title('Unique Student Interactions')

# Save the figure to a file
plt.savefig('unique_student_interactions_boxplot.pdf', bbox_inches='tight')


