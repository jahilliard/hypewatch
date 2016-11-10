import requests as r
import urllib


class RequestManager:

    @staticmethod
    def get(url):
        resp = r.get(url)
        if RequestManager.confirm_response(resp):
            try:
                return resp.json()
            except ValueError:
                return resp.decode('utf-8')
        else:
            raise Exception('status code not 200')

    @staticmethod
    def confirm_response(resp):
        if 199 < resp.status_code < 300:
            return True
        else:
            print("Status Code: " + str(resp.status_code))
            return False
