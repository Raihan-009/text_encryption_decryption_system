from tkinter import *
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

    #print("Enter your text: ")
    text = entry1.get()
    encrypted = ""

    for x in text:
        if x in dictionary:
            encrypted += dictionary[x]
        else:
            encrypted += x
    text1.insert(1.0, encrypted)

def decryption():
    text2.delete(1.0, END)
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

    #print("Enter your encrypted code: ")
    text = entry2.get()
    decrypted = ""

    for x in text:
        if x in dictionary:
            decrypted += dictionary[x]
        else:
            decrypted += x
    text2.insert(1.0, decrypted)
def TRY():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    text1.delete(1.0, END)
    text2.delete(1.0, END)

if __name__ == "__main__" :
    pro = Tk()
    pro.title('Text Encoder & Decoder')
    pro.geometry('500x600')
    pro.resizable(0,0)
    pro.configure(background = "light green")
    label1 = Label(pro, text = "Enter your message: " , bg = 'light green', height = 2)
    label1.configure(font = 'Impact 16')
    #label1.pack(side =  LEFT)
    label1.pack(side = TOP)
    entry1 = Entry(pro, bd = 3, width = 45, font=('Arial', 10))
    entry1.pack(side = TOP)
    button1 = Button(pro, text = 'Encrypt', bg = 'green', bd = 3, command = encyption )
    button1.pack(side = TOP)
    label2 = Label(pro, text = "Here is your secret code", bg = 'light green', height =2)
    label2.configure(font='Mimmo 16')
    label2.pack(side = TOP)
    text1 = Text(pro, width = 35, height = 3, bd = 4)
    text1.configure(font='Calibri 12')
    text1.pack(side = TOP)
    label3 = Label(pro,text = 'Enter your Secret Code : ' , bg = 'light green' , height = 2)
    label3.configure(font='Mimmo 16')
    label3.pack(side = TOP)
    entry2 = Entry(pro, bd = 3, width = 45, font=('Arial', 10))
    entry2.pack(side = TOP)
    button2 = Button(pro, text = 'Decrypt', bg = 'green', bd = 3, command = decryption )
    button2.pack(side = TOP)
    label4 = Label(pro, text = "Here is your decoded message", bg = 'light green' , height = 2)
    label4.configure(font='Mimmo 16')
    label4.pack(side = TOP)
    text2 = Text(pro, width = 35, height = 3, bd = 4, wrap = WORD)
    text2.configure(font = 'Calibri 12')
    text2.pack(side = TOP)
    button3 = Button(pro, text = 'Clear ALL', bd = 3,bg = 'green', command = TRY)
    button3.pack(side = TOP)
    button4 = Button(pro, text = "Quit", bg = 'green', bd = 3, command=pro.destroy)
    button4.pack(side = TOP )
    pro.mainloop()
