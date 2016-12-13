import requests as r
import json
import ast
import urllib


class RequestManager:

    #TODO: Add response decoder

    @staticmethod
    def get(s, url):
        resp = s.get(url)
        print(url)
        if RequestManager.confirm_response(resp):
            try:
                return json.loads(resp.content.decode("utf-8"))
            except ValueError:
                return resp.decode('utf-8')
        else:
            raise Exception('status code not 200')

    @staticmethod
    def post(s, url):
        resp = s.post(url)
        if RequestManager.confirm_response(resp):
            try:
                return json.loads(resp.content.decode("utf-8"))
            except ValueError:
                return resp
        else:
            raise Exception('status code not 200')

    @staticmethod
    def init_session():
        s = r.Session()
        return s

    @staticmethod
    def confirm_response(resp):
        if 199 < resp.status_code < 300:
            return True
        else:
            print("Status Code: " + str(resp.status_code))
            print("Content: " + str(resp.content))
            return False
