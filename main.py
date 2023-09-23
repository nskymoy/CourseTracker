import tkinter as tk
from tkinter import ttk
import sqlite3


window = tk.Tk()
window.title("Course Tracker")


bg_color = "#f0f0f0"  # Light gray
text_color = "#333333"  # Dark gray
accent_color = "#007acc"  # Blue


window.configure(bg=bg_color)


frame = ttk.Frame(window)
frame.pack(padx=20, pady=20)


custom_font = ("Arial", 10)


def enter_data():
    coursename = course_name_entry.get()
    professorname = professor_name_entry.get()
    room = room_entry.get()
    startdate = start_date_entry.get()
    enddate = end_date_entry.get()
    grade = grade_entry.get()
    labcheckif = lab_var.get()
    creditsamount = credits_entry.get()

    # Open the database connection
    conn = sqlite3.connect('coursetracker.db')

    # Create the table if it doesn't exist
    table_create_query = '''CREATE TABLE IF NOT EXISTS Course_Tracker_Data
            (coursename TEXT, professorname TEXT, room TEXT, startdate TEXT,
            enddate TEXT, grade TEXT, labcheckif TEXT, creditsamount INT)
    '''
    conn.execute(table_create_query)

    # Insert the data into the table
    data_insert_query = '''INSERT INTO Course_Tracker_Data (coursename, professorname, room, startdate,
    enddate, grade, labcheckif, creditsamount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

    data_insert_tuple = (coursename, professorname, room, startdate, enddate, grade, labcheckif, creditsamount)

    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)

    # Commit changes and close the database connection
    conn.commit()
    conn.close()

    # Print the inserted data (for debugging)
    print("Data Inserted:")
    print("Course Name:", coursename)
    print("Professor:", professorname)
    print("Room:", room)
    print("Start Date:", startdate)
    print("End Date:", enddate)
    print("Overall Grade:", grade)
    print("Lab Check:", labcheckif)
    print("Credits Amount:", creditsamount)


# Function to create labels with the font and color
def create_label(parent, text, row, column, columnspan=1):
    label = ttk.Label(parent, text=text, font=custom_font, foreground=text_color)
    label.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=5, sticky="w")

# Create a labeled frame for Course Tracker
course_tracker_frame = ttk.LabelFrame(frame, text="Course Tracker", labelanchor="n", padding=10)
course_tracker_frame.grid(row=0, column=0, sticky="nsew")

# Labels and entry widgets for course information
create_label(course_tracker_frame, "Course Name", 0, 0)
course_name_entry = ttk.Entry(course_tracker_frame, font=custom_font)
course_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

create_label(course_tracker_frame, "Professor", 1, 0)
professor_name_entry = ttk.Entry(course_tracker_frame, font=custom_font)
professor_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

create_label(course_tracker_frame, "Room/Location", 2, 0)
room_entry = ttk.Entry(course_tracker_frame, font=custom_font)
room_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

create_label(course_tracker_frame, "Course Start Date", 3, 0)
start_date_entry = ttk.Entry(course_tracker_frame, font=custom_font)
start_date_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

create_label(course_tracker_frame, "Course End Date", 4, 0)
end_date_entry = ttk.Entry(course_tracker_frame, font=custom_font)
end_date_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

create_label(course_tracker_frame, "Overall Grade", 5, 0)
grade_entry = ttk.Entry(course_tracker_frame, font=custom_font)
grade_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

# Create a labeled frame for miscellaneous information
misc_frame = ttk.LabelFrame(frame, labelanchor="n", padding=10)
misc_frame.grid(row=1, column=0, sticky="nsew")

create_label(misc_frame, "Lab (Is there a lab class?)", 0, 0, columnspan=2)
lab_var = tk.StringVar()
lab_check = ttk.Checkbutton(misc_frame, text="Yes", variable=lab_var, onvalue="Yes", offvalue="No", style="TCheckbutton")
lab_check.grid(row=0, column=2, padx=10, pady=5, sticky="w")

create_label(misc_frame, "Course Credit(s)", 1, 0)
credits_entry = ttk.Spinbox(misc_frame, from_=0, to=999, font=custom_font)
credits_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Set uniform column weights for resizing
frame.grid_columnconfigure(0, weight=1)
course_tracker_frame.grid_columnconfigure(1, weight=1)
misc_frame.grid_columnconfigure(1, weight=1)

button_style = ttk.Style()
button_style.configure("Modern.TButton", font=custom_font, foreground=text_color)
button = ttk.Button(frame, text="Enter Data", style="Modern.TButton", command = enter_data)
button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")



window.geometry("800x500")
window.minsize(400, 300)


window.mainloop()