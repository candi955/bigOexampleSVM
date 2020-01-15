# attempting to take template of argumentPracticeFunctionsClasses.py from the
# reference: # reference: https://stackoverflow.com/questions/11421659/passing-variables-creating-instances-self-the-mechanics-and-usage-of-classes
# and add in new variables to evaluate mechanics of code, as a self-study and guide.

class Foo(object):
    # ^class name  #^ inherits from object

    fooClassAttributeVariable = "Foo Class Attribute variable 'bar'" #Class attribute.

    def __init__(self):
        #        #^ The first variable is the class instance in methods.
        #        #  This is called "self" by convention, but could be any name you want.
        #^ double underscore (dunder) methods are usually special.  This one
        #  gets called immediately after a new instance is created.

        self.variable = "This is class Foo's self _init_ self.variable instance attribute" #instance attribute.
        print(self.variable, self.fooClassAttributeVariable)  #<---self.bar references class attribute
        self.fooClassAttributeVariable = " under _init_ changed Foo Class Attribute variable from 'bar' to 'Baz'"   #<---self.bar is now an instance attribute
        print(self.variable, self.fooClassAttributeVariable)

    def method(self, arg1, arg2):
        #This method has arguments.  You would call it like this:  instance.method(1, 2)
        print("in method (args):", arg1, arg2)
        print("in method (attributes):", self.variable, self.fooClassAttributeVariable)


FooClassVariable = Foo() # this calls __init__ (indirectly), output:
                 # Foo bar
                 # Foo  Bar is now Baz
print(FooClassVariable.variable) # Foo
FooClassVariable.variable = "This is the variable created later for FooClassVariable.variable"
FooClassVariable.method(1, 2) # output:
               # in method (args): 1 2
               # in method (attributes): bar  Bar is now Baz
Foo.method(FooClassVariable, 1, 2) #<--- Same as a.method(1, 2).  This makes it a little more explicit what the argument "self" actually is.

class Bar(object):
    def __init__(self, arg):
        self.arg = arg
        self.Foo = Foo()

variableOfBarClasswithFooClassVariableAsArgument = Bar(FooClassVariable)
variableOfBarClasswithFooClassVariableAsArgument.arg.variable = "something"
print(FooClassVariable.variable) # something
print(variableOfBarClasswithFooClassVariableAsArgument.Foo.variable) # Foo

# Results
# This is class Foo's self _init_ self.variable instance attribute Foo Class Attribute variable 'bar'
# This is class Foo's self _init_ self.variable instance attribute  under _init_ changed Foo Class Attribute variable from 'bar' to 'Baz'
# This is class Foo's self _init_ self.variable instance attribute
# in method (args): 1 2
# in method (attributes): This is the variable created later for FooClassVariable.variable  under _init_ changed Foo Class Attribute variable from 'bar' to 'Baz'
# in method (args): 1 2
# in method (attributes): This is the variable created later for FooClassVariable.variable  under _init_ changed Foo Class Attribute variable from 'bar' to 'Baz'
# This is class Foo's self _init_ self.variable instance attribute Foo Class Attribute variable 'bar'
# This is class Foo's self _init_ self.variable instance attribute  under _init_ changed Foo Class Attribute variable from 'bar' to 'Baz'
# something
# This is class Foo's self _init_ self.variable instance attribute