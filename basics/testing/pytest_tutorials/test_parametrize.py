import pytest

@pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 35), (4, 44), (5, 55)])
def test_multiplication(num, output):
    assert 11*num == output

# execute as
# pytest test_parametrize.py -v

"""
### Notes
-----------------------------------------
Check for the syntax clearly, args for the function which are loaded into the parametrize marking are within a single set of "".
"""