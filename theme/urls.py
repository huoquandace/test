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

    path('form_basic', FormBasicView.as_view(), name='form_basic'),
    path('advanced_component', FormAdvanceComponentView.as_view(), name='advanced_component'),
    path('form_wizard', FormWizardView.as_view(), name='form_wizard'),
    path('html5_editor', FormHtml5EditorView.as_view(), name='html5_editor'),
    path('form_pickers', FormPickersView.as_view(), name='form_pickers'),
    path('image_cropper', FormImageCropperView.as_view(), name='image_cropper'),
    path('image_dropzone', FormImageDropzoneView.as_view(), name='image_dropzone'),

    path('basic_table', TableBasicView.as_view(), name='basic_table'),
    path('datatable', TableDataView.as_view(), name='datatable'),

    path('calendar', CalendarView.as_view(), name='calendar'),

]
