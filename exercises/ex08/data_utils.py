"""EX08 - Data_Utils."""

__author__ = "730557985"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table under a certain header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str,list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Creates table with n rows."""
    result: dict[str, list[str]] = {}
    for key in table:
        idx: int = 0
        n_list: list[str] = []
        if len(table[key]) < n:
            n = len(table[key])
        while idx < n:
            n_list.append(table[key][idx])
            idx += 1
        result[key] = n_list
    return result

def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce column-based table with a certain subset of original columns."""
    result: dict[str, list[str]] = {}
    for item in col_names:
        result[item] = table[item]
    return result

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table with two combined tables."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result

def count(vals_list: list[str]) -> dict[str, int]:
    """Counts the number of values in the list in a dictionary format."""
    result: dict[str, int] = {}
    for item in vals_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result