from hy.lex.tokenize import tokenize


def test_list_lex():
    """test basic lexing of lists"""
    fn = tokenize("(fn [1 2 3 4])")[0]
    assert fn == [
        "fn", ["1", "2", "3", "4"]
    ]


def test_list_recurse():
    """ test we can recurse lists """
    fn = tokenize("(fn [1 2 3 4 [5 6 7]])")[0]
    assert fn == [
        "fn", ["1", "2", "3", "4", ["5", "6", "7"]]
    ]


def test_double_rainbow():
    """ DOUBLE LISTS """
    fn = tokenize("(fn [1 2 3 4] [5 6 7])")[0]
    assert fn == [
        "fn", ["1", "2", "3", "4"], ["5", "6", "7"]
    ]
