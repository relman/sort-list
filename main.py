import sys


def sort_list(s):
    """
    Returns sorted list.
    :param s: list of words and numbers
    """
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if compare(s[i], s[j]):
                s[i], s[j] = s[j], s[i]
    return s


def compare(x, y):
    """
    Returns 1 when x is greater than y.
    :param x: string representation of word or number
    :param y: string representation of word or number
    """
    if x.isalpha() != y.isalpha():
        return 0
    if not x.isalpha():
        return 1 if int(x) > int(y) else 0
    return 1 if x > y else 0


if __name__ == '__main__':
    print sort_list(sys.argv[1:])
