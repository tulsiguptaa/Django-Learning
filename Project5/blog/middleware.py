import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"[{datetime.datetime.now()}] Request URL: {request.path}")

    def process_response(self, response, request):
        print(f"[{datetime.datetime.now()}] Response Status code: {response.status_code}")
        return response
