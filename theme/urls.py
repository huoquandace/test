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

    path('ui_buttons', UIButtonsView.as_view(), name='ui_buttons'),
    path('ui_cards', UICardsView.as_view(), name='ui_cards'),
    path('ui_cards_hover', UICardsHoverView.as_view(), name='ui_cards_hover'),
    path('ui_modals', UIModalsView.as_view(), name='ui_modals'),
    path('ui_tabs', UITabsView.as_view(), name='ui_tabs'),
    path('ui_tooltip_popover', UITooltipPopoverView.as_view(), name='ui_tooltip_popover'),
    path('ui_sweet_alert', UISweetAlertView.as_view(), name='ui_sweet_alert'),
    path('ui_notification', UINotificationView.as_view(), name='ui_notification'),
    path('ui_timeline', UITimelineView.as_view(), name='ui_timeline'),
    path('ui_progressbar', UIProgressbarView.as_view(), name='ui_progressbar'),
    path('ui_typography', UITypographyView.as_view(), name='ui_typography'),
    path('ui_list_group', UIListGroupView.as_view(), name='ui_list_group'),
    path('ui_range_slider', UIRangeSliderView.as_view(), name='ui_range_slider'),
    path('ui_carousel', UICarouselView.as_view(), name='ui_carousel'),

    path('icon_bootstrap', IconBootstrapView.as_view(), name='icon_bootstrap'),
    path('icon_font_awesome', IconFontAwesomeView.as_view(), name='icon_font_awesome'),
    path('icon_foundation', IconFoundationView.as_view(), name='icon_foundation'),
    path('icon_ionicons', IconIoniconsView.as_view(), name='icon_ionicons'),
    path('icon_themify', IconThemifyView.as_view(), name='icon_themify'),
    path('icon_custom', IconCustomView.as_view(), name='icon_custom'),

    path('highchart', HighchartView.as_view(), name='highchart'),
    path('knobchart', KnobchartView.as_view(), name='knobchart'),
    path('jvectormap', JvectormapView.as_view(), name='jvectormap'),
    path('apexchart', ApexchartView.as_view(), name='apexchart'),

    path('chat', ChatView.as_view(), name='chat'),

    path('invoice', InvoiceView.as_view(), name='invoice'),

    path('sitemap', SitemapView.as_view(), name='sitemap'),
    
    path('comming_soon', CommingSoonView.as_view(), name='comming_soon'),

    path('introduction', IntroductionView.as_view(), name='introduction'),
    path('getting_started', GettingStartedView.as_view(), name='getting_started'),
    path('color_settings', ColorSettingsView.as_view(), name='color_settings'),
    path('third_party_plugins', ThirdPartyPluginsView.as_view(), name='third_party_plugins'),

    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('forgot_password', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset_password', ResetPasswordView.as_view(), name='reset_password'),
]
