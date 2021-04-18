"""Middleware."""
import time

from logger.models import Log


class LoggerMiddleware:
    """LoggerMiddleware class."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        if '/admin/' not in request.path:
            diff = time.time() - start
            log = Log(path=request.path, method=request.method, execution_time_sec=diff)
            log.save()
        return response