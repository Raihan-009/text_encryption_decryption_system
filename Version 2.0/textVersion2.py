from tkinter import *
from tkinter import filedialog

pro = Tk()
pro.geometry("460x615+80+40")
pro.resizable(0, 0)
pro.configure(background="light green")
pro.title("Text Encryption Decryption System")

label = Label(pro, text="Text Encryption System", height=2, bg="light green")
label.configure(font="Mimmo 15")
label.pack(side=TOP)

encode_icon = PhotoImage(file="F://Python_with_Atom//text_V2//encoded.png")
label0 = Label(pro, image=encode_icon, bg="light green")
label0.pack(side=TOP)

label1 = Label(pro, text="\nEnter Your Message or Browse your file", bg="light green")
label1.configure(font="Mimmo 15")
label1.pack(side=TOP)

def openFile():
    zeroEntry.delete(0,END)
    file_var = filedialog.askopenfilename(initialdir= "/", title = "Select file", filetypes = (("text files", ".txt"),("all files", "*.*")))
    entryText.set(file_var)

    with open(file_var, 'r') as file:
        data = file.read()
        #print(data)
        text.insert(INSERT, data)

def saveFile():
    encodedTextContent = text1.get(1.0, END)
    text1_var = filedialog.asksaveasfilename(initialdir = "/", title = "Save file",filetypes = (("text files", ".txt"),("all files", "*.*")))

    with open(text1_var, 'w+') as encodedfile:
        encodedfile.write(encodedTextContent)

oneFrame = Frame(pro)
oneFrame.pack(side = TOP)

scrollBar = Scrollbar(oneFrame)
scrollBar.pack(side = RIGHT, fill = Y)
text = Text(oneFrame, width=50, height=7, wrap=WORD, bd=5, padx=3, pady=3, yscrollcommand = scrollBar.set)
scrollBar.config(command = text.yview)
text.configure(font="Arial 10")
text.pack()

zeroLable = Label(pro, bg = "light green")
zeroLable.pack()

entryText = StringVar()
zeroEntry = Entry(pro, textvariable = entryText, width = 59, bd = 5)
zeroEntry.pack(side = TOP)

zeroFrame = Frame(pro,width=300, height=70)
zeroFrame.pack(side = TOP)



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


zeroButton = Button(zeroFrame, text="Browse", bd=4, bg="green", command=openFile)
zeroButton.configure(font="Mimmo 13")
zeroButton.grid(row = 1, column = 1)
button = Button(zeroFrame, text="Encrypt", bd=4, bg="green", command=encyption)
button.configure(font="Mimmo 13")
button.grid(row = 1, column = 2)



label2 = Label(pro, text="\nHere is your secret code", bg="light green")
label2.configure(font="Mimmo 14")
label2.pack(side=TOP)

secondFrame = Frame(pro)
secondFrame.pack(side = TOP)

OnescrollBar = Scrollbar(secondFrame)
OnescrollBar.pack(side = RIGHT, fill = Y)
text1 = Text(secondFrame, width=50, height=7, wrap=WORD, bd=5, padx=3, pady=3, yscrollcommand = OnescrollBar.set)
OnescrollBar.config(command = text1.yview)
text1.configure(font="Arial 10")
text1.pack()

frame = Frame(pro, width=300, height=70)
frame.pack(side=TOP)


def enter():
    bro = Toplevel()
    bro.geometry("460x615+670+40")
    bro.title("Text Encryption Decryption System")
    bro.resizable(0, 0)
    bro.configure(background="light blue")

    label9 = Label(bro, text="Text Decryption System", height=2, bg="light blue")
    label9.configure(font="Mimmo 15")
    label9.pack(side=TOP)

    decode_icon = PhotoImage(file="F://Python_with_Atom//text_V2//decoded.png")
    label8 = Label(bro, image=decode_icon, bg="light blue")
    label8.pack(side=TOP)

    label7 = Label(bro, text="\nEnter Your Secret Code or Browse your file", bg="light blue")
    label7.configure(font="Mimmo 15")
    label7.pack(side=TOP)

    thirdFrame = Frame(bro)
    thirdFrame.pack(side = TOP)

    twoscrollBar = Scrollbar(thirdFrame)
    twoscrollBar.pack(side = RIGHT, fill = Y)
    text9 = Text(thirdFrame, width=50, height=7, wrap=WORD, bd=5, padx=3, pady=3, yscrollcommand = twoscrollBar.set)
    twoscrollBar.config(command = text9.yview)
    text9.configure(font="Arial 10")
    text9.pack()

    oneLable = Label(bro, bg = "light blue")
    oneLable.pack()

    def openFile2():
        zeroEntry2.delete(0,END)
        file_var2 = filedialog.askopenfilename(initialdir= "/", title = "Select file", filetypes = (("text files", ".txt"),("all files", "*.*")))
        entryText2.set(file_var2)

        with open(file_var2, 'r') as file2:
            data2 = file2.read()
            #print(data)
            text9.insert(INSERT, data2)

    def saveFile2():
        decodedTextContent = text8.get(1.0, END)
        text8_var = filedialog.asksaveasfilename(initialdir= "/", title = "Save file", filetypes = (("text files", ".txt"),("all files", "*.*")))

        with open(text8_var, 'w+') as decodedfile:
            decodedfile.write(decodedTextContent)

    entryText2 = StringVar()
    zeroEntry2 = Entry(bro, textvariable = entryText2, width = 59, bd = 5)
    zeroEntry2.pack(side = TOP)

    fourthFrame = Frame(bro, width = 300, height = 70)
    fourthFrame.pack()

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
            "o": ",",
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

    oneButton = Button(fourthFrame, text="Browse", bd=4, bg="Blue", command=openFile2)
    oneButton.configure(font="Mimmo 13")
    oneButton.grid(row = 1, column = 1)
    button2 = Button(fourthFrame, text="Decrypt", bd=4, bg="Blue", command=decryption)
    button2.configure(font="Mimmo 13")
    button2.grid(row = 1, column = 2)

    label6 = Label(bro, text="\nHere is your message", bg="light blue")
    label6.configure(font="Mimmo 14")
    label6.pack(side=TOP)

    fifthFrame = Frame(bro)
    fifthFrame.pack(side = TOP)

    threescrollBar = Scrollbar(fifthFrame)
    threescrollBar.pack(side = RIGHT, fill = Y)
    text8 = Text(fifthFrame, width=50, height=7, wrap=WORD, bd=5, padx=3, pady=3, yscrollcommand = threescrollBar.set)
    threescrollBar.config(command = text8.yview)
    text8.configure(font="Arial 10")
    text8.pack()

    bro_frame = Frame(bro, width=300, height=70)
    bro_frame.pack(side=TOP)

    def clear2():
        text8.delete(1.0, END)
        text9.delete(1.0, END)
        zeroEntry2.delete(0,END)

    bro_frame_button1 = Button(bro_frame, text="Clear", bd=4, bg="blue", command=clear2)
    bro_frame_button1.configure(font="Mimmo 12")
    bro_frame_button1.grid(row=1, column=1)
    bro_frame_button2 = Button(bro_frame, text="Back?", bd=4, bg="blue", command=bro.destroy)
    bro_frame_button2.configure(font="Mimmo 12")
    bro_frame_button2.grid(row=1, column=2)
    bro_frame_button3 = Button(bro_frame, text="Quit", bd=4, bg="blue", command=pro.destroy)
    bro_frame_button3.configure(font="Mimmo 12")
    bro_frame_button3.grid(row=1, column=3)
    bro_frame_button4 = Button(bro_frame, text="Save", bd=4, bg="blue", command = saveFile2)
    bro_frame_button4.configure(font="Mimmo 12")
    bro_frame_button4.grid(row=1, column=4)

    bro.mainloop()


def clear1():
    text.delete(1.0, END)
    text1.delete(1.0, END)
    zeroEntry.delete(0,END)


frame_button1 = Button(frame, text="Clear", bd=4, bg="green", command=clear1)
frame_button1.configure(font="Mimmo 12")
frame_button1.grid(row=1, column=1)
frame_button2 = Button(frame, text="Decode?", bd=4, bg="green", command=enter)
frame_button2.configure(font="Mimmo 12")
frame_button2.grid(row=1, column=2)
frame_button3 = Button(frame, text="Quit", bd=4, bg="green", command=pro.destroy)
frame_button3.configure(font="Mimmo 12")
frame_button3.grid(row=1, column=3)
frame_button4 = Button(frame, text = "Save", bd = 4, bg = "green", command = saveFile)
frame_button4.configure(font = "Mimmo 12")
frame_button4.grid(row = 1, column = 4)

pro.mainloop()
