# EULER 1
import itertools
import math
import time
import re

from resources.constants import euler13_big_num_array, euler67_huge_triangle
from util.primes import Primes


def euler01():
    limit = 1000
    res = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            res += n

    print(res)


def euler02():
    # euler 2
    class Fib:
        buff = [0, 1]
        def next_num(self):
            ret = sum(self.buff)
            self.buff.pop(0)
            self.buff.append(ret)
            return ret

    limit = 4000000
    fib = Fib()
    val = 0
    res_sum = 0
    while True:
        val = fib.next_num()
        if val > limit:
            break

        #print(val)
        if val % 2 == 0:
            res_sum += val

    print("result e2: " + str(res_sum))


def euler03():
    def reduce_num(n, prime):
        # divide number by prime factor as long as possible
        f = 0
        while n % prime == 0:
            n = int(n / prime)
            f += 1
        
        print(str(prime) + " ( " + str(f) + " )")
        return n
    
    p_util = Primes()
    number =  600851475143 #13195
    max_p = 0
    while number > 1:
        for p in p_util.generate_primes(number, start_from=max_p + 1):
            if number % p == 0:
                max_p = p
                number = reduce_num(number, p)
                break



    print("result " + str(max_p))


def euler04():

    def check_palin(n):
        s = str(n)
        return s == s[::-1]

    limit = 1000
    res = 0
    for a in range(1, limit):
        for b in range(1, limit):
            if check_palin(a * b) and a * b > res:
                res = a * b
                print(res)

    print("result " + str(res))


def euler05():
    p_util = Primes()

    number = 1
    limit = 20
    num_dict = {}
    for n in range(2, 21):
        fact = p_util.prime_factorisation_obj(n)
        for k in fact:
            if k not in num_dict or num_dict[k] < fact[k]:
                num_dict[k] = fact[k]

    for k in num_dict:
        number *= math.pow(k, num_dict[k])

    print("result " + str(number))


def euler06(limit):
    #limit = 100
    print('result' + str(math.pow(sum([n for n in range(1, limit + 1)]), 2) - sum([n*n for n in range(1, limit + 1)])))


def euler50():
    p_util = Primes()
    p_util.max_lookup_size = 50000
    limit = 1000000
    max_len = 0
    result = 0
    primes = []

    def nex_prime(num=1):
        while True:
            num += 1
            if p_util.is_prime(num):
                primes.append(num)
                return num

    nex_prime()
    for _ in range(1, 100):
        nex_prime(primes[-1])

    cont_sum = 0
    start = 0
    while True:
        val = 0
        for end in range(max_len, len(primes)):
            val = sum(primes[start:end])
            if p_util.is_prime(val) and end - start > max_len:
                result = val
                max_len = end - start
                print("hit " + str(val) + " mlen  " + str(max_len) + " " + str(primes[start:end]))

        if val < limit:
            nex_prime(primes[-1])
        elif val > limit:
            start += 1

        if start > 100:
            break


    print("result " + str(result))


def euler59():



    with open('resources/euler/1000-most-common-words.txt') as word_file:
        words = [char for char in word_file.read().split('\n')]

    with open('resources/euler/0059_cipher.txt', 'r') as secret_file:
        data = [ int(char) for char in secret_file.read().split(',')]

    def decrypt(key):
        bin_key = [ ord(c) for c in key ]
        tmp_data = []
        for i in range(len(data)):
            tmp_data.append(data[i] ^ bin_key[i % len(bin_key)])

        return ''.join([chr(n) for n in tmp_data])

    def gen_key():
        char_range = range(ord('a') - 1, ord('z'))
        for c1 in char_range:
            for c2 in char_range:
                for c3 in char_range:
                    yield chr(c1) + chr(c2) + chr(c3)


    max_res = 0
    max_str = ""
    max_key = ""
    res = 0
    for k in gen_key():
        dec_str = decrypt(k)
        count = sum([ 1  for word in words if word in dec_str])
        if count > max_res:
            max_res = count
            max_str = dec_str
            max_key = k
            res = sum([ ord(c) for c in dec_str])
            print(str(max_res) + " " + k + " str: " + dec_str)

    print("result " + str(res))


def euler07():
    p_util = Primes()
    def nex_prime(num=1):
        while True:
            num += 1
            if p_util.is_prime(num):
                return num

    target = 10001
    result = 1
    for i in range(0, target):
        result = nex_prime(result)

    print("result " + str(result))


def euler60():
    p_util = Primes()
    p_util.max_lookup_size *= 10
    def util_check(a, b):
        return p_util.is_prime(int(str(a) + str(b)))

    def check(a, b):
        return util_check(a, b) and util_check(b, a)

    limit = 1000
    set_len = 4
    print("gen primes")
    primes = [ p for p in p_util.generate_primes(2000) ]
    groups = []
    print("find pairs")
    for p1 in primes:
        for p2 in [ n for n in primes if n > p1]:
            if check(p1, p2):
                groups.append([p1, p2])
                #print(groups[-1])

    print("extend pairs")
    for i in range(set_len - 2):
        for group_a in groups:
            for group in groups:
                if group_a == group:
                    continue
                prime = "todo"
                add = True
                for p in group:
                    if not check(p, prime):
                        add = False
                        break

                if add:
                    group.append(prime)
                    print(group)

        groups = [ g for g in groups if len(g) > i + 2]


    min_group = None
    min_val = None
    for group in groups:
        val = sum(group)
        if min_val is None or val < min_val:
            min_val = val
            min_group = group

    print("result " + str(min_val) + "  " + str(min_group))

def euler08():
    span_len = 13
    num = """
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450"""
    num = re.sub(r"\s|\n", "", num)
    print(num)
    numbers = [ int(c) for c in num ]

    max_prod = 0
    max_span = [0]
    for i in range(span_len, len(numbers) -1):
        span = numbers[i: i + span_len]
        val = math.prod(span)
        if val > max_prod:
            max_span = span
            max_prod = val

    print("result " + str(max_prod) + "  " + str(max_span))


def euler09():
    limit = 1000
    for a in range(1,limit):
        for b in range(a + 1, limit):
            c = limit - a - b
            if c < b:
                break

            if a * a + b * b == c * c:
                print("result " + str(a * b * c) +   " abc " + str(a) + " " + str(b) + " " + str(c) + " ")


def euler10():
    p_util = Primes()
    result = sum(p_util.sieve(2000000))


    print("result " + str(result))

# not finished TODO understand the math
def euler12():
    p_util = Primes()
    p_util.lookup = p_util.sieve(2000000)
    def gen_triangle(_limit):
        n = 0
        for i in range(1, _limit):
            if i % 1000 == 0: print(str(i) + " thinking ... " )
            n += i
            yield n

    def count_factors(num):
        ret = 0
        for f in range(1, num + 1):
            if num % f == 0:
                ret += 1

        return ret


    limit = 500

    max_facts_len = 0
    max_num = 0
    for n in gen_triangle(100000):
        len_factors = count_factors(n)
        if len_factors > max_facts_len:
            max_facts_len = len_factors
            max_num = n
            print(str(n) + " " + str(max_facts_len))
            if max_facts_len > limit:
                print("result " + str(n))
                break


def euler13():
    result = 0
    mask = math.pow(10, 40)
    for n in euler13_big_num_array:
        result += n
    rs = str(result)
    print("result " + rs[:10])


def euler14():
    def collatz(n):
        return n / 2 if n % 2 == 0 else 3 * n + 1

    limit = 1000000
    max_len = 0
    max_num = 0
    for n in range(1, limit):
        num = n
        c = 0
        while n > 1:
            c += 1
            n = collatz(n)

        if c > max_len:
            max_len = c
            max_num = num
            print("nex max " + str(num) + " len: " + str(c))

    print("result " + str(max_num))


def euler15():

    lattice_size = 20
    size = lattice_size + 1
    grid = [ [0] * size for _ in range(size) ]

    grid[0][0] = 1
    for x in range(size):
        for y in range(size):
            if x + 1 < size:
                grid[x + 1][y] += grid[x][y]
            if y + 1 < size:
                grid[x][y + 1] += grid[x][y]

    print("result " + str(grid[lattice_size][lattice_size]))

def euler16():
    pow = 1000
    num = int(1)
    for _ in range(pow):
        num *= 2

    print(num)
    print(sum([ int(c) for c in str(num) ]))


# euler 67 is the same as 18 with a bigger triangle but the algo is identical
# and easier since only one iteration of the array is required isntad of O(n^2) paths
def euler18_67():
    triangle = euler67_huge_triangle
    for y, row in reversed(list(enumerate(triangle[:-1]))):
        for x in range(len(row)):
            row[x] += max(triangle[y + 1][x], triangle[y + 1][x + 1])


    print("result " + str(triangle[0][0]))


def euler68():

    def rotate(l, n=1):
        return l[n:] + l[:n]

    n_gon = 5
    numbers = [ n + 1 for n in range(n_gon * 2)]

    matches = []
    result = 0

    # let's try brute forcing this by just testing all permutations
    for p_nums in list(itertools.permutations(numbers)):
        data = [[0 for x in range(3)] for y in range(n_gon)]
        i = 0
        for row in range(n_gon):
            for col in [0, 2]:
                data[row][col] = p_nums[i]
                if col == 2:
                    data[(row + 1) % n_gon][1] = p_nums[i]

                i += 1


        # check for solved criteria
        eval_dat = list(set([ sum(row) for row in data ]))
        if len(eval_dat) == 1:
            # rotate data till the smallest row is first
            min_val = min([row[0] for row in data])
            while data[0][0] != min_val:
                data = rotate(data)

            # get the number from the solution
            num = int("".join([ str(n) for row in data for n in row]))
            if num > result and math.log(num, 10) <= 16:
                result = num

            # print new matches not requried for the algo but makes the waiting more intersting
            if data not in matches:
                print(str(eval_dat) + " " + str(data))
                matches.append(data)

    print("result " + str(result))


def euler71():

    def gcd(a, b):
        if b == 0:
            return a

        return gcd(b, a % b)

    limit = 1000000
    max_frac = 3 / 7
    n = 2
    d = 5
    min_frac = n / d
    result = None
    while n < limit and d < limit:
        if n / d < max_frac:
            n += 1
        else:
            d += 1

        if min_frac < n / d < max_frac and gcd(n, d) == 1:
            min_frac = n / d
            result = (n, d)

    print("result " + str(result))


def euler81():

    with open('resources/euler/0081_matrix.txt') as matrix_file:
        lines = [char for char in matrix_file.read().split('\n')]

    matrix = []
    for line in lines:
        matrix.append([ int(c) for c in line.split(',') ])

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if x > 0 < y:
                matrix[y][x] += min(matrix[y - 1][x], matrix[y][x - 1])
            elif x == 0 < y:
                matrix[y][x] += matrix[y - 1][x]
            elif y == 0 < x:
                matrix[y][x] += matrix[y][x - 1]

    print("result " + str(matrix[-1][-1]))

def euler82():

    with open('resources/euler/0082_matrix.txt', 'r') as f:
        matrix = [[ int(c) for c in line.split(',') ] for line in f]

    size = len(matrix)
    nav_cost_matrix = [[0] * size for _ in range(size)]

    for x in range(size):
        for y in range(size):
            if x == 0:
                nav_cost_matrix[y][0] = matrix[y][0]
                continue
            elif x == size - 1:
                nav_cost_matrix[y][x] = nav_cost_matrix[y][x - 1] + matrix[y][x]
                continue

            nav_col = [row[x] for row in matrix]
            min_cost = 999999999999999999999
            for y_start in range(size):
                start, end = min(y, y_start), max(y, y_start)
                cost = nav_cost_matrix[y_start][x - 1] + sum(nav_col[start : end + 1])
                min_cost = min(min_cost, cost)

            nav_cost_matrix[y][x] = min_cost

    print("result " + str(min([ row[-1] for row in nav_cost_matrix ])))

def euler83():
    with open('resources/euler/0082_matrix.txt', 'r') as f:
        matrix = [[ int(c) for c in line.split(',') ] for line in f]


def euler85():
    def test_grid(width, height):
        ret = 0
        for x in range(1, width + 1):
            for y in range(1, height + 1):
                ret += (1 + width - x) * (1 + height - y)

        return ret

    limit = 2000000
    max_dimension = 100
    closest_dist = 9999
    res = 0
    for w in range(max_dimension):
        for h in range(max_dimension):
            r = test_grid(w, h)
            if abs(r - limit) < closest_dist:
                closest_dist = abs(r - limit)
                res = w * h
            elif r > limit * 1.1:
                break

    print("result " + str(res))


def euler87():
    limit = 50000000
    p_list = Primes().sieve(round(math.sqrt(limit)))
    numbers = set()
    for a in p_list:
        for b in p_list:
            if a**2 + b**3 > limit:
                break

            for c in p_list:
                n = a**2 + b**3 + c**4
                if n < limit:
                    numbers.add(n)
                else:
                    break

    print("result " + str(len(numbers)))


def euler108():
    # gen moves
    fields = [ n for n in range(1, 21) ] + [25]
    fact_map = ["!", "S", "D", "T"]

    solutions = []

    def throw(score, hist, darts=3):
        m_list = [1, 2, 3] if darts < 3 else [2]
        for f in fields:
            if f > score:
                break

            for m in m_list:
                new_score = score - f * m
                if new_score < 0 or (m > 2 and f == 25):
                    continue

                if new_score == 0:
                    solutions.append(hist + [fact_map[m] + str(f)])
                elif darts > 1:
                    throw(new_score, hist + [fact_map[m] + str(f)], darts - 1)

    result = 0
    for start_score in range(2, 100):
        throw(start_score, [])
        for i, s in enumerate(solutions):
            if len(s) > 2 and s[1] < s[2]:
                solutions[i] = [s[0], s[2], s[1]]

        solutions = set([ " ".join(reversed(s)) for s in solutions])
        result += len(solutions)
        solutions = []

    print("result " + str(result))



start_time = time.time()
euler108()
print("--- %s seconds ---" % (time.time() - start_time))