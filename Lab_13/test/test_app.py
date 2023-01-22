from app import sortowanie_babelkowe
import pytest

testdata = [([1,0,6,2],[0,1,2,6]),([9,8,7,5,4,1],[1,4,5,7,8,9]),([-1,-4,-6,-2],[-6,-4,-2,-1])]
testdata_1 = [('antoni'),(4),({'key':4})]


@pytest.mark.parametrize('input_data, expected_data', testdata)
def test_babelkowe(input_data, expected_data):
    got = sortowanie_babelkowe(input_data)
    want = expected_data
    
    assert got == want

@pytest.mark.parametrize('input_data, expected_data', testdata)
def test_babelkowe_return_type(input_data, expected_data):
    got = type(sortowanie_babelkowe(input_data))
    want = list

    assert got == want

@pytest.mark.parametrize('input_data', testdata_1)
def test_babelkowe_input_type(input_data):
    got = sortowanie_babelkowe(input_data)
    want = None

    assert got == want