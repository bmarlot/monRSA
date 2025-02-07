#from chiffrement_dechiffrement import encryption
#from chiffrement_dechiffrement import decryption
import random
from operator import truediv
import base64
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

    hex_n = hex(n)
    hex_e = hex(e)
    hex_d = hex(d)

    public_key = f"{hex_n}\n{hex_e}"
    private_key = f"{hex_n}\n{hex_d}"

    with open("public_key.txt", "w") as fichier:
        fichier.write("---begin monRSA public key---\n" + base64.b64encode(public_key.encode('utf-8')).decode(
            'utf-8') + "\n---end monRSA key---")

    with open("private_key.txt", "w") as fichier:
        fichier.write("---begin monRSA private key---\n" + base64.b64encode(private_key.encode('utf-8')).decode(
            'utf-8') + "\n---end monRSA key---")



def print_manual():
    manual = """
    Script monRSA par bryan et jb
    -----------------------------------
    Syntaxe :
      monRSA <commande> [<clé>] [<texte>] [switchs]

    Commandes :
      keygen                : Génère une paire de clés RSA.
      crypt <clé> <texte>   : Chiffre <texte> avec la clé publique <clé>.
      decrypt <clé> <texte> : Déchiffre <texte> avec la clé privée <clé>.
      help                  : Affiche ce manuel.

    Clé :
      Un fichier contenant une clé publique ("crypt") ou une clé privée ("decrypt").

    Texte :
      Une phrase en clair ("crypt") ou une phrase chiffrée ("decrypt").
    """
    print(manual)

def main():
    # Vérifier les arguments passés en ligne de commande
    if len(sys.argv) < 2 or sys.argv[1] == "help":
        print_manual()
        return

    command = sys.argv[1]

    if command == "--help":
        print_manual()
    elif command == "--keygen":
        key_gen()
    elif command == "--crypt":
        #    encryption()
        print_manual()
    elif command == "--decrypt":
        #    decryption()
        print_manual()
    else:
        print("Erreur : Commande invalide ou arguments manquants.\n")
        print_manual()




# TODO : Faire un main qui lance le programme avec les bonnes fonctions


if __name__ == '__main__':
    main()
