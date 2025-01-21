from chiffrement_dechiffrement import chiffrement
from chiffrement_dechiffrement import dechiffrement

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


def key_gen():
    print("PLACEHOLDER")


def main():
    chiffrement()
    dechiffrement()


# TODO : Faire un main qui lance le programme avec les bonnes fonctions


if __name__ == '__main__':
    main()
