from hello import hello


def test_hello():
    assert hello() == 'Hello world! Hi!'
    assert hello('') == 'Hello! Hi!'
    assert hello('Martians') == 'Hello Martians! Hi!'
