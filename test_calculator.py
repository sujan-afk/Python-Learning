from calculator import square

num = [-1,-3,-6,0,1,2,4,9]
def test_square():
    for test in num:
          assert square(test) == pow(test,2)