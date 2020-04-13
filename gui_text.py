

LABEL_INTRO = "This program was developed to demonstrate the usage of SVM for classification and regression analysis. We'll examine whether a person’s income is higher or lower than 50K according to several features"
LABEL_INSTRUCTION = "Instructions:\n1. Run Training\n2. Run Testing to calculate the prectnage error\n3. Send the results by email"
LABEL_EMAIL_NOT_READY = "Please run testing in order to calculate the error percentage or wait until testing is over before sending email"
LABEL_EMAIL_SENT = "Email was sent"
LABEL_EMAIL_IN_PROGRESS = "Sending email is in progress"
LABEL_SOME_CORRUPTED_DATA = "Pay Attention, some data was found to be corrupted"
LABEL_TRAINING_FINISHED = "Training was finished, please proceed to Testing"
LABEL_TESTING_FINISHED = "Testing was finished, you can now send the results"
LABEL_TRAIN_BEFORE_TEST = "Please run training before testing or wait until training is over"
LABEL_EMAIL_FAILED = "Failed to send"

def label_already_defined(string):
    return f"{string} is already running, please wait until it's finished"


def label_corrupted(string):
    return f"{string} Data is corrupted"



