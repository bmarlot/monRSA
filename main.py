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

def key_gen():
    p = random_nb()
    q = random_nb()
    e = random_nb()
    d = random_nb()

    while not is_prime(p) :
       p = random_nb()

    while not is_prime(q) and q != p:
        q = random_nb()

    while not is_prime(e) and e != q and e != p:
        e = random_nb()

    while not is_prime(d) and d != e and d != p and d != q:
        d = random_nb()



    n = p * q
    n2 = (p - 1) * (q - 1)
    ed = e * d




def main():
#    encryption()
#    decryption()
    key_gen()


# TODO : Faire un main qui lance le programme avec les bonnes fonctions


if __name__ == '__main__':
    main()
