import pytest

from util_collection.string import split_by_cleaning


@pytest.mark.parametrize(
    "str_value, expected_list",
    [
        (" ,", []),
        ("800-533-2923 , , ", ['800-533-2923']),
        (", (508) 872-7878 , (508) 405-9158", ['(508) 872-7878', '(508) 405-9158']),
        ("   Hi! , Sean, how are , you.    ", ['Hi!', 'Sean', 'how are', 'you.']),
    ],
)
def test_split_by_cleaning(str_value, expected_list):
    assert split_by_cleaning(str_value) == expected_list
