from django.urls import include, path
from shorterurl import views

app_name = 'shorterurl'

urlpatterns = [
    path('', views.index, name='index'),
    path('<short_id>', views.redirect_original, name='redirect'),
    path('makeshort/', views.shorten_url, name='shortenurl'),
]

