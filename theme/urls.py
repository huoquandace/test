from django.urls import path
from theme.views import *


app_name = 'theme'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index2', IndexView2.as_view(), name='index2'),
    path('index3', IndexView3.as_view(), name='index3'),

    path('error_404', ErrorPage404View.as_view(), name='error_404')
]
