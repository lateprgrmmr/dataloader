import argparse

import os
import sys

my_parser = argparse.ArgumentParser(description='List the contents of a folder')

my_parser.add_argument('Path', metavar='path', type=str, help='the path to the list')
my_parser.add_argument('-l', '--long', action='store_true', help='enable the long listing format')

args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d %s' % (size, line)
    print(line)

