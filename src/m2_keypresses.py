import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# Done: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 2. (2 pts)
#   
#   Now, create a frame called frm_b that has a width of 50 and a height of 50.
#
#   Add a label to that frame that starts out with an empty string as its text.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 3. (2 pts)
#
#   For this _todo_, write a function called that update() that takes two
#   parameters:
#       - lbl       <-- Label
#       - text      <-- str
#
#   This function should update the value of the text within the given label
#   to be the string that is given.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 4. (3 pts)
#
#   For this _todo_, write an event handler function to handle any keypress. In
#   the function, check if the key pressed is a number (remember that you can
#   check if a string is a digit by using isdigit() ). If the key is a number,
#   use the update() function that you defined in the previous todo to change
#   the text in the label to be the number that was pressed.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 5. (1 pt)
#
#   Now, bind your window to your event handler.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
def update(lbl, text):
    lbl.config(text=text)

def key_pressed(event):
    if event.char.isdigit():
        update(label, event.char)

window = tk.Tk()
window.title("KeyPress Event")

frm_b = tk.Frame(window, width=50, height=50)
frm_b.pack()

label = tk.Label(frm_b, text="")
label.pack()

window.bind("<Key>", key_pressed)

window.mainloop()