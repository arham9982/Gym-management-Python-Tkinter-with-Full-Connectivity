from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from reportform import Report

class AttendanceRecord:
    def __init__(self, root):
        self.root = root
        self.root.title("GYM ATTENDANCE RECORD")
        self.root.geometry("1200x550+200+50")

        self.member_id = StringVar()
        self.member_name = StringVar()
        self.attendance_status = StringVar()
        self.date_var = StringVar()
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))

        lbl_title = Label(self.root, text="GYM ATTENDANCE RECORD", bd=10, relief=GROOVE,
                          font=("Helvetica", 30, "bold italic"))
        lbl_title.pack(side=TOP, fill=X)

        labelframe_left = LabelFrame(
            self.root, text="Attendance Details", font=("times new roman", 14, "bold"), padx=2, pady=2, bd=4, relief=RIDGE)
        labelframe_left.place(x=10, y=80, width=400, height=450)

        lbl_member_id = Label(
            labelframe_left,
            text="Member ID",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_member_id.grid(row=0, column=0, sticky=W)

        entry_member_id = ttk.Entry(
            labelframe_left,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.member_id
        )
        entry_member_id.grid(row=0, column=1, sticky=W)

        lbl_member_name = Label(
            labelframe_left,
            text="Member Name",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_member_name.grid(row=1, column=0, sticky=W)

        entry_member_name = ttk.Entry(
            labelframe_left,
            width=18,
            font=("times new roman", 11, "bold"),
            textvariable=self.member_name
        )
        entry_member_name.grid(row=1, column=1, sticky=W)

        lbl_attendance_status = Label(
            labelframe_left,
            text="Attendance Status",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_attendance_status.grid(row=2, column=0, sticky=W)

        combobox_attendance_status = ttk.Combobox(
            labelframe_left,
            values=["Present", "Absent"],
            font=("times new roman", 11, "bold"),
            textvariable=self.attendance_status
        )
        combobox_attendance_status.grid(row=2, column=1, sticky=W)
        combobox_attendance_status.current(0)

        lbl_date = Label(
            labelframe_left,
            text="Date",
            font=("arial", 11, "bold"),
            padx=2,
            pady=5,
        )
        lbl_date.grid(row=3, column=0, sticky=W)

        entry_date = ttk.Entry(
            labelframe_left,
            width=18,
            font=("times new roman", 11, "bold"),
            state='readonly',
            textvariable=self.date_var
        )
        entry_date.grid(row=3, column=1, sticky=W)

        btnframe = Frame(labelframe_left, bd=4, relief=RIDGE)
        btnframe.place(x=0, y=150, width=375, height=30)

        btn_mark_attendance = Button(btnframe, text="Mark Attendance", bg="black",
                         fg="white", width=15, command=self.mark_attendance)
        btn_mark_attendance.grid(row=0, column=0)
        btn_mark_attendance = Button(btnframe, text="Delete", bg="black",
                         fg="white", width=15, command=self.delete_attendance)
        btn_mark_attendance.grid(row=0, column=2)

        btn_open_report = Button(btnframe, text="Open Report Form", bg="black", 
                         fg="white", width=15, command=self.open_report_form)
        btn_open_report.grid(row=0,column=4)

        tableframe = LabelFrame(
            self.root, text="Attendance Record", font=("times new roman", 15, "bold"))
        tableframe.place(x=420, y=80, width=750, height=450)

        columns = ("Member ID", "Member Name", "Attendance Status", "Date")

        self.attendance_table = ttk.Treeview(tableframe, column=columns, show="headings")

        for col in columns:
            self.attendance_table.heading(col, text=col)

        self.attendance_table.pack(fill=BOTH, expand=1)
        self.fetch_attendance_data()

    def mark_attendance(self):
        member_id = self.member_id.get()
        member_name = self.member_name.get()
        attendance_status = self.attendance_status.get()
        date = self.date_var.get()

    

        if member_id == "" or member_name == "":
            messagebox.showerror("Error", "Member ID and Member Name are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="attend",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO attendance (member_id, member_name, attendance_status, date) VALUES (%s, %s, %s, %s)",
                                  (member_id, member_name, attendance_status, date))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Attendance marked successfully")
                self.fetch_attendance_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def fetch_attendance_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="attend",
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM attendance")
            rows = my_cursor.fetchall()

            self.attendance_table.delete(*self.attendance_table.get_children())

            for row in rows:
                self.attendance_table.insert("", END, values=row)

            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def delete_attendance(self):
        selected_item = self.attendance_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        confirmation = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this record?")
        if confirmation:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="arham",
                    database="attend",
                )
                my_cursor = conn.cursor()

                # Get the selected record's ID
                selected_record_id = self.attendance_table.item(selected_item, "values")[0]

                # Execute the delete query
                my_cursor.execute("DELETE FROM attendance WHERE id=%s", (selected_record_id,))
                
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Record deleted successfully")
                self.fetch_attendance_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def open_report_form(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)
   



if __name__ == "__main__":
    root = Tk()
    obj = AttendanceRecord(root)
    root.mainloop()
