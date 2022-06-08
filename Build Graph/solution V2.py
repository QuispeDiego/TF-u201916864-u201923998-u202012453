

from random import uniform


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
print(len(ways))