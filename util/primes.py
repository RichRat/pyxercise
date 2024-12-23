from unicodedata import lookup


class Primes:

    max_lookup_size = 1000

    def generate_primes(self,max_n, start_from = 1):
        for n in range(start_from, max_n + 1):
            if n % 100000 == 0:
                print("thinking" + str(n))

            if self.is_prime(n):
                yield n

    lookup = [2]
    def is_prime(self, n):
        if n == 1: return False
        if n == 2 or n in self.lookup: return True

        for p in self.lookup:
            if n % p == 0:
                return False

        for tn in range(self.lookup[-1] + 1, n):
            if n % tn == 0:
                return False

        if len(self.lookup) < self.max_lookup_size:
            self.lookup.append(n)

        return True

    def prime_factorisation(self, number):
        ret = []
        for p in self.generate_primes(number):
            while number % p == 0:
                number /= p
                ret.append(p)

            if p > number:
                break

        return ret

    def prime_factorisation_obj(self, number):
        ret = {}
        for n in self.prime_factorisation(number):
            if n in ret:
                ret[n] += 1
            else:
                ret[n] = 1

        return ret

    def next_prime(self, number=1):
        while True:
            number += 1
            if self.is_prime(number):
                return number

    # damn this is so fast
    def sieve(self, limit):
        na = [ True ] * limit

        for i in range(2, limit):
            if na[i]:
                num = i + i
                while num < limit:
                    na[num] = False
                    num += i

        return [ i for i in range(len(na)) if na[i] and i > 1 ]

