 #!/usr/bin/env python
 
 #####################################
 # ModSecurity LogType: concurent ( logs séparés par jour/heure-minute/ensembleDeLaTransaction )
 #
 # Executer :
 #   python matchRegexLogModSec.py /directory/Path/
 #    result : [id "960024"] [rev "2"] [msg "SQL Character Anomaly Detection Alert - Repetative Non-Word Characters"]
 #   python matchRegexLogModSec.py /directory/Path/ url
 #    result : [id "960024"] [rev "2"] [msg "SQL Character Anomaly Detection Alert - Repetative Non-Word Characters"] [url "GET /-Page-?var=232&nom=%5c%5c%5c%5c%5c%5c%5c'toto%2520titi HTTP/1.1"]
 #####################################
 
 import re
 import sys
 import os
 import os.path
 
 # Declaration de la Pattern Regex
 p = re.compile(ur'\[id (.*?)\] \[msg (.*?)\]', re.IGNORECASE)
 
 # Liste des fichier dans le repertoire courant et les sous repertoire
 for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
     for filename in [f for f in filenames ]:
         # On concatene le fullpath
         fullName=os.path.join(dirpath, filename)
         #print 'Fichier : ', fullName
 
         #On match l'expression reguliere
         for line in open(fullName):
             # On enregistre l'url
             if "GET /" in line:
                 text = line.replace('\n', '')
                 url="[url \"%s\"]" % (text)
             # On extrait ID de chaque ligne
             if "id " in line:
                 match = re.search(p, line)
                 # Si on a le parametre "url" on affiche l'url
                 if match:
                     if len(sys.argv) > 2:
                         if sys.argv[2] == "url" :
                             print match.group(), url
                     #Dans tout les cas on affiche la rules modsecurity
                     else:
                         print match.group()
