# Python 3 program to calculate Distance Between Two Points on Earth
from math import radians, cos, sin, asin, sqrt
import random as ra
dict_nodes_lat = dict()
with open("nodes_lat.txt") as f:
  for line in f:
    val = [float(x) for x in line.split(',')]
    dict_nodes_lat[val[0]] = val[1],val[2]

arr_nodes = []
with open("AdsList.txt") as f2:
    for line in f2:
        #arr_nodes.append([])
        val = line.split(':')
        val = str(val[1].strip("[\n"))
        val = val.replace("]","")
        arr_nodes.append([int(x) for x in val.split(',')])

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
           trafic = float(dist*ra.uniform(0.1,0.9))
           return trafic
       if hora < 22 and hora > 6:
           trafic = float(dist*ra.uniform(1.0,1.9))
           return trafic

def peso(traf,dist):
    return float(traf/100)*dist
# 0:[(19,4), (3549,7), (1245,4), (5319,4)]
arr_nodos_pesos1 = []
def Crear_nodos_pesos(arr_nodos_pesos):
    k=0
    for data in arr_nodes:
        arr_nodos_pesos.append([])
        for d in data:
            lat1,lon1 = dict_nodes_lat[k]
            lat2,lon2 = dict_nodes_lat[d]
            dist = distance(lat1, lat2, lon1, lon2)
            arr_nodos_pesos[k].append((d,peso(trafico(dist,20),dist)))
        k+=1

Crear_nodos_pesos(arr_nodos_pesos1)
print(arr_nodos_pesos1)

# TRAFICO = DISTANCIA * SI HORA ESTA ENTRE 22 Y 6 RANDOM(0.1, 0.9) Y SI HORA ESTA ENTRE 7 Y 21 RANDOM(1.0, 1.9)
# PESO = (TRAFICO / 100) * DISTANCIA
