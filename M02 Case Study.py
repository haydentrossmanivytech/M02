"""
Hayden Trossman
M02 Case Study.py
The app will ask user for a name and GPA and will then give a response as to whether the student has made dean's list or honor roll
"""
name = input("What is the student's first name?: ")

#exit if name is ZZZ
if name == "ZZZ":
    exit()

#if name is not ZZZ, ask for GPA and then give the proper responses
GPA = float(input("What is the student's GPA?: "))

if GPA >= 3.5:
    print("{} has made the Dean's List".format(name))
if GPA >= 3.25:
    print("{} has made the Honor Roll".format(name))
else:
    print("{} has made neither the Honor Roll or Dean's List".format(name))
