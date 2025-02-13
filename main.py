from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Define login credentials
USER_ID = "1"
PASSWORD = "1"

# Prioritizing Indian languages at the top
indian_languages = ["hindi", "bengali", "tamil", "telugu", "marathi", "urdu", "gujarati", "malayalam", "kannada", "punjabi","english"]
all_languages = sorted(list(LANGUAGES.values()))
languages_sorted = indian_languages + [lang for lang in all_languages if lang not in indian_languages]

# Language mapping (Full name -> Language Code)
lang_map = {v.lower(): k for k, v in LANGUAGES.items()}  # {'english': 'en', 'hindi': 'hi', ...}

# Function to verify login
def login():
    if user_id.get() == USER_ID and password.get() == PASSWORD:
        login_window.destroy()  # Close login window
        main_window()  # Open translation app
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password!")

# Function to translate text
def Translate():
    translator = Translator()
    input_text = Input_text.get(1.0, END).strip()
    source_lang = src_lang.get().strip().lower()
    target_lang = dest_lang.get().strip().lower()

    if not input_text:
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return
    
    if source_lang not in lang_map or target_lang not in lang_map:
        messagebox.showerror("Error", "Invalid languages selected! Please choose from the dropdown.")
        return

    try:
        translated = translator.translate(text=input_text, src=lang_map[source_lang], dest=lang_map[target_lang])
        Output_text.config(state=NORMAL)  # Enable editing
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
        Output_text.config(state=DISABLED)  # Disable editing after insertion
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {str(e)}")

# Function to create the main translation window
def main_window():
    global root, src_lang, dest_lang, Input_text, Output_text

    root = Tk()
    root.geometry('1080x500')
    root.resizable(0, 0)
    root.title("Language Translator")
    root.config(bg='#2C3E50')

    # Heading Label
    Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='#1ABC9C', fg='white', pady=8).pack(fill=X)
    Label(root, text="Infotact Internship Project", font='arial 15 bold', bg='white smoke', width='25').pack(side='bottom')

    # Input Text Area
    Label(root, text="Enter Text", font='arial 13 bold', bg='#2C3E50', fg='white').place(x=250, y=60)
    Input_text = Text(root, font='arial 12', height=11, wrap=WORD, padx=5, pady=5, width=60, bg='#ECF0F1', fg='#2C3E50')
    Input_text.place(x=30, y=100)

    # Output Text Area (Read-Only)
    Label(root, text="Output", font='arial 13 bold', bg='#2C3E50', fg='white').place(x=780, y=60)
    Output_text = Text(root, font='arial 12', height=11, wrap=WORD, padx=5, pady=5, width=60, bg='#BDC3C7', fg='#2C3E50')
    Output_text.place(x=600, y=100)
    Output_text.config(state=DISABLED)  # Make output read-only

    # Dropdown for Language Selection
    Label(root, text="From Language:", font="arial 12 bold", bg="#2C3E50", fg="white").place(x=20, y=30)
    src_lang = ttk.Combobox(root, values=languages_sorted, width=30, state="readonly")
    src_lang.place(x=20, y=60)
    src_lang.set("Select Input Language")

    Label(root, text="To Language:", font="arial 12 bold", bg="#2C3E50", fg="white").place(x=890, y=30)
    dest_lang = ttk.Combobox(root, values=languages_sorted, width=30, state="readonly")
    dest_lang.place(x=890, y=60)
    dest_lang.set("Select Output Language")

    # Translate Button
    trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='#E74C3C', fg='white', activebackground='red')
    trans_btn.place(x=490, y=180)

    root.mainloop()

# Create Login Window
login_window = Tk()
login_window.geometry('400x300')
login_window.resizable(0, 0)
login_window.title("Login")
login_window.config(bg='#87CEFA')

Label(login_window, text="Login", font="arial 20 bold", fg='black').pack(pady=20)

# Username Field
Label(login_window, text="Username:", font="arial 12").place(x=50, y=80)
user_id = Entry(login_window, font="arial 12")
user_id.place(x=150, y=80)

# Password Field
Label(login_window, text="Password:", font="arial 12").place(x=50, y=120)
password = Entry(login_window, font="arial 12", show="*")
password.place(x=150, y=120)

# Login Button
login_btn = Button(login_window, text="Login", font="arial 12 bold", command=login, bg="dark blue", fg="white")
login_btn.place(x=170, y=180)

# Bind the Enter key to the login function
login_window.bind('<Return>', lambda event: login())

login_window.mainloop()
