"""
parse input data in common formats

for more complicated data formats just treat it as a part of the challenge
"""

from typing import List


def lines_to_str(fname:str) -> str:
    """ base function : convert input to string (separated by \n) """
    # rstrip removes the last \n
    with open(fname) as f:
        return f.read().rstrip('\n')

def lines_to_list(fname:str) -> List[str]:
    """return input as a list of strings, with each line as element of list"""
    return lines_to_str(fname).split('\n')

def lines_to_ints(fname:str) -> List[int]:
    """ return input as list of ints """
    out = lines_to_list(fname)
    return [int(i) for i in out]
    