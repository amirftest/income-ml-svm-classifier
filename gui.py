__author__ = 'amirf'
from tkinter import *
from tkinter import ttk
from svm_handler import SVMHandler
from mail import sendemail
from status import *
from tkinter import messagebox
import threading

def run_gui():
    svm_handler = SVMHandler()
    root = Tk()
    root.title("SVM GUI")

    # frame, grid, row and column configurations of the root.
    mainframe = ttk.Frame(root)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    def activate_train():
        threading.Thread(target=activate_train_util, name="activate_train").start()

    def activate_test():
        threading.Thread(target=activate_test_util, name="activate_test").start()

    def send_mail():
        threading.Thread(target=send_mail_util, name="send_mail").start()

    def send_mail_util():
        error_percentage = svm_handler.get_error_percentage()
        if error_percentage>=0:
            sendemail(error_percentage)

    def activate_train_util():
        training_status = svm_handler.training_status
        if svm_handler.training_status == Status.UNINITIALIZED:
            svm_handler.run_train()
            if svm_handler.training_status == Status.DONE:
                messagebox.showinfo("Success", "Completed Training")
            else:
                messagebox.showerror("Error", "Training Data is corrupted")
        elif training_status == Status.IN_PROGRESS:
            messagebox.showinfo("Alert", "Training is already running, please wait until it's finished")
        elif training_status == Status.DONE:
            messagebox.showinfo("Alert", "Training was finished, please proceed to Testing")

    def activate_test_util():
        testing_status = svm_handler.testing_status
        if svm_handler.training_status != Status.DONE:
            messagebox.showerror("Error", "Please run training before testing or wait until training is over")
        elif testing_status == Status.UNINITIALIZED:
            svm_handler.run_test()
            if svm_handler.testing_status == Status.DONE:
                messagebox.showinfo("Success", "Completed Testing")
            else:
                messagebox.showerror("Error", "Testing Data is corrupted")
        elif testing_status == Status.IN_PROGRESS:
            messagebox.showinfo("Alert", "Testing is already running, please wait until it's finished")
        elif testing_status == Status.DONE:
            messagebox.showinfo("Alert", "Testing was finished, you can now send the results")


    def create_button(text, command, row):
        Button(root, text=text, padx=50, command=command).pack()
        # Button(root, text=text, padx=50, command=command).grid(row=row, column=0, pady=5, sticky="")


    Label(root, text="This program was developed to demonstrate the usage of SVM for classification and regression analysis.\n We'll examine whether a person’s income is higher or lower than 50K according to several features.\nInstructions:\n1. Run Training\n 2. Run Testing to calculate the prectnage error\n 3. Send the results by email").pack()
    #Label(root, text="This program was developed to demonstrate the usage of SVM for classification and regression analysis.\n We'll examine whether a person’s income is higher or lower than 50K according to several features.\nInstructions:\n1. Run Training\n 2. Run Testing to calculate the prectnage error\n 3. Send the results by email").grid(row=0,column=0, pady=5)
    create_button("Run Training", activate_train, 1)
    create_button("Run Testing", activate_test, 2)
    create_button("Send Results", send_mail, 3)

    root.mainloop()



if __name__ == "__main__":
    run_gui()