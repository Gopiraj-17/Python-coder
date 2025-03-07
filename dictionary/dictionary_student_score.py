from tkinter import Listbox

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for mark in student_scores:
    student_mark = student_scores[mark]
   # print(student_mark)
    if 91 < student_mark < 100:
        student_grades={mark,"Outstanding"}
    elif 81 <student_mark < 90:
        student_grades = {mark, "Exceeds Expectations"}
    elif 71 < student_mark < 80:
        student_grades = {mark, "Acceptable"}
    elif  student_mark < 70:
        student_grades = {mark, "Fail"}
#print(student_grades)



# Nested in Dictonary and List

travel_log = {
    "India" : ["Chennai","Bangalore","Mumbai","Kolkata"],
    "Saudi arabia" : {"Riyadh","Alula","Diriyah"}
}

#print mumbai.
#print(travel_log["India"][2])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

