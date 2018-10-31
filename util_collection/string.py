
def split_by_cleaning(value, split_by_char=','):
    """
    The method returns elements from a string value by deleting extra spaces
    :param value: A string value
    :param split_by_char: A character in the value to split
    :return: list of split elements
    """
    elements = value.strip().strip(split_by_char).split(split_by_char)
    return [element.strip() for element in elements if element.strip()]
