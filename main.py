import sys
import random


def encode():
    seed = int(sys.argv[2])
    random.seed(seed)
    args = sys.argv[3:]
    args_str = " ".join(args)
    lst = list(args_str)

    for i, char in enumerate(args_str):
        lst[i] = chr(ord(char) + random.randint(-10, 10))

    args_str = "".join(lst)

    print(args_str)


def decode():
    seed = int(sys.argv[2])
    random.seed(seed)
    args = sys.argv[3:]
    args_str = " ".join(args)
    lst = list(args_str)

    for i, char in enumerate(args_str):
        lst[i] = chr(ord(char) - random.randint(-10, 10))

    args_str = "".join(lst)

    print(args_str)


if __name__ == "__main__":
    if sys.argv[1] == "encode":
        encode()
    else:
        decode()
