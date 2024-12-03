import tkinter as tk
from tkinter import font
from PIL import ImageTk,Image
import database

def register():
    # Functionality for register button
    print("Register button clicked")

def attendance():
    # Functionality for attendance button
    print("Attendance button clicked")

# Create the main window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

bg_image = Image.open("b4.jpeg")
bg_image = bg_image.resize((700, 500))
background = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=700, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background, anchor="nw")

# Set a custom font
# Set custom fonts
header_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(family="Helvetica", size=12)

# Create and place a header label
header_label = tk.Label(root, text="Welcome to Face Recognition Attendance", font=header_font, bg="black",fg="white")
header_label.place(relx=0.5, rely=0.1, anchor="center")

# Create and place the Register button
register_button = tk.Button(root, text="Register", command=register, width=20, height=2, font=button_font, bg="#4CAF50", fg="white")
register_button.place(relx=0.4, rely=0.5, anchor="e")

# Create and place the Attendance button
attendance_button = tk.Button(root, text="Attendance", command=attendance, width=20, height=2, font=button_font, bg="#2196F3", fg="white")
attendance_button.place(relx=0.4, rely=0.7, anchor="e")

# Start the Tkinter event loop
root.mainloop()
