import tkinter as tk

# Create a window
mywindow = tk.Tk()

# Create an instance of the label
greeting = tk.Label(text = "Salam!!", fg="white", bg="black", width=20, height=3)

# Create Label and Entry
namelabel = tk.Label(text="Name")
nameBox = tk.Entry()

# Create an instance of a button
def showname():
    print("Hello " + nameBox.get())
# Mac systems use highlightbackground instead of bg
button = tk.Button(text = "Click Here!", fg="white", bg="pink", command=showname)

# Create Label and Entry
emaillabel = tk.Label(text="Type Letter")
emailBox = tk.Text()

# Create an instance of a button
def clearbox():
    nameBox.delete(0, tk.END)
    emailBox.delete(0.0, tk.END)
# Mac systems use highlightbackground instead of bg
clearbutton = tk.Button(text = "Clear Box!", fg="white", bg="black", command=clearbox)

# Insert the GUI element into the window
greeting.pack()
namelabel.pack()
nameBox.pack()
button.pack()
emaillabel.pack()
emailBox.pack()
clearbutton.pack()

# Keeps the focus on the window I created
mywindow.mainloop()