class MyClass:
    __privatevar = 27;
    
    def privmath (self):
        print("I am inside my class")
    def hello(self):
        print("printable var value:",MyClass.__privatevar)
foo = MyClass()
foo.hello()
foo.privmath()