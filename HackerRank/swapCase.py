def swap_case(s):
    result = ''
    for i in s:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result

