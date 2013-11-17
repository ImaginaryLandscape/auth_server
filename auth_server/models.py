from django.db import models
from jsonfield import JSONField
from .utils import get_client_ip, lookup_domain

class AuthenticationLogManager(models.Manager):
    
    def record(self, username, request):
        client_information = get_client_ip(request)
        client_hostname_info = lookup_domain(client_information['ip_address'])
        client_information.update(client_hostname_info)
        self.create(username=username, client_information=client_information)

class AuthenticationLog(models.Model):
    created = models.DateTimeField(u'Created Date', auto_now_add=True)
    username = models.CharField(max_length=100)
    client_information = JSONField(blank=True, null=True)
    
    objects = AuthenticationLogManager()