from django.shortcuts import render, render_to_response, get_object_or_404
import random, string, json
from shorterurl.models import Urls
from django.template.context_processors import csrf
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('shorterurl/index.html', c)


def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id)
    url.save()
    return HttpResponseRedirect(url.http_url)


def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Urls(http_url=url, short_id=short_id)
        b.save()
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error ocurs"}), content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        if not Urls.objects.filter(pk=short_id).exists():
            return short_id












