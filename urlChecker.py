#!/usr/bin/python
# -*- coding: utf-8 -*-
#############################
 
## Par William Vincent - william66750 - @ - g m a i l (.) com
## Description : Url Checker 
## Dependances :
## Utilisation : python urlChecker.py path/to/list.txt path/to/result.txt
 
#############################


#############################
####### Libraries
#############################

import sys
import urllib



##################
### Fonctions
##################



##################
# Fontion > Get arguments
def checkFile():
	nbArgument = len(sys.argv)
	if nbArgument != 3:
		print " Usage : python urlChecker.py path/to/list.txt path/to/result.txt"
		exit()
        else:
		# Init des parametres
		global fileList, fileOut
		fileList     = sys.argv[1]
		fileOut      = sys.argv[2]


##################
# Fontion > Get list URLs
def getList():
	# Liste des urls
	global listUrl
	listUrl = [line.rstrip() for line in open(fileList)]


##################
# Fontion > Test list URLs
def testList():
        # Tests des urls
	for urlCheck in listUrl :
	
	    	print(urlCheck)
		# Créer une erreur si dans le fichier de liste il y a une ligne vide, urllib bloque
		codeResult=urllib.urlopen(urlCheck).getcode()
		# On met en forme le resultat	
		result="%s , %s \n" %(urlCheck,codeResult)
		# On ecrit le resultat dans le fichier
		fileWr.write(result)



##################
### Main
##################


# On vérifie les parametres
checkFile()

# Lecture des URLs
getList ()

# On ouvre le fichier de resultats
fileWr = open(fileOut, "w")

# On traite les Urls
testList()

# On ferme le fichier
fileWr.close()
