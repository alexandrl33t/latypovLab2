from itertools import chain, product
import string


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=5)
                                                 for i in range(1, maxlength + 1)))

with open("combindations.txt", mode='w') as file:
    combs = list(bruteforce(string.ascii_lowercase, 5))
    file.write("\n".join(combs))
