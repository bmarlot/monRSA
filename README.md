# monRSA

Un outil de chiffrement RSA simple développé en Python.

## Description
monRSA est un programme développé dans le cadre d'un TP de cours, permettant de générer des clés RSA et de chiffrer/déchiffrer des messages. Il implémente l'algorithme RSA avec des clés de 10 chiffres.

## Installation

### Option 1 : Téléchargement via wget
```bash
wget https://github.com/bmarlot/monRSA/releases/download/v1.0/monRSA.exe
```

### Option 2 : Téléchargement manuel
Allez sur la page des releases
Téléchargez monRSA.exe depuis la dernière version
Placez l'exécutable dans le dossier de votre choix

## Utilisation

### Générer une paire de clés

monRSA --keygen

Cette commande génère :
public_key.txt : Votre clé publique pour chiffrer
private_key.txt : Votre clé privée pour déchiffrer

### Chiffrer un message

monRSA --crypt

Cette commande :
Utilise la clé publique dans public_key.txt
Vous demande d'entrer le message à chiffrer
Génère message_chiffre.txt

### Déchiffrer un message

monRSA --decrypt

Cette commande :
Utilise la clé privée dans private_key.txt
Lit le message chiffré dans message_chiffre.txt
Affiche le message déchiffré

### Afficher l'aide

monRSA --help

### Structure des fichiers
public_key.txt : Contient votre clé publique
private_key.txt : Contient votre clé privée
message_chiffre.txt : Contient le message chiffré

## Notes importantes

Gardez votre clé privée (private_key.txt) secrète
La clé publique (public_key.txt) peut être partagée
Les fichiers sont générés dans le même dossier que l'exécutable

## Sécurité

Les clés générées font 10 chiffres
Ce programme est à but éducatif et ne doit pas être utilisé pour des données sensibles
Pour une utilisation en production, privilégiez des solutions éprouvées comme OpenSSL

## Auteurs
Bryan MARLOT
Jean-Baptiste VIAL
