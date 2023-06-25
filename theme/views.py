from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'mock/index.html'

class IndexView2(TemplateView):
    template_name = 'mock/index2.html'

class IndexView3(TemplateView):
    template_name = 'mock/index3.html'