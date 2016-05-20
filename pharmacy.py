# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:54:55 2016

@author: aek
"""

from xml.dom.minidom import *
from xml.etree import ElementTree

PharmacyXml=None
EndFlag=0

def printMenu():
    print("\n 문서로 가져오는 파트입니다.")
    print(" 원하는 메뉴의 번호를 입력하세요,")
    print("1. 파일 불러오기")
    print("2. XML문서 보기")
    print("3. 약국이름목록 출력하기")
    print("4. 지역으로 약국찾기")
    print("5. 종료")

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
        xmlFree()
        global EndFlag
        EndFlag=1

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
        
    """
    PharmacyXml
    response=PharmacyXml.childNodes
    body=response[0].childNodes
   
     """
def searchPharmacyAddr(key):
    global PharmacyXml
    if not checkXml():
        return
    
    items=PharmacyXml.getElementsByTagName("item")
    for item in items:
        subitem=item.childNodes
        for a in subitem:
            if a.nodeName=="dutyName":
                name=a
            elif a.nodeName=="dutyAddr":
                addr=a
        if (addr.firstChild.nodeValue.find(key)>=0):
            print(name.firstChild.nodeValue)
            """
            nameItems=item.childNodes
        if item.nodeName=="dutyAddr":
            subitems=item.childNodes
            if(subitems.firstChild.nodeValue.find(key)>=0):
                print(nameItems.firstChild.nodeValue)
             """  
     
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






















