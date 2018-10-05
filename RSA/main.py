import algoritmer as algo
import numpy as np


def test_enc_dec():
    # public key pair
    n = 653859799
    e = 235
    # message table
    T1 = [00, 19, 19, 00]
    T2 = [0o02, 10, 27, 18]
    T3 = [14, 20, 19, 0o07]
    TT = [T1, T2, T3]
    # secret key
    d = 267077827

    enc = [[]]
    plass = 0
    arr = 0
    for liste in TT:
        for tall in liste:
            enc[arr][plass] = algo.powermod(tall, e, n)
            plass += 1
        plass = 0
        arr += 1

    for l in enc:
        for t in l:
            print(t, " ")


def find_primes(start, stop):
    print(algo.generate_primes(start, stop))


def oppg_a():
    word = "dead"
    code_word = 3040003

    # public key
    n = 115912873
    e = 133

    return algo.powermod(code_word, e, n)


def oppg_b(n):
    sqrt_n = int(np.floor(np.sqrt(n)))
    return algo.generate_primes(2, sqrt_n)


def oppg_c(prime_list, n):
    for num in prime_list:
        if n % num == 0:
            p = num
            return p, n / p
    return 0, 0


def main():
    n = 115912873
    e = 133
    prime_list = oppg_b(n)

    p, q = oppg_c(prime_list, n)

    phi = (p - 1) * (q - 1)

    g, x, y = algo.gcd(phi, e)
    d = int(y)
    print(d)

    dead_enc = oppg_a()
    dead_dec = algo.powermod(dead_enc, d, n)
    print("dead encrypted is ", dead_enc)
    print("dead decrypted again is ", dead_dec)

    real_code = [88709091, 115282881, 44754833, 5274204, 37162740, 69569552, 73765472]
    real_decrypt = []

    for code in real_code:
        real_decrypt.append(algo.powermod(code, d, n))

    print("Real decrypt: ", real_decrypt)
    print("".join([tallTilTekst(tall, 4) for tall in real_decrypt]))


alf = 'abcdefghijklmnopqrstuvwxyz'


def tallTilTekst(tall, max):
    if max == 0:
        return ""
    bokstav = tall % 100
    if bokstav == 99:
        return tallTilTekst(tall // 100, max - 1) + " "
    else:
        return tallTilTekst(tall // 100, max - 1) + alf[bokstav]


if __name__ == '__main__':
    main()
