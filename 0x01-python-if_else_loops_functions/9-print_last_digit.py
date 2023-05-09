def print_last_digit(number):
    if number >= 0:
        ld = number % 10
    elif number < 0:
        ld = -number % 10
    print("{:d}".format(ld), end="")
    return ld
