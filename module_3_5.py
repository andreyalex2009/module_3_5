def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    else:
        first = int(str_number[0])
        rest = int(str_number[1:])
        return first * get_multiplied_digits(rest)

result = get_multiplied_digits((40203))
print(result)
