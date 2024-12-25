from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_staff:
            return HttpResponseForbidden("У вас нет прав для доступа к этой странице.")
        return super().dispatch(request, *args, **kwargs)
