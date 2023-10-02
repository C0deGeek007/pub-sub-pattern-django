from django.http import HttpResponseBadRequest
from cache.redis import redis_connection

class CheckHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the 'X-My-Header' header is present in the request
        if(redis_connection.get("user1@gmail.com") is None):
            return HttpResponseBadRequest('cache does not have user')
        
        # If the header is present, continue processing the request
        response = self.get_response(request)
        return response