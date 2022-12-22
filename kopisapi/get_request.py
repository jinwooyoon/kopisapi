import requests
from requests.sessions import Session
from requests.adapters import HTTPAdapter, Retry


def get_requests(url, params):

    with Session() as session:
        retries = 3
        backoff_factor = 0.3
        RETRY_AFTER_STATUS_CODES = (500, 503, 504)

        retry = Retry(
            total=retries,
            connect=retries,
            read=retries,
            backoff_factor=backoff_factor,
            status_forcelist=RETRY_AFTER_STATUS_CODES
        )

        adapter = HTTPAdapter(max_retries=retry)

        session.mount("http://", adapter)

        session.mount("https://", adapter)

        data = session.get(url, params=params,verify=False)
        
        data.raise_for_status()
        
        

    return data.text
