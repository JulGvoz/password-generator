from random import SystemRandom
from math import log

rng = SystemRandom()

numberOfWords = int(input("Number of words: "))
randomCasing = bool(input("Random Casing?(empty if no): "))
numberOfPasswords = int(input("Number of passwords: "))

with open('4000-most-common-english-words-csv.csv') as file:
    passwords = file.read().split("\n")
    passwords = passwords[1:len(passwords)-2]

def randomUpper(s):
    upper = False
    if randomCasing:
        upper = rng.random() >= 0.5
    if upper:
        return s.upper()
    else:
        return s.lower()

for i in range(0, numberOfPasswords):
    password = randomUpper(rng.choice(passwords))

    for j in range(1, numberOfWords):
        password +=  "-" + randomUpper(rng.choice(passwords))

    print(password)

entropyPosibilities = len(passwords)**numberOfWords
if randomCasing:
    entropyPosibilities = entropyPosibilities * 2**numberOfWords
entropyBits = log(entropyPosibilities, 2)
print("Number of bits: " + str(entropyBits))
