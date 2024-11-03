from mypackage import myModule

def test_top_n():
    """Make sure top_n works correctly."""
    assert myModule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], "Test case 1 failed: incorrect result"
    assert myModule.top_n([9, 3, 2, 6, 5, 3], 3) == [9, 6, 5], "Test case 2 failed: incorrect result"
    assert myModule.top_n([11, 3, 8, 7, 4], 3) == [11, 8, 7], "Test case 3 failed: incorrect result"
