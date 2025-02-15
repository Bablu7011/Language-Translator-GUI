from tkinter import *
from tkinter import ttk, messagebox

# the code for main window
login_window = Tk()
login_window.geometry('400x300')
login_window.resizable(0, 0)
login_window.title("Login")
login_window.config(bg='#87CEFA')

Label(login_window, text="Login", font="arial 20 bold", fg='black').pack(pady=20)

# Username box code
Label(login_window, text="Username:", font="arial 12").place(x=50, y=80)
user_id = Entry(login_window, font="arial 12")
user_id.place(x=150, y=80)

# Password box code
Label(login_window, text="Password:", font="arial 12").place(x=50, y=120)
password = Entry(login_window, font="arial 12", show="*")
password.place(x=150, y=120)

# Button for login
Button(login_window, text="Login", font="arial 12 bold", command=lambda: login(), bg="dark blue", fg="white").place(x=170, y=180)

# at the login time throgh Enter key also login happended
login_window.bind('<Return>', lambda event: login())

# not show window initially
root = Toplevel(login_window)
root.withdraw()

# write function to create the main translation window
def main_window():
    global root, src_lang, dest_lang, Input_text, Output_text

    root.deiconify()  # Show the main window
    root.update_idletasks()  # Speed up rendering

    root.geometry('1100x500')
    root.resizable(0, 0)
    root.title("Language Translator")
    root.config(bg='#2C3E50')
    root.iconbitmap("C:/Users/bk701/OneDrive/Desktop/Language-Translator-GUI/translate.ico")

    # Heading of the translatin window
    Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='#1ABC9C', fg='white', pady=8).pack(fill=X)
    Label(root, text="Infotact Internship Project", font='arial 15 bold', bg='#1ABC9C', fg='white', width=30, pady=5, relief=RAISED, bd=3).pack(side=BOTTOM, fill=X)

    # this is the input section
    Label(root, text="Enter Text", font='arial 13 bold', bg='#2C3E50', fg='white').place(x=50, y=90)
    input_frame = Frame(root, bg='#2C3E50')
    input_frame.place(x=30, y=120)
    Input_text = Text(input_frame, font='arial 12', height=10, wrap=WORD, padx=5, pady=5, width=40, bg='#34495E', fg='white')
    Scrollbar(input_frame, orient=VERTICAL, command=Input_text.yview).pack(side=RIGHT, fill=Y)
    Input_text.pack()

    # Othis is the output section
    Label(root, text="Output", font='arial 13 bold', bg='#2C3E50', fg='white').place(x=800, y=90)
    output_frame = Frame(root, bg='#2C3E50')
    output_frame.place(x=700, y=120)
    Output_text = Text(output_frame, font='arial 12', height=10, wrap=WORD, padx=5, pady=5, width=40, bg='#2C3E50', fg='white')
    Scrollbar(output_frame, orient=VERTICAL, command=Output_text.yview).pack(side=RIGHT, fill=Y)
    Output_text.pack()
