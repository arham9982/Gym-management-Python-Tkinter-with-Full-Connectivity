from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from GymManagement import GymManagement


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1100x600")

        self.bg = ImageTk.PhotoImage(
            file=r"img\1.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=400, y=150, width=320, height=400)

        # img1 = Image.open(
        #     r"E:\Python\Projects\Gym Project\img\password.png")
        # img1 = img1.resize((90, 90), Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # lblimg = Label(self.root, image=self.photoimg1,
        #                bg="black")
        # lblimg.place(x=515, y=155, width=90, height=90)

        get_str = Label(frame, text="Admin Login", font=(
            "times new roman", 28, "bold"), fg="white", bg="black")
        get_str.place(x=47, y=30)

        #####labels####
        username_lbl = Label(frame, text="Admin ID", font=(
            "times new roman", 13, "bold"), fg="white", bg="black")

        username_lbl.place(x=35, y=148)

        self.txtuser = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), width=23)

        self.txtuser.place(x=45, y=180)

        password_lbl = Label(frame, text="Password", font=(
            "times new roman", 13, "bold"), fg="white", bg="black")

        password_lbl.place(x=35, y=218)

        self.passuser = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), width=23)

        self.passuser.place(x=45, y=240)

    

        #######login########
        btnlogin = Button(frame, text="Login", command=self.login, font=(
            "times new roman", 13, "bold"), bd=4, relief=RIDGE, fg="white", bg="green")
        btnlogin.place(x=90, y=290, width=120, height=30)

        #####register#####
        btnreg = Button(frame, text="Register New User", command=self.register_window, font=(
            "times new roman", 8, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        btnreg.place(x=5, y=335, width=155)

        #####password#####
        btnforg = Button(frame, text="Forget Password", font=(
            "times new roman", 8, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black", command=self.forgot_password_window)
        btnforg.place(x=0, y=355, width=155)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
     if self.txtuser.get() == "" or self.passuser.get() == "":
        messagebox.showerror("Error", "All fields are required")

     else:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="arham",
            database="register",
        )
        my_cursor = conn.cursor()

        # Use the correct column name 'pass' instead of 'password'
        my_cursor.execute("SELECT * FROM register WHERE email = %s AND pass = %s", (
            self.txtuser.get(),
            self.passuser.get()
        ))

        row = my_cursor.fetchone()
        if row is None:
            messagebox.showerror("Error", "Invalid username and password")
        else:
            open_main = messagebox.askyesno("YesNo", "Do You Want To Login")
            if open_main > 0:
                self.new_window = Toplevel(self.root)
                self.app = GymManagement(self.new_window)
            else:
                if not open_main:
                    return

        conn.close()


    def reset(self):
        if self.combo_secques.get() == "Select":
            messagebox.showerror(
                "Error", "Please select a security question", parent=self.root2)

        elif self.entrysecans.get() == "":
            messagebox.showerror(
                "Error", "Please enter the security answer", parent=self.root2)

        elif self.entrynewpassword.get() == "":
            messagebox.showerror(
                "Error", "Please enter the new password", parent=self.root2)

        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="register",
            )
            my_cursor = conn.cursor()
            query = (
                "select * from register where email = %s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_secques.get(),
                     self.entrysecans.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Wrong answer", parent=self.root2)
            else:
                query = ("update register set pass = %s where email = %s")
                value = (self.entrynewpassword.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Password has been reset successfully", parent=self.root2)
                self.root2.destroy()

    #####forget password####

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Enter a valid Username")

        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="register",
            )
            my_cursor = conn.cursor()
            query = ("select * from register where email =%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter a valid username")

            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+450+170")

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 15, "bold"), fg="cadetblue", bg="white")
                l.place(x=0, y=0, relwidth=1)

                secques = Label(self.root2, text="Select Security Question", font=(
                    "times new roman", 17, "bold"), bg="white")
                secques.place(x=50, y=50)

                self.combo_secques = ttk.Combobox(
                    self.root2,
                    font=("times new roman", 10, "bold"),
                    width=25,
                    state="readonly"
                )
                self.combo_secques["value"] = ("Select",
                                               "Your Girlfriend's Name", "Your Pet's Name", "Your Birth Place")
                self.combo_secques.current(0)
                self.combo_secques.place(x=75, y=90)

            # entrysecques = ttk.Entry(frame, font=(
            #     "times new roman", 13, "bold"))
            # entrysecques.place(x=330, y=195, width=220)

            ####forget password####
                secans = Label(self.root2, text="Select Security Answer", font=(
                    "times new roman", 17, "bold"), bg="white")
                secans.place(x=50, y=130)

                self.entrysecans = ttk.Entry(self.root2, font=(
                    "times new roman", 10, "bold"))
                self.entrysecans.place(x=75, y=170, width=200)

                newpassword = Label(self.root2, text="Enter New Password", font=(
                    "times new roman", 17, "bold"), bg="white")
                newpassword.place(x=50, y=210)

                self.entrynewpassword = ttk.Entry(self.root2, font=(
                    "times new roman", 10, "bold"))
                self.entrynewpassword.place(x=75, y=250, width=200)

                btnn = Button(self.root2, text="Reset", font=(
                    "times new roman", 15, "bold"), fg="white", bg="cadetblue", command=self.reset)
                btnn.place(x=130, y=310)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1100x800")

        #####variables####
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        ####bglogo#####

        self.bg = ImageTk.PhotoImage(
            file=r"img\6.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        ###left image####
        # self.bg2 = ImageTk.PhotoImage(
        #     file=r"E:\Python\Projects\Gym Project\img\4.jpg")

        # lbl_bg2 = Label(self.root, image=self.bg2)
        # lbl_bg2.place(x=10, y=90, width=400, height=500)

        #####mainframe#####

        frame = Frame(self.root, bg="white")
        frame.place(x=215, y=90, width=680, height=500)

        lblreg = Label(frame, text="REGISTER", font=(
            "times new roman", 20, "bold"), fg="red", bg="white")
        lblreg.place(x=10, y=10)

        ########labels##########

        fname = Label(frame, text="First Name", font=(
            "times new roman", 17, "bold"), bg="white")
        fname.place(x=30, y=80)

        self.entryname = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_fname)
        self.entryname.place(x=30, y=115, width=220)

        ####lastname####
        flastname = Label(frame, text="Last Name", font=(
            "times new roman", 17, "bold"), bg="white")
        flastname.place(x=330, y=80)

        self.entrylname = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_lname)
        self.entrylname.place(x=330, y=115, width=220)

        ####contact####
        contact = Label(frame, text="Contact Number", font=(
            "times new roman", 17, "bold"), bg="white")
        contact.place(x=30, y=160)

        self.entrycontact = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_contact)
        self.entrycontact.place(x=30, y=195, width=220)

        ####email####
        email = Label(frame, text="Email", font=(
            "times new roman", 17, "bold"), bg="white")
        email.place(x=330, y=160)

        self.entryemail = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_email)
        self.entryemail.place(x=330, y=195, width=220)

        ####security question####
        secques = Label(frame, text="Select Security Question", font=(
            "times new roman", 17, "bold"), bg="white")
        secques.place(x=30, y=240)

        self.combo_secques = ttk.Combobox(
            frame,
            font=("times new roman", 10, "bold"),
            width=25,
            state="readonly", textvariable=self.var_securityQ
        )
        self.combo_secques["value"] = ("Select",
                                       "Your Girlfriend's Name", "Your Pet's Name", "Your Birth Place")
        self.combo_secques.current(0)
        self.combo_secques.place(x=30, y=275)

        # entrysecques = ttk.Entry(frame, font=(
        #     "times new roman", 13, "bold"))
        # entrysecques.place(x=330, y=195, width=220)

        ####security Answer####
        secans = Label(frame, text="Security Answer", font=(
            "times new roman", 17, "bold"), bg="white")
        secans.place(x=330, y=240)

        self.entrysecans = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_securityA)
        self.entrysecans.place(x=330, y=275, width=220)

        #####password###
        password = Label(frame, text="Password", font=(
            "times new roman", 17, "bold"), bg="white")
        password.place(x=30, y=320)

        self.entrypassword = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_pass)
        self.entrypassword.place(x=30, y=355, width=220)

        #####confirm  password###
        conpassword = Label(frame, text="Confirm Password", font=(
            "times new roman", 17, "bold"), bg="white")
        conpassword.place(x=330, y=320)

        self.entryconpassword = ttk.Entry(frame, font=(
            "times new roman", 13, "bold"), textvariable=self.var_confpass)
        self.entryconpassword.place(x=330, y=355, width=220)

        #####checkbutton#####
        self.var_check = IntVar()

        self.checkbtn = Checkbutton(
            frame, text="I Agree To The Terms And Conditions", font=("times new roman", 10, "bold"), variable=self.var_check, onvalue=1, offvalue=0)
        self.checkbtn.place(x=30, y=395)


        #BUTTON##
        btn1 = Button(frame, text="Register", bd=0, relief="ridge", cursor="hand2", bg="green",fg="white", command=self.register_data)
        btn1.place(x=70, y=430, width=100, height=40)

        btn2 = Button(frame, text="Login", bd=0, relief="ridge", cursor="hand2", bg="green",fg="white", command=self.return_login)
        btn2.place(x=200, y=430, width=100, height=40)

        ##########func ######

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityA.get() == "Select":
            messagebox.showerror("Error", "All fields are required")

        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords Do Not Match")

        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please Accept the Terms and Condition")

        else:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="register",
            )
            my_cursor = conn.cursor()
            query_check_email = "SELECT * FROM register WHERE email = %s"
            value_check_email = (self.var_email.get(),)
            my_cursor.execute(query_check_email, value_check_email)
            existing_row = my_cursor.fetchone()
            if existing_row:
                messagebox.showerror("Error","Email already exists, Please try another")
    

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            # self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
