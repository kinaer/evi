# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:54:55 2016

@author: aek
"""


from pharmacymodul import *
PharmacyXml=None
EndFlag=0

def printMenu():
    print("\n 문서로 가져오는 파트입니다.")
    print(" 원하는 메뉴의 번호를 입력하세요,")
    print("1. XML문서 보기")
    print("2. 약국이름목록 출력하기")
    print("3. 지역으로 약국찾기")
    print("4. 지도에 찍기")
    print("--------------------------------")
    print("5. 사업자 등록")
    print("6. 지역 입력으로 찾은 내용 이메일 보내기")
    print("7. 종료")

def menuSelection(num):
    global PharmacyXml
    if num==1:
        printFileXML()
    elif num==2:
        searchPharmacyName("dutyName")
    elif num==3:
        key=str(input("지역을 입력하세요 : "))
        searchPharmacyAddr(key)
    elif num==4:
        key=str(input("약국을 찾을 지역을 입력하세요 : "))
        getAddrToPharmacyList(key)
        searchPharmacyAddr(key)
        keyword=str(input("약국이름을 적으세요 : "))
        displaymap(keyword)
    elif num==5:
        dic=[]
        dic=residentPharmacy()
        AddPharmacy(dic)
        print("등록완료")
    elif num==6:
        sendMail();
    elif num==7:
        xmlFree()
        global EndFlag
        EndFlag=1
    else:
        print("없는 키워드 입니다.")



while(1):
    PharmacyXml=getPharmacyData()
    printMenu()
    
    num=int(input("번호입력 : "))

    menuSelection(num)
    if EndFlag==1:
        break






















