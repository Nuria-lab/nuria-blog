from django import urls
from django.urls import path
from .views import (BlogHomePageView,)
#ñrkljrlyjelkujy
app_name='blog'   #blog/bloghome

urlpatterns=[
    path('bloghome/',BlogHomePageView.as_view, name='home'),
]