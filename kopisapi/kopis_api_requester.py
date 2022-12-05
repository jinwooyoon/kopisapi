from .get_request import get_requests
from .parser import parse
import json
from .constants import AREA_CODE, GENRE_CODE


class KopisApiRequester:

    def __init__(self, service_key):
        self._service_key = service_key
        self._url = "http://www.kopis.or.kr/openApi/restful/"

    def request_a_type(self, param_type, region=None, genre=None, start_date=None, end_date=None, area=None):

        data_result = []

        if genre is not None:
            for key, value in GENRE_CODE.items():
                if value == genre:
                    genre = key

        if region is not None:
            for key, value in AREA_CODE.items():
                if value == region:
                    region = key

        url = self._url + param_type + '?service=' + self._service_key

        page_count = 1

        params = {"cpage": str(page_count), "rows": "500",
                  "stdate": start_date, "eddate": end_date, "signgucode": region, "shcate": genre, "sharea": area}

        while True:

            data = get_requests(url, params)

            data_list = parse(param_type, data)

            for i in data_list:

                data_result.append(i[0])

                break_parse = i[1]

            if break_parse < 500:

                return data_result

            page_count += 1
            params.update({"cpage": str(page_count)})

    def request_b_type(self, param_type, date_type=None, start_date=None, end_date=None, date=None):

        data_result = []

        url = self._url + param_type + '?service=' + self._service_key

        params = {"ststype": date_type, "stdate": start_date,
                  "eddate": end_date, "date": date}

        data = get_requests(url, params)

        data_list = parse(param_type, data)

        for i in data_list:

            data_result.append(i[0])

        return data_result

    def request_c_type(self, param_type, genre=None, area=None, date_type=None, date=None):

        data_result = []

        url = self._url + param_type + '?service=' + self._service_key
        
        
        if genre is not None:
            for key, value in GENRE_CODE.items():
                if value == genre:
                    genre = key

        if area is not None:
            for key, value in AREA_CODE.items():
                if value == area:
                    area = key


        params = {"ststype": date_type, "date": date,
                    "catecode": genre, "area": area}

        data = get_requests(url, params)

        data_list = parse(param_type, data)

        for i in data_list:
            data_result.append(i[0])

        return data_result
