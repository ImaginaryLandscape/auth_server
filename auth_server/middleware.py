try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class FixZopeMiddleware(object):

    def process_request(self, request):
        r = urlparse(request.path_info).path
        if not r:
            r = "/"
        request.path = r
        request.path_info = r
