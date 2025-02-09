# ---- GUI Section (You) ---- #
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox


root = Tk()
root.title("Language Translater")
root.iconbitmap(r"C:/Users/bk701/OneDrive/Desktop/Language-Translator-GUI/image/translate.ico") 
root.geometry("880x300")

#function for translation
def translate_it():
    pass


#Text Boxes
original_text=Text(root, height=10, width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translate_button = Button(root, text="Translate\nThe input", font=("Helvetica",24), command=translate_it)
translate_button.grid(row=0, column=1,padx=10)

translated_text=Text(root, height=10, width=40)
translated_text.grid(row=0,column=2,pady=20,padx=10)


#Combo Boxes
original_combo=ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)


translated_combo=ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=2, column=0)


root.mainloop()








# ---- Translation Section (Vaidhi) ---- #



# ---- TTS Section (mayank) ---- #