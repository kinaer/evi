# -*- coding: utf-8 -*-
"""
Created on Sun May 22 07:07:44 2016

@author: aek
"""
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlencode,urlparse, quote_plus
from urllib.request import Request, urlopen



server="openapi.e-gen.or.kr/openapi/service/rest/ErmctInsttInfoInqireService/getParmacyBassInfoInqire"

regkey="gb8oDEcLH8PoOl4SPS8OHg1ItD16wUM7Pzji0NyIyQiGeUWCsFc7Vdzic0WSN1tZIJt0NRDyHjvaFeB9DhEcTw%3D%3D"
conn=None
def URIcreate(server,**user):
    str=""
    #str='http://'+server+'?'
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connetOpenAPI():
    global server, conn
    conn=HTTPConnection(server)
    
def getPharmacyData(page):
    global server, conn,regkey
    if conn==None:
        connetOpenAPI()
    
    uri=URIcreate(server,serviceKey=regkey,numOfRows="1010",pageNo=page)
    parts = urlparse(uri)
    print(parts.geturl())
    print(parts)
    #conn.request("GET",parts.geturl())
    return parts
    
    """
    #uri = URIcreate(server,serviceKey=regkey,numOfRows="1010",pageNo=page)
    uri='http://'+server+'?'+URIcreate(server,serviceKey=regkey,numOfRows="1010",pageNo=page)
   
    #urllib.quote(uri.encode('utf8'),'/:')
    conn.request("GET", uri)
    #req = conn.getresponse()
    #print (req.status)
    """
   
    """
    url = 'http://openapi.e-gen.or.kr/openapi/service/rest/ErmctInsttInfoInqireService/getParmacyBassInfoInqire'
    queryParams = '?' + urlencode({ 'ServiceKey': regkey,quote_plus('numOfRows') : '1010', quote_plus('pageNo') : page })
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    PharmacyXml=urlparse(response_body) 
    print(url+queryParams)
    """
    
getPharmacyData("5")
    