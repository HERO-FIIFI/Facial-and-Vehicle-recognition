import tkinter as tk
from tkinter import simpledialog, messagebox
import cv2
from vehiclerecognition import recognize_license_plate
from db_workers import is_operator_assigned
from facialrecognition import capture_face_from_camera, load_known_faces_from_db

# Function to handle the login button click
def login():
    admin_name = admin_name_entry.get()
    password = password_entry.get()

    # Implement your authentication logic here
    # For simplicity, we will consider any input as valid
    if admin_name and password:
        main_login_interface.withdraw()
        options_interface.deiconify()
    else:
        messagebox.showerror("Login Error", "Invalid credentials")

# Create the main login interface
main_login_interface = tk.Tk()
main_login_interface.title("Admin Login")
main_login_interface.geometry('900x550')  # Set the size of the main interface

# Set core colors
blue_color = '#0A0A5C'
white_color = '#FFFFFF'

# Create a frame for the pattern around the login box
pattern_frame = tk.Frame(main_login_interface, bg=blue_color, width=900, height=550)
pattern_frame.place(x=0, y=0)

# Create a smaller login box within the main interface
login_box = tk.Frame(main_login_interface, bg=white_color, width=400, height=200)
login_box.place(relx=0.5, rely=0.5, anchor='center')

# Create widgets for the login box
admin_name_label = tk.Label(login_box, text="Admin Name:", bg=white_color)
admin_name_label.grid(row=0, column=0)
admin_name_entry = tk.Entry(login_box)
admin_name_entry.grid(row=0, column=1)
password_label = tk.Label(login_box, text="Password:", bg=white_color)
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_box, show="*")
password_entry.grid(row=1, column=1)
login_button = tk.Button(login_box, text="Login", command=login)
login_button.grid(row=2, columnspan=2)



def verify_employee_gui():

    from vehicle_recognition import recognize_license_plate
    from facialrecognition import capture_face_from_camera

    def open_camera_for_recognition(recognition_type):
        frame = capture_image_from_camera()

        if frame is not None:
            if recognition_type == 'recognize_license_plate':
                license_plate = recognize_license_plate(frame)
                print("License Plate:", license_plate)
            elif recognition_type == 'capture_face_from_camera':
                    face_data = capture_face_from_camera(frame)
                    print("Face Data:", face_data)
            else:
                        print("Invalid recognition type specified")
        else:
                    print("No image captured from camera")

        open_camera('recognize_license_plate')

        open_camera('capture_face_from_camera')

    pass
pass


def add_employee():

    def add_employee_gui():

    # Add widgets, labels, entry fields, buttons, etc., to the add_employee_dialog
        label = tk.Label(add_employee_dialog, text="Enter Employee Details")
        label.pack()

    # Set core colors
        blue_color = '#0A0A5C'
        white_color = '#FFFFFF'


        # Ask for employee details using simpledialog
        first_name = simpledialog.askstring("Input", "Enter first name")
        last_name = simpledialog.askstring("Input", "Enter last name")
        emp_id = simpledialog.askstring("Input", "Enter employee ID")
        birth_date = simpledialog.askstring("Input", "Enter birth date (YYYY-MM-DD)")
        email = simpledialog.askstring("Input", "Enter email")
        phone = simpledialog.askstring("Input", "Enter phone")
        address = simpledialog.askstring("Input", "Enter address")

        # Perform database operation (add_employee)
        if all([first_name, last_name, emp_id, birth_date, email, phone, address]):
            connection = get_db_connection()
            add_employee(conn, first_name, last_name, emp_id, birth_date, email, phone, address)

        # print the entered details
            print("Employee Details:")
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Employee ID: {emp_id}")
            print(f"Birth Date: {birth_date}")
            print(f"Email: {email}")
            print(f"Phone: {phone}")
            print(f"Address: {address}")


        add_employee(conn, first_name, last_name, emp_id, birth_date, email, phone, address)
        if first_name and last_name and emp_id and birth_date and email and phone and address:
            add_employee_window.destroy()
        else:
            messagebox.showerror("Input Error", "Please fill in all fields.")

    add_employee_gui()
pass


def delete_employee():

    def delete_employee_gui():
        add_employee_window = tk.Toplevel(main_login_interface)
        add_employee_window.title("Delete Employee")
        add_employee_window.geometry('400x300')

        label = tk.Label(add_employee_dialog, text="Enter Employee ID")
        label.pack()

    # Set core colors
        blue_color = '#0A0A5C'
        white_color = '#FFFFFF'

        emp_id = simpledialog.askstring("Input", "Enter employee ID")

        # Perform database operation (delete_employee)
        if all([emp_id]):
            connection = get_db_connection()

    delete_employee_gui()
pass

def logout():
    options_interface.withdraw()
    main_program()


# Create the options interface
options_interface = tk.Toplevel(main_login_interface)
options_interface.title("Access Garuntor")
options_interface.geometry('900x550')  # Set the size of the options interface
options_interface.withdraw()  # Hide it initially

# Buttons for options interface
add_employee_button = tk.Button(options_interface, text="Add New Employee", command=add_employee_gui)
add_employee_button.pack()
delete_employee_button = tk.Button(options_interface, text="Delete Employee",command=delete_employee_gui)
delete_employee_button.pack()
verify_employees_button = tk.Button(options_interface, text="Verify Employees",command=verify_employee_gui)
verify_employees_button.pack()
logout_button = tk.Button(options_interface, text="Logout",command=logout)
logout_button.pack()

# Start the Tkinter main loop
main_login_interface.mainloop()


