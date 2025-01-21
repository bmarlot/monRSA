# TODO : Faire l'algorithme de chiffrement et de dechiffrement

'''

Chiffrement
 Pour chiffrer une chaîne de caractères avec la clé publique n et e, il faut :
 • Transformer chaque caractère en entrée en un chiffre en utilisant le code ASCII
 • Assembler & redécouper cette chaîne en blocs :
◦ On prends des blocs de longueur (taille de n) – 1 de long
 ◦ On part de la droite et on complète, éventuellement le dernier avec des 0 non
significatifs
 ◦ Chaque bloc en clair B est chiffré en un bloc C par la formule C = Be modulo n
 • Assembler les blocs chiffrés C en une suite de chiffres
 • Transformer cette suite de chiffres en texte affichable grâce un double encodage ASCII puis
Base64

Déchiffrement
 Pour déchiffrer une chaîne de caractères avec la clé privée n et d, il faut :
 • « défaire » les 2 encodages de la dernière étape de chiffrement : Base64 décode puis ASCII
encode
 • Découper la chaîne en blocs C de longueur (taille de n) – 1 de long
 • Déchiffrer chaque bloc C en un bloc B avec la formule B = Cd modulo n
 • Découper cette nouvelle chaîne en blocs de 3 chiffes et procéder à un encodage ASCI

'''


def chiffrement():



def dechiffrement():
