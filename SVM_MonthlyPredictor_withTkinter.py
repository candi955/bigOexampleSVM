# Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox

# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd



import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# pulling excel file and creating variable
lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = lottoExcel.sheets()


for sheet in sheets:
    lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# creating dataframe for tkinter
df = pd.DataFrame(lottoSheetData)

sources = lottoSheetData[:, :-2]
target = lottoSheetData[:, len(lottoSheetData[0]) - 1]

sourceNoHeader = np.delete(sources, (0), axis=0)
targetNoHeader = np.delete(target, (0), axis=0)

X = sourceNoHeader
y = targetNoHeader

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

model = svm.SVC(kernel='linear')
model.fit(X_train, y_train.ravel())
y_pred = model.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
###################################################################################################################
root = tk.Tk()
root.title('SVM Prediction (predicting the month a set of dummy lottery numbers will win)')
#root.geometry("1000x1000")
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

# Tabs and Frames
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Dataset')
tab_control.add(tab2, text='Prediction Accuracy')
tab_control.add(tab3, text='Dummy Values and Prediction')

tab_control.pack(expand=1, fill='both')

###################################################################################################################
# the dataframe method, tab 1
def writeDataset():
    tab1_display.insert(1.0, pd.DataFrame(df))

# the accuracy score method, tab 2
def writeAccuracy():
    tab2_display.insert(4.0, str(accuracy_score(y_test, y_pred)))

# creating a method so that the user can tab from one dummy number textbox to the next, instead of clicking
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

# the dummy number value method, for tab 3 input entries from the user
def dummyValues():
    while True:
        try:

            # getting user-input for dummy numbers to be used in the algorithm; preferably the most recent
            # lottery numbers
            dummyTextOne = dummyNumberOne.get('1.0', tk.END)
            dummyTextTwo = dummyNumberTwo.get('1.0', tk.END)
            dummyTextThree = dummyNumberThree.get('1.0', tk.END)
            dummyTextFour = dummyNumberFour.get('1.0', tk.END)
            dummyTextFive = dummyNumberFive.get('1.0', tk.END)

            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = int(dummyTextOne)
            dummyValues.dummyTextTwo = int(dummyTextTwo)
            dummyValues.dummyTextThree = int(dummyTextThree)
            dummyValues.dummyTextFour = int(dummyTextFour)
            dummyValues.dummyTextFive = int(dummyTextFive)

        # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
        # is made, the program brings the user back to the main menu by calling the Predictions class and menu
        # method
        except ValueError:
            # error message variable
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()



        if dummyValues.dummyTextOne < 1 or dummyValues.dummyTextOne > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()


        if dummyValues.dummyTextTwo < 1 or dummyValues.dummyTextTwo > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        if dummyValues.dummyTextThree < 1 or dummyValues.dummyTextThree > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        if dummyValues.dummyTextFour < 1 or dummyValues.dummyTextFour > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        if dummyValues.dummyTextFive < 1 or dummyValues.dummyTextFive > 69:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        else:
            # breaking the loop to avoid infinite loop
            break

# the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
# is called at the beginning of the finalPrediction method (for the user-input variables)
def finalPrediction():


    while True:
        try:
            #calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour, dummyValues.dummyTextFive])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            tab3_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please enter a number between 1 and 69.")
            clear_display_result()

        else:
            break

def clear_display_result():
    tab3_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)
    dummyNumberFive.delete(1.0, END)

    dummyNumberOne.focus()

def mainMenu():

    while True:
        try:
            # placing this as example, since this module will be moved to another program and menu module will need changed
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                root.protocol("WM_DELETE_WINDOW", mainMenu)
                import mainPageWithTkinter

        except ValueError:
            import mainPageWithTkinter
        else:
            break

def exitProgram():
    exit()

def flush(self):
    pass
###################################################################################################################
# Labels for tabs
l1 = Label(tab1, text='Please click the button below to scroll through the original dataset model.', padx=5, pady=5)
l1.grid(row=1, column=0)
l2 = Label(tab2, text='Please click the button below to see the prediction accuracy of the model in decimal ' +
                      'format.', padx=5, pady=5)
l2.grid(row=1, column=0)
l3 = Label(tab3, text='Please enter five dummy numbers in the cells below,\n and then click the Prediction button to ' +
                      'see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)


# Dummy Number Input Boxes
dummyNumberOne = ScrolledText(tab3, height=1)
# the next piece of code is calling from the focus_next_widget method so that the user can tab from textbox to textbox,
# rather than clicking
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=0, columnspan=1, padx=5, pady=5)

dummyNumberTwo = ScrolledText(tab3, height=1)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

dummyNumberThree = ScrolledText(tab3, height=1)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

dummyNumberFour = ScrolledText(tab3, height=1)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

dummyNumberFive = ScrolledText(tab3, height=1)
dummyNumberFive.bind("<Tab>", focus_next_widget)
dummyNumberFive.grid(row=6, column=0, columnspan=1, padx=5, pady=5)

# Dataset Button
datasetButton = Button(tab1, text='Dataset', command=writeDataset, width=12, bg='purple', fg='#fff')
datasetButton.grid(row=3, column=0, padx=15, pady=15)

# Accuracy Button
AccuracyButton = Button(tab2, text='Prediction Accuracy', command=writeAccuracy, width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=15, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab3, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='purple', fg='#fff')
PredictionButton.grid(row=7, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab3, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=9, column=0, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab1, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=3, column=3, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab1, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=4, column=3, padx=5, pady=5)

# Display Screen for Result
tab1_display = ScrolledText(tab1, height=20, width=50)
tab1_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

tab2_display = ScrolledText(tab2, height=1, width=20)
tab2_display.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

tab3_display = ScrolledText(tab3, height=1)
tab3_display.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

# Keep window alive
mainloop()