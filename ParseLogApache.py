#!/usr/bin/python

# -*- coding: utf-8 -*-
#############################

## Par William Vincent - william66750 - @ - g m a i l (.) com
## Description : Parser logs erreurs Apache ModSecurity et ajout en base MongoDb pour post traitement

# Executer :
#   python ParseLogApache.py /logs/directory/www.domaine.fr-error.log
#####################################

##Base Mongo 
#Creer base
#> use modsec_rules
#Lister bases
#> db
#Creer user
#> db.users.save( {username:"LaWix"} )
#Lister users
#> db.users.find()
#ID autoincrement
#> db.counters.insert(   {      _id: "logid",      seq: 0   })
#> db.logs.insert({    _id: getNextSequence("logid"),    idrule: 1000000,    description: 'Test insert' })
# Remove par id
#> db.logs.remove({    _id: ObjectId("581c593e1e35722ffa667466")})
# Remove all documents
#> db.logs.deleteMany({})



import re
import sys, getopt
import pymongo



def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.modsec_rules
    return db

def add_log(idrule,msg):
    db.logs.insert({ "_id": db.logs.find().count()+1,  "idrule": idrule,  "description": msg })


def main(argv):
   global inputfile
   inputfile = 'notDefine'
   outputfile = 'notDefine'
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'programName.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'programName.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file : ', inputfile
   print 'Output file : ', outputfile


if __name__ == "__main__":
    main(sys.argv[1:])

    db = get_db()

    with open(inputfile) as fp:
        for line in fp:
            count=0
            #print "count : ",count
            regex = r"\[id(.*?)\]|\[msg(.*?)\]"
            matches = re.finditer(regex, line)

            for matchNum, match in enumerate(matches):
                count=count+1
                if count==1:
                    idrule=match.group(1)
                    idrule=idrule.replace("\"",'')
                    print "IdRule:",idrule

                if count==2:
                     msg=match.group(2)
                     msg=msg.replace("\"",'')
                     print "Desc:",msg

            add_log(idrule,msg)
