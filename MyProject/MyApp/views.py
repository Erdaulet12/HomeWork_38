from django.views.generic import TemplateView
from .mixins import CustomLoginRequiredMixin

# Create your views here.


class ProtectedView(CustomLoginRequiredMixin, TemplateView):
    template_name = 'protected_page.html'
