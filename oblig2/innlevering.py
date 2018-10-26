import RSA as rsa
import regression as reg
import pca as pca
import numpy as np


def finn_p_q(prime_list, n):
    for num in prime_list:
        if n % num == 0:
            p = num
            return p, n / p
    return 0, 0


# metode som gjør tekst tall til tekst

alf = 'abcdefghijklmnopqrstuvwxyz'


def tallTilTekst(tall, max):
    # print(tall)
    if max == 0:
        return ""
    bokstav = tall % 100
    if bokstav == 99:
        return tallTilTekst(tall // 100, max - 1) + " "
    else:
        return tallTilTekst(tall // 100, max - 1) + alf[bokstav]


# --- Oppgave 1 RSA ---
print("------ START OPPGAVE 1 ------\n")

n = 160169311
e = 1737

# a)  [1041706, 4139999]
# Svar: BERGEN

# b) HEI SJEF
# Svar: [9061099, 20110607]

# c) Krypter HEI SJEF
print("HEI SJEF kryptert:", rsa.RSA_encrypt(n, e, [9061099, 20110607]))
# Svar: [79369226, 69649354]

U = [112718817, 85128008, 148479246, 91503316, 26066602, 95584344, 142943071]

# d) Finn primtallene p og q slik at n = pq.
sqrt_n = int(np.floor(np.sqrt(n)))
primtall = rsa.generate_primes(2, sqrt_n)
p, q = finn_p_q(primtall, n)
print("p = ", p, ", q = ", q)

# e) Hva må til for at (n, e) skal være en korrekt valgt nøkkel for RSA? Sjekk dette
# for den oppgitte nøkkelen (n, e).

# Svar: (p - 1) * (q -1) = phi. n må da være gdc for phi og e
print("svar oppgave 1e: ", rsa.check_key(p, q, e))

# f) Regn ut dekrypteringsnøkkelen (n, d). Kontroller svaret ved å dekryptere re-
# sultatet fra deloppgave c).

phi = (p - 1) * (q - 1)

d = int(rsa.mult_inverse(e, phi))

c_dekryptert = []

for code in [79369226, 69649354]:
    c_dekryptert.append(rsa.powermod(code, d, n))

print("svar oppgave 1f", c_dekryptert)

# g) Dekrypter og dekod den hemmelige beskjeden U .

u_dekryptert = []

for code in U:
    u_dekryptert.append(rsa.powermod(code, d, n))

print("svar oppgave 1g, U dekryptert:", "".join([tallTilTekst(tall, 4) for tall in u_dekryptert]))
print("\n------ SLUTT OPPGAVE 1 ------")

