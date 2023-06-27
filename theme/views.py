from django.views.generic import TemplateView
from django.shortcuts import HttpResponse

class IndexView(TemplateView):
    template_name = 'mock/dashboards/index.html'

class IndexView2(TemplateView):
    template_name = 'mock/dashboards/index2.html'

class IndexView3(TemplateView):
    template_name = 'mock/dashboards/index3.html'


class ErrorPage400View(TemplateView):
    template_name = 'mock/error_pages/400.html'

class ErrorPage403View(TemplateView):
    template_name = 'mock/error_pages/403.html'

class ErrorPage404View(TemplateView):
    template_name = 'mock/error_pages/404.html'

class ErrorPage500View(TemplateView):
    template_name = 'mock/error_pages/500.html'

class ErrorPage503View(TemplateView):
    template_name = 'mock/error_pages/503.html'


class FormBasicView(TemplateView):
    template_name = 'mock/forms/form-basic.html'

class FormAdvanceComponentView(TemplateView):
    template_name = 'mock/forms/advanced-components.html'

class FormWizardView(TemplateView):
    template_name = 'mock/forms/form-wizard.html'

class FormHtml5EditorView(TemplateView):
    template_name = 'mock/forms/html5-editor.html'

class FormPickersView(TemplateView):
    template_name = 'mock/forms/form-pickers.html'

class FormImageCropperView(TemplateView):
    template_name = 'mock/forms/image-cropper.html'
    
class FormImageDropzoneView(TemplateView):
    template_name = 'mock/forms/image-dropzone.html'

    def post(self, request, *args, **kwargs):
        return HttpResponse('123123')
    

class TableBasicView(TemplateView):
    template_name = 'mock/tables/basic-table.html'

class TableDataView(TemplateView):
    template_name = 'mock/tables/datatable.html'


class CalendarView(TemplateView):
    template_name = 'mock/calendar/calendar.html'
