from django.conf.urls import url, include

from views import landing_page

urlpatterns = [
    url('^landing_page$', landing_page),
]