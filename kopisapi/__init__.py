from .kopis_api_requester import KopisApiRequester

class KopisAPI:
    def __init__(self, service_key):

        self._requester = KopisApiRequester(service_key)

    def get_performance_list(self, start_date, end_date):

        return self._requester.request_a_type(param_type="pblprfr", start_date=start_date, end_date=end_date)

    def get_performance_facility_list(self):

        return self._requester.request_a_type(param_type="prfplc")

    def get_production_company_list(self):

        return self._requester.request_a_type(param_type="mnfct")

    def get_festival_list(self, start_date, end_date):

        return self._requester.request_a_type(param_type="prffest", start_date=start_date, end_date=end_date)

    def get_award_list(self, start_date, end_date):

        return self._requester.request_a_type(param_type="prfawad", start_date=start_date, end_date=end_date)

    def get_playwright_list(self, start_date, end_date):

        return self._requester.request_a_type(param_type="prfper", start_date=start_date, end_date=end_date)

    def get_reservation_status_list(self, date_type, date, mode="nationwide"):

        if mode == "nationwide":

            return self._requester.request_b_type(param_type="boxoffice", date_type=date_type, date=date)

        if mode == "region":

            return self._requester.request_c_type(param_type="boxoffice", date_type=date_type, date=date)

    def get_daily_ticket_sales(self, start_month):

        return self._requester.request_b_type(param_type="prfstsTotal", date_type="day", start_date=start_month)

    def get_monthly_ticket_sales(self, start_year):

        return self._requester.request_b_type(param_type="prfstsTotal", date_type="month", start_date=start_year)

    def get_statistics_by_domestic_abroad(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsCreate", start_date=start_date, end_date=end_date)

    def get_statistics_by_facility(self, start_date, end_date):

        return self._requester.request_a_type(param_type="prfstsPrfByFct", start_date=start_date, end_date=end_date)

    def get_statistics_by_region(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsArea", start_date=start_date, end_date=end_date)

    def get_statistics_by_genre(self, start_date, end_date):

        return self._requester.request_b_type(param_type="prfstsCate", start_date=start_date, end_date=end_date)

    def get_statistics_by_performance(self, start_date, end_date):
        return self._requester.request_a_type(param_type="prfstsPrfBy", start_date=start_date, end_date=end_date)
