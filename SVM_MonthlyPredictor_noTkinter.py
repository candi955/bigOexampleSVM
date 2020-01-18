# references for timer functionality:
# https://stackoverflow.com/questions/85451/pythons-time-clock-vs-time-time-accuracy
# https://docs.python.org/3.7/library/timeit.html
# https://docs.python.org/2/library/timeit.html
# https://www.youtube.com/watch?v=l0MI6TILasM


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

import time

# ____________________________________________________________________________________________________
# timer reference: https://www.youtube.com/watch?v=l0MI6TILasM
startDataPull = time.time()
print('\nEpoch start-time concerning pulling data for program functionality: ', startDataPull)

# pulling excel file and creating variable
lottoExcel = xlrd.open_workbook('PastWinningNum_SVM_Excel.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = lottoExcel.sheets()
for sheet in sheets:
    lottoSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

endDataPull = time.time()
print('Epoch end-time concerning pulling data for program functionality: ', endDataPull)
DataPullElapsed = endDataPull - startDataPull
print('Epoch elapsed-time concerning pulling data for program functionality: ', DataPullElapsed, ' seconds')
# timer reference: https://www.youtube.com/watch?v=l0MI6TILasM
# ____________________________________________________________________________________________________

# creating variable to print dataframe at beginning of the program later
df = pd.DataFrame(lottoSheetData)


sources = lottoSheetData[:, :-2]
target = lottoSheetData[:, len(lottoSheetData[0]) - 1]

sourceNoHeader = np.delete(sources, (0), axis=0)
targetNoHeader = np.delete(target, (0), axis=0)

X = sourceNoHeader
y = targetNoHeader

# ____________________________________________________________________________________________________
# timing various functionalities
# timer reference: https://www.youtube.com/watch?v=l0MI6TILasM
startTrain = time.time()
print('\nEpoch start-time for Trainer functionality: ', startTrain)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

endTrain = time.time()
print('Epoch end-time for Trainer functionality: ', endTrain)
elapsedTrain = endTrain - startTrain
print('Epoch elapsed-time for Trainer functionality: ', elapsedTrain, ' seconds')

# ____________________________________________________________________________________________________
# timing the model.fit functionality

startModelFit = time.time()
print('\nEpoch-start of model.fit functionality: ', startModelFit)

model = svm.SVC(kernel='linear')
model.fit(X_train, y_train.ravel())

endModelFit = time.time()
print('Epoch-end of model.fit functionality: ', endModelFit)

elapsedModelFit = endModelFit - startModelFit
print('Elapsed-time of model.fit functionality: ', elapsedModelFit, ' seconds\n')

# ____________________________________________________________________________________________________
y_pred = model.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=1)

# ____________________________________________________________________________________________________
# timing the knn functionality

knnFunctStart = time.time()
print('\nEpoch-start of knn functionality: ', knnFunctStart)

knn.fit(X, y)

knnFunctEnd = time.time()
print('Epoch-end of knn functionality: ', knnFunctEnd)

knnFunctElapsed = knnFunctEnd - knnFunctStart
print('Elapsed-time of knn functionality: ', elapsedModelFit, ' seconds\n')
# ____________________________________________________________________________________________________

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

                # timer reference: https://www.youtube.com/watch?v=l0MI6TILasM
                start = time.time()
                # timer reference: https://www.youtube.com/watch?v=l0MI6TILasM

                #calling dummy values function to call variables from that function
                # turning the dummy values, which were string then integer, back into an array for the prediction
                a = np.array([dummyTextOne, dummyTextTwo, dummyTextThree, dummyTextFour, dummyTextFive])


                # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
                # placed within the prediction variable
                prediction = knn.predict([a])
                print("\nThe prediction is: ", prediction)

                print('\nThe accuracy score of the prediction is: ', accuracy_score(y_test, y_pred))

                # timer reference: https://www.youtube.com/watch?v=l0MI6TILasM
                print('\nEpoch start-time of prediction functionality is: ', start)
                end = time.time()
                print('Epoch end-time of prediction functionality is:', end)
                elapsed = end - start
                print("This amount of time has elapsed during the processing of the prediction function: ", elapsed,
                      'seconds')
                # timer reference: https://www.youtube.com/watch?v=l0MI6TILasM

            except ValueError:
                print("Error, Please enter a number between 1 and 69.")

            else:
                break

SVM()

def Main():

    mysvm = SVM()
    mysvm._dummyNums_()


    # Entering timing data from steps in beginning of program for comparison to the prediction function _dummyNums_()
    # timer reference: https://www.youtube.com/watch?v=l0MI6TILasM
    print('\nCompare this to:\n')

    print('Epoch elapsed-time concerning pulling data for program functionality: ', DataPullElapsed, ' seconds')
    print('Time elapsed for the training functionality: ', elapsedTrain, ' seconds')
    print('Elapsed-time of model.fit functionality:', elapsedModelFit, ' seconds')
    print('Elapsed-time of knn functionality: ', knnFunctElapsed, ' seconds\n')

    # timer reference: https://www.youtube.com/watch?v=l0MI6TILasM

    import mainPageForNoTkinter

Main()
