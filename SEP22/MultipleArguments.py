def myFun(*args):
    for arg in args:
        print(arg, end=", ")
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def myFun2(*args):
    product=1
    for arg in args:
        product = product * arg
    print ("The product is: ", product)
myFun2(3,4,5,2)
