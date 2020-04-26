# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:32:04 2020

@author: Tanguy
"""

# Connexion à redis

import redis

r = redis.Redis(port=6379)

# Question 1
r.geoadd("Ville",49.8986514,2.2145979,"Amiens")
r.geoadd("Ville",50.1101392,1.7962242,"Abbeville")
r.geoadd("Ville",50.0033988,2.6340819,"Albert")
r.geoadd("Ville",50.1514695,2.2819405,"Doullens")
r.geoadd("Ville",49.9216618,2.4800254,"Corbie")
r.geoadd("Ville",49.647487,2.5486319,"Montdidier")
r.geoadd("Ville",49.6907257,2.7521182,"Roye")
r.geoadd("Ville",49.8726485,2.3500182,"Longueau")
r.geoadd("Ville",49.7529828,3.0523779,"Ham")

a="Technicien de maintenance"
b="Assistant chef de projet"
c="Conseiller en clientèle"
d="Consultant informatique"

r.lpush("Amiens",a,b,d,d)
r.lpush("Péronne",a)
r.lpush("Corbie",a,d)
r.lpush("Longueau",a)
r.lpush("Abbeville",b,d)
r.lpush("Roye",c)
r.lpush("Ham",c)

# Question 2
print(r.geopos("Ville","Amiens"))
print(r.geopos("Ville","Abbeville"))
print(r.geopos("Ville","Albert"))
print(r.geopos("Ville","Doullens"))
print(r.geopos("Ville","Corbie"))
print(r.geopos("Ville","Montdidier"))
print(r.geopos("Ville","Roye"))
print(r.geopos("Ville","Longueau"))
print(r.geopos("Ville","Ham"))

print(r.lrange("Amiens",0,-1))
print(r.lrange("Péronne",0,-1))
print(r.lrange("Corbie",0,-1))
print(r.lrange("Longueau",0,-1))
print(r.lrange("Abbeville",0,-1))
print(r.lrange("Roye",0,-1))
print(r.lrange("Ham",0,-1))


# Question 3
print(r.georadiusbymember("Ville", "Amiens", 35,unit="km"))




