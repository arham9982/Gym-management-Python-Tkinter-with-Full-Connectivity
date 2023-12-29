from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk")
        self.root.geometry("650x600")
        self.root.bind('<Return>', self.enter_func)

        main_frame = Frame(self.root, width=620)
        main_frame.pack()

        img_title = Image.open(r"img\chat.jpg")
        img_title = img_title.resize((150, 80))
        self.photoimg_title = ImageTk.PhotoImage(img_title)

        title_label = Label(main_frame, image=self.photoimg_title, text="      Help Assistant! How can i help", font=(
            "times new roman", 22, "bold"), relief=RAISED, anchor="nw", width=610, compound=LEFT, bg='black', fg='white', bd=4)
        title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=54, height=18, bd=3, relief=RAISED, font=(
            "arial", 14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, width=620)
        btn_frame.pack()

        lbl1 = Label(btn_frame, text="Ask a Question", font=(
            "times new roman", 13, "bold"), fg="blue", bg="white")
        lbl1.grid(row=0, column=0, padx=4, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, width=41, font=(
            "times new roman", 13, "bold"), textvariable=self.entry)
        self.entry1.grid(row=0, column=1, padx=4, sticky=W)

        self.send1 = Button(btn_frame, text="Send", font=(
            "times new roman", 13, "bold"), width=6, bg="cadetblue", fg="black", command=self.send)
        self.send1.grid(row=0, column=2, padx=4, sticky=W)

        self.send2 = Button(btn_frame, text="Clear Data", font=(
            "times new roman", 13, "bold"), width=8, bg="blue", fg="white", command=self.clear)
        self.send2.grid(row=1, column=0, padx=4, sticky=W)

        self.msg = ""
        self.lbl_1 = Label(btn_frame, text=self.msg, font=(
            "times new roman", 13, "bold"), fg="gold")
        self.lbl_1.grid(row=1, column=1, padx=4, sticky=W)

    def enter_func(self, event):
        self.send1.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete("1.0", END)
        self.entry.set("")

    def send(self):
        send = '\t\t\t'+"You:"+self.entry1.get()
        self.text.insert(END, "\n"+send)
        self.text.yview(END)
        if (self.entry.get() == ""):
            self.msg = "please ask your query"
            self.text.insert(END, "\n\n"+"Help: Please ask your query!")
            self.lbl_1.config(text=self.msg, fg="gold")
        else:
            self.msg = ""
            self.lbl_1.config(text=self.msg, fg="gold")
        if (self.entry.get() == "hello"):
            self.text.insert(END, "\n\n"+"Help: Hi!")
        elif (self.entry.get() == "how are you"):
            self.text.insert(END, "\n\n"+"Help: I am fine and What about you")
        elif (self.entry.get() == "hi"):
            self.text.insert(END, "\n\n"+"Help: Hello")
        elif (self.entry.get() == "who are you"):
            self.text.insert(
                END, "\n\n"+"Help: I'm arham , sameer , amaan is my master")
        elif (self.entry.get() == "who made this app"):
            self.text.insert(
                END, "\n\n"+"Help: Arham,sameer,amaan")
        elif (self.entry.get() == "who made you"):
            self.text.insert(
                END, "\n\n"+"Help: ARHAM\n")


if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
