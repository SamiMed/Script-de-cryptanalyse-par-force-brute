# Script de cryptanalyse par force-brute


Script python de cryptanalyse par force brute qui essaie tous 
les mots de passe de longueur 1 à 2, jusqu’à ce qu’il trouve le bon, pour déchiffrer un fichier 
chiffré symétriquement avec gpg:

- Le script prend en paramètre le nom du fichier chiffré
- Le mot de passe est composé uniquement de caractères ASCII (pas utf-8), donc dont  la valeur numérique (ord()) est comprise entre 32 et 126 inclusivement
- À chaque tentative, le mot de passe est affiché à l’écran entre apostrophes
- Lorsque le bon mot de passe est trouvé, le script s’arrête
