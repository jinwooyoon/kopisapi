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
- kopisapi service key는  
https://www.kopis.or.kr/por/cs/openapi/openApiInfo.do?menuId=MNU_00074&searchType=total&searchWord= 에서 받으실 수 있습니다.

