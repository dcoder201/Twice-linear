def dbl_linear(n):
	# your code
    u = [1]
    i, j = 0, 0
    while len(u) <= n:
        y = 2 * u[i] + 1
        z = 3 * u[j] + 1
        if y < z:
            u.append(y)
            i += 1
        elif y > z:
            u.append(z)
            j += 1
        else:
            i += 1
    return u[n]
  
  import codewars_test as test
from solution import dbl_linear

@test.describe("Twice linear")
def tests():
    def testing(actual, expected):
	    test.assert_equals(actual, expected)
    @test.it("basic tests")
    def basics():
        testing(dbl_linear(10), 22)
        testing(dbl_linear(20), 57)
        testing(dbl_linear(30), 91)
        testing(dbl_linear(50), 175)
        

