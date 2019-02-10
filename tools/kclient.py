import json
import http.client as client


DEFAULT_TIMEOUT = 10.0


class KClient:
    def __init__(self, timeout=DEFAULT_TIMEOUT):
        print('creating http client KClient object')

    @staticmethod
    def get_data(server: str, url: str, **kwargs):
        conn = client.HTTPSConnection(server, timeout=DEFAULT_TIMEOUT)

        parsed_url = url
        for key in kwargs:
            parsed_url = parsed_url.replace("[%s]" % key, kwargs[key])

        conn.request("GET", parsed_url)
        response = conn.getresponse()

        return json.loads(response.read())
