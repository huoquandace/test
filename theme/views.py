from django.views.generic import TemplateView


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