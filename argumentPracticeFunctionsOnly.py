# reference https://www.youtube.com/watch?v=KeRxe9rll2Q&t=299s

#set width and height as keyword arguments (parameters need to be assigned due to no default), font and bgc have
# defaults, and scrollbar was also added to the window as a default.
def basic_window(width, height, font='TNR', bgc='w', scrollbar=True):
    print(width, height, font, bgc)

# set parameters for width and height in the order originally listed, but then changed the default value of bgc only
basic_window(500, 350, bgc='b')

#set parameters for width and height in the order originally listed, and left all other values as default
basic_window(10, 50)

# put width and height out of order, to show the parameter assignment to the keyword arguments
basic_window(height=6000, width=1)

# results when the program runs:
# 00 350 TNR b
# 10 50 TNR w
# 1 6000 TNR w