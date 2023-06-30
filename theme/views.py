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


class UIButtonsView(TemplateView):
    template_name = 'mock/ui_elements/ui-buttons.html'

class UICardsView(TemplateView):
    template_name = 'mock/ui_elements/ui-cards.html'

class UICardsHoverView(TemplateView):
    template_name = 'mock/ui_elements/ui-cards-hover.html'

class UIModalsView(TemplateView):
    template_name = 'mock/ui_elements/ui-modals.html'

class UITabsView(TemplateView):
    template_name = 'mock/ui_elements/ui-tabs.html'

class UITooltipPopoverView(TemplateView):
    template_name = 'mock/ui_elements/ui-tooltip-popover.html'

class UISweetAlertView(TemplateView):
    template_name = 'mock/ui_elements/ui-sweet-alert.html'

class UINotificationView(TemplateView):
    template_name = 'mock/ui_elements/ui-notification.html'

class UITimelineView(TemplateView):
    template_name = 'mock/ui_elements/ui-timeline.html'

class UIProgressbarView(TemplateView):
    template_name = 'mock/ui_elements/ui-progressbar.html'

class UITypographyView(TemplateView):
    template_name = 'mock/ui_elements/ui-typography.html'

class UIListGroupView(TemplateView):
    template_name = 'mock/ui_elements/ui-list-group.html'

class UIRangeSliderView(TemplateView):
    template_name = 'mock/ui_elements/ui-range-slider.html'

class UICarouselView(TemplateView):
    template_name = 'mock/ui_elements/ui-carousel.html'


class IconBootstrapView(TemplateView):
    template_name = 'mock/icons/bootstrap-icon.html'

class IconFontAwesomeView(TemplateView):
    template_name = 'mock/icons/font-awesome.html'

class IconFoundationView(TemplateView):
    template_name = 'mock/icons/foundation.html'

class IconIoniconsView(TemplateView):
    template_name = 'mock/icons/ionicons.html'

class IconThemifyView(TemplateView):
    template_name = 'mock/icons/themify.html'

class IconCustomView(TemplateView):
    template_name = 'mock/icons/custom-icon.html'


class HighchartView(TemplateView):
    template_name = 'mock/charts/highchart.html'

class KnobchartView(TemplateView):
    template_name = 'mock/charts/knob-chart.html'

class JvectormapView(TemplateView):
    template_name = 'mock/charts/jvectormap.html'

class ApexchartView(TemplateView):
    template_name = 'mock/charts/apexcharts.html'


class ChatView(TemplateView):
    template_name = 'mock/chat/chat.html'


class InvoiceView(TemplateView):
    template_name = 'mock/invoice/invoice.html'

class SitemapView(TemplateView):
    template_name = 'mock/sitemap/sitemap.html'

class CommingSoonView(TemplateView):
    template_name = 'mock/comming_soon.html'


class IntroductionView(TemplateView):
    template_name = 'mock/documentation/introduction.html'

class GettingStartedView(TemplateView):
    template_name = 'mock/documentation/getting-started.html'

class ColorSettingsView(TemplateView):
    template_name = 'mock/documentation/color-settings.html'

class ThirdPartyPluginsView(TemplateView):
    template_name = 'mock/documentation/third-party-plugins.html'


class LoginView(TemplateView):
    template_name = 'mock/additional_pages/login.html'

class RegisterView(TemplateView):
    template_name = 'mock/additional_pages/register.html'

class ForgotPasswordView(TemplateView):
    template_name = 'mock/additional_pages/forgot-password.html'

class ResetPasswordView(TemplateView):
    template_name = 'mock/additional_pages/reset-password.html'