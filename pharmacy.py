# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:54:55 2016

@author: aek
"""


from webPharmacy import *
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
    print("8. 지역 입력으로 찾은 내용 이메일 보내기")
    print("9. 종료")

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
        page=str(input("확인할 페이지를 입력하세요.(최대 20) : "))
        PharmacyXml=getPharmacyData(page)
    elif num==8:
        sendMail();
    elif num==9:
        xmlFree()
        global EndFlag
        EndFlag=1
    else:
        print("없는 키워드 입니다.")



while(1):
    printMenu()

    num=int(input("번호입력 : "))

    menuSelection(num)
    if EndFlag==1:
        break






















