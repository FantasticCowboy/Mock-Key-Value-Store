from src.circular_array import SortedCircularArray


def test_simple():
    arr = SortedCircularArray()
    arr.insert(1)
    assert arr.get_upper_bound(101) == 1    
    assert arr.get_upper_bound(1) == 1    
    arr.insert(100)
    assert arr.get_upper_bound(100) == 1
    assert arr.get_upper_bound(99) == 100
    assert arr.get_upper_bound(1) == 100
    arr.insert(50)
    assert arr.get_upper_bound(2) == 50
    