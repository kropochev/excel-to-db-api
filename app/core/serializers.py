from .models import Client, Organization, Bill, Upload
from rest_framework import serializers


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('bills_file', 'clients_file',)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'client_name',)


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('client_org', 'number', 'date', 'sum',)
