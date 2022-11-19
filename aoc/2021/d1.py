from aoc.utils import parse 
import numpy as np

data = parse.lines_to_ints('data_av/d1.txt')
data_test = parse.lines_to_ints('data_av/d1_test.txt')


def p1(data):
    diff = np.diff(data)
    # number of increases
    return np.sum(diff > 0)

def p2(data):
    # summing in a sliding window : convolution?
    slide = np.convolve(data, np.ones(3, dtype=int), 'valid')
    # print(f'sliding window with summing 3 at a time : {slide}')

    # now comput diff on this slid thing
    diff = np.diff(slide)
    return np.sum(diff > 0)


if __name__ == "__main__":
    a1 = p1(data)
    a2 = p2(data)
    print(a1, a2)
    
