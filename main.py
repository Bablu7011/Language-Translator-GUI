
# ---- Login Section (mayank) ---- #
"""
mayank - Login Page and Related Functions
Responsible for authentication, user verification, and data security."""



# Define login credentials
USER_ID = "1"
PASSWORD = "1"

# Function to verify login
def login():
    if user_id.get() == USER_ID and password.get() == PASSWORD:
        login_window.withdraw()  # Hide login window instead of destroying it
        root.after(100, main_window)  # Open translation app smoothly
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password!")

# Prioritizing Indian languages at the top
indian_languages = ["hindi", "bengali", "tamil", "telugu", "marathi", "urdu", "gujarati", "malayalam", "kannada", "punjabi", "english"]
all_languages = sorted(list(LANGUAGES.values()))
languages_sorted = indian_languages + [lang for lang in all_languages if lang not in indian_languages]

# Language mapping (Full name -> Language Code)
lang_map = {v.lower(): k for k, v in LANGUAGES.items()}  # {'english': 'en', 'hindi': 'hi', ...}

# Language Selection
Label(root, text="From Language:", font="arial 12 bold", bg="#2C3E50", fg="white").place(x=80, y=30)
src_lang = ttk.Combobox(root, values=languages_sorted, width=30, state="readonly")
src_lang.place(x=50, y=60)
src_lang.set("Select Input Language")

Label(root, text="To Language:", font="arial 12 bold", bg="#2C3E50", fg="white").place(x=850, y=30)
dest_lang = ttk.Combobox(root, values=languages_sorted, width=30, state="readonly")
dest_lang.place(x=800, y=60)
dest_lang.set("Select Output Language")

# Translate Button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='#E74C3C', fg='white', activebackground='red')
trans_btn.place(x=500, y=250)

# Copy & Paste Buttons
Button(root, text="📋 Copy", font='arial 10 bold', command=lambda: copy_text(Input_text), bg='#1ABC9C', fg='white').place(x=300, y=90)
Button(root, text="📄 Paste", font='arial 10 bold', command=lambda: paste_text(Input_text), bg='#3498DB', fg='white').place(x=370, y=90)

root.mainloop()