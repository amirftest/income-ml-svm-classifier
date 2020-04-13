
# income-ml-svm-classifier

## Implementation Details
  
  ####SVM_handler
  * For training the svm machine, i used SCV(C-Support Vector Classification),  and applied the SelectKBest ,feature selection algorithm, to minimize the error percentage.
 * training/testing status var was created to handle multi-thread environment and preventing unnecessary repeated job
  
  ####GUI
  * I've used tkinter for making the gui and messagebox to alert the user. In order to make the gui responsive, for each task a new thread will be created.
   * To handle Cuncurrency issues, a boolean var will be checked to see if some task already been done / in process
  
## Installation

  * Clone/Download this repo.
  * Install the required packages such as sklearn, numpy, tkinter, etc.
  * Execute in CMD\Terminal:
    ```
    python gui.py
    ``` 
  * Follow the instructions
  
##Apendix - Finding the best K Features
  * k = 1:   &nbsp;  &nbsp; 24.568393094289508   &nbsp;  &nbsp;(Martial-status)
  * k = 2:   &nbsp;  &nbsp; 18.300132802124832   &nbsp;  &nbsp;(Education-num, Martial-status)
  * k = 3:   &nbsp;  &nbsp; 18.97078353253652   &nbsp;&nbsp;&nbsp;&nbsp; (Age, Education-num, Martial-status)
  * k = 4:   &nbsp;  &nbsp; 18.579017264276228  &nbsp;  &nbsp;(Age, Education-num, Martial-status, Hours-per-week)
  * k = 5:   &nbsp;  &nbsp; 20.53120849933599  &nbsp;&nbsp;&nbsp;&nbsp; (Age, Education-num, Martial-status,Capital-gain,  Hours-per-week)
  * k = 6:   &nbsp;  &nbsp; 20.53120849933599
  * k = 7:   &nbsp;  &nbsp; 20.53120849933599
  * k = 8:   &nbsp;  &nbsp; 20.35856573705179
  * k = 9:   &nbsp;  &nbsp; 20.35856573705179
  * k = 10:  &nbsp; 20.35856573705179
  * k = 11:  &nbsp; 20.35856573705179
  * k = 12:  &nbsp; 20.35856573705179
  * k = 13:  &nbsp; 20.35856573705179
  * k = 14:  &nbsp; 20.916334661354583












  
  


