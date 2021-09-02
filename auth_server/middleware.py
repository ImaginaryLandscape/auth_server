from urllib import parse
from django.utils.deprecation import MiddlewareMixin

class FixZopeMiddleware(MiddlewareMixin):

	def process_request(self, request):
		r = parse.urlparse(request.path_info).path
		if not r:
			r = "/"
		request.path = r
		request.path_info = r
		
