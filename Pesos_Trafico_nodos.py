# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt
import random as ra
def distance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)
     
     
# driver code
lat1 = -12.0948728
lat2 = -12.0952242
lon1 = -77.0763293
lon2 =  -77.0753134
print(distance(lat1, lat2, lon1, lon2), "K.M")

def trafico(dist,hora):
       if (hora > 21 and hora < 24) or (hora < 7 and hora >-1):
           trafic = dist*ra.randint(0.1,0.9)
       if hora < 22 and hora > 6:
           trafic = dist*ra.randint(1.0,1.9)

def peso(traf,dist):
    return (traf/100)*dist
# 0:[(19,4), (3549,7), (1245,4), (5319,4)]

# TRAFICO = DISTANCIA * SI HORA ESTA ENTRE 22 Y 6 RANDOM(0.1, 0.9) Y SI HORA ESTA ENTRE 7 Y 21 RANDOM(1.0, 1.9)
# PESO = (TRAFICO / 100) * DISTANCIA