from django.urls import path
from theme.views import *


app_name = 'theme'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index2', IndexView2.as_view(), name='index2'),
    path('index3', IndexView3.as_view(), name='index3'),

    path('error_400', ErrorPage400View.as_view(), name='error_400'),
    path('error_403', ErrorPage403View.as_view(), name='error_403'),
    path('error_404', ErrorPage404View.as_view(), name='error_404'),
    path('error_500', ErrorPage500View.as_view(), name='error_500'),
    path('error_503', ErrorPage503View.as_view(), name='error_503'),
]
