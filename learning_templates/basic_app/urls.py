from django.conf.urls import url
from basic_app import views

#Template tagging
app_news = 'basic_app'

urlpatterns = [
    path(' relative/',views.relative,name='relative'),
    path(' other/',views.other,name='other'),
]
