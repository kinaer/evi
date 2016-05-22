# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:54:55 2016

@author: aek
"""

from xml.dom.minidom import *
import webPharmacy
PharmacyXml=None
EndFlag=0

def printMenu():
    print("\n 문서로 가져오는 파트입니다.")
    print(" 원하는 메뉴의 번호를 입력하세요,")
    print("1. 파일 불러오기")
    print("2. XML문서 보기")
    print("3. 약국이름목록 출력하기")
    print("4. 지역으로 약국찾기")
    print("5. 지역약국 html로 출력")
    print("--------------------------------")
    print("6. 사업자 등록")
    print("7. 웹에서 xml불러오기")
    print("8. 종료")

def menuSelection(num):
    global PharmacyXml
    if num==1:
        PharmacyXml=xmlFileRead()
    elif num==2:
        printFileXML()
    elif num==3:
        searchPharmacyName("dutyName")
    elif num==4:
        key=str(input("지역을 입력하세요 : "))
        searchPharmacyAddr(key)
    elif num==5:
        key=str(input("약국을 찾을 지역을 입력하세요 : "))
        html=MakeHTML(getAddrToPharmacyList(key))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif num==6:
        dic=[]
        dic=residentPharmacy()
        AddPharmacy(dic)
        print("등록완료")
    elif num==7:
        page=str(input("확인할 페이지를 입력하세요.(최대 21) : "))
        PharmacyXml=getPharmacyData(page)
    elif num==8:
        xmlFree()
        global EndFlag
        EndFlag=1
    else:
        print("없는 키워드 입니다.")

def residentPharmacy():
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
        x=open("pharmacy.xml", encoding="utf8")
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


def getAddrToPharmacyList(key):
    global PharmacyXml
   
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
            list1.append((name.firstChild.nodeValue,addr.firstChild.nodeValue,tel.firstChild.nodeValue))
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
    
    newPharmacy=PharmacyXml.createElement('item')
    
    addr=PharmacyXml.createElement('dutyAddr')
    addrText=PharmacyXml.createTextNode(data['dutyAddr'])
    addr.appendChild(addrText)
    newPharmacy.appendChild(addr)
    if data['dutyMapimg']!=None:
        maping=PharmacyXml.createElement('dutyMapimg')
        mText=PharmacyXml.createTextNode(data['dutyMapimg'])
        maping.appendChild(mText)
        newPharmacy.appendChild(maping)
    name=PharmacyXml.createElement('dutyName')
    nText=PharmacyXml.createTextNode(data['dutyName'])
    name.appendChild(nText)
    newPharmacy.appendChild(name)
    tel=PharmacyXml.createElement('dutyTel1')
    telText=PharmacyXml.createTextNode(data['dutyTel1'])
    tel.appendChild(telText)
    newPharmacy.appendChild(tel)
    
    t1c=PharmacyXml.createElement('dutyTime1c')
    t1cText=PharmacyXml.createTextNode(data['dutyTime1c'])
    t1c.appendChild(t1cText)
    newPharmacy.appendChild(t1c)
    t1s=PharmacyXml.createElement('dutyTime1s')
    t1sText=PharmacyXml.createTextNode(data['dutyTime1s'])
    t1s.appendChild(t1sText)
    newPharmacy.appendChild(t1s)
    
    t2c=PharmacyXml.createElement('dutyTime2c')
    t2cText=PharmacyXml.createTextNode(data['dutyTime2c'])
    t2c.appendChild(t2cText)
    newPharmacy.appendChild(t2c)
    t2s=PharmacyXml.createElement('dutyTime2s')
    t2sText=PharmacyXml.createTextNode(data['dutyTime2s'])
    t2s.appendChild(t2sText)
    newPharmacy.appendChild(t2s)
    
    t3c=PharmacyXml.createElement('dutyTime3c')
    t3cText=PharmacyXml.createTextNode(data['dutyTime3c'])
    t3c.appendChild(t3cText)
    newPharmacy.appendChild(t3c)
    t3s=PharmacyXml.createElement('dutyTime3s')
    t3sText=PharmacyXml.createTextNode(data['dutyTime3s'])
    t3s.appendChild(t3sText)
    newPharmacy.appendChild(t3s)
    
    t4c=PharmacyXml.createElement('dutyTime4c')
    t4cText=PharmacyXml.createTextNode(data['dutyTime4c'])
    t4c.appendChild(t4cText)
    newPharmacy.appendChild(t4c)
    t4s=PharmacyXml.createElement('dutyTime4s')
    t4sText=PharmacyXml.createTextNode(data['dutyTime4s'])
    t4s.appendChild(t4sText)
    newPharmacy.appendChild(t4s)
    
    t5c=PharmacyXml.createElement('dutyTime5c')
    t5cText=PharmacyXml.createTextNode(data['dutyTime5c'])
    t5c.appendChild(t5cText)
    newPharmacy.appendChild(t5c)
    t5s=PharmacyXml.createElement('dutyTime5s')
    t5sText=PharmacyXml.createTextNode(data['dutyTime5s'])
    t5s.appendChild(t5sText)
    newPharmacy.appendChild(t5s)
    
    t6c=PharmacyXml.createElement('dutyTime6c')
    t6cText=PharmacyXml.createTextNode(data['dutyTime6c'])
    t6c.appendChild(t6cText)
    newPharmacy.appendChild(t6c)
    t6s=PharmacyXml.createElement('dutyTime6s')
    t6sText=PharmacyXml.createTextNode(data['dutyTime6s'])
    t6s.appendChild(t6sText)
    newPharmacy.appendChild(t6s)
    
    t7c=PharmacyXml.createElement('dutyTime7c')
    t7cText=PharmacyXml.createTextNode(data['dutyTime7c'])
    t7c.appendChild(t7cText)
    newPharmacy.appendChild(t7c)
    t7s=PharmacyXml.createElement('dutyTime7s')
    t7sText=PharmacyXml.createTextNode(data['dutyTime7s'])
    t7s.appendChild(t7sText)
    newPharmacy.appendChild(t7s)
    
    PharmacyList=PharmacyXml.firstChild
    PharmacyList.appendChild(newPharmacy)

def xmlFree():
    if checkXml():
        PharmacyXml.unlink()
        


PharmacyXml=xmlFileRead()
while(1):
    printMenu()

    num=int(input("번호입력 : "))

    menuSelection(num)
    if EndFlag==1:
        break






















