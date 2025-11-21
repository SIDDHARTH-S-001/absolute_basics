import pytest

def test_div_by_3(input_value):
    print("I/P: ", input_value)
    assert input_value % 3 == 0

# execute as, 
# pytest test_conftest.py -v -s 
# -v for verbose (detailed output)
# -s for print statements (if -s flag is not specified, pytest automatically ignores -s).