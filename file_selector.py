import os
from tkinter import filedialog


def check_containing(filepath, text):
    t = read_file(filepath)
    if text in t:
        return True
    return False

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception:
        print("Error while reading path: " + path)
        print("no such file")
        return None

def choose_file():
    file_path = filedialog.askopenfilename()
    return file_path

def test():

    test_text = "helloworld"
    path = input("press enter to choose a file with the explorer, or enter a path: ")
    choose_file()
    print("ok...")

    if path == "":
        path = choose_file()

    res = check_containing(path, test_text)
    if res:
        print(f"This file contains '{test_text}'!")
    else:
        print("This file is not containing the given text")


if __name__ == "__main__":
    test()
