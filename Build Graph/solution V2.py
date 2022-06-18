

from random import uniform
from numpy import double
from sqlalchemy import false, true
from node import Node
from node import Data
from math import radians, cos, sin, asin, sqrt
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

def tex_to_list(text_nodes):
    nodes_in_string=text_nodes[1:-1].split(',')
    nodes_in_int=[int(x) for x in nodes_in_string]
    return nodes_in_int

def assign_traffic_info():
    number_of_hours=24
    list_traffic=[]
    #traffic early
    traffic_earlyMoornig_begin=0.0
    traffic_earlyMoornig_end=0.3
    #traffic early
    traffic_moornig_begin=1
    traffic_moornig_end=1.5
    #traffic affternoon
    traffic_affternoon_begin=0.4
    traffic_afternoon_end=0.9
    #traffic night
    traffic_night_begin=0.5
    traffic_nigt_end=0.8
    for i in range(number_of_hours):
      if(i>=0 and i<=7):
        list_traffic.append(uniform(traffic_earlyMoornig_begin,traffic_earlyMoornig_end))
        continue
      if(i>=8 and i<=15):
         list_traffic.append(uniform(traffic_moornig_begin,traffic_moornig_end))
         continue
      if(i>=16 and i<=20):
         list_traffic.append(uniform(traffic_affternoon_begin,traffic_afternoon_end))
         continue
      if(i>=21 and i<=23):
        list_traffic.append(uniform( traffic_night_begin, traffic_nigt_end))
    return list_traffic 


ways_connect_whith_nodes={}
with open("Ways_and_nodes.txt") as f_obj:  
    for line in f_obj:
        k,v_text=line.strip().split(':')
        v=tex_to_list(v_text)
        ways_connect_whith_nodes[int(k.strip())]=v

ways={}

with open("ways.txt",encoding="cp437", errors='ignore') as f_obj:  
    for line in f_obj:
        k,v_text=line.strip().split(',')
        ways[int(k.strip())]=(v_text, assign_traffic_info())

nodes={}
with open("nodes.txt",encoding="cp437", errors='ignore') as f_obj:  
    for line in f_obj:
        k,lat,long=line.strip().split(',')
        nodes[int(k.strip())]=(double(lat.strip()),double(long.strip()))



keepFirst=false
ListAds=[]
for i in range(7096):
    ListAds.append([])
for  _way in ways_connect_whith_nodes:
   for node in ways_connect_whith_nodes[_way]:
       current_node=node
       if keepFirst==true:
           lat1=nodes[current_node][0]
           lon1=nodes[current_node][1]
           lat2=nodes[back_node][0]
           lon2=nodes[back_node][1]

           theDistance=distance(lat1,lat2,lon1,lon2)
           ListAds[current_node].append(Node(back_node,Data(theDistance,ways[_way])))
           ListAds[back_node].append(Node(current_node,Data(theDistance,ways[_way])))
           back_node=  current_node
       if keepFirst==false:
         back_node=node
         keepFirst=true

for i in ListAds[0]:
        print(i.id)