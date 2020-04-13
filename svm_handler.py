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
        self.error_percentage = -1
        self.corrupted_data = False

    def run_train(self):
        try:
            if self.training_status == Status.UNINITIALIZED:
                self.training_status = Status.IN_PROGRESS
                x_train, y_train, corrupted_data = parse_data('data/adult.data')
                self.corrupted_data = corrupted_data
                self.clf.fit(x_train, y_train)  # train the svm
                self.training_status = Status.DONE
        except Exception as e:
            print(e)
            self.training_status = Status.UNINITIALIZED



    def run_test(self):
        if self.training_status == Status.DONE and self.testing_status == Status.UNINITIALIZED:
            try:
                self.corrupted_data = False
                self.testing_status = Status.IN_PROGRESS
                x_test, y_test, corrupted_data = parse_data('data/adult.test')
                self.corrupted_data = corrupted_data
                y_pred = self.clf.predict(x_test)  # test
                self.error_percentage = calculate_error_percentage(y_test, y_pred)
                self.testing_status = Status.DONE
            except Exception as e:
                self.testing_status = Status.UNINITIALIZED
                print(e)

    def get_error_percentage(self):
        return self.error_percentage


if __name__ == "__main__":
    my_svm = SVMHandler()
