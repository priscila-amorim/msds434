from hello import add


def test_add():
	assert 5 == add(2, 3), "add is not correctly defined"
