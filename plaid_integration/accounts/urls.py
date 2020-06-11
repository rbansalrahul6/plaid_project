from rest_framework.routers import DefaultRouter

from .views import PlaidLinkViewSet, IdentityViewSet, TransactionsViewSet

app_name = 'accounts'
router = DefaultRouter()
router.register(r'plain-link', PlaidLinkViewSet, basename='plaid-link')
router.register(r'identity', IdentityViewSet, basename='plaid-identity')
router.register(r'transactions', TransactionsViewSet, basename='transactions')
urlpatterns = router.urls