from calci import add,sub,prod,div


def addition():
    assert(add(3,4)) == 7

def subtraction():
    assert(sub(6,4)) == 2

def multiply():
    assert(prod(3,6)) == 18

def divide():
    assert(div(8,2))  == 4
    assert(div(8,0)) == "ZeroDivisionError"
    
if __name__=='main':
    addition()
