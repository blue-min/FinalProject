# 1. 뷰의 코드 형식: 함수형, 클래스형
# 함수형: request를 매개변수로 받고 (추가 매개변수 가능), 모양은 함수, 내가 원하는대로 동작들을 설계하고 만들고 싶을 때
# 클래스형: CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고 상속받아 사용한다
# 장고의 제네릭 뷰를 많이 사용한다
import concurrent.futures

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # 어떤 계산이나 데이터베이스 조회, 수정, 등록
    # 응답 메시지를 만들어 반환
    html = '<html><body>Index Page <html></body>'
    return HttpResponse(html)





