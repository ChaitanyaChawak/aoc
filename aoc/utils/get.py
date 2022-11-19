"""
fetch input data automatically
"""
import argparse
import subprocess


def main(args):
    day = args.day
    year = args.year
    user = args.user
    with open(args.cookie, 'r') as f:
        cookie = f.read().rstrip('\n')

    cls = f"curl 'https://adventofcode.com/{year}/day/{day}/input' -H 'Cookie: {cookie}'"
    print(f'calling : {cls}')

    out = subprocess.run(cls, shell=True, capture_output=True)
    print(out.stdout)

    # put the fetched data somewhere
    path_to_file = f'../{year}/data_{user}/d{day}.txt'
    print(path_to_file)

    cls_store = f'{out.stdout}'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('year', type=int, default=2021)
    parser.add_argument('cookie', type=str) # path to cookie
    parser.add_argument('user', type=str) # either av or cc
    args = parser.parse_args()
    print(args.day, args.year, args.cookie, args.user)
    main(args)
