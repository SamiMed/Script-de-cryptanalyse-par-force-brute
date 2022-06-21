#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys

if len(sys.argv) != 2:
    print("Usage: ", sys.argv[0], "fichier")
    sys.exit()

fichier = sys.argv[1]
nbEssais = 1

l= [chr(x) for x in range(32, 127)]

for i in l:
    print("essai {}, mot de passe: '{}'".format(nbEssais, i))
    nbEssais += 1
    if os.system("gpg --decrypt --passphrase \{} --batch --quiet {}".format(i, fichier)) == 0:
        sys.exit()

for i in l:
   for j in l:
        print("essai {}, mot de passe: '{}{}'".format(nbEssais, i, j))
        nbEssais += 1
        if os.system("gpg --decrypt --passphrase \{}\{} --batch --quiet {}".format(i, j, fichier)) == 0:
            sys.exit()

