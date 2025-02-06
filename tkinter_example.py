import tkinter as tk

def change_text():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Button Click Example")

# Add a label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Add a button widget
button = tk.Button(window, text="Click Me", command=change_text)
button.pack()

# Run the application
window.mainloop()
