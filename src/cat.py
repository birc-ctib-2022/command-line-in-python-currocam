import sys
from echo import split_args

flags, args = split_args(sys.argv[1:])

if not args:
    args.append('/dev/stdin')

for arg in args:
    with open(arg) as f:
        for line_number, line in enumerate(f):
            if '-n' in flags:
                print(f"{line_number}\t{line}", sep='')
            else:
                print(line, sep='')
