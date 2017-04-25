from Rover import location

""" This modules provides tests for Rover functionality"""

# Test 1: check the correctness of the result.
input = list(["6 7", "3 1 W", "MMMLLMRM"])
expected = "1 0 S"
test_out = location(input[0], input[1], input[2])
if test_out == expected:
    print("Test 1: pass")
else:
    print("Test 2: fail")

# Test 2: check error outside the zone.
input = list(["4 4", "1 1 W", "MMMM"])
try:
    test_out = location(input[0], input[1], input[2])
    print("Test 2: fail")
except ValueError:
    print("Test 2: pass")


# Test 3: check incorrect zone dimension command.
input = list(["4 ", "1 1 N", "MML"])
try:
    test_out = location(input[0], input[1], input[2])
    print("Test 3: fail")
except ValueError:
    print("Test 3: pass")


# Test 4: check incorrect starting position command.
input = list(["4 4", "1 1  E", "MMLM"])
try:
    test_out = location(input[0], input[1], input[2])
    print("Test 4: fail")
except ValueError:
    print("Test 4: pass")




# Test 5: check incorrect movement and rotation sequence command.
input = list(["4 4", "1 1 E", "0MRMRRMMLM"])
try:
    test_out = location(input[0], input[1], input[2])
    print("Test 5: fail")
except ValueError:
    print("Test 5: pass")
