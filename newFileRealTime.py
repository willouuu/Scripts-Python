#!/usr/bin/python
# -*- coding: utf-8 -*-
#############################
#############################

## Par William Vincent - william66750 - @ - g m a i l (.) com
## Description : List new files in real time // Liste des nouveaux fichiers en temps réel
## Dependances: Subprocess

#############################
#############################

#############################
####### Libraries
#############################

from subprocess import Popen, PIPE

##################
### Variables
##################

liste = ["init"]


##################
### Main
##################

while True:

  # On liste les fichiers
  pipe = Popen('ls', shell=True, stdout=PIPE)

  # On traite le resultat
  for line in pipe.stdout:

     # Si le fichier n'est pas deja ecrit
     if not line.strip() in liste:

        # Alors on l'ecrit
        print(line.strip())

        # Et on l'ajoute a la liste
        liste.append(line.strip())


