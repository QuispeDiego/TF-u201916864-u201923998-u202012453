from hashlib import new
from regex import F
from sqlalchemy import false, true
#Function convert text to list
def tex_to_list(text_nodes):
    nodes=text_nodes.split(',')
    return nodes
#Declarate numbers of nodes  and fill empty
ListAds=[]
for i in range(7096):
    ListAds.append([])
# read ways and connect with his nodes  and create ways map
ways={}

with open("waysWithNodes.txt") as f_obj:  
    for line in f_obj:
        k,v_text=line.strip().split('.')
        v=tex_to_list(v_text)
        ways[k.strip()]=v
#diccionario de nodos       
number_to_index={}
index_to_number={}
with open("nodes.txt") as f_obj:  
    index=0
    for line in f_obj:
        number_to_index[line.strip()]=index
        index_to_number[index]=line.strip()
        index+=1

#Create Nodes    
waysIndexs=[]
for i in range(1630):
    waysIndexs.append([])
ways_index_count=0    
keepFirst=false
for  way in ways:
   for node in ways[way]:
       current_index= number_to_index[node]
       waysIndexs[ways_index_count].append(current_index)
       if keepFirst==true:
           ListAds[current_index].append(back_index)
           ListAds[back_index].append(current_index)
           back_index=current_index
       if keepFirst==false:
         back_index= number_to_index[node]
         keepFirst=true
   ways_index_count+=1     
cont=0

with open("AdsList","a") as file:  
    for  lista in  ListAds:
      file.write(f"{cont}:{str(lista)} \n")
      cont+=1

contways=0
with open("Ways_and_nodes","a") as file:  
    for  lista in  waysIndexs:
      file.write(f"{contways}:{str(lista)} \n")
      contways+=1

    
print("finish")        