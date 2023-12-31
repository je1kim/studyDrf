
# [Self Study] 백엔드를 위한 DJANGO REST FRAMEWORK with Python

[학습 일지]
  * 2023-11-10 : myweb 프로젝트를 학습(게시판 CRUD)
  * 2023-11-11 : mytodo 프로젝트 학습(TODO 리스트 CRUD)
  * 2023-11-12 : django-rest-framework 시리얼라이즈(serialize) 첫 시작
    - serialize : "데이터 구조나 오브젝트 상태를 동일하게 하거나 다른 컴퓨터 환경에 저장(이를테면 파일이나 메모리 버퍼에서, 또는 네트워크 연결ㄹ 링크 간 전송) 하고, 나중에 재구성할 수 잇는 포맷으로 변환하는 과정
    - python에서는 serialize를 통해 JSON 형식으로 변환하여 client에 전송
  * 2023-11-13 : 함수 기반 뷰 API와 클래스 기반 뷰 API 만들고 자료 조회 및 생성 공부
    - FBV(Function Based View) : 함수기반 views
    - CBV(Class Based View) : 클래스 기반 뷰
      => 아주 기본척인 형태에서 다양한 방법으로 확정될 수 있다는 장점이 있음
    - FBV와 CBV의 성능의 큰 차이는 없음

    *** DRF 개발 절차 <br/>
    (1) MODEL <br/>
    (2) Serializers <br/>
    (3) Views <br/>
    (4) URLs <br/>
    (5) 다시 2번으로 <br/>

  * 2023-11-14 : DRF mixins/generics/viewset & Router  학습 ; 중복적으로 사용하는 내용을 간소화 시켜주는 기능을 함
    - [mixins]
      (1) 목록 가져오기 (GET) (list)                  - ListModelMixin     <br/>
      (2) 정보 등록하기 (POST) (create)               - CreateModelMixin <br/>
      (3) 특정 정보 가져오기 (GET) (retrieve) ; 검색    - RetrieveModelMixin<br/>
      (4) 특정 정보 수정하기 (PUT) (update)            - UpdateModelMixin<br/>
      (5) 특정 정보 삭제하기 (DELETE) (destory)        - DestroyModelMixin<br/>
    - [generics]  ** generics 내부를 보면 결국 mixins 조합
      (1) generics.ListAPIView (전체 목록)<br/>
      (2) generics.CreateAPIView (생성)<br/>
      (3) generics.RetrieveAPIView (1개 조회)<br/>
      (4) generics.UpdateAPIView (1개 수정)<br/>
      (5) generics.DestroyAPIView (1개 삭제)<br/>
      (6) generics.ListCreateAPIView (전체 목록 + 생성)<br/>
      (7) generics.RetrieveUpdateAPIView (1개 + 1개 수정)<br/>
      (8) generics.RetrieveDestroyAPIView (1개 + 1개 삭제)<br/>
      (9) generics.RetrieveUpdateDestoryAPIView (1개 + 1개 수정 + 1개 삭제)<br/>
    - [ViewSet] ; 하나의 클래스로 위 과정을 모두 처리 ** 마찬가지로 mixins 기반

      
    *** Check !!<br/>
      : ViewSet & Router와 같이 개발자를 위한 강력한 편의를 제공하는 반면, 무언가를 커스텀할 때 한계가 있다는 점을 알아둘 것!!!!<br/>
  
  * 2023-11-18 : DRF 를 이용한 Todo 페이지 만들기
  
  * 2023-12-04 : DRF 마지막 챕터 게시판 만들기
    - 회원관련기능
    - 게시글 관련 기능
    - 댓글 관련 기능

  * 2023-12-06 : DRF 게시판 만들기 로그인 기능 학습
    - 로그인 계정을 만들고 Token 등록
    - 로그인 시 토큰이 잘 조회되는지 확인