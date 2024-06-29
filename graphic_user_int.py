import tkinter as tk
from tkinter import messagebox, ttk
from personen import Person, Mitarbeiter, Kunde, Course

def button_add_person(class_name, name, subject=None):
    try:
        if class_name == 'Mitarbeiter':
            person = Person.add_person(Mitarbeiter, name, subject)
        elif class_name == 'Kunde':
            person = Person.add_person(Kunde, name)

        messagebox.showinfo("Success", f"added {class_name}: {name}.")
        
    except Exception as e:
        messagebox.showerror("Error", f"failed to add {class_name}: {name} due to {e}.")

def button_add_interface():
    new_window = tk.Toplevel(root)
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

    def button_add_confirm():
        class_name  = class_name_entry.get()
        name = name_entry.get()
        subject = subject_entry.get() if class_name == 'Mitarbeiter' else None
        button_add_person(class_name, name, subject)

    button_add_confirm = ttk.Button(new_window, text='Add Vehicle', command=button_add_confirm)
    button_add_confirm.grid(row=3, column=0, columnspan=2, pady=10)

    close_button = ttk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.grid(row=4, column=0, columnspan=2, pady=10)

# Main Tkinter Window

root = tk.Tk()
root.title("Vereinsverwaltung")
root.geometry("500x309")

label = ttk.Label(root, text="Vereinsverwaltungs App")
label.grid(row=0, column=1, padx=5, pady=5)

# Button for adding new persons
button_add_interface_label = ttk.Label(root, text="add a Person")
button_add_interface_label.grid(row=1, column=0, padx=5, pady=5)
button_add_interface = ttk.Button(root, text="click to add", command=button_add_interface)
button_add_interface.grid(row=1, column=1)
# Button for deleting persons


# Button for exporting Persons


# Button for importing Persons


root.mainloop()