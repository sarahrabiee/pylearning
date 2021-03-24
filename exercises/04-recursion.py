import sys


def sum_up_to(num):
    if num == 1:
        return num
    else:
        return num + sum_up_to(num - 1)


if __name__ == '__main__':
    print(sum_up_to(10))