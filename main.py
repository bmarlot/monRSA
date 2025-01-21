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
        return False  # Les nombres <= 1 ne sont pas premiers
    if n == 2:
        return True  # 2 est un nombre premier
    if n % 2 == 0:
        return False  # Les nombres pairs autres que 2 ne sont pas premiers
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # On teste uniquement les impairs
        if n % i == 0:
            return False  # Si n est divisible par i, il n'est pas premier
    return True  # Si on n'a trouvé aucun diviseur, alors c'est un nombre premier


def key_gen():
    p = random.randint(1000000000, 9999999999)
    q = random.randint(1000000000, 9999999999)
    e = random.randint(1000000000, 9999999999)
    d = random.randint(1000000000, 9999999999)
    a = 0
    b = 0
    while a < 1 :
        if is_prime(p):
         print("Le premier nombre est premier !")
         a = 1
        else:
         key_gen()
    while b < 1 :
        if is_prime(q):
           print("Le deuxième nombre est premier !")
        b = 1
        else:
          key_gen()
    if p != q and e != d:
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
