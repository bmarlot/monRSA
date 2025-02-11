import base64


def encrypt_message(message, n, e):
    # 1. Convertir en ASCII
    ascii_values = [ord(char) for char in message]
    print(f"Valeurs ASCII: {ascii_values}")

    # 2. Convertir en chaîne ASCII
    ascii_string = ''.join(str(val).zfill(3) for val in ascii_values)
    print(f"Chaîne ASCII: {ascii_string}")

    # 3. Chiffrer chaque valeur ASCII individuellement
    encrypted_values = []
    for val in ascii_values:
        encrypted_val = pow(val, e, n)
        encrypted_values.append(str(encrypted_val))
    print(f"Valeurs chiffrées: {encrypted_values}")

    # 4. Joindre les valeurs chiffrées avec un séparateur
    encrypted_string = '#'.join(encrypted_values)
    print(f"Chaîne chiffrée: {encrypted_string}")

    # 5. Encoder en base64
    encrypted_bytes = encrypted_string.encode('ascii')
    base64_bytes = base64.b64encode(encrypted_bytes)
    base64_string = base64_bytes.decode('ascii')

    return base64_string


def decrypt_message(encrypted_base64, n, d):
    # 1. Décoder le Base64
    encrypted_bytes = base64.b64decode(encrypted_base64)
    encrypted_string = encrypted_bytes.decode('ascii')
    print(f"Chaîne décodée du Base64: {encrypted_string}")

    # 2. Séparer les valeurs
    encrypted_values = encrypted_string.split('#')
    print(f"Valeurs chiffrées: {encrypted_values}")

    # 3. Déchiffrer chaque valeur
    decrypted_values = []
    for val in encrypted_values:
        decrypted_val = pow(int(val), d, n)
        decrypted_values.append(decrypted_val)
    print(f"Valeurs déchiffrées: {decrypted_values}")

    # 4. Convertir en caractères
    message = ''.join(chr(val) for val in decrypted_values)

    return message


def encryption():
    try:
        # Lire la clé publique
        with open("public_key.txt", "r") as f:
            content = f.read()
            # Extraire la partie Base64 entre les marqueurs
            b64_content = content.split("\n")[1]
            key_content = base64.b64decode(b64_content).decode('utf-8')
            hex_n, hex_e = key_content.split("\n")
            n = int(hex_n, 16)
            e = int(hex_e, 16)

        # Demander le message à l'utilisateur
        message = input("Entrez le message à chiffrer : ")

        # Chiffrer le message
        encrypted = encrypt_message(message, n, e)

        # Sauvegarder le message chiffré
        with open("message_chiffre.txt", "w") as f:
            f.write("---begin monRSA message---\n")
            f.write(encrypted)
            f.write("\n---end monRSA message---")

        print("Message chiffré sauvegardé dans 'message_chiffre.txt'")

    except Exception as e:
        print(f"Erreur lors du chiffrement : {e}")


def decryption():
    try:
        # Lire la clé privée
        with open("private_key.txt", "r") as f:
            content = f.read()
            # Extraire la partie Base64 entre les marqueurs
            b64_content = content.split("\n")[1]
            key_content = base64.b64decode(b64_content).decode('utf-8')
            hex_n, hex_d = key_content.split("\n")
            n = int(hex_n, 16)
            d = int(hex_d, 16)

        # Lire le message chiffré
        with open("message_chiffre.txt", "r") as f:
            content = f.read()
            encrypted = content.split("\n")[1]

        # Déchiffrer le message
        decrypted = decrypt_message(encrypted, n, d)

        print(f"Message déchiffré : {decrypted}")

    except Exception as e:
        print(f"Erreur lors du déchiffrement : {e}")
