from typing import Union


# task 1
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        powered = 1.0
    elif exp == 1:
        powered = x
    else:
        powered = x * (to_power(x, exp - 1))
    return powered


# task 2
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) - 2 * index <= 1:
        return True
    if looking_str[index] == looking_str[-(index + 1)]:
        return is_palindrome(looking_str, index + 1)
    return False


# task 3
def mult(a: int, n: int) -> int:
    try:
        if n == 0:
            return 0
        elif n == 1:
            return a
        else:
            return a + mult(a, n - 1)
    except TypeError:
        print('a, n should be digits')


# task 4
def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    else:
        res = reverse(input_str[1:]) + input_str[0]
        return res


# task 5
def sum_of_digits(digit_string: str) -> int:
    ind = 0
    summa = 0
    try:
        if len(digit_string) <= 1:
            return int(digit_string)
        if len(digit_string) > 1:
            summa = int(digit_string[ind]) + sum_of_digits(digit_string[(ind + 1):])
            ind += 1
        return summa
    except ValueError:
        print('string should contains digits')
