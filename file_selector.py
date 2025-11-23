import tkinter as tk
from tkinter import filedialog

def choose_file():
    root = tk.Tk()
    root.withdraw()  # versteckt das Hauptfenster
    file_path = filedialog.askopenfilename()
    root.destroy()   # Root nach dem Dialog schließen
    return file_path

def check_containing(path, text):
    if not path:
        return False
    try:
        with open(path, "r", encoding="utf8", errors="ignore") as f:
            return text in f.read()
    except Exception as e:
        print("Error:", e)
        return False

def test():
    test_text = "helloworld"
    path = choose_file()
    res = check_containing(path, test_text)
    if res:
        print(f"This file contains '{test_text}'!")
    else:
        print("This file is not containing the given text")

test()