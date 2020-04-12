from sklearn import svm
from parse_data import parse_data
from calc_error_pct import *
from tkinter import messagebox
from status import *


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
        self.clf = svm.SVC()
        self.training_status = Status.UNINITIALIZED
        self.testing_status = Status.UNINITIALIZED
        self.error = -1

    def run_train(self):
        try:
            if self.training_status == Status.UNINITIALIZED:
                self.training_status = Status.IN_PROGRESS
                X_train, y_train = parse_data('data/adult.data')
                self.clf.fit(X_train, y_train)  # train the svm
                self.training_status = Status.DONE
                print(self.training_status)
        except Exception as e:
            self.training_status = Status.UNINITIALIZED
            print(e)

    def run_test(self):
        if self.training_status == Status.DONE and self.testing_status == Status.UNINITIALIZED:
            try:
                self.testing_status = Status.IN_PROGRESS
                X_test, y_test = parse_data('data/adult.test')
                y_pred = self.clf.predict(X_test)  # test
                self.error = calculate_error_percentage(y_test, y_pred)
                print(self.error)

            except Exception as e:
                self.testing_status = Status.UNINITIALIZED
                print(e)

    def get_error_percentage(self):
        if (self.error==-1):
            messagebox.showerror("Error", "Please run testing in order to calculate the error percentage or wait until testing is over")
        return self.error

