import pytest

@pytest.fixture
def input_value(): # fixture function.
    input = 39
    return input

@pytest.mark.divisible
def test_divisible_by_3(input_value): # The fixture funcion must be the input parameter.
    assert input_value % 3 == 0 # value returned by the fixture function is stored in the variable input_value.

@pytest.mark.divisible
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

# execute as, 
# pytest -m divisible -v


"""
### Notes ###
------------------------------------------------------------------------------------------------------------------------
A fixture function defined inside a test file has a scope within the test file only. 
We cannot use that fixture in another test file. 
To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py. 
conftest.py is explained in the next chapter.
"""
