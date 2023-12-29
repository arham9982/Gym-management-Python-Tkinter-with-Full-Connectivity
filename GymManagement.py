from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from memberDetails import Members
from feedetails import Fee
from chatbot import ChatBot
from Attendance import AttendanceRecord




class GymManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("GYM MANAGEMENT SYSTEM")
        self.root.geometry("1270x650+0+0")

        img = Image.open(r"img\1.jpg")
        img = img.resize((1270, 650))
        self.photoimg = ImageTk.PhotoImage(img)

        lblimg = Label(self.root, image=self.photoimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1270, height=650)

        img2 = Image.open(r"img\2.jpg")
        img2 = img2.resize((250, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        btnimg2 = Button(lblimg, image=self.photoimg2,
                         bd=4, relief=RIDGE, command=self.memberDetails)
        btnimg2.place(x=50, y=350, width=250, height=200)

        lblimg2 = Label(lblimg, text="Member Details",
                        bd=4, bg="black", relief=RIDGE, fg="white", font=("times new roman", 18, "bold"))
        lblimg2.place(x=50, y=550, width=250, height=35)
        
        
        img3 = Image.open(r"img\3.jpg")
        img3 = img3.resize((250, 200))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        btnimg3 = Button(lblimg, image=self.photoimg3,
                         bd=4, relief=RIDGE, command=self.feedetails)
        btnimg3.place(x=360, y=350, width=250, height=200)

        lblimg3 = Label(lblimg, text="Fee Details",
                        bd=4, bg="black", relief=RIDGE, fg="white", font=("times new roman", 18, "bold"))
        lblimg3.place(x=360, y=550, width=250, height=35)

        img4 = Image.open(r"img\7.png")
        img4 = img4.resize((250, 200))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btnimg4 = Button(lblimg, image=self.photoimg4,text="attendance",
                         bd=4, relief=RIDGE,command=self.attendance)
        btnimg4.place(x=670, y=350, width=250, height=200)

        lblimg4 = Label(lblimg, text="Attendance",
                        bd=4, bg="black", relief=RIDGE, fg="white", font=("times new roman", 18, "bold"))
        lblimg4.place(x=670, y=550, width=250, height=35)

        img5 = Image.open(r"img\8.png")
        img5 = img5.resize((250, 200))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btnimg5 = Button(lblimg, image=self.photoimg5,
                         bd=4, relief=RIDGE, command=self.nexit)
        btnimg5.place(x=980, y=350, width=250, height=200)

        lblimg5 = Label(lblimg, text="Exit",
                        bd=4, bg="black", relief=RIDGE, fg="white", font=("times new roman", 18, "bold"))
        lblimg5.place(x=980, y=550, width=250, height=35)

        img6 = Image.open(r"img\4.jpg")
        img6 = img6.resize((635, 300))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btnimg6 = Label(lblimg, image=self.photoimg6, relief=RIDGE)
        btnimg6.place(x=0, y=0, width=635, height=250)

        lblimg6 = Label(lblimg, text="Welcome to the Great Grand Fitness Gym",
                        bd=4, bg="black", relief=RIDGE, fg="white", font=("Ariel", 30, "italic"))
        lblimg6.place(x=0, y=250, width=1270, height=70)

        img7 = Image.open(r"img\5.jpg")
        img7 = img7.resize((635, 300))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btnimg7 = Label(lblimg, image=self.photoimg7, relief=RIDGE)
        btnimg7.place(x=635, y=0, width=635, height=250)

        buttonhelp = Button(lblimg, text="Need Help?", bd=4,
                            relief=RIDGE, bg='black', fg='white', command=self.chatbot)
        buttonhelp.place(x=1152, y=600)

    def memberDetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Members(self.new_window)

    def feedetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Fee(self.new_window)

    def nexit(self):
        self.root.destroy()

    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)
    

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceRecord(self.new_window)
    
    
      
    

if __name__ == "__main__":
    root = Tk()
    obj = GymManagement(root)
    root.mainloop()
