import itertools
import sys
from echo import split_args

flags, args = split_args(sys.argv[1:])

if not args:
    args.append('/dev/stdin')

for line_number, line in enumerate(itertools.chain.from_iterable(map(open, args))):
    if '-n' in flags:
        print(f"{line_number}\t{line}", sep='')
    else:
        print(line, sep='')
