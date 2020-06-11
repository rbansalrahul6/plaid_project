from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(
            template_name='user/index.html',
            extra_context={'pk': settings.PLAID_PUBLIC_KEY}
        )
    ),
    path(
        'login/',
        TemplateView.as_view(template_name='user/login.html')
    ),
    path(
        'accounts/',
        TemplateView.as_view(template_name='user/accounts.html'),
        name='accounts'
    )
]