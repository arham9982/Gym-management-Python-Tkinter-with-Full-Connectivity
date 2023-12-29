from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class EmployeeForm:
    def __init__(self, root):
        self.root = root
        self.root.title("EMPLOYEE MANAGEMENT SYSTEM")
        self.root.geometry("1000x610+170+0")

        self.contact = StringVar()
        self.employeeId = StringVar()
        self.employeeName = StringVar()
        self.position = StringVar()
        self.gender = StringVar()
        self.email = StringVar()
        self.address = StringVar()

        lblimg = Label(self.root, text="EMPLOYEE DETAILS", bd=10, bg="#007BFF", relief=GROOVE,
                       fg="white", font=("Helvetica", 30, "bold italic"))
        lblimg.place(x=0, y=0, width=1000, height=70)

        labelframeright = LabelFrame(
            self.root, text="Employee Details", font=("times new roman", 11, "bold"), padx=2, bd=4, relief=RIDGE)
        labelframeright.place(x=120, y=90, width=800, height=400)

        lbl_cust_contact = Label(
            labelframeright,
            text="Employee Contact",
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

        lbl_emp_Id = Label(
            labelframeright,
            text="Employee ID",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_emp_Id.grid(row=1, column=0, sticky=W)

        entry_emp_Id = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.employeeId
        )
        entry_emp_Id.grid(row=1, column=1, sticky=W)

        lbl_emp_name = Label(
            labelframeright,
            text="Employee Name",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_emp_name.grid(row=2, column=0, sticky=W)

        entry_emp_name = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.employeeName
        )
        entry_emp_name.grid(row=2, column=1, sticky=W)

        lbl_emp_position = Label(
            labelframeright,
            text="Position",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_emp_position.grid(row=3, column=0, sticky=W)

        positions = ["Manager", "Developer", "Designer", "Administrator"]
        entry_emp_position = ttk.Combobox(
          labelframeright,
          values=positions,
          font=("times new roman", 11, "bold"),
          textvariable=self.position)
        entry_emp_position.grid(row=3, column=1, sticky=W)
        entry_emp_position.current(0)

        

        entry_emp_position = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.position
        )
        entry_emp_position.grid(row=3, column=1, sticky=W)

        lbl_emp_gender = Label(
            labelframeright,
            text="Gender",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_emp_gender.grid(row=4, column=1, sticky=W)

        combogender = ttk.Combobox(
            labelframeright,
            font=("arial", 11, "bold"),
            width=16,
            state="readonly",
            textvariable=self.gender
        )
        combogender["value"] = ("Male", "Female", "Other")
        combogender.current(0)
        combogender.grid(row=4, column=1)

        lbl_emp_email = Label(
            labelframeright,
            text="Email",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_emp_email.grid(row=5, column=0, sticky=W)

        entry_emp_email = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.email
        )
        entry_emp_email.grid(row=5, column=1, sticky=W)

        lbl_emp_address = Label(
            labelframeright,
            text="Address",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_emp_address.grid(row=6, column=0, sticky=W)

        entry_emp_address = ttk.Entry(
            labelframeright,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.address
        )
        entry_emp_address.grid(row=6, column=1, sticky=W)

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

        self.fetch_data()  # Added to fetch data initially

    def add_data(self):
        if self.contact.get() == "" or self.employeeId.get() == "" or self.employeeName.get() == "" or self.position.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="your_password",
                    database="your_database",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s,%s)", (
                    self.contact.get(),
                    self.employeeId.get(),
                    self.employeeName.get(),
                    self.position.get(),
                    self.gender.get(),
                    self.email.get(),
                    self.address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Employee has been added successfully")

            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="arham",
                database="your_database",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from employee")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.employee_table.delete(
                    *self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert('', END, values=row)
                conn.commit()
            conn.close()

        except Exception as es:
            messagebox.showwarning(
                "Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_contact(self):
        if self.contact.get() == "":
            messagebox.showerror(
                "Error", "Contact Number must be required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="your_password",
                    database="your_database",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select * from employee where contact=%s", (self.contact.get(),))
                row = my_cursor.fetchone()
                self.contact.set(row[0])
                self.employeeId.set(row[1])
                self.employeeName.set(row[2])
                self.position.set(row[3])
                self.gender.set(row[4])
                self.email.set(row[5])
                self.address.set(row[6])
                conn.close()

            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def update(self):
        if self.contact.get() == "":
            messagebox.showerror(
                "Error", "Contact Number must be required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="your_password",
                    database="your_database",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("update employee set emp_id=%s, emp_name=%s, position=%s, gender=%s, email=%s, address=%s where contact=%s", (
                    self.employeeId.get(),
                    self.employeeName.get(),
                    self.position.get(),
                    self.gender.get(),
                    self.email.get(),
                    self.address.get(),
                    self.contact.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Employee details have been updated successfully")

            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def ndelete(self):
        if self.contact.get() == "":
            messagebox.showerror(
                "Error", "Contact Number must be required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="your_password",
                    database="your_database",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "delete from employee where contact=%s", (self.contact.get(),))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()
                messagebox.showinfo(
                    "Success", "Employee details have been deleted successfully")

            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def clear(self):
        self.contact.set("")
        self.employeeId.set("")
        self.employeeName.set("")
        self.position.set("")
        self.gender.set("")
        self.email.set("")
        self.address.set()

root = Tk()
obj = EmployeeForm(root)
root.mainloop()
