import tkinter as tk

###############################################################################
# Done: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# Done: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()
window.title("Form")

def print_form():
    form_data = {}
    for label_text, entry in zip(labels, entries):
        form_data[label_text] = entry.get()
    print("Form Submitted")
    for label, value in form_data.items():
        print(label + ":", value)

header_frame = tk.Frame(window)
header_frame.pack(side=tk.TOP)

form_frame = tk.Frame(window)
form_frame.pack(side=tk.TOP)

header_label = tk.Label(header_frame, text="Form Details", font=("Helvetica", 16))
header_label.pack()

labels = ["Name", "Address Line 1", "Address Line 2", "City", "State", "Zip Code", "Phone Number", "Email Address"]
entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(form_frame, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5)
    
    entry = tk.Entry(form_frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

submit_button = tk.Button(window, text="Submit", command=print_form)  # Connect button to print_form function
submit_button.pack(pady=10)

window.configure(bg='cyan')
for entry in entries:
    entry.configure(bg='yellow')

window.mainloop()