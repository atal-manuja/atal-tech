from django.conf.urls import url, include
from .views import CheckView
from rest_framework.urlpatterns import format_suffix_patterns
print('check.urls')
from django.urls import path

urlpatterns = [
    url('', CheckView.as_view())
]
