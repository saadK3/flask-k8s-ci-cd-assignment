from dummy_app import simple_add


def test_simple_add():
    """Tests the simple_add function"""
    assert simple_add(2, 3) == 5
    assert simple_add(-1, 1) == 0
    

