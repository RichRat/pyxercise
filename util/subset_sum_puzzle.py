from util.timing import timed_run


# https://www.youtube.com/shorts/4h5BEALuh44
# yea turns out choosing ten numbers below 100 that don't have two subsets with identical sums is not possible
# but there is the code regardless

number_range = 100
target_size = 7

def solve():
    for n in range(1, number_range - target_size + 1):
        recurse(n, [])


def recurse(n, arr):
    if len(arr) == target_size:
        print("we got a winner")
        print(arr)
        return True

    if do_check_eff(arr + [n]):
        return False

    arr += [ n ]
    for num in range(n + 1, number_range - target_size + len(arr) + 1):
        if recurse(num, arr):
            return True

    return False

# returns true if array contains same sum subsets
def do_check_eff(arr):
    if len(arr) < 2:
        return False

    for pick_n in range(2, len(arr)):
        if do_check(arr, 0, pick_n,[],[]):
            return True

    return False

solutions = []

# returns true if array contains same sum subsets
def do_check(arr, i, pick_n, set1, set2):
    if len(set1) + len(set2) == pick_n:
        #print(str(set1) + " " + str(set2))
        return sum(set1) == sum(set2)

    if len(set1) < pick_n - 1 and do_check(arr, i + 1, pick_n, set1 + [arr[i]], set2):
        return True
    if len(set2) < pick_n - 1 and do_check(arr, i + 1, pick_n, set1, set2 + [arr[i]]):
        return True
    if i < len(arr) - pick_n + len(set1) + len(set2) and do_check(arr, i + 1, pick_n, set1, set2):
        return True

    return False


#print(do_check_eff([2, 3, 4, 5]))
timed_run(solve)