__author__ = 'amirf'
from tkinter import *
from tkinter import ttk
from svm_handler import SVMHandler
from mail import sendemail
import threading


def run_gui():
    root = Tk()
    root.title("SVM GUI")
    # Here you need to set the frame, grid, row and column configurations of the root.

    svm_handler = SVMHandler()


    # Here you need to start the training of the svm. Remember, the other actions (testing/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_train():


    # Here you need to start the testing with the svm. Remember, the other actions (training/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_test():


    # Here you need to send an email with the svm testing result. Remember, the other actions (training/testing)
    # must be responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def send_mail():


    # Here you need to implement three buttons, one for each action.


    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()