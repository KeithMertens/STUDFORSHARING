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
        self.root.geometry("500x500")
        self.root.resizable(False, False)  # Prevent resizing
        
        # Colors and fonts
        self.bg_color = "#f4f4f4"
        self.button_color = "#4CAF50"
        self.button_hover = "#45a049"
        self.font_title = ("Arial", 20, "bold")
        self.font_label = ("Arial", 12)
        self.font_button = ("Arial", 14, "bold")
        
        self.btn_txt = ["Add Student", "Print All Students", "Print Student by ID", "Logout"]
        self.func = [self.add_student_screen, self.print_all_students_gui, self.print_student_screen, self.login_screen]

        # Initial Login Screen
        self.login_screen()

    def style_button(self, button):
        button.config(
            bg=self.button_color, 
            fg="white", 
            activebackground=self.button_hover, 
            cursor="hand2",
            relief="flat"
        )

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()
        self.root.config(bg=self.bg_color)

        login_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        login_frame.pack(expand=True)

        tk.Label(login_frame, text="Student Management System", font=self.font_title, bg=self.bg_color).pack(pady=10)
        tk.Label(login_frame, text="Enter Student ID:", font=self.font_label, bg=self.bg_color).pack(pady=5)

        self.student_id_entry = tk.Entry(login_frame, font=self.font_label, justify="center")
        self.student_id_entry.pack(pady=5)

        login_button = tk.Button(login_frame, text="Login", font=self.font_button, command=self.login)
        self.style_button(login_button)
        login_button.pack(pady=10)

    def main_menu(self):
        self.clear_screen()
        self.root.config(bg=self.bg_color)

        menu_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        menu_frame.pack(expand=True)

        tk.Label(menu_frame, text="Main Menu", font=self.font_title, bg=self.bg_color).pack(pady=10)

        for i, txt in enumerate(self.btn_txt):
            button = tk.Button(menu_frame, text=txt, font=self.font_button, width=20, command=self.func[i])
            self.style_button(button)
            button.pack(pady=5)

    def add_student_screen(self):
        self.clear_screen()

        add_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        add_frame.pack(expand=True)

        tk.Label(add_frame, text="Add Student", font=self.font_title, bg=self.bg_color).pack(pady=10)

        fields = [("Student ID:", "id"), ("Name:", "name"), ("Age:", "age"), ("Email:", "email"), ("Phone Number:", "phone")]
        entries = {}

        for label_text, key in fields:
            tk.Label(add_frame, text=label_text, font=self.font_label, bg=self.bg_color).pack(pady=5)
            entry = tk.Entry(add_frame, font=self.font_label)
            entry.pack(pady=5)
            entries[key] = entry

        def submit():
            try:
                student_id = entries["id"].get().strip()
                name = entries["name"].get().strip()
                age = int(entries["age"].get().strip())
                email = entries["email"].get().strip()
                phone = entries["phone"].get().strip()

                if student_id and name and age and email and phone:
                    add_student(name, age, student_id, email, phone)
                    messagebox.showinfo("Success", "Student added successfully!")
                    self.main_menu()
                else:
                    messagebox.showerror("Error", "All fields are required.")
            except ValueError:
                messagebox.showerror("Error", "Age must be a valid number.")

        tk.Button(add_frame, text="Submit", font=self.font_button, command=submit).pack(pady=10)
        tk.Button(add_frame, text="Back", font=self.font_button, command=self.main_menu).pack(pady=5)

    def print_student_screen(self):
        self.clear_screen()

        print_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        print_frame.pack(expand=True)

        tk.Label(print_frame, text="Print Student by ID", font=self.font_title, bg=self.bg_color).pack(pady=10)

        tk.Label(print_frame, text="Enter Student ID:", font=self.font_label, bg=self.bg_color).pack(pady=5)
        student_id_entry = tk.Entry(print_frame, font=self.font_label)
        student_id_entry.pack(pady=5)

        def submit():
            student_id = student_id_entry.get().strip()
            student = print_student(student_id)
            if student:
                messagebox.showinfo(
                    "Student Details",
                    f"ID: {student.student_id}\nName: {student.name}\nAge: {student.age}\nEmail: {student.email}\nPhone: {student.phonenum}"
                )
            else:
                messagebox.showerror("Error", "Student not found!")

        tk.Button(print_frame, text="Submit", font=self.font_button, command=submit).pack(pady=10)
        tk.Button(print_frame, text="Back", font=self.font_button, command=self.main_menu).pack(pady=5)

    def print_all_students_gui(self):
        self.clear_screen()

        all_students_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        all_students_frame.pack(expand=True)

        tk.Label(all_students_frame, text="All Students", font=self.font_title, bg=self.bg_color).pack(pady=10)

        listbox = tk.Listbox(all_students_frame, font=self.font_label, width=50, height=10)
        listbox.pack(pady=5)

        for student in students:
            listbox.insert(tk.END, f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}")

        tk.Button(all_students_frame, text="Back", font=self.font_button, command=self.main_menu).pack(pady=10)

    def login(self):
        student_id = self.student_id_entry.get().strip()
        if any(student.student_id == student_id for student in students):
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid Student ID.")


root = tk.Tk()
app = StudentApp(root)
root.mainloop()
