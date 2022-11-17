from .get_request import get_requests
from .parser import parse
import json
from .constants import AREA_CODE, GENRE_CODE


class KopisApiRequester:

    def __init__(self, service_key):
        self._service_key = service_key
        self._url = "http://www.kopis.or.kr/openApi/restful/"
        self.data_result = []

    def request_a_type(self, param_type, start_date=None, end_date=None):

        url = self._url + param_type + '?service=' + self._service_key

        page_count = 1

        params = {"cpage": str(page_count), "rows": "500",
                  "stdate": start_date, "eddate": end_date}

        while True:

            data = get_requests(url, params)

            data_list = parse(param_type, data)

            break_parse = None

            for i in data_list:

                self.data_result.append(json.dumps(i[0], ensure_ascii=False))

                break_parse = i[1]

            if break_parse < 500:

                return self.data_result

            page_count += 1
            params.update({"cpage": str(page_count)})

    def request_b_type(self, param_type, date_type=None, start_date=None, end_date=None, date=None):

        url = self._url + param_type + '?service=' + self._service_key

        params = {"ststype": date_type, "stdate": start_date,
                  "eddate": end_date, "date": date}

        data = get_requests(url, params)

        data_list = parse(param_type, data)

        for i in data_list:

            self.data_result.append(json.dumps(i[0], ensure_ascii=False))

        return self.data_result

    def request_c_type(self, param_type, date_type=None, date=None):

        url = self._url + param_type + '?service=' + self._service_key

        for genre in GENRE_CODE:

            for area in AREA_CODE:
                params = {"ststype": date_type, "date": date,
                          "catecode": {genre}, "area": {area}}

                data = get_requests(url, params)

                data_list = parse(param_type, data)

                for i in data_list:
                    self.data_result.append(json.dumps(
                        i[0], ensure_ascii=False))

            return self.data_result
