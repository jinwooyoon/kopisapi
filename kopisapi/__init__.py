from .kopis_api_requester import KopisApiRequester


class KopisAPI:
    def __init__(self, service_key):

        self._requester = KopisApiRequester(service_key)

    def get_performance_list(self, start_date, end_date, region=None, genre=None):

        return self._requester.request_a_type(param_type="pblprfr", start_date=start_date, end_date=end_date, region=region, genre=genre)

    def get_performance_facility_list(self, region=None):

        return self._requester.request_a_type(param_type="prfplc", region=region)

    def get_production_company_list(self, genre=None):

        return self._requester.request_a_type(param_type="mnfct", genre=genre)

    def get_festival_list(self, start_date, end_date, region=None, genre=None):

        return self._requester.request_a_type(param_type="prffest", start_date=start_date, end_date=end_date, region=region, genre=genre)

    def get_award_list(self, start_date, end_date,  region=None, genre=None):

        return self._requester.request_a_type(param_type="prfawad", start_date=start_date, end_date=end_date, region=region, genre=genre)

    def get_playwright_list(self, start_date, end_date, region=None, genre=None):

        return self._requester.request_a_type(param_type="prfper", start_date=start_date, end_date=end_date, region=region, genre=genre)

    def get_reservation_status_list(self, date_type, start_date, genre=None, region=None):

        return self._requester.request_c_type(param_type="boxoffice", date_type=date_type, date=start_date, genre=genre, area=region)

    def get_daily_ticket_sales(self, start_month):

        return self._requester.request_b_type(param_type="prfstsTotal", date_type="day", start_date=start_month)

    def get_day_ticket_sales(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsTotal", date_type="dayWeek", start_date=start_date, end_date=end_date)

    def get_monthly_ticket_sales(self, start_year):

        return self._requester.request_b_type(param_type="prfstsTotal", date_type="month", start_date=start_year)

    def get_statistics_by_domestic_abroad(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsCreate", start_date=start_date, end_date=end_date)

    def get_statistics_by_facility(self, start_date, end_date, region=None):

        return self._requester.request_a_type(param_type="prfstsPrfByFct", start_date=start_date, end_date=end_date, area=region)

    def get_statistics_by_region(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsArea", start_date=start_date, end_date=end_date)

    def get_statistics_by_genre(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsCate", start_date=start_date, end_date=end_date)

    def get_statistics_by_performance(self, start_date, end_date, genre=None):

        return self._requester.request_a_type(param_type="prfstsPrfBy", start_date=start_date, end_date=end_date, genre=genre)
