import tkinter as tk
from tkinter import messagebox, ttk
from personen import Member, Official, Ordinary, Course


# class method call add_member
def button_add_Member(class_name, name, subject=None):
    try:
        if class_name == 'Official':
            member = Member.add_Member(Official, name, subject)
        elif class_name == 'Ordinary':
            member = Member.add_Member(Ordinary, name)

        messagebox.showinfo("Success", f"added {class_name}: {name}.")

    except Exception as e:
        messagebox.showerror("Error", f"failed to add {class_name}: {name} due to {e}.")

# class method call del_Member
def button_del_Member(class_name, name, subject=None):
    try:
        if class_name == 'Official':
            member = Member.del_Member(Official, name, subject)
        elif class_name == 'Ordinary':
            member = Member.del_Member(Ordinary, name)
        messagebox.showinfo("Success", f"deleted {class_name}: {name}.")

    except Exception as e:
        messagebox.showerror("Error", f"failed due to {e}")

# method call to import export functions
def button_import_export(file, action):
    try:
        if action == 'import':
            Member.import_Members(file)
            Member.print_Member_imports(file)
            messagebox.showinfo("Success", f"imported: {Member.name}")
        elif action == 'export':
            Member.export_Member_to_new_file(file, Member.instances)
            messagebox.showinfo("Success", f"members exported")
        elif action == 'export append':
            Member.export_Member_append(file, Member.instances)
            messagebox.showinfo("Success", f"members appended")

    except Exception as e:
        messagebox.showerror("Error", f"failed due to {e}")
        
def button_interface():
    new_window = tk.Toplevel()
    new_window.title("Add new object Dialogue")
    new_window.geometry("500x309")

    class_name_label = ttk.Label(new_window, text="Class:")
    class_name_label.grid(row=0, column=0, padx=5, pady=5)
    class_name_entry = ttk.Entry(new_window, width=35)
    class_name_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = ttk.Label(new_window, text="name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(new_window, width=35)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    subject_label = ttk.Label(new_window, text="subject:")
    subject_label.grid(row=2, column=0, padx=5, pady=5)
    subject_entry = ttk.Entry(new_window, width=35)
    subject_entry.grid(row=2, column=1, padx=5, pady=5)

    # button to delete member
    def button_del_confirm():
        class_name  = class_name_entry.get()
        name = name_entry.get()
        subject = subject_entry.get() if class_name == 'Official' else None
        button_del_Member(class_name, name, subject)
    button_del_confirm = ttk.Button(new_window, text="Delete a Member", command=button_del_confirm)
    button_del_confirm.grid(row=3, column=0, columnspan=2, pady=10)

    # button to add member
    def button_add_confirm():
        class_name  = class_name_entry.get()
        name = name_entry.get()
        subject = subject_entry.get() if class_name == 'Official' else None
        button_add_Member(class_name, name, subject)

    button_add_confirm = ttk.Button(new_window, text='Add a Member', command=button_add_confirm)
    button_add_confirm.grid(row=4, column=0, columnspan=2, pady=10)

    close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.grid(row=5, column=0, columnspan=2, pady=10)


# import/export interface

# code option menu with single input line for import and export
def button_export_options_interface():
    new_window = tk.Tk()
    new_window.title("import/export dialogue")
    new_window.geometry("500x309")

    options_list = ["import", "export", "export append"] 

    # Variable to keep track of the option 
    # selected in OptionMenu 
    value_inside = tk.StringVar(new_window) 
    
    # Set the default value of the variable 
    value_inside.set("Select an Option") 
    
    # Create the optionmenu widget and passing  
    # the options_list and value_inside to it. 
    question_menu = tk.OptionMenu(new_window, value_inside, *options_list) 
    question_menu.grid(row=1, column=0, padx=5, pady=5)

    file_label = ttk.Label(new_window, text="File location:")
    file_label.grid(row=1, column=0, padx=5, pady=5)
    file_entry = ttk.Entry(new_window, width=35)
    file_entry.grid(row=1, column=1, padx=5, pady=5)

    def button_confirm_import():
        file = file_entry.get()
        action = value_inside.get()
        button_import_export(file, action)

    button_confirm_import = ttk.Button(new_window, text="OK", command=button_confirm_import)
    button_confirm_import.grid(row=2, column=0, padx=5, pady=5)
# Main Tkinter Window

root = tk.Tk()
root.title("Vereinsverwaltung")
root.geometry("500x309")

label = ttk.Label(root, text="Vereinsverwaltungs App")
label.grid(row=0, column=1, padx=5, pady=5)

# Button for adding new Members
button_add_interface_label = ttk.Label(root, text="add or delete a Member")
button_add_interface_label.grid(row=1, column=0, padx=5, pady=5)
button_add_interface = ttk.Button(root, text="click to add", command=button_interface)
button_add_interface.grid(row=1, column=1)

# Button for exporting Members
button_export_interface_label = ttk.Label(root, text="import/export dialogue")
button_export_interface_label.grid(row=2, column=0, padx=5, pady=5)
button_export_interface = ttk.Button(root, text="options", command=button_export_options_interface)
button_export_interface.grid(row=2, column=1)

# Button for importing Members


root.mainloop()