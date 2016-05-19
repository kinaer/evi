# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:54:55 2016

@author: aek
"""

from xml.dom.minidom import *
from xml.etree import *

PharmacyXml=None

def printMenu():
    print("\n 문서로 가져오는 파트입니다.")
    print(" 원하는 메뉴의 번호를 입력하세요,")
    print("1. 파일 불러오기")
    print("2. XML문서 보기")

def menuSelection(num):
    global PharmacyXml
    if num==1:
        PharmacyXml=xmlFileRead()
    elif num==2:
        printFileXml()
        

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






































"""
try:
    xmlop=open(str("pharmacy.xml"));
except IOError:
    print("파일이 같은 위치에 없어.");
else:
    try:
        dom=parse(xmladdr);
    except Exception:
        print("로딩에러")
    
parse(xmlop)
prin
"""
