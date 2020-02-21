"""The pycep format function library."""
# coding=utf-8


def strip_end_space(string_value: str):
    """Remove escape character from end of input string value and return."""
    while string_value[-1:] == " ":
        string_value = string_value[:-1]
    return string_value


def add_newline(input_item: str) -> str:
    return f"{input_item}\n"


def strip_unsafe_file_names(string_data: str) -> str:
    new_string = ""
    for character in string_data:
        if character != "/":
            new_string += character
        else:
            new_string += "-"
    return new_string


def format_table(dict_value):
    package_data = ""
    package_spacer = ""
    package_headers = ""
    for data_value, value in dict_value.items():
        if value and data_value != 'questions':
            package_data += f"{data_value} |"
            package_spacer += ":---------- |"
            package_headers += f"{value} |"

    package_data += f"\n{package_spacer}\n{package_headers}"
    return package_data


def h_one_format(heading_data):
    return f"# {add_newline(heading_data)}"