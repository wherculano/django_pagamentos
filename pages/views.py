from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Client, Bills
from .serializers import ClientSerializer, BillsSerializer


class ClientViewSet(viewsets.ViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Client.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(user)
        return Response(serializer.data)


class BillsViewSet(viewsets.ViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Bills.objects.all()
        serializer = BillsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Bills.objects.all()
        user = get_object_or_404(queryset, pk)
        serializer = BillsSerializer(user)
        return Response(serializer.data)
