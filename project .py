import tkinter as tk
from tkinter import messagebox

# Store student data
students = []

# Function to add student
def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    marks = entry_marks.get()

    if name == "" or roll == "" or marks == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    student = f"Name: {name}, Roll: {roll}, Marks: {marks}"
    students.append(student)
    listbox.insert(tk.END, student)

    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

# Function to delete student
def delete_student():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Select", "Select a student to delete")

# Main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

# Labels
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Marks").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()

# Buttons
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

root.mainloop()
with open("students.txt", "a") as f:
    f.write(student + "\n")
    if int(marks) > 90:
     grade = "A"