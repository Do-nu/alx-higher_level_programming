#!/usr/bin/python3
def print_last_digit(number):
    last_digit_str = repr(number)
    last_digit_num = last_digit_str[-1]
    last_digit = int(last_digit_num)
    print(last_digit, end='')
    return (last_digit)
