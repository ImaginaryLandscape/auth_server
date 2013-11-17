from django.contrib import admin
from auth_server.models import AuthenticationLog

class AuthenticationLogAdmin(admin.ModelAdmin):
    list_display = ['created', 'username', 'client_information']
    readonly_fields = ['username', 'client_information', 'created']
    search_fields = ['username', 'client_information']

    def get_actions(self, request):
        return []
    
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(AuthenticationLog, AuthenticationLogAdmin)