# if test is correct no output on the REPL

# if incorrect, this will fail with an AssertionError and
# the message "Should be 6".


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_tuple():
    assert sum((2, 2, 2)) == 6, "Should be 6"


# The statement if __name__ == "__main__" is used to check
# whether the current Python module is being run as the main
# program or if it is being imported as a module into another
# program.

# If this module is imported into another program the function in this file
# will be available for use, but the code within the if __name__ == "__main__"
# block will not be executed
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
