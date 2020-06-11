from django.shortcuts import render
from django.db import transaction
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from plaid_integration.accounts.models import PlaidToken
from plaid_integration.plaid import plaid_client

# Create your views here.

class PlaidLinkViewSet(GenericViewSet):
    @transaction.atomic()
    def create(self, request: Request) -> Response:
        public_token = request.data['public_token']
        exchange = plaid_client.Item.public_token.exchange(public_token)
        token, created = PlaidToken.objects.get_or_create(
            user=request.user,
            defaults={'access_token': exchange['access_token']}
        )
        if not created:
            token.access_token = exchange['access_token']
            token.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IdentityViewSet(GenericViewSet):
    def list(self, request: Request) -> Response:
        try:
            token = PlaidToken.objects.get(user=request.user)
        except PlaidToken.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        plaid_resp = plaid_client.Identity.get(access_token=token.access_token)
        return Response(data={'content': plaid_resp})


class TransactionsViewSet(GenericViewSet):
    def list(self, request: Request) -> Response:
        try:
            token = PlaidToken.objects.get(user=request.user)
        except PlaidToken.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        plaid_resp = plaid_client.Transactions.get(
            access_token=token.access_token,
            start_date='2010-01-01',
            end_date='2020-01-31',
            account_ids=[request.query_params['account']]
        )
        return Response(data={'content': plaid_resp['transactions']})

