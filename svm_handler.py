from sklearn import svm
from parse_data import parse_data
from calc_error_pct import *
from tkinter import messagebox



class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
        X_train, y_train = parse_data('C:\\Velis\\data\\adult.test')
        X_test, y_test = parse_data('C:\\Velis\\data\\adult.data')
        clf = svm.SVC()
        clf.fit(X_train, y_train)    # train the svm
        y_pred = clf.predict(X_test) # test
        print(calculate_error_percentage(y_test,y_pred))


if __name__ == "__main__":
    mysvm = SVMHandler()






