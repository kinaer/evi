# -*- coding: utf-8 -*-
"""
Created on Sun May 22 07:07:44 2016

@author: aek
"""
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import Request, urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pharmacymodul import *
from pharmacymodul import PharmacyXml
#import pharmacymodul
 
#from xml.dom.minidom import *

host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

server="openapi.e-gen.or.kr/openapi/service/rest/ErmctInsttInfoInqireService/getParmacyBassInfoInqire"

regkey="gb8oDEcLH8PoOl4SPS8OHg1ItD16wUM7Pzji0NyIyQiGeUWCsFc7Vdzic0WSN1tZIJt0NRDyHjvaFeB9DhEcTw%3D%3D"
conn=None


def URIcreate(server,**user):
    str=""
    str='http://'+server+'?'
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connetOpenAPI():
    global server, conn
    conn=HTTPConnection(server)
    
def getPharmacyData(page):
    global server, conn,regkey, PharmacyXml
    if conn==None:
        connetOpenAPI()
    #minidom 으로 URL파싱하는 법
    url=URIcreate(server,serviceKey=regkey,numOfRows="1010",pageNo=page)
    dom=parse(urlopen(url))
    print(dom.toxml())
    PharmacyXml=dom
    return dom
    """
    #urllib.urlopen 은 URL로 부터 데이터 얻음
    url=URIcreate(server,serviceKey=regkey,numOfRows="1010",pageNo=page)
    request = Request(url)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    print(response_body)
    """
def sendMail():
    global host, port
    title=str(input("메일 제목 입력 : "))
    senderAddr=str(input("보낸이의 G메일 주소 입력 : "))
    passwd = str(input (' 비밀번호를 입력하세요 :'))
    recipientAddr = str(input ("받는 이의 이메일 주소 입력 :"))
    key=str(input("약국을 찾을 지역을 입력하세요 : "))
    html=MakeHTML(getAddrToPharmacyList(key))
     #Message container를 생성합니다.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    msg.attach(MIMEText(html,'html', _charset = 'UTF-8'))
    s=SMTP(host,port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)    # 로긴을 합니다. 
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    
    print ("메일 보내기 완료")

