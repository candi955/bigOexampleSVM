# Libraries

from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import time

start = time.clock()
elapsed = time.clock() - start


# pulling excel file and creating variable
lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = lottoExcel.sheets()
for sheet in sheets:
    lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
    #lottoSheetData_DataFrame = pd.DataFrame(lottoSheetData)
    # print('\n' + '\n' + 'LottoSheet Data, DataFrame(excel) format:')
    # print(lottoSheetData_DataFrame)
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
# the dummy number value method, for tab 3 input entries from the user

print('The lottery dataframe this prediction is being trained off of is as follows:\n ')
print(pd.DataFrame(df))
print('\n')

# __________________________________________________________________________________________


class SVM():


    def _dummyNums_(self):
        # getting user-input for dummy numbers to be used in the algorithm; preferably the most recent
        # lottery numbers
        dummyTextOne = input("Please enter first predicted number: ")
        dummyTextTwo = input("Please enter second predicted number: ")
        dummyTextThree = input("Please enter third predicted number: ")
        dummyTextFour = input("Please enter fourth predicted number: ")
        dummyTextFive = input("Please enter fifth predicted number: ")

        dummyTextOne = int(dummyTextOne)
        dummyTextTwo = int(dummyTextTwo)
        dummyTextThree = int(dummyTextThree)
        dummyTextFour = int(dummyTextFour)
        dummyTextFive = int(dummyTextFive)


        while True:
            try:

                if dummyTextOne < 1 or dummyTextOne > 69:
                    print("Error, Please enter a number between 1 and 69.")

                if dummyTextTwo < 1 or dummyTextTwo > 69:
                    print("Error, Please enter a number between 1 and 69.")


                if dummyTextThree < 1 or dummyTextThree > 69:
                    print("Error, Please enter a number between 1 and 69.")

                if dummyTextFour< 1 or dummyTextFour > 69:
                    print("Error, Please enter a number between 1 and 69.")

                if dummyTextFive < 1 or dummyTextFive > 69:
                    print("Error, Please enter a number between 1 and 69.")

            except ValueError:
                print('Please try again.')

            else:
                break

        # the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
        # is called at the beginning of the finalPrediction method (for the user-input variables)

        while True:
            try:

                #calling dummy values function to call variables from that function

                # turning the dummy values, which were string then integer, back into an array for the prediction
                a = np.array([dummyTextOne, dummyTextTwo, dummyTextThree, dummyTextFour, dummyTextFive])


                # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
                # placed within the prediction variable
                prediction = knn.predict([a])
                print("\nThe prediction is: ")
                print(prediction)

                print('\nThe accuracy score of the prediction is: ')
                print(accuracy_score(y_test, y_pred))

            except ValueError:
                print("Error, Please enter a number between 1 and 69.")

            else:
                break


SVM()

def Main():

    mySVM = SVM()
    mySVM._dummyNums_()


Main()
