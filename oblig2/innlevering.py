import RSA as rsa
import regression as reg
import pca as pca
import numpy as np
import matplotlib.pyplot as plt
import pylab


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

# ----- OPPGAVE 2 -----

print("\n\n----- OPPGAVE 2 -----")

# a)

T = [13.14, 12.89, 12.26, 12.64, 12.22, 12.47, 12.51, 12.80, 12.24, 12.77, 13.35,
     12.82, 13.57, 13.38, 14.41, 14.00, 15.68, 15.41, 15.51, 15.86, 15.72]

X = []
for i in range(0, 62, 3):
    X.append(i)

plt.scatter(X, T)

# Svar: plottet viser at temperaturen er på vei ned, før den snur og stiger igjen
# vi ser den sikkert snu når ovnen ble skrudd på. Dataene ser ut til å passe plottet

# b)
[a, b] = reg.linearRegression(X, T)
# plt.figure(0)

# xplot = np.array(list(range(-1,6))) # litt større område enn x-ene
yplot = np.dot(a, X) + b
plot_lin = plt.plot(X, yplot, label="Linear")

Sy2 = sum((T - np.mean(T)) ** 2)
SSELin = sum((T - np.dot(a, X) - b) ** 2)
r2Linear = (Sy2 - SSELin) / Sy2
print("\n2b)\nr² = ", r2Linear)

# c)

# Kvadratisk tilnærming:
[a, b, c] = reg.quadraticRegression(X, T)  # så kvadratisk
yplot = np.dot(a, np.power(X, 2)) + np.dot(b, X) + c
plot_qua = plt.plot(X, yplot, label="Quadratic")
SSEQuad = sum((T - (np.dot(a, np.power(X, 2)) + np.dot(b, X) + c)) ** 2)
r2Quadratic = (Sy2 - SSEQuad) / Sy2

print("\nc)\nKvadratisk tilnærming r² = ", r2Quadratic)

# Kubisk tilnærming:
[a, b, c, d] = reg.cubicRegression(X, T)
yplot = np.dot(a, np.power(X, 3)) + np.dot(b, np.power(X, 2)) + np.dot(c, X) + d
plot_cubic = plt.plot(X, yplot, label="Cubic")
SSECubic = sum((T - (np.dot(a, np.power(X, 3)) + np.dot(b, np.power(X, 2)) + np.dot(c, X) + d)) ** 2)
r2Cubic = (Sy2 - SSECubic) / Sy2

print("\nKubisk tilnærming r² = ", r2Cubic)

# Svar oppgave 2d:
# Vi kan se ved grafen at den kubiske ser ut til å passe situasjonen best. Dette stemmer også med
# determinasjonskoeffisienten som også er høyest for kubisk.

plt.legend()
plt.show()

print("\n\n ----- SLUTT OPPGAVE 2 -----")

print("\n\n ----- OPPGAVE 3 -----")

# Fylker (alfabetisk, tallene under står i den samme rekkefølgen):
Fylker = ['Akershus', 'Aust-Agder', 'Buskerud', 'Finnmark', 'Hedmark', 'Hordaland', 'Møre og Romsdal', 'Nordland',
          'Nord-Trøndelag', 'Oppland', 'Oslo', 'Rogaland', 'Sogn og Fjordane', 'Sør-Trøndelag', 'Telemark', 'Troms',
          'Vest-Agder', 'Vestfold', 'Østfold']
Indikatorer = ['Areal', 'Folketall', 'BNP/kapita', 'BNP/sysselsatt', 'Sysselsatte']
# Areal målt i kvadratkilometer
Areal = [4917.95, 9155.36, 14912.19, 48631.38, 27397.85, 15436.98, 15101.07, 38478.13, 22414, 25192.09, 454.10, 9376.77,
         18622.44, 18848, 15298.23, 25876.85, 7278.71, 2225.38, 4187.22]
# Folketall 1/1 2017
Folketall = [604368, 116673, 279714, 76149, 196190, 519963, 266274, 242866, 137233, 189479, 666759, 472024, 110266,
             317363, 173307, 165632, 184116, 247048, 292893, ]
# BNP og sysselsatte: Tall fra 2017
BNPKap = [435982, 337974, 397080, 438594, 364944, 488515, 433030, 428402, 367157, 363111, 820117, 488463, 455872,
          473954, 371886, 451887, 403893, 364007, 331575]
BNPSyss = [918710, 771973, 831298, 808765, 777248, 922939, 834642, 850163, 759414, 731136, 1125019, 899272, 846111,
           886057, 817060, 824648, 811833, 792748, 778412]
Sysselsatte = [270338, 47868, 125938, 37143, 86627, 254290, 127060, 116020, 62621, 86968, 468375, 233986, 54490, 166479,
               74749, 84537, 86997, 106931, 118320]

X = np.transpose(np.array([Areal, Folketall, BNPKap, BNPSyss, Sysselsatte]))

X = pca.meanCenter(X)
X = pca.standardize(X)

print("Oppgave 3a, prossesert X = \n", X)

# b)

[T,P,E] = pca.pca(X, a=2)

print("\nOppgave 3b, T =\n", T)
print("\nP =\n", P)

# c)

# plotter skåreplot med fylkenavn
plt.figure(1)
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(Fylker, T[:, 0], T[:, 1]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
plt.show()

# plotter ladningsplot med indikatorer
plt.figure(2)
plt.scatter(P[:, 0], P[:, 1])
for label, x, y in zip(Indikatorer, P[:, 0], P[:, 1]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
plt.show()

# plotter begge to samlet i et biplot

plt.figure(3)
ax = pylab.subplot(111)
ax.scatter(T[:,0],T[:,1])
ax.scatter(5*P[:,0],5*P[:,1])
ax.figure.show()

# d) Hvilke to fylker er likest?
# svar: Ved å se på skåreplottet ser det ut som Oppland og Nord-Trøndelag er likest

# e) Hvilket fylke skiller seg fra de andre?
# svar: Olso

# f) Hvilket fylke skiller seg mest grunnet areal?
# svar Oslo skiller seg mest ut, deretter kommer Finnmark og Nordland.


# g) Svar: Antall sysselsatte er den faktoren som er likest mellom fylkene.



