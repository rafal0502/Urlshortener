from django.urls import include, url

app_name = 'shorterurl'

urlpatterns = [
    path('', views.index, name='home'),
    path('<short_id>', views.redirect_original, name='redirect'),
    path('makeshort/', views.shorter_url, name='shorterurl')
]

