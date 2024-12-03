import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import messagebox
cred = credentials.Certificate("secret_key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://attendance-system-bd010-default-rtdb.firebaseio.com/'
})

# Initialize Firebase

ref_students = db.reference('/Students')
ref_teachers = db.reference('/Teachers')


# Function to add student details to the Firebase Realtime Database
def add_student():
    reg_id = reg_id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    # Push student details to the database
    student_ref = ref_students.child(reg_id)
    student_ref.set({'name': name, 'age': age, 'grade': grade})

    messagebox.showinfo("Success", "Student details added successfully!")


# Function to add teacher details to the Firebase Realtime Database
def add_teacher():
    teacher_id = teacher_id_entry.get()
    name = teacher_name_entry.get()
    subject = subject_entry.get()

    # Push teacher details to the database
    teacher_ref = ref_teachers.child(teacher_id)
    teacher_ref.set({'name': name, 'subject': subject})

    messagebox.showinfo("Success", "Teacher details added successfully!")


# Function to switch to the student details page
def show_student_page():
    teacher_frame.grid_forget()
    student_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


# Function to switch to the teacher details page
def show_teacher_page():
    student_frame.grid_forget()
    teacher_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


# Create the main application window
root = tk.Tk()
root.title("Student and Teacher Details")

# Create frames for student and teacher input fields
student_frame = ttk.Frame(root, padding="20")
teacher_frame = ttk.Frame(root, padding="20")

# Create labels and entry fields for student details
reg_id_label = ttk.Label(student_frame, text="Registration ID:")
reg_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
reg_id_entry = ttk.Entry(student_frame)
reg_id_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = ttk.Label(student_frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
name_entry = ttk.Entry(student_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)

age_label = ttk.Label(student_frame, text="Age:")
age_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
age_entry = ttk.Entry(student_frame)
age_entry.grid(row=2, column=1, padx=5, pady=5)

grade_label = ttk.Label(student_frame, text="Grade:")
grade_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
grade_entry = ttk.Entry(student_frame)
grade_entry.grid(row=3, column=1, padx=5, pady=5)

add_student_button = ttk.Button(student_frame, text="Add Student", command=add_student)
add_student_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create labels and entry fields for teacher details
teacher_id_label = ttk.Label(teacher_frame, text="Teacher ID:")
teacher_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
teacher_id_entry = ttk.Entry(teacher_frame)
teacher_id_entry.grid(row=0, column=1, padx=5, pady=5)

teacher_name_label = ttk.Label(teacher_frame, text="Name:")
teacher_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
teacher_name_entry = ttk.Entry(teacher_frame)
teacher_name_entry.grid(row=1, column=1, padx=5, pady=5)

subject_label = ttk.Label(teacher_frame, text="Subject:")
subject_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
subject_entry = ttk.Entry(teacher_frame)
subject_entry.grid(row=2, column=1, padx=5, pady=5)

add_teacher_button = ttk.Button(teacher_frame, text="Add Teacher", command=add_teacher)
add_teacher_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create buttons to switch between student and teacher pages
student_page_button = ttk.Button(root, text="Student Page", command=show_student_page)
student_page_button.grid(row=1, column=0, padx=5, pady=5)

teacher_page_button = ttk.Button(root, text="Teacher Page", command=show_teacher_page)
teacher_page_button.grid(row=1, column=1, padx=5, pady=5)

# Show the student page initially
show_student_page()

# Configure grid weights to make frames expandable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Start the main event loop
root.mainloop()