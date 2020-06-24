from tkinter import *

pro = Tk()
pro.geometry("450x575+375+40")
pro.resizable(0, 0)
pro.configure(background="light green")
pro.title("Text Encryption Decryption System")

label = Label(pro, text="Text Encryption System", height=2, bg="light green")
label.configure(font="Mimmo 16")
label.pack(side=TOP)

encode_icon = PhotoImage(file="code.png")
label0 = Label(pro, image=encode_icon, bg="light green")
label0.pack(side=TOP)

label1 = Label(pro, text="\nEnter Your Message..", bg="light green")
label1.configure(font="Mimmo 15")
label1.pack(side=TOP)

text = Text(pro, width=50, height=5, wrap=WORD, bd=5, padx=3, pady=3)
text.configure(font="Arial 10")
text.pack(side=TOP)


def encyption():
    text1.delete(1.0, END)
    dictionary = {
        # UPPER_CASE
        "A": "T",
        "B": "Z",
        "C": "8",
        "D": "!",
        "E": "%",
        "F": "c",
        "G": "&",
        "H": "0",
        "I": "t",
        "J": "i",
        "K": "m",
        "L": ">",
        "M": "a",
        "N": "7",
        "O": "p",
        "P": "=",
        "Q": "K",
        "R": ":",
        "S": "U",
        "T": "N",
        "U": "*",
        "V": "D",
        "W": "v",
        "X": "^",
        "Y": "S",
        "Z": "?",
        # LOWER_CASE
        "a": "M",
        "b": "E",
        "c": "}",
        "d": "q",
        "e": "6",
        "f": "9",
        "g": "<",
        "h": "j",
        "i": "@",
        "j": "P",
        "k": "n",
        "l": "+",
        "m": "_",
        "n": "4",
        "o": "$",
        "p": "e",
        "q": "b",
        "r": ".",
        "s": "Y",
        "t": ",",
        "u": "Q",
        "v": "x",
        "w": ";",
        "x": "C",
        "y": "A",
        "z": "/",
        # NUMBER
        "0": "5",
        "1": "H",
        "2": "(",
        "3": "V",
        "4": "r",
        "5": "[",
        "6": "f",
        "7": "O",
        "8": "u",
        "9": "R",
        # SYMBOL
        "!": "g",
        "@": "w",
        "#": ")",
        "$": "F",
        "%": "z",
        "^": "L",
        "&": "3",
        "*": "-",
        "(": "G",
        ")": "k",
        "_": "#",
        "-": "1",
        "+": "s",
        "{": "W",
        "}": "2",
        "[": "J",
        "]": "d",
        ":": "h",
        ",": "o",
        ".": "X",
        "?": "{",
        "<": "I",
        ">": "y",
        "/": "]",
        "=": "B",
        ";": "l",
    }

    # print("Enter your text: ")
    message1 = text.get(1.0, END)
    encrypted = ""

    for x in message1:
        if x in dictionary:
            encrypted += dictionary[x]
        else:
            encrypted += x
    text1.insert(1.0, encrypted)


button = Button(pro, text="Encrypt", bd=4, bg="green", command=encyption)
button.configure(font="Mimmo 13")
button.pack(side=TOP)

label2 = Label(pro, text="\nHere is your secret code", bg="light green")
label2.configure(font="Mimmo 14")
label2.pack(side=TOP)

text1 = Text(pro, width=50, height=5, bd=5)
text1.configure(font="Arial 10")
text1.pack(side=TOP)

frame = Frame(pro, width=300, height=70)
frame.pack(side=TOP)


def enter():
    bro = Toplevel()
    bro.geometry("450x575+375+40")
    bro.title("Text Encryption Decryption System")
    bro.resizable(0, 0)
    bro.configure(background="light blue")

    label9 = Label(bro, text="Text Decryption System", height=2, bg="light blue")
    label9.configure(font="Mimmo 16")
    label9.pack(side=TOP)

    decode_icon = PhotoImage(file="decode.png")
    label8 = Label(bro, image=decode_icon, bg="light blue")
    label8.pack(side=TOP)

    label7 = Label(bro, text="\nEnter Your Secret Code..", bg="light blue")
    label7.configure(font="Mimmo 15")
    label7.pack(side=TOP)

    text9 = Text(bro, width=50, height=5, wrap=WORD, bd=5, padx=3, pady=3)
    text9.configure(font="Arial 10")
    text9.pack(side=TOP)

    def decryption():
        text8.delete(1.0, END)
        dictionary = {
            # UPPER_CASE
            "T": "A",
            "Z": "B",
            "8": "C",
            "!": "D",
            "%": "E",
            "c": "F",
            "&": "G",
            "0": "H",
            "t": "I",
            "i": "J",
            "m": "K",
            ">": "L",
            "a": "M",
            "7": "N",
            "p": "O",
            "=": "P",
            "K": "Q",
            ":": "R",
            "U": "S",
            "N": "T",
            "*": "U",
            "D": "V",
            "v": "W",
            "^": "X",
            "S": "Y",
            "?": "Z",
            # LOWER_CASE
            "M": "a",
            "E": "b",
            "}": "c",
            "q": "d",
            "6": "e",
            "9": "f",
            "<": "g",
            "j": "h",
            "@": "i",
            "P": "j",
            "n": "k",
            "+": "l",
            "_": "m",
            "4": "n",
            "$": "o",
            "e": "p",
            "b": "q",
            ".": "r",
            "Y": "s",
            ",": "t",
            "Q": "u",
            "x": "v",
            ";": "w",
            "C": "x",
            "A": "y",
            "/": "z",
            # NUMBER
            "5": "0",
            "H": "1",
            "(": "2",
            "V": "3",
            "r": "4",
            "[": "5",
            "f": "6",
            "O": "7",
            "u": "8",
            "R": "9",
            # SYMBOL
            "g": "!",
            "w": "@",
            ")": "#",
            "F": "$",
            "z": "%",
            "L": "^",
            "3": "&",
            "-": "*",
            "G": "(",
            "k": ")",
            "#": "_",
            "1": "-",
            "s": "+",
            "W": "{",
            "2": "}",
            "J": "[",
            "d": "]",
            "h": ":",
            "o": "'",
            "X": ".",
            "{": "?",
            "I": "<",
            "y": ">",
            "]": "/",
            "B": "=",
            "l": ";",
        }

        # print("Enter your encrypted code: ")
        message2 = text9.get(1.0, END)
        decrypted = ""

        for x in message2:
            if x in dictionary:
                decrypted += dictionary[x]
            else:
                decrypted += x
        text8.insert(1.0, decrypted)

    button8 = Button(bro, text="Decrypt", bd=4, bg="Blue", command=decryption)
    button8.configure(font="Mimmo 13")
    button8.pack(side=TOP)

    label6 = Label(bro, text="\nHere is your message", bg="light blue")
    label6.configure(font="Mimmo 14")
    label6.pack(side=TOP)

    text8 = Text(bro, width=50, height=5, bd=5, wrap=WORD, padx=3, pady=3)
    text8.configure(font="Arial 10")
    text8.pack(side=TOP)

    bro_frame = Frame(bro, width=300, height=70)
    bro_frame.pack(side=TOP)

    def clear2():
        text8.delete(1.0, END)
        text9.delete(1.0, END)

    bro_frame_button1 = Button(bro_frame, text="Clear", bd=4, bg="blue", command=clear2)
    bro_frame_button1.configure(font="Mimmo 12")
    bro_frame_button1.grid(row=1, column=1)
    bro_frame_button2 = Button(bro_frame, text="Back?", bd=4, bg="blue", command=bro.destroy)
    bro_frame_button2.configure(font="Mimmo 12")
    bro_frame_button2.grid(row=1, column=2)
    bro_frame_button3 = Button(bro_frame, text="Quit", bd=4, bg="blue", command=pro.destroy)
    bro_frame_button3.configure(font="Mimmo 12")
    bro_frame_button3.grid(row=1, column=3)

    bro.mainloop()


def clear1():
    text.delete(1.0, END)
    text1.delete(1.0, END)


frame_button1 = Button(frame, text="Clear", bd=4, bg="green", command=clear1)
frame_button1.configure(font="Mimmo 12")
frame_button1.grid(row=1, column=1)
frame_button2 = Button(frame, text="Decode?", bd=4, bg="green", command=enter)
frame_button2.configure(font="Mimmo 12")
frame_button2.grid(row=1, column=2)
frame_button3 = Button(frame, text="Quit", bd=4, bg="green", command=pro.destroy)
frame_button3.configure(font="Mimmo 12")
frame_button3.grid(row=1, column=3)

pro.mainloop()
