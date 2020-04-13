from sklearn import svm
from parse_data import parse_data
from calc_error_pct import *
from status import *
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif

BEST_K_FEATURES = 2
class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
        self.clf = svm.SVC()
        self.training_status = Status.UNINITIALIZED
        self.testing_status = Status.UNINITIALIZED
        self.error_percentage = -1
        self.corrupted_data = False
        self.cols = []

    def run_train(self):
        try:
            if self.training_status == Status.UNINITIALIZED:
                self.training_status = Status.IN_PROGRESS
                x_train, y_train, corrupted_data = parse_data('data/adult.data')
                x_train = np.array(x_train)
                y_train = np.array(y_train)
                selector = SelectKBest(f_classif, k=BEST_K_FEATURES)
                selector.fit(x_train, y_train)
                self.cols = selector.get_support(indices=True)
                x_train = x_train[:, self.cols]
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
                x_test = np.array(x_test)
                x_test = x_test[:, self.cols]
                y_pred = self.clf.predict(x_test)  # test
                self.error_percentage = calculate_error_percentage(y_test, y_pred)
                self.testing_status = Status.DONE
            except Exception as e:
                self.testing_status = Status.UNINITIALIZED
                print(e)

    def get_error_percentage(self):
        return self.error_percentage

