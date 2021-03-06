

def oppgave1():

    for i in range(1, 26):
        print(ceaser("xcy", i))

def oppgave2():

    for i in range(1,26):
        decrypt = ceaser("uibpmuibqkaqauwzmncvbpivxzwoziuuqvo", i)
        if findNumE(decrypt) > 1:
            print(decrypt)


def ceaser(crypt, key):
    decrypt=""
    for char in crypt:
        if(ord(char) >= ord("a") and ord(char) <= ord("z")):
            num = (ord(char) - ord("a") + key)%26
            num = num + ord("a")
            decrypt = decrypt + chr(num)
        else:
            decrypt = decrypt + char


    return decrypt

def findNumE(string):
    return string.count("e")

def compareFreq(compared):
    ref = frequency("test1")
    freqCompared = frequency(compared)

    return chiSquare(ref, freqCompared)

def chiSquare(ref, compare):
    chiSum = 0

    for i in range(0, 26):
        num = ((compare[i]) - (ref[i]))**2/ref[i]
        chiSum = chiSum + num

    return chiSum

def frequency(filnavn):
    fil = open(filnavn, "r")
    antall_tegn = 0
    antall_tegn_no_space = 0
    tegn_array = [0] * 26
    tegn_deci = []
    for linje in fil:
        for tegn in linje:
            tegn = tegn.lower()
            if (ord(tegn) >= ord('a') and ord(tegn) <= ord('z')):
                tegn_array[ord(tegn) - ord('a')] += 1
                antall_tegn_no_space += 1

    for x in tegn_array:
        tegn_deci.append(float(x / antall_tegn_no_space))

    return tegn_deci

def crackWithChi(crypt):
    lowestChi=""
    lowestChiNum=100000
    
    for i in range(0, 26):
        decrypt = ceaser(crypt, i)
        numChi = compareFreq("test2")
        if numChi < 1:
            print(decrypt)
        if numChi < lowestChiNum:
            lowestChiNum = numChi
            lowestChi=decrypt
        
    print("Lowest chiSquared found:", lowestChiNum)
    print("Decrypt result: ", lowestChi)
    
    
crackWithChi("nlscha migy gily xywlsjncha qcnb fihayl myhnyhwym qcff nbcm qile c xihn ehiq")
#print(ceaser("trying some more decrypting with longer sentences will this work i dont know", -6))