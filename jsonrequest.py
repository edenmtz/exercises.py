#!/usr/bin/python
## Third Problem

import urllib, json

def retrive_info ( value ):
    #url = "http://api.somecompany.corp/rest/info/" + value
    #client = urllib.request.urlopen(url)
    #return json.loads(client.read())
    if value == "A":
        return {"name":"USER1","position":"User name 1","Reported":["B","C"]}
    elif value == "B":
        return {"name":"USER2","position":"User name 2","Reported":["D","E"]}
    elif value == "C":
        return {"name":"USER3","position":"User name 3","Reported":[]}
    elif value == "D":
        return {"name":"USER4","position":"User name 4","Reported":[]}
    elif value == "E":
        return {"name":"USER5","position":"User name 5","Reported":[]}
    
def format_result ( reported = "A", tabs = "" ):
    data = retrive_info ( reported )
    tabs += '\t'
    i = ""
    #i =  tabs+data.get("name")+"-"+data.get("position")+"\n" + i
    if (len (data.get("Reported")) > 0):
       i = format_result(data.get("Reported").pop(),tabs) + i
    
    return tabs+data.get("name")+"-"+data.get("position")+"\n" + i


d = format_result ("A","\t")


print d

        
    
