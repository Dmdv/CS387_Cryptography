__author__ = 'dmitrijdackov'

def convert_to_bits(n, pad):
    result = []
    while n > 0:
        if n % 2 == 0:
            result = [0] + result
        else:
            result = [1] + result
        n = int(n / 2)
    while len(result) < pad:
        result = [0] + result
    return result

def string_to_bits(s):
    result =[]
    for c in s:
        result = convert_to_bits(ord(c), 7) + result
    return result

print (convert_to_bits(66, 7))