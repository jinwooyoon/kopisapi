# KOPIS API
KOPIS(공연 예술 통합 전산망)의 데이터를  
쉽게 활용하기 위해 만든 API입니다.  


## How to install
`pip install kopisapi`


## How to use

```  
import kopisapi

kopis = kopisapi("input your kopis service key")

kopis.get_performance_list(start_date="20220101",end_date="20220102")

```  
- kopisapi service key는 밑에 링크를 통하여 발급 받으실 수 있습니다.   
https://www.kopis.or.kr/por/cs/openapi/openApiInfo.do?menuId=MNU_00074&searchType=total&searchWord=  

- 총 14개의 API 항목을 지원하며 목록은 다음과 같습니다.  
API 마다 인자값이 상이하므로 밑에 예시를 통하여 적절히 사용하시면 됩니다.


example)
```
1. 공연 목록 get_performance_list(start_date="20210101", end_date=20220101")
  
2. 공연시설 목록 get_performance_facility_list()
  
3. 기획/제작사 목록 get_production_company_list()

4. 축제 목록 get_festival_list(start_date="20210101", end_date=20220101")

5. 수상작 목록 get_award_list(start_date="20210101", end_date=20220101")

6. 극작가 목록 get_playwright_list(start_date="20210101", end_date=20220101")

:bulb: start_date, end_date 는 인자값으로 string type의 

7. 예매 상황판 get_reservation_status_list(date_type =(), date, mode= "nationwide")
```


