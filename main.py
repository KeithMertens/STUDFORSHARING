import tkinter as tk
from tkinter import messagebox
from add_student import *
from print_all_students import print_all_students
from print_student import print_student

# Load students from the database
add_student_from_database()


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.btn_txt = ["Add Student", "Print All Students", "Print Student by ID", "Logout"]
        self.func = [self.add_student_screen, self.print_all_students_screen, self.print_student_screen, self.login_screen]

        # Create Login Screen
        self.login_screen()

    def login_screen(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create Login Frame
        login_frame = tk.Frame(self.root)
        login_frame.pack(pady=50)

        tk.Label(login_frame, text="Student Management System", font=("Arial", 20)).pack(pady=10)
        tk.Label(login_frame, text="Enter Student ID:", font=("Arial", 14)).pack(pady=5)

        self.student_id_entry = tk.Entry(login_frame, font=("Arial", 14))
        self.student_id_entry.pack(pady=5)

        login_button = tk.Button(
            login_frame,
            text="Login",
            font=("Arial", 14),
            command=self.login
        )
        login_button.pack(pady=10)

    def main_menu(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create Main Menu Frame
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=50)

        tk.Label(menu_frame, text="Main Menu", font=("Arial", 20)).pack(pady=10)

        # Dynamically create buttons from btn_txt and func
        for i, txt in enumerate(self.btn_txt):
            tk.Button(
                menu_frame,
                text=txt,
                font=("Arial", 14),
                command=self.func[i]
            ).pack(pady=5)

    def add_student_screen(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=50)

        tk.Label(add_frame, text="Add Student", font=("Arial", 20)).pack(pady=10)

        tk.Label(add_frame, text="Student ID:", font=("Arial", 14)).pack(pady=5)
        student_id_entry = tk.Entry(add_frame, font=("Arial", 14))
        student_id_entry.pack(pady=5)

        tk.Label(add_frame, text="Name:", font=("Arial", 14)).pack(pady=5)
        name_entry = tk.Entry(add_frame, font=("Arial", 14))
        name_entry.pack(pady=5)

        tk.Label(add_frame, text="Age:", font=("Arial", 14)).pack(pady=5)
        age_entry = tk.Entry(add_frame, font=("Arial", 14))
        age_entry.pack(pady=5)

        tk.Label(add_frame, text="Email:", font=("Arial", 14)).pack(pady=5)
        email_entry = tk.Entry(add_frame, font=("Arial", 14))
        email_entry.pack(pady=5)

        tk.Label(add_frame, text="Phone Number:", font=("Arial", 14)).pack(pady=5)
        phonenum_entry = tk.Entry(add_frame, font=("Arial", 14))
        phonenum_entry.pack(pady=5)

        def submit():
            student_id = student_id_entry.get()
            name = name_entry.get()
            age = age_entry.get()
            email = email_entry.get()
            phonenum = phonenum_entry.get()
            if student_id and name and age and email and phonenum:
                try:
                    age = int(age)  # Validate age as a number
                    add_student(name, age, student_id, email, phonenum)
                    messagebox.showinfo("Success", "Student added successfully!")
                    self.main_menu()
                except ValueError:
                    messagebox.showerror("Error", "Age must be a valid number.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(
            add_frame,
            text="Submit",
            font=("Arial", 14),
            command=submit
        ).pack(pady=10)

        tk.Button(
            add_frame,
            text="Back",
            font=("Arial", 14),
            command=self.main_menu
        ).pack(pady=5)

    def print_all_students_screen(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        print_all_frame = tk.Frame(self.root)
        print_all_frame.pack(pady=50)

        tk.Label(print_all_frame, text="All Students", font=("Arial", 20)).pack(pady=10)

        # Fetch and display all students
        all_students = print_all_students()  # Assume this returns a list of strings
        if all_students:
            for student in all_students:
                tk.Label(print_all_frame, text=student, font=("Arial", 12)).pack(anchor="w", padx=10, pady=2)
        else:
            tk.Label(print_all_frame, text="No students found.", font=("Arial", 14)).pack(pady=5)

        tk.Button(
            print_all_frame,
            text="Back",
            font=("Arial", 14),
            command=self.main_menu
        ).pack(pady=10)

    def print_student_screen(self):
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        print_frame = tk.Frame(self.root)
        print_frame.pack(pady=50)

        tk.Label(print_frame, text="Print Student by ID", font=("Arial", 20)).pack(pady=10)

        tk.Label(print_frame, text="Enter Student ID:", font=("Arial", 14)).pack(pady=5)
        student_id_entry = tk.Entry(print_frame, font=("Arial", 14))
        student_id_entry.pack(pady=5)

        def submit():
            student_id = student_id_entry.get()
            if student_id:
                print_student(student_id)
            else:
                messagebox.showerror("Error", "Student ID is required.")

        tk.Button(
            print_frame,
            text="Submit",
            font=("Arial", 14),
            command=submit
        ).pack(pady=10)

        tk.Button(
            print_frame,
            text="Back",
            font=("Arial", 14),
            command=self.main_menu
        ).pack(pady=5)

    def login(self):
        student_id = self.student_id_entry.get()
        if any(student.student_id == student_id for student in students):  # Validate ID
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid Student ID.")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
