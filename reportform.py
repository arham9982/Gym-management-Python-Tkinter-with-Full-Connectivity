from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Report Form")
        self.root.geometry("600x500+300+150")

        self.create_widgets()

    def create_widgets(self):
        main_frame = Frame(self.root, bg="#f0f0f0")
        main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        lbl_report_title = Label(main_frame, text="Report Title", font=("Arial", 12, "bold"), bg="#f0f0f0")
        lbl_report_title.grid(row=0, column=0, pady=10, padx=10, sticky=W)

        self.entry_report_title = Entry(main_frame, font=("Arial", 12), bd=2, relief=GROOVE)
        self.entry_report_title.grid(row=0, column=1, pady=10, padx=10, sticky=W+E)

        lbl_report_content = Label(main_frame, text="Report Content", font=("Arial", 12, "bold"), bg="#f0f0f0")
        lbl_report_content.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        self.entry_report_content = Text(main_frame, height=8, width=40, font=("Arial", 12), wrap=WORD, bd=2, relief=GROOVE)
        self.entry_report_content.grid(row=1, column=1, pady=10, padx=10, sticky=W+E)

        # Additional information/questions
        additional_info = [
            ("Your Age", "numeric"),
            ("How did you hear about us?", "text"),
            ("Rate your overall satisfaction (1-10)", "numeric"),
            ("Suggestions for improvement", "text")
        ]

        entry_widgets = []

        for i, (question, input_type) in enumerate(additional_info, start=2):
            lbl_question = Label(main_frame, text=question, font=("Arial", 12, "bold"), bg="#f0f0f0")
            lbl_question.grid(row=i, column=0, pady=10, padx=10, sticky=W)

            if input_type == "numeric":
                entry_widget = Entry(main_frame, font=("Arial", 12), bd=2, relief=GROOVE)
            else:
                entry_widget = Text(main_frame, height=3, width=30, font=("Arial", 12), wrap=WORD, bd=2, relief=GROOVE)

            entry_widget.grid(row=i, column=1, pady=10, padx=10, sticky=W+E)
            entry_widgets.append(entry_widget)

        btn_submit_report = Button(main_frame, text="Submit Report", bg="#4CAF50", fg="white", width=15, command=lambda: self.submit_report(entry_widgets))
        btn_submit_report.grid(row=len(additional_info) + 2, column=1, pady=20, padx=10)

    def submit_report(self, entry_widgets):
        title = self.entry_report_title.get()
        content = self.entry_report_content.get("1.0", "end-1c")

        additional_info_answers = [entry_widget.get("1.0", "end-1c").strip() if isinstance(entry_widget, Text) else entry_widget.get() for entry_widget in entry_widgets]

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="arham",
                database="attend",
            )
            my_cursor = conn.cursor()


 



            # Insert the report information into the 'reports' table
            placeholders = ', '.join(['%s'] * (len(additional_info_answers) + 2))
            my_cursor.execute("INSERT INTO reports (title, content, {}) VALUES ({})".format(', '.join(["info{}".format(i+1) for i in range(len(additional_info_answers))]), placeholders), (title, content, *additional_info_answers))
            
            conn.commit()
            conn.close()

            messagebox.showinfo("Report Submitted", f"Report Title: {title}\nReport Content:\n{content}\n\nAdditional Information:\n{', '.join(additional_info_answers)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()
