# ---- GUI Section (You) ---- #
from tkinter import *

root =Tk()
root.title("Language translater")
root.iconbitmap("C:/Users/bk701/OneDrive/Desktop/Language-Translator-GUI/image/translate.ico")
root.geometry("880x300")

def translate_it():
    pass


#Text Boxes
original_text= Text(root, height=10, width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translate_button=Button(root, text="Translate!",font=("Helvetica",24), command=translate_it)
translate_button.grid(row=0,column=1,padx=10)

translate_text=Text(root, height=10, width=40)
translate_text.grid(row=0,column=2,pady=20,padx=10)

#original_combo=ttk.Combobox(root, width=50,value=)


root.mainloop()


# ---- Translation Section (Vaidhi) ---- #



# ---- TTS Section (mayank) ---- #