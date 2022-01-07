from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home'

class SnackListView(TemplateView):
    template_name = 'snacks-view'
    
class SnackDetailView(TemplateView):
    template_name = 'snacks-detail'    