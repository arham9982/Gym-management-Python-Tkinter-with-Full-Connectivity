from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
import random
from random import randint


class Fee:
    def __init__(self, root):
        self.root = root
        self.root.title("GYM MANAGEMENT SYSTEM")
        self.root.geometry("1000x610+170+0")

        


        self.contact = StringVar()
        self.memberId = StringVar()
        self.membership = StringVar()
        self.feedate = StringVar()
        self.month = StringVar()
        self.status = StringVar()
        self.paidtax = StringVar()
        self.fee = StringVar()
        self.total = StringVar()

        lblimg = Label(self.root, text="MEMBER FEE DETAILS", bd=10, bg="#007BFF", relief=GROOVE,
                       fg="white", font=("Helvetica", 30, "bold italic"))
        lblimg.place(x=0, y=0, width=1000, height=70)

        labelframeright = LabelFrame(
            self.root, text="Fee Details", font=("times new roman", 11, "bold"), padx=2, bd=4, relief=RIDGE)
        labelframeright.place(x=632, y=90, width=360, height=400)

        ###labels####
        lbl_cust_contact = Label(
            labelframeright,
            text="Member Contact",
            font=("arial", 11, "bold"),
            padx=5,
            pady=5,
        )
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.contact
        )
        entry_contact.grid(row=0, column=1, sticky=W)

        # fetch data button
        btnfetchdata = Button(
            labelframeright,
            text="Fetch Data",
            font=("times new roman", 9, "bold"),
            bg="red",
            fg="black",
            width=9,
            command=self.fetch_contact

        )
        btnfetchdata.place(x=302, y=1)

        lbl_cust_Id = Label(
            labelframeright,
            text="Customer ID",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_cust_Id.grid(row=1, column=0, sticky=W)

        entry_Id = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.memberId
        )
        entry_Id.grid(row=1, column=1, sticky=W)

        lblPlan = Label(
            labelframeright,
            text="Membership Plan",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblPlan.grid(row=2, column=0, sticky=W)

        comboplan = ttk.Combobox(
            labelframeright,
            font=("arial", 11, "bold"),
            width=16,
            state="readonly",
            textvariable=self.membership
        )
        comboplan["value"] = (
            "Plan", "Basic", "Special", "Premium")
        comboplan.current(0)
        comboplan.grid(row=2, column=1)

        lblsubmit = Label(
            labelframeright,
            text="Fee submitting date",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblsubmit.grid(row=3, column=0, sticky=W)

        entrysubmit = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.feedate
        )
        entrysubmit.grid(row=3, column=1, sticky=W)

        lblsubmit = Label(
            labelframeright,
            text="Fee Month",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblsubmit.grid(row=4, column=0, sticky=W)

        combomonth = ttk.Combobox(
            labelframeright,
            font=("arial", 11, "bold"),
            width=16,
            state="readonly",
            textvariable=self.month
        )
        combomonth["value"] = (
            "Month", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        combomonth.current(0)
        combomonth.grid(row=4, column=1)

        lblstatus = Label(
            labelframeright,
            text="Fee Status",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblstatus.grid(row=5, column=0, sticky=W)

        combomonth = ttk.Combobox(
            labelframeright,
            font=("arial", 11, "bold"),
            width=16,
            state="readonly",
            textvariable=self.status
        )
        combomonth["value"] = (
            "Not-Paid", "Paid")
        combomonth.current(0)
        combomonth.grid(row=5, column=1)

        lbltaxpaid = Label(
            labelframeright,
            text="Paid Tax",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbltaxpaid.grid(row=6, column=0, sticky=W)

        entrytaxpaid = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.paidtax
        )
        entrytaxpaid.grid(row=6, column=1, sticky=W)

        lblgymfee = Label(
            labelframeright,
            text="Gym Fee",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lblgymfee.grid(row=7, column=0, sticky=W)

        entrygymfee = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.fee
        )
        entrygymfee.grid(row=7, column=1, sticky=W)

        lbl_subTotal = Label(
            labelframeright,
            text="Sub Total",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_subTotal.grid(row=8, column=0, sticky=W)

        entry_subTotal = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.total
        )
        entry_subTotal.grid(row=8, column=1, sticky=W)

        btnBill = Button(
            labelframeright,
            text="Bill",
            font=("times new roman", 9, "bold"),
            bg="red",
            fg="black",
            width=11,
            command=self.totalfee

        )
        btnBill.place(x=0, y=300)

        btnframe = Frame(labelframeright, bd=4, relief=RIDGE)
        btnframe.place(x=0, y=342, width=375, height=30)

        btnadd = Button(btnframe, text="Add", bg="black",
                        fg="white", width=12, command=self.add_data)
        btnadd.grid(row=0, column=0)

        btnupdate = Button(btnframe, text="Update", bg="black",
                           fg="white", width=12, command=self.update)
        btnupdate.grid(row=0, column=2)

        btnDelete = Button(btnframe, text="Delete", bg="black",
                           fg="white", width=12, command=self.ndelete)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(btnframe, text="Reset", bg="black",
                          fg="white", width=12, command=self.reset)
        btnReset.grid(row=0, column=4)

        

        tableframe = LabelFrame(
            self.root, text="Search system",  font=("times new roman", 15, "bold"))
        tableframe.place(x=7, y=300, width=590, height=280),

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
        combo_search["value"] = "Contact"
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

        framedetails = Frame(tableframe, bd=2, relief=RIDGE)
        framedetails.place(x=5, y=40, width=575, height=210)

        scrollx = ttk.Scrollbar(framedetails, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(framedetails, orient=VERTICAL)

        self.memberdetailstable = ttk.Treeview(framedetails, column=(
            "Contact",
            "Member Id",
            "Membership Plan",
            "Fee submitting date",
            "Month",
            "Fee Status",
            "Paid Tax",
            "Fee",
            "Total",
        ), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.memberdetailstable.xview)
        scrolly.config(command=self.memberdetailstable.yview)

        self.memberdetailstable.heading("Contact", text="Member Contact")
        self.memberdetailstable.heading("Member Id", text="Member Id")
        self.memberdetailstable.heading(
            "Membership Plan", text="Membership Plan")
        self.memberdetailstable.heading(
            "Fee submitting date", text="Fee submitting date")
        self.memberdetailstable.heading("Month", text="Month")
        self.memberdetailstable.heading("Fee Status", text="Fee Status")
        self.memberdetailstable.heading("Paid Tax", text="Paid Tax")
        self.memberdetailstable.heading("Fee", text="Fee")
        self.memberdetailstable.heading("Total", text="Total")

        self.memberdetailstable["show"] = "headings"

        self.memberdetailstable.column("Contact", width=120)
        self.memberdetailstable.column("Member Id", width=50)
        self.memberdetailstable.column("Membership Plan", width=70)
        self.memberdetailstable.column("Fee submitting date", width=80)
        self.memberdetailstable.column("Month", width=105)
        self.memberdetailstable.column("Fee Status", width=190)
        self.memberdetailstable.column("Paid Tax", width=80)
        self.memberdetailstable.column("Fee", width=110)
        self.memberdetailstable.column("Total", width=210)
        self.memberdetailstable.pack(fill=BOTH, expand=1)
        self.memberdetailstable.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.contact.get() == "" or self.membership.get() == "":
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
                my_cursor.execute("insert into fee values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (

                    self.contact.get(),
                    self.memberId.get(),
                    self.membership.get(),
                    self.feedate.get(),
                    self.month.get(),
                    self.status.get(),
                    self.paidtax.get(),
                    self.fee.get(),
                    self.total.get()
                ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Success", "Member has been added successfully")

            except Exception as es:
                messagebox.showwarning(
                    "warning", f"Something went wrong:{str(es)}", parent=self.root
                )

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="arham", database="gym"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from fee")
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

        self.contact.set(row[0])
        self.memberId.set(row[1])
        self.membership.set(row[2])
        self.feedate.set(row[3])
        self.month.set(row[4])
        self.status.set(row[5])
        self.paidtax.set(row[6])
        self.fee.set(row[7])
        self.total.set(row[8])

    def update(self):
        if self.contact.get() == "":
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
                "UPDATE fee SET MemberId = %s, Membership = %s, Feedate = %s,Month = %s, Status = %s, PaidTax = %s, Fee = %s, Total= %s WHERE Contact = %s",
                (
                    self.memberId.get(),
                    self.membership.get(),
                    self.feedate.get(),
                    self.month.get(),
                    self.status.get(),
                    self.paidtax.get(),
                    self.fee.get(),
                    self.total.get(),
                    self.contact.get(),

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
            query = "delete from fee where Contact=%s"
            value = (self.contact.get(),)
            my_cursor.execute(query, value)

        else:
            if not ndelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.contact.set("")
        self.memberId.set("")
        # self.membership.set("")
        self.feedate.set("")
        # self.idtype.set("")
        # self.month.set("")
        self.fee.set("")
        self.paidtax.set("")
        self.total.set("")

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="arham",
            database="gym",
        )
        my_cursor = conn.cursor()

        my_cursor.execute(
            "select * from fee where "
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

    def totalfee(self):
        membership_plans = {
            "Basic": 700,
            "Special": 1000,
            "Premium": 1300
        }

        selected_plan = self.membership.get()
        if selected_plan in membership_plans:
            plan_fee = membership_plans[selected_plan]
            tax = str("%.2f" % (plan_fee * 0.1))
            stotal = str("%.2f" % (plan_fee))
            Ttotal = str("%.2f" % (plan_fee + (plan_fee * 0.1)))

            self.paidtax.set(tax)
            self.fee.set(stotal)
            self.total.set(Ttotal)
        else:
            messagebox.showerror("Error", "Invalid Membership Plan")

    def fetch_contact(self):
        if self.contact.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="gym",
            )
            my_cursor = conn.cursor()
            query = ("select MemberName from gym where Mobile = %s")
            value = (self.contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "This number is not found", parent=self.root)

            else:
                conn.commit
                conn.close

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=301, y=70, width=299, height=229)

                lblname = Label(showDataFrame, text="username:",
                                font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row,
                            font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="gym",
                )
                my_cursor = conn.cursor()
                query = ("select Gender from gym where Mobile = %s")
                value = (self.contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showDataFrame, text="Gender:",
                                  font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lblg = Label(showDataFrame, text=row,
                             font=("arial", 12, "bold"))
                lblg.place(x=90, y=30)

                ###email###

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="gym",
                )
                my_cursor = conn.cursor()
                query = ("select Email from gym where Mobile = %s")
                value = (self.contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataFrame, text="Email:",
                                 font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)

                lble = Label(showDataFrame, text=row,
                             font=("arial", 12, "bold"))
                lble.place(x=60, y=60)

                ###address###

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="gym",
                )
                my_cursor = conn.cursor()
                query = ("select Address from gym where Mobile = %s")
                value = (self.contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataFrame, text="Address:",
                                   font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=90)

                lbladd = Label(showDataFrame, text=row,
                               font=("arial", 12, "bold"))
                lbladd.place(x=90, y=90)

                ###memid###

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="gym",
                )
                my_cursor = conn.cursor()
                query = ("select MemberId from gym where Mobile = %s")
                value = (self.contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataFrame, text="Member Id:",
                                   font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbladd = Label(showDataFrame, text=row,
                               font=("arial", 12, "bold"))
                lbladd.place(x=90, y=120)


if __name__ == "__main__":
    root = Tk()
    obj = Fee(root)
    root.mainloop()
