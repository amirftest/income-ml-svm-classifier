__author__ = 'amirf'

from tkinter import *
from tkinter import ttk
from gui_text import *
from svm_handler import SVMHandler
from mail import sendemail
from status import *
from tkinter import messagebox
import threading
from tkinter.filedialog import askopenfilename

def run_gui():
    svm_handler = SVMHandler()
    root = Tk()
    root.title("SVM GUI")
    root.geometry('330x275')
    # frame, grid, row and column configurations of the root.

    def activate_train():
        threading.Thread(target=activate_train_util, name="activate_train").start()

    def activate_test():
        threading.Thread(target=activate_test_util, name="activate_test").start()

    def send_mail():
        threading.Thread(target=send_mail_util, name="send_mail").start()

    def send_mail_util():
        error_percentage = svm_handler.get_error_percentage()
        if error_percentage == -1:
            messagebox.showerror("Error", LABEL_EMAIL_NOT_READY)
        if error_percentage >= 0:
            res = sendemail(error_percentage)
            if res == Status.DONE:
                messagebox.showinfo("Success", LABEL_EMAIL_SENT)
            elif res == Status.IN_PROGRESS:
                messagebox.showinfo("Success", LABEL_EMAIL_IN_PROGRESS)
            elif res == -1:
                messagebox.showerror("Error", LABEL_EMAIL_FAILED)

    def check_if_corrupted_data():
        if svm_handler.corrupted_data:
            return LABEL_SOME_CORRUPTED_DATA
        else:
            return ""

    def activate_train_util():
        training_status = svm_handler.training_status
        if svm_handler.training_status == Status.UNINITIALIZED:
            svm_handler.run_train()
            if svm_handler.training_status == Status.DONE:
                messagebox.showinfo("Success", "Completed Training. "+check_if_corrupted_data())
            else:
                messagebox.showerror("Error", label_corrupted("Training"))
        elif training_status == Status.IN_PROGRESS:
            messagebox.showinfo("Alert",  label_already_defined("Training"))
        elif training_status == Status.DONE:
            messagebox.showinfo("Alert", LABEL_TRAINING_FINISHED)

    def activate_test_util():
        testing_status = svm_handler.testing_status
        if svm_handler.training_status != Status.DONE:
            messagebox.showerror("Error", LABEL_TRAIN_BEFORE_TEST)
        elif testing_status == Status.UNINITIALIZED:
            svm_handler.run_test()
            if svm_handler.testing_status == Status.DONE:
                messagebox.showinfo("Success", "Completed Testing. "+check_if_corrupted_data())
            else:
                messagebox.showerror("Error",  label_corrupted("Testing"))
        elif testing_status == Status.IN_PROGRESS:
            messagebox.showinfo("Alert", label_already_defined("Testing"))
        elif testing_status == Status.DONE:
            messagebox.showinfo("Alert", LABEL_TESTING_FINISHED)

    def create_button(text, command):
        Button(root, text=text, padx=50, bg = "white", command=command).pack(pady=4)

    Label(root, text=LABEL_INTRO, wraplength=330).pack(expand=True)
    Label(root, text=LABEL_INSTRUCTION, wraplength=330, justify=LEFT).pack(expand=True, anchor="w")
    create_button("Run Training", activate_train)
    create_button("Run Testing", activate_test)
    create_button("Send Results", send_mail)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
