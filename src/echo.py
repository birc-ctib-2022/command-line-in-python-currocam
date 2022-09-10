from ast import arg
import sys


def split_args(args: list[str]) -> tuple[list[str], list[str]]:
    """
    Split argv and return the flags separated from the rest.

    >>> split_args(['-n', 'foo', 'bar'])
    (['-n'], ['foo', 'bar'])
    >>> split_args(['-n', 'foo', '-s', 'bar'])
    (['-n', '-s'], ['foo', 'bar'])
    """
    flags, rest = [], []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            rest.append(arg)
    return flags, rest


def check_flags(flags: list[str]) -> tuple[list[str], list[str]]:
    if '-n' in flags:
        end = ""
    else:
        end = "\n"
    if '-n' in flags:
        sep = ""
    else:
        sep = " "
    return end, sep


def main():
    flags, args = split_args(sys.argv[1:])
    end, sep = check_flags(flags)
    print(sep.join(args), end=end)


if __name__ == '__main__':
    main()
