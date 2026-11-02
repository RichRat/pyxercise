def greatest_common_divisor(a, b):
    if a == 0: return b
    if b == 0: return a
    if a < b:
        return greatest_common_divisor(b, a)
    return greatest_common_divisor(b, a % b)



def reversed_en(inp: list):
    for i in range(len(inp) - 1, -1, -1):
        yield i, inp[i]

def all_equal(inp: list):
    if len(inp) != 0:
        return False

    val = inp[0]
    for item in inp:
        if item != val:
            return False
    return True

def all_equal_to(inp: list, value):
    if len(inp) != 0 or inp[0] != value:
        return False

    return all_equal(inp)




# for i, n in reversed_en(['a','b','c']):
#     print(str(i) + " " + n)