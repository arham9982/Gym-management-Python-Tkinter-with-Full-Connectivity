from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random
from random import randint


class Members:
    def __init__(self, root):
        self.root = root
        self.root.title("GYM MANAGEMENT SYSTEM")
        self.root.geometry("1000x610+170+0")

        ###variables###

        self.memberId = StringVar()
        x = random.randint(1, 1000)
        self.memberId.set(str(x))

        self.name = StringVar()
        self.gender = StringVar()
        self.pincode = StringVar()
        self.mobile = StringVar()
        self.email = StringVar()
        self.idtype = StringVar()
        self.idnumber = StringVar()
        self.address = StringVar()

        imgfoot = Image.open("img/9.jpg")
        imgfoot = imgfoot.resize((1000, 120))
        self.photoimgfoot = ImageTk.PhotoImage(imgfoot)

        lblimgfoot = Label(
            self.root, image=self.photoimgfoot)
        lblimgfoot.place(x=0, y=490, width=1000, height=120)

        lblimg6 = Label(self.root, text="Customer Details",
                        bd=10, bg="black", relief=GROOVE, fg="white", font=("Ariel", 25, "italic"))
        lblimg6.place(x=0, y=0, width=1000, height=70)

        labelframeleft = LabelFrame(
            self.root, text="Customer's Details", font=("times new roman", 11, "bold"), padx=2, bd=4, relief=RIDGE)
        labelframeleft.place(x=632, y=90, width=360, height=400)

        #####member details labels and entries######
        ##id##
        lblmemId = Label(labelframeleft, text="Customer's Id Number", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemId.grid(row=0, column=0, sticky=W)

        lblmemIdentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.memberId)
        lblmemIdentry.grid(row=0, column=1)

        ##name##
        lblmemName = Label(labelframeleft, text="Member's Name", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemName.grid(row=1, column=0, sticky=W)

        lblmemNameentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.name)
        lblmemNameentry.grid(row=1, column=1)

        ##Gender##
        lblmemGender = Label(labelframeleft, text="Gender", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemGender.grid(row=2, column=0, sticky=W)

        lblmemGenderentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.gender)
        lblmemGenderentry.grid(row=2, column=1)

        # ##Gender##
        # lblmemGender = Label(labelframeleft, text="Gender", font=(
        #     "ariel", 11, "bold"), padx=2, pady=6)
        # lblmemGender.grid(row=2, column=0, sticky=W)

        # lblmemGenderentry = ttk.Entry(labelframeleft, font=(
        #     "times new roman", 11, "bold"), width=20,textvariable=self.name)
        # lblmemGenderentry.grid(row=2, column=1)

        ##Pin-Code##
        lblmemPin = Label(labelframeleft, text="PinCode", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemPin.grid(row=3, column=0, sticky=W)

        lblmemPinentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.pincode)
        lblmemPinentry.grid(row=3, column=1)

        ##MobileNumber##
        lblmemMobile = Label(labelframeleft, text="Mobile Number", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemMobile.grid(row=4, column=0, sticky=W)

        lblmemMobileentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.mobile)
        lblmemMobileentry.grid(row=4, column=1)

        ##Email##
        lblmemEmail = Label(labelframeleft, text="Email", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemEmail.grid(row=5, column=0, sticky=W)

        lblmemEmailentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.email)
        lblmemEmailentry.grid(row=5, column=1)

        ##Idtype##
        lblmemIdType = Label(labelframeleft, text="Id-Proof Type", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemIdType.grid(row=6, column=0, sticky=W)

        # lblmemIdTypeentry = ttk.Combobox(labelframeleft, font=(
        #     "ariel", 11, "bold"), state="readonly", width=18)
        # lblmemIdType["value"] = ("Aadhar Card", "Driving Liscence", "PanCard")
        # lblmemIdType.current(0)
        # lblmemIdTypeentry.grid(row=6, column=1)

        combo_nation = ttk.Combobox(
            labelframeleft,
            font=("arial", 11, "bold"),
            width=18,
            state="readonly", textvariable=self.idtype
        )
        combo_nation["value"] = (
            "ID-Type", "Aadhar-Card", "Drivers Liscence", "Pan-Card")
        combo_nation.current(0)
        combo_nation.grid(row=6, column=1)

        ##Idnumber##
        lblmemIdNumber = Label(labelframeleft, text="Id-Proof Number", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemIdNumber.grid(row=7, column=0, sticky=W)

        lblmemIdNumberentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.idnumber)
        lblmemIdNumberentry.grid(row=7, column=1)

        #address##
        lblmemIdAddress = Label(labelframeleft, text="Address", font=(
            "ariel", 11, "bold"), padx=2, pady=6)
        lblmemIdAddress.grid(row=8, column=0, sticky=W)

        lblmemIdAddressentry = ttk.Entry(labelframeleft, font=(
            "times new roman", 11, "bold"), width=20, textvariable=self.address)
        lblmemIdAddressentry.grid(row=8, column=1)

        ####buttons####

        btnframe = Frame(labelframeleft, bd=4, relief=RIDGE)
        btnframe.place(x=0, y=320, width=345, height=30)

        btnadd = Button(btnframe, text="Add", bg="black",
                        fg="white", width=11, command=self.add_data)
        btnadd.grid(row=0, column=0)

        btnupdate = Button(btnframe, text="Update", bg="black",
                           fg="white", width=11, command=self.update)
        btnupdate.grid(row=0, column=2)

        btnDelete = Button(btnframe, text="Delete", bg="black",
                           fg="white", width=11, command=self.ndelete)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(btnframe, text="Reset", bg="black",
                          fg="white", width=11, command=self.reset)
        btnReset.grid(row=0, column=4)

        ###table frame###

        tableframe = LabelFrame(
            self.root, text="Search system",  font=("times new roman", 15, "bold"))
        tableframe.place(x=15, y=90, width=590, height=400),

        lbl1 = Label(tableframe, text="Search By", bg="blue", fg="white")
        lbl1.grid(row=0, column=0, padx=2, sticky=W)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(
            tableframe,
            font=("arial", 11, "bold"),
            width=16,
            state="readonly",
            textvariable=self.search_var,
        )
        combo_search["value"] = "Mobile"
        combo_search.current(0)
        combo_search.grid(row=0, column=1)

        self.txt_search = StringVar()

        entrysearch = ttk.Entry(tableframe, width=20,
                                font=("times new roman", 11, "bold"), textvariable=self.txt_search)
        entrysearch.grid(row=0, column=2, padx=3)

        ###button search###
        btnsearch = Button(tableframe, text="Search", bg="black",
                           fg="white", width=12, command=self.search)
        btnsearch.grid(row=0, column=3, padx=2)

        btnshowall = Button(tableframe, text="Show All", bg="black",
                            fg="white", width=12, padx=2, command=self.fetch_data)
        btnshowall.grid(row=0, column=4)

        ####scroll bar####

        framedetails = Frame(tableframe, bd=2, relief=RIDGE)
        framedetails.place(x=5, y=40, width=575, height=326)

        scrollx = ttk.Scrollbar(framedetails, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(framedetails, orient=VERTICAL)

        self.memberdetailstable = ttk.Treeview(framedetails, column=(
            "Id",
            "name",
            "gender",
            "pin",
            "mobile",
            "email",
            "idprooftype",
            "idnumber",
            "address",
        ), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.memberdetailstable.xview)
        scrolly.config(command=self.memberdetailstable.yview)

        self.memberdetailstable.heading("Id", text="Member Id")
        self.memberdetailstable.heading("name", text="Member name")
        self.memberdetailstable.heading("gender", text="Gender")
        self.memberdetailstable.heading("pin", text="pincode")
        self.memberdetailstable.heading("mobile", text="mobile")
        self.memberdetailstable.heading("email", text="email")
        self.memberdetailstable.heading("idprooftype", text="Idproof")
        self.memberdetailstable.heading("idnumber", text="IdproofNumber")
        self.memberdetailstable.heading("address", text="Address")

        self.memberdetailstable["show"] = "headings"

        self.memberdetailstable.column("Id", width=50)
        self.memberdetailstable.column("name", width=120)
        self.memberdetailstable.column("gender", width=70)
        self.memberdetailstable.column("pin", width=80)
        self.memberdetailstable.column("mobile", width=105)
        self.memberdetailstable.column("email", width=190)
        self.memberdetailstable.column("idprooftype", width=80)
        self.memberdetailstable.column("idnumber", width=110)
        self.memberdetailstable.column("address", width=210)
        self.memberdetailstable.pack(fill=BOTH, expand=1)
        self.memberdetailstable.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.memberId.get() == "" or self.name.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="gym",
                )

                my_cursor = conn.cursor()
                my_cursor.execute("insert into gym values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.memberId.get(),
                    self.name.get(),
                    self.gender.get(),
                    self.pincode.get(),
                    self.mobile.get(),
                    self.email.get(),
                    self.idtype.get(),
                    self.idnumber.get(),
                    self.address.get()
                    
                ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Success", "Member has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showwarning(
                    "warning", f"Something went wrong:{str(es)}", parent=self.root
                )

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="arham", database="gym"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from gym")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.memberdetailstable.delete(
                *self.memberdetailstable.get_children())
            for i in rows:
                self.memberdetailstable.insert("", END, values=i)

            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_rows = self.memberdetailstable.focus()
        content = self.memberdetailstable.item(cursor_rows)
        row = content["values"]

        self.memberId.set(row[0])
        self.name.set(row[1])
        self.gender.set(row[2])
        self.pincode.set(row[3])
        self.mobile.set(row[4])
        self.email.set(row[5])
        self.idtype.set(row[6])
        self.idnumber.set(row[7])
        self.address.set(row[8])

    def update(self):
        if self.mobile.get() == "":
            messagebox.showerror(
                "Error", "Please Enter The Registered Mobile Number")

        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="gym",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE gym SET MemberName = %s, Gender = %s, PinCode = %s,Mobile = %s, Email = %s, IdProofType = %s, IdProofNumber = %s, Address= %s WHERE MemberId = %s",
                (
                    self.name.get(),
                    self.gender.get(),
                    self.pincode.get(),
                    self.mobile.get(),
                    self.email.get(),
                    self.idtype.get(),
                    self.idnumber.get(),
                    self.address.get(),
                    self.memberId.get(),
                    

                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "update",
                "Member details have been updated successfully",
                parent=self.root,
            )

    def ndelete(self):
        ndelete = messagebox.askyesno(
            "Gym Membership", "Do you want to delete this member?", parent=self.root)

        if ndelete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="gym",
            )
            my_cursor = conn.cursor()
            query = "delete from gym where MemberId=%s"
            value = (self.memberId.get(),)
            my_cursor.execute(query, value)

        else:
            if not ndelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.name.set("")
        self.gender.set("")
        self.mobile.set("")
        self.email.set("")
        # self.idtype.set("")
        self.idnumber.set("")
        self.address.set("")
        self.pincode.set("")
        x = random.randint(1, 1000)
        self.memberId.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="arham",
            database="gym",
        )
        my_cursor = conn.cursor()

        my_cursor.execute(
            "select * from gym where "
            + str(self.search_var.get())
            + " LIKE '%"
            + str(self.txt_search.get())
            + "%'"
        )

        row = my_cursor.fetchall()
        if len(row) != 0:
            self.memberdetailstable.delete(
                *self.memberdetailstable.get_children())
            for i in row:
                self.memberdetailstable.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Members(root)
    root.mainloop()
