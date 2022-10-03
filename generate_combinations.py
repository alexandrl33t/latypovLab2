from itertools import product
import string


def bruteforce(charset):
    return (''.join(candidate)
            for candidate in product(charset, repeat=5))


with open("combindations.txt", mode='w') as file:
    combs = list(bruteforce(string.ascii_lowercase))
    file.write("\n".join(combs))
