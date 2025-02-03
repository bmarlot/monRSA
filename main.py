#from chiffrement_dechiffrement import encryption
#from chiffrement_dechiffrement import decryption
import random
from operator import truediv

# TODO : Faire un main qui prends l'algo de base.

'''
# ALGO DE BASE :

Génération des clé
On utilise 6 nombres entiers p, q, n, n’, d et e qui respectent les règles suivantes :
• p & q sont deux nombres premiers différents
• n = pq
• n’ = (p - 1) (q – 1)
• e est un nombre premier différent de d
• ed = 1 modulo n’

Concrètement :
• Générer 2 nombres 1er différents de 10 chiffres de long2
: p & q
• Calculer n et n’ (facile)
• Faire une boucle3
 qui teste des valeurs pour e et d jusqu’à ce que :
◦ e soit premier
◦ e soit différent de d
◦ ed % n’ = 1 (ou, dit autrement, ed = 1 modulo n’)
Bravo, vous avez une clé privée : n et d et une clé publique : n et e


 
'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def random_nb():
    return random.randint(1000000000, 9999999999)

def egcd(a, b):
    """ Algorithme d'Euclide étendu : retourne (gcd, x, y) tel que ax + by = gcd(a, b) """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """ Trouve l'inverse modulaire de e modulo phi en utilisant l'algorithme d'Euclide étendu """
    gcd, x, _ = egcd(e, phi)
    if gcd != 1:
        return None  # Aucun inverse modulaire n'existe si gcd(e, phi) ≠ 1
    return x % phi  # Assure un résultat positif

def key_gen():
    p = random_nb()
    while not is_prime(p):
        p = random_nb()

    q = random_nb()
    while not is_prime(q) or q == p:
        q = random_nb()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random_nb()
    while not is_prime(e) or e >= phi_n or phi_n % e == 0:
        e = random_nb()

    d = mod_inverse(e, phi_n)
    if d is None:
        return key_gen()  # Relance la génération si l'inverse modulaire n'existe pas

    nb1 = n * e
    nb2 = n * d
    return nb1, nb2

print(key_gen())



def main():
#    encryption()
#    decryption()
    key_gen()


# TODO : Faire un main qui lance le programme avec les bonnes fonctions


if __name__ == '__main__':
    main()
