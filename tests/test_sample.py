import pytest
from src.sample import sum_of_list

# CONSTANTS
MY_LIST = [1,2,3]

def test_passing():
    assert sum_of_list(MY_LIST) == 6

def test_failing():
    assert sum_of_list(MY_LIST) == 7
