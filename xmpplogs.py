#!/usr/bin/python
# -*- coding: utf-8 -*-
#############################
#############################
 
## Par William Vincent - william66750 - @ - g m a i l (.) com
## Description : Send log file to xmpp 
## Dependances: python-pydns xmpppy ( http://xmpppy.sourceforge.net/ ) 
 
#############################
#############################
 
#############################
####### Libraries
#############################
import xmpp, os, time, sys


##################
### Variables
##################
global destinataire,login, password, server

server       = 'irit.fr'
login        = 'annie.belaval'
password     = 'iP8uZKid'
destinataire = 'william.vincent@irit.fr'
logFile      = "/tmp/log.log"



##################
# Fontion > Etablissement de la connexion
def startBot():
  global connexion
  connexion = xmpp.Client(server)
  connexionSrv=connexion.connect()
  if not connexionSrv:
      print "Connexion a %s impossible!"%server
      sys.exit(1)
  if connexionSrv<>'tls':
      print "Warning: TLS failed!"
  connexionAuth=connexion.auth(login,password)
  if not connexionAuth:
      print "Login fail."%server
      sys.exit(1)
  if connexionAuth<>'sasl':
      print "Warning: Old authentication method used!"%server
  connexion.sendInitPresence()


##################
# Fontion > Envoi d'un log
def sendmsg(text):
  connexion.send( xmpp.Message( destinataire , text ) )


#############################
# Main
#############################

# Taille du fichier d'origine
oldSizeLog = newSizeLog = os.path.getsize(logFile)

# Initialisation de la connexion
startBot()
print "Bot started."

# Analyse de log
while True:
  # Recuperer la taille
  newSizeLog = os.path.getsize(logFile)
  # Check diff de taille
  if newSizeLog != oldSizeLog:
    # On ouvre le fichier
    buffLogFile = open(logFile)
    # On transforme l'ancienne valeur (oldSizeLog) en le debut du nouveau fichier (os.SEEK_SET = 0)
    buffLogFile.seek(oldSizeLog, os.SEEK_SET)
    # On enregistre les nouvelles ligne
    newLogFile = buffLogFile.read()
    if newLogFile[-1] == '\n':
      # On envoie au destinataire les nouvelles lignes
      sendmsg(newLogFile)
      # On enregistre la nouvelle taille ( position )
      oldSizeLog = buffLogFile.tell()
    buffLogFile.close()
  # On defini quand aura lieu la prochaine analyse ( en seconde )
  time.sleep(10)
