# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:52:14 2016

@author: aek
"""

from xml.dom.minidom import *

from http.client import HTTPConnection
from urllib.request import Request, urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import webbrowser


PharmacyXml=None
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

server="openapi.e-gen.or.kr/openapi/service/rest/ErmctInsttInfoInqireService/getParmacyBassInfoInqire"

regkey="gb8oDEcLH8PoOl4SPS8OHg1ItD16wUM7Pzji0NyIyQiGeUWCsFc7Vdzic0WSN1tZIJt0NRDyHjvaFeB9DhEcTw%3D%3D"
conn=None
searchItemList=[]
maps="https://www.google.co.kr/maps/place/"

def URIcreate(server,**user):
    str=""
    str='http://'+server+'?'
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connetOpenAPI():
    global server, conn
    #서버 연결 요청
    conn=HTTPConnection(server)
    
def getPharmacyData():
    global server, conn,regkey,PharmacyXml
    if conn==None:
        connetOpenAPI()
    #minidom 으로 URL파싱하는 법
    url=URIcreate(server,serviceKey=regkey,numOfRows="21000",pageNo="1")
    dom=parse(urlopen(url))
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
    s=smtplib.SMTP(host,port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)    # 로긴을 합니다. 
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    
    print ("메일 보내기 완료")
    
   
    #여기까지 웹
 ###############################################################################3   
def residentPharmacy():
    ##################################################### 사업자 등록 xml파일에 적을 내용들을 기록
    hpid=str(input("사업자 아이디를 입력하세요. : "))
    dutyName=str(input("약국 이름을 입력하세요 : "))
    dutyAddr=str(input("약국 주소를 입력하세요 : "))
    dutyMapimg=str(input("약국 약식을 입력하세요 (없으면 None을 입력하세요.) : "))
    dutyTel1=str(input("전화번호를 입력하세요 : "))
    dutyTime1s=str(input("월요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime1c=str(input("월요일 종료시간을 입력하세요 (ex 2000): "))
    dutyTime2s=str(input("화요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime2c=str(input("화요일 종료시간을 입력하세요 (ex 2000): "))
    dutyTime3s=str(input("수요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime3c=str(input("수요일 종료시간을 입력하세요 (ex 2000): "))
    dutyTime4s=str(input("목요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime4c=str(input("목요일 종료시간을 입력하세요 (ex 2000): "))
    dutyTime5s=str(input("금요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime5c=str(input("금요일 종료시간을 입력하세요 (ex 2000): "))
    dutyTime6s=str(input("토요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime6c=str(input("토요일 종료시간을 입력하세요 (ex 2000): "))
    dutyTime7s=str(input("일요일 시작시간을 입력하세요 (ex 0800): "))
    dutyTime7c=str(input("일요일 종료시간을 입력하세요 (ex 2000): "))
    return {"dutyName":dutyName,"dutyMapimg":dutyMapimg,"dutyAddr":dutyAddr,"dutyTel1":dutyTel1,
            "dutyTime1c":dutyTime1c,"dutyTime1s":dutyTime1s,"dutyTime2c":dutyTime2c,"dutyTime2s":dutyTime2s,
            "dutyTime3c":dutyTime3c,"dutyTime3s":dutyTime3s,"dutyTime4c":dutyTime4c,"dutyTime4s":dutyTime4s,
            "dutyTime5c":dutyTime5c,"dutyTime5s":dutyTime5s,"dutyTime6c":dutyTime6c,"dutyTime6s":dutyTime6s,
            "dutyTime7c":dutyTime7c,"dutyTime7s":dutyTime7s,"hpid":hpid}
    

def xmlFileRead():
    
#인코딩해줘야되
    try:
        x=open("pharmacy.xml",encoding="utf8")
    except  IOError:
        print(" 파일 이름이나 경로가 잘못되었습니다.")
        return
    try:
        dom=parse(x)
    except Exception:
        print("불러오기 실패")
    else:
        print("정상적으로 XML파일에 연결되었습니다.")
    
        return dom
    return

def printFileXML():
    if checkXml():
        print(PharmacyXml.toxml())


def checkXml():
    global PharmacyXml
    if PharmacyXml==None:
        print("xml을 먼저 등록하세요.")
        return False
    return True

def searchPharmacyName(tag):
    global PharmacyXml
    if not checkXml():
        return
    PharmacyNameList=PharmacyXml.getElementsByTagName(tag)
    for item in PharmacyNameList:
        print("약국 이름 : ",item.firstChild.nodeValue) #약국 목록 출력
 
def searchPharmacyAddr(key):
    global PharmacyXml
    if not checkXml():
        return
    items=PharmacyXml.getElementsByTagName("item")
    for item in items:
        subitem=item.childNodes
        maping=None
        for a in subitem:
            if a.nodeName=="dutyName":
                name=a
            elif a.nodeName=="dutyMapimg":
                maping=a
            elif a.nodeName=="dutyAddr":
                addr=a
            elif a.nodeName=="dutyTel1":
                tel=a
        if (addr.firstChild.nodeValue.find(key)>=0):
            print("\n약국이름 : ",name.firstChild.nodeValue)
            print("약국주소 : ",addr.firstChild.nodeValue)
            if maping!=None:
                print("약국약식 : ",maping.firstChild.nodeValue)
            print("전화번호 : ",tel.firstChild.nodeValue)

def displaymap(keyword):
    global searchItemList,maps
    if not checkXml():
        return
    addr=maps
    for item in searchItemList:
        subitem=item.childNodes
        for a in subitem:
            if a.nodeName=="dutyName":
                name=a
            elif a.nodeName=="wgs84Lat":
                lat=a
            elif a.nodeName=="wgs84Lon":
                lon=a
        if (name.firstChild.nodeValue.find(keyword)>=0):
            print(lat.firstChild.nodeValue+"   "+lon.firstChild.nodeValue)
            latlon=lat.firstChild.nodeValue+","+lon.firstChild.nodeValue
    addr+=latlon
    webbrowser.open_new(addr)
    
        
def getAddrToPharmacyList(key):
    global PharmacyXml
    global searchItemList
    if not checkXml():
        return
    list1=[]
    items=PharmacyXml.getElementsByTagName("item")
    for item in items:
        subitem=item.childNodes
        for a in subitem:
            if a.nodeName=="dutyName":
                name=a
            elif a.nodeName=="dutyAddr":
                addr=a
            elif a.nodeName=="dutyTel1":
                tel=a
        if (addr.firstChild.nodeValue.find(key)>=0):
            list1.append((name.firstChild.nodeValue,
                          addr.firstChild.nodeValue,
                          tel.firstChild.nodeValue))
            searchItemList.append(item)
    return list1

    """
    try:
        tree=ElementTree.fromstring(str(PharmacyXml.toxml()))
    except Exception:
        print("에러, xml파일을 확인해주세요.")
        return None
    itemList=tree.getiterator("item")
    for item in itemList:
        addrStr=item.find("dutyAddr")
        if(addrStr.text.find(key)>=0):  #addr의 텍스트를 키로 검색해 존재하면
            print(item.find("dutyName").text)
    """  

def MakeHTML(list1):
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)
    body = newdoc.createElement('body')
    for item in list1:
        name=newdoc.createElement('dutyName')
        nameText=newdoc.createTextNode(item[0])
        name.appendChild(nameText)
        body.appendChild(name)
        
        addr=newdoc.createElement('dutyAddr')
        addrText=newdoc.createTextNode(item[1])
        addr.appendChild(addrText)
        body.appendChild(addr)
        
        tel=newdoc.createElement('dutyTel1')
        telText=newdoc.createTextNode(item[2])
        tel.appendChild(telText)
        body.appendChild(tel)
       
    top_element.appendChild(body)
    return newdoc.toxml()

def AddPharmacy(data):
    global PharmacyXml
    if not checkXml():
        return
    mDom=xmlFileRead()
    newPharmacy=mDom.createElement('item')
    
    addr=mDom.createElement('dutyAddr')
    addrText=mDom.createTextNode(data['dutyAddr'])
    addr.appendChild(addrText)
    newPharmacy.appendChild(addr)
    if data['dutyMapimg']!=None:
        maping=mDom.createElement('dutyMapimg')
        mText=mDom.createTextNode(data['dutyMapimg'])
        maping.appendChild(mText)
        newPharmacy.appendChild(maping)
    name=mDom.createElement('dutyName')
    nText=mDom.createTextNode(data['dutyName'])
    name.appendChild(nText)
    newPharmacy.appendChild(name)
    tel=mDom.createElement('dutyTel1')
    telText=mDom.createTextNode(data['dutyTel1'])
    tel.appendChild(telText)
    newPharmacy.appendChild(tel)
    
    t1c=mDom.createElement('dutyTime1c')
    t1cText=mDom.createTextNode(data['dutyTime1c'])
    t1c.appendChild(t1cText)
    newPharmacy.appendChild(t1c)
    t1s=mDom.createElement('dutyTime1s')
    t1sText=mDom.createTextNode(data['dutyTime1s'])
    t1s.appendChild(t1sText)
    newPharmacy.appendChild(t1s)
    
    t2c=mDom.createElement('dutyTime2c')
    t2cText=mDom.createTextNode(data['dutyTime2c'])
    t2c.appendChild(t2cText)
    newPharmacy.appendChild(t2c)
    t2s=mDom.createElement('dutyTime2s')
    t2sText=mDom.createTextNode(data['dutyTime2s'])
    t2s.appendChild(t2sText)
    newPharmacy.appendChild(t2s)
    
    t3c=mDom.createElement('dutyTime3c')
    t3cText=mDom.createTextNode(data['dutyTime3c'])
    t3c.appendChild(t3cText)
    newPharmacy.appendChild(t3c)
    t3s=mDom.createElement('dutyTime3s')
    t3sText=mDom.createTextNode(data['dutyTime3s'])
    t3s.appendChild(t3sText)
    newPharmacy.appendChild(t3s)
    
    t4c=mDom.createElement('dutyTime4c')
    t4cText=mDom.createTextNode(data['dutyTime4c'])
    t4c.appendChild(t4cText)
    newPharmacy.appendChild(t4c)
    t4s=mDom.createElement('dutyTime4s')
    t4sText=mDom.createTextNode(data['dutyTime4s'])
    t4s.appendChild(t4sText)
    newPharmacy.appendChild(t4s)
    
    t5c=mDom.createElement('dutyTime5c')
    t5cText=mDom.createTextNode(data['dutyTime5c'])
    t5c.appendChild(t5cText)
    newPharmacy.appendChild(t5c)
    t5s=mDom.createElement('dutyTime5s')
    t5sText=mDom.createTextNode(data['dutyTime5s'])
    t5s.appendChild(t5sText)
    newPharmacy.appendChild(t5s)
    
    t6c=mDom.createElement('dutyTime6c')
    t6cText=mDom.createTextNode(data['dutyTime6c'])
    t6c.appendChild(t6cText)
    newPharmacy.appendChild(t6c)
    t6s=mDom.createElement('dutyTime6s')
    t6sText=mDom.createTextNode(data['dutyTime6s'])
    t6s.appendChild(t6sText)
    newPharmacy.appendChild(t6s)
    
    t7c=mDom.createElement('dutyTime7c')
    t7cText=mDom.createTextNode(data['dutyTime7c'])
    t7c.appendChild(t7cText)
    newPharmacy.appendChild(t7c)
    t7s=mDom.createElement('dutyTime7s')
    t7sText=mDom.createTextNode(data['dutyTime7s'])
    t7s.appendChild(t7sText)
    newPharmacy.appendChild(t7s)
    
    #HierarchyRequestErr: #text nodes cannot have children 에러가 자꾸떠서 이게 최선인가
    lis1=mDom.getElementsByTagName("items")
    lis2=lis1[0]
    lis2.appendChild(newPharmacy)
    print(mDom.toxml())
    f=open("pharmacy.xml",'w',encoding="utf8")
    f.write(mDom.toxml())
    f.close()
    mDom.unlink()

def xmlFree():
    if checkXml():
        PharmacyXml.unlink()
        

