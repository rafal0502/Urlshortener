from django.contrib import admin
from shorterurl.models import Urls
# Register your models here.

class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'http_url')

admin.site.register(Urls, UrlsAdmin)
