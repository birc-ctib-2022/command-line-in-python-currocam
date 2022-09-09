import itertools
import sys
from echo import split_args

flags, args = split_args(sys.argv[1:])

if not args:
    args.append('/dev/stdin')

files_opener = map(open, args)
for line_number, line in enumerate(itertools.chain.from_iterable(files_opener)):
    if '-n' in flags:
        print(f"{line_number}\t{line}", end='')
    else:
        print(line, sep='')
