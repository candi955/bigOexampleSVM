# The main page for the program and module page SVM_MonthlyPredictor_noTkinter.py


class mainPage():

    def _returnToPage_(self):
        choose = input('Please press 1 to return to the SVM page, or 2 to exit the program: ')
        print(choose)
        while True:
            try:
                if choose == '1':
                    import SVM_MonthlyPredictor_noTkinter
                if choose == '2':
                    exit()
            except ValueError:
                print("There was an error, let's start over.")

            else:
                break



mainPage()

ma = mainPage()

def Main():
    ma._returnToPage_()

Main()
