from calci import add,sub,prod,div


def test_cases():
    assert(add(3,4)) == 7


    assert(sub(6,4)) == 2


    assert(prod(3,6)) == 18


    assert(div(8,2))  == 4
    assert(div(8,0)) == "ZeroDivisionError"
    

