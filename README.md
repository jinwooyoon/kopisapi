# KOPIS API
KOPIS(공연 예술 통합 전산망)의 데이터를  
쉽게 활용하기 위해 만든 API입니다.  


## How to install
`pip install kopisapi`


## How to use

```python
import kopisapi

kopis = kopisapi("INPUT YOUR KOPIS SERVICE KEY")

kopis.get_performance_list(start_date="20220101",end_date="20220102")

```  
:bulb: `KOPIS SERVICE KEY` 는 밑에 링크를 통하여 발급 받으실 수 있습니다.   
https://www.kopis.or.kr/por/cs/openapi/openApiInfo.do?menuId=MNU_00074&searchType=total&searchWord=  
  
  
  
  

### :information_desk_person: 총 14개의 API 항목을 지원하며 목록은 다음과 같습니다.

```
1. 공연 목록 get_performance_list(start_date="20210101", end_date=20220101")
  
2. 공연시설 목록 get_performance_facility_list()
  
3. 기획/제작사 목록 get_production_company_list()

4. 축제 목록 get_festival_list(start_date="20210101", end_date=20220101")

5. 수상작 목록 get_award_list(start_date="20210101", end_date=20220101")

6. 극작가 목록 get_playwright_list(start_date="20210101", end_date=20220101")

7. 예매 상황판 get_reservation_status_list(date_type="day", date="20220101", mode="nationwide")

8. 일별 티켓판매수 및 티켓판매액 get_daily_ticket_sales(start_month="202201")

9. 월별 티켓판매수 및 티켓판매액 get_monthly_ticket_sales(start_year="2022")

10. 국내/내한별 통계 get_statistics_by_domestic_abroad(start_date="20210101", end_date=20220101")

11. 공연 시설별 통계 get_statistics_by_facility(start_date="20210101", end_date=20220101")

12. 지역별 통계 get_statistics_by_region(start_date="20210101", end_date=20220101")

13. 장르별 통계 get_statistics_by_genre(start_date="20210101", end_date=20220101")

14. 공연별 통계 get_statistics_by_performance(start_date="20210101", end_date=20220101")
```

:bulb:  API 마다 인자값이 상이하므로 밑에 예시를 통하여 적절히 값을 입력하시면 됩니다.  

 API에 입력되는 인자값은 모두 `string type`입니다.
  
  
* start_date = "년/월/일"
* end_date = "년/월/일"
* date = "년/월/일"
* start_month = "년/월"
* start_year = "년"
* date_type = "month" or "week" or "day"
* mode = "nationwide" or "region" [nationwide는 전국 공연 예매 랭킹 순위 / region은 지역별 공연 예매 랭킹 순위]

