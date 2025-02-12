# ---- GUI Section (You) ---- #



# ---- Translation Section (Vaidhi) ---- #



# ---- TTS Section (mayank) ---- #
from tkinter import *
from tts import text_to_speech  # Importing TTS module

root = Tk()
root.title("Language Translator")
root.iconbitmap("C:/Users/bk701/OneDrive/Desktop/Language-Translator-GUI/image/translate.ico")
root.geometry("880x350")

def translate_it():
    """Dummy translation function (Replace with actual logic)"""
    translated_text = original_text.get("1.0", END).strip()[::-1]  # Reverse text as placeholder
    translate_text.delete("1.0", END)
    translate_text.insert(END, translated_text)

def speak_text():
    """Fetch translated text and pass it to TTS module."""
    text = translate_text.get("1.0", END).strip()
    text_to_speech(text)  # Call TTS function

# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translate_text = Text(root, height=10, width=40)
translate_text.grid(row=0, column=2, pady=20, padx=10)

# TTS Button
tts_button = Button(root, text="🔊 Speak", font=("Helvetica", 14), command=speak_text)
tts_button.grid(row=1, column=2, pady=10)

root.mainloop()
