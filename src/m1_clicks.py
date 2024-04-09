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
# Done: 2. (4 pts)
#
#   Now, create a frame called frm_a that has a width of 100 and height of 100.
#
#   Use the bind() method to bind that frame to both a left mouse click and a
#   right mouse click. You will need to bind frm_a twice.
#
#   You will see this in the resources for Session 21, but the event pattern
#   for left click is "<Button-1>" and the event pattern for right click is
#   "<Button-3>".
#
#   When the user presses the left mouse button, the program should print
#   "Left". Similarly, when the user presses the right mouse button, it should
#   print "Right".
#
#   To accomplish this, you will need two event handlers, one for the left
#   mouse click and one for the right mouse click.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
def left_click(event):
    print("Left")

def right_click(event):
    print("Right")

window = tk.Tk()
window.title("Mouse Click Events")

frm_a = tk.Frame(window, width=100, height=100)
frm_a.pack()

frm_a.bind("<Button-1>", left_click)
frm_a.bind("<Button-3>", right_click)

window.mainloop()