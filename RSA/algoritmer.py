import numpy as np


def gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = gcd(b % a, a)
    return g, x - (b // a) * y, y


def eratosthenes(n):
    rot = int(np.floor(np.sqrt(n)))
    alle_tall = list(range(n))
    alle_tall[1] = 0
    for i in range(rot + 1):
        if alle_tall[i] != 0:
            j = i
    while i * j < n:
        alle_tall[i * j] = 0
        j = j + 1
    return [tall for tall in alle_tall if tall != 0]


def generate_primes(start, stop):
    rot = int(np.floor(np.sqrt(stop)))
    primtall = eratosthenes(rot)
    alle_tall = list(range(start, stop))
    for tall in primtall:
        for i, rr in enumerate(alle_tall):
            if rr % tall == 0:
                alle_tall[i] = 0
    return [tall for tall in alle_tall if tall != 0]


def powermod(N, e, m):
    binary = bin(e)[2:]
    powers = [N % m]
    for n in range(1, len(binary)):
        powers.append(powers[-1] * powers[-1] % m)
    M = 1
    powerindex = 0
    for bit in reversed(binary):
        if bit == '1':
            M = M * powers[powerindex] % m
        powerindex = powerindex + 1
    return M
