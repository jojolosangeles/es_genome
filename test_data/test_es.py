# content of test_sample.py
def inc(x):
    return x + 1

def test_basic_pass():
    assert inc(3) == 4

def test_basic_fail():
    assert inc(3) == 5