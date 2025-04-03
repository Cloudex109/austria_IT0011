# Import necessary libraries
import tkinter as tk              
from tkinter import messagebox    
import json                      
import os                        
from PIL import Image, ImageTk    # For handling and displaying images
from datetime import datetime     

# Create the main window
root = tk.Tk()                   
root.title("Three Kings and the Queen - Attendance Monitoring System")  
root.geometry("500x300")         
root.configure(bg="#FFD700")      

# Define the filename for saving student data
filename = "students.json"     

# Load existing data or create an empty dictionary if file doesn't exist
if os.path.exists(filename):      
    with open(filename, 'r') as file:  
        students = json.load(file)     
else:
    students = {}           

# Function to save data to file
def save_data():
    with open(filename, 'w') as file:  
        json.dump(students, file)      

# Function to clear all widgets from the window
def clear_window():
    for widget in root.winfo_children(): 
        widget.destroy()                  

# Function to create the main menu
def create_menu():
    clear_window()                   
    image = Image.open("feu_logo.png") 
    photo = ImageTk.PhotoImage(image)   
    logo_label = tk.Label(root, image=photo, bg="#FFD700")  
    logo_label.image = photo         
    logo_label.pack(pady=10)          
    
    tk.Label(root, text="Three Kings and the Queen\nAttendance Monitoring System", 
             font=("Arial", 16), bg="#FFD700").pack(pady=20)  
    
    # Create menu buttons with commands to switch screens
    tk.Button(root, text="[1] Sign-up", command=signup_form, bg="#2E8B57", 
              font=("Arial", 12), width=20).pack(pady=5)   
    tk.Button(root, text="[2] Attendance", command=attendance_form, bg="#2E8B57", 
              font=("Arial", 12), width=20).pack(pady=5)   
    tk.Button(root, text="[3] View all records", command=view_records, bg="#2E8B57", 
              font=("Arial", 12), width=20).pack(pady=5)    
    tk.Button(root, text="[4] Search a record", command=search_record, bg="#2E8B57", 
              font=("Arial", 12), width=20).pack(pady=5)     
    tk.Button(root, text="[5] Exit", command=root.quit, bg="#2E8B57", 
              font=("Arial", 12), width=20).pack(pady=5)     

# Function to create sign-up form
def signup_form():
    clear_window()                 
    image = Image.open("feu_logo.png") 
    photo = ImageTk.PhotoImage(image)  
    logo_label = tk.Label(root, image=photo, bg="#FFD700")  
    logo_label.image = photo          
    logo_label.pack(pady=10)          
    
    global entries                    
    entries = {}                     
    fields = ["First Name", "Middle Name", "Last Name", "Birthday (DD/MM/YYYY)", "Gender", "Student Number"]
 
    
    for field in fields:             
        frame = tk.Frame(root, bg="#FFD700")  
        frame.pack(pady=5)            
        tk.Label(frame, text=field, width=20, bg="#FFD700").pack(side=tk.LEFT)  
        entry = tk.Entry(frame)     
        entry.pack(side=tk.LEFT)     
        entries[field] = entry        
    
    tk.Button(root, text="Submit", command=save_signup, bg="#2E8B57", width=15).pack(pady=10)  
    tk.Button(root, text="Back", command=create_menu, bg="#2E8B57", width=15).pack(pady=5)     

# Function to save sign-up data
def save_signup():
    student_num = entries["Student Number"].get() 
    if student_num in students:       
        messagebox.showerror("Error", "Student number already exists!")  
        return                        
    
    birthday = entries["Birthday (DD/MM/YYYY)"].get()  #
    try:
        datetime.strptime(birthday, "%d/%m/%Y")  # Validate birthday format (DD/MM/YYYY)
    except ValueError:                
        messagebox.showerror("Error", "Invalid birthday format! Use DD/MM/YYYY (e.g., 25/12/2000)") 
        return                     
    
    students[student_num] = {        
        "first_name": entries["First Name"].get(),      
        "middle_name": entries["Middle Name"].get(),    
        "last_name": entries["Last Name"].get(),        
        "birthday": birthday,        
        "gender": entries["Gender"].get(),           
        "attendance": []              
    }
    save_data()                      
    messagebox.showinfo("Success", "Sign-up successful!")  
    create_menu()                    

# Function to create attendance form
def attendance_form():
    clear_window()                    
    image = Image.open("feu_logo.png")  
    photo = ImageTk.PhotoImage(image)   
    logo_label = tk.Label(root, image=photo, bg="#FFD700")  
    logo_label.image = photo        
    logo_label.pack(pady=10)          
    
    global att_entries               
    att_entries = {}                  
    fields = ["Student Number", "Date (mm/dd/yyyy)", "Time In", "Time Out"]
    
    for field in fields:             
        frame = tk.Frame(root, bg="#FFD700") 
        frame.pack(pady=5)            
        tk.Label(frame, text=field, width=20, bg="#FFD700").pack(side=tk.LEFT) 
        entry = tk.Entry(frame)       
        entry.pack(side=tk.LEFT)      
        att_entries[field] = entry    
    
    tk.Button(root, text="Submit", command=save_attendance, bg="#2E8B57", width=15).pack(pady=10)  
    tk.Button(root, text="Back", command=create_menu, bg="#2E8B57", width=15).pack(pady=5)        

# Function to save attendance data
def save_attendance():
    student_num = att_entries["Student Number"].get()  
    if student_num not in students:   
        messagebox.showerror("Error", "Student not found!") 
        return                      
    
    attendance_record = {            
        "date": att_entries["Date (mm/dd/yyyy)"].get(),  
        "time_in": att_entries["Time In"].get(),        
        "time_out": att_entries["Time Out"].get()      
    }
    students[student_num]["attendance"].append(attendance_record)  
    save_data()                       
    messagebox.showinfo("Success", "Attendance recorded!")  
    create_menu()                     

# Function to view all records
def view_records():
    clear_window()                  
    image = Image.open("feu_logo.png")  
    photo = ImageTk.PhotoImage(image)  
    logo_label = tk.Label(root, image=photo, bg="#FFD700")  
    logo_label.image = photo          
    logo_label.pack(pady=10)         
    
    text = tk.Text(root, height=15, width=50)  
    text.pack(pady=10)                
    
    for student_num, data in students.items():
        text.insert(tk.END, f"Student Number: {student_num}\n")       
        text.insert(tk.END, f"Name: {data['first_name']} {data['middle_name']} {data['last_name']}\n") 
        text.insert(tk.END, f"Birthday: {data['birthday']}\n")      
        text.insert(tk.END, f"Gender: {data['gender']}\n\n")         
    
    tk.Button(root, text="Back", command=create_menu, bg="#2E8B57", width=15).pack(pady=5) 

# Function to search for a record
def search_record():
    clear_window()                    
    image = Image.open("feu_logo.png")  
    photo = ImageTk.PhotoImage(image)   
    logo_label = tk.Label(root, image=photo, bg="#FFD700") 
    logo_label.image = photo        
    logo_label.pack(pady=10)         
    
    tk.Label(root, text="Enter Student Number:", bg="#FFD700").pack(pady=5) 
    global search_entry              
    search_entry = tk.Entry(root)     
    search_entry.pack()               
    
    tk.Button(root, text="Search", command=show_search_result, bg="#2E8B57", width=15).pack(pady=5)  
    tk.Button(root, text="Back", command=create_menu, bg="#2E8B57", width=15).pack(pady=5)          
    
    global result_text                
    result_text = tk.Text(root, height=10, width=50)  
    result_text.pack(pady=10)        

# Function to show search results
def show_search_result():
    result_text.delete(1.0, tk.END)   
    student_num = search_entry.get()  
    
    if student_num in students:      
        data = students[student_num]  
        result_text.insert(tk.END, f"Student Number: {student_num}\n")       
        result_text.insert(tk.END, f"Name: {data['first_name']} {data['middle_name']} {data['last_name']}\n")  
        text.insert(tk.END, f"Birthday: {data['birthday']}\n")    
        result_text.insert(tk.END, f"Gender: {data['gender']}\n")           
        result_text.insert(tk.END, "\nAttendance:\n")                     
        for att in data["attendance"]:  
            result_text.insert(tk.END, f"Date: {att['date']}, In: {att['time_in']}, Out: {att['time_out']}\n")  
    else:
        result_text.insert(tk.END, "Student not found!") 

# Start the program by showing the menu
create_menu()
root.mainloop()   
