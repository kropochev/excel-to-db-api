from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BillSerializer, UploadSerializer
from .models import Client, Organization, Bill
from .utils.functions import excel_to_database


class UploadFilesView(APIView):

    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            bills_file = serializer.data["bills_file"]
            clients_file = serializer.data["clients_file"]
            excel_to_database(bills_file, clients_file)
            return Response(
                {"Message": "Files processing"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientsViewSet(APIView):

    def get(self, request, format=None):

        bills = Bill.objects.all()

        resp_data = {}
        for bill in bills:
            client_name = bill.client_org.client_name.name
            client_org = bill.client_org.name
            bill_sum = bill.sum

            if client_name not in resp_data:
                resp_data[client_name] = {
                    "organizations": [client_org],
                    "sum": bill_sum
                }
            else:
                if client_org not in resp_data[client_name]["organizations"]:
                    resp_data[client_name]["organizations"].append(client_org)
                resp_data[client_name]["sum"] += bill_sum

        return Response(resp_data)


class BillsViewSet(APIView):

    def get(self, request, format=None):
        organization = request.query_params.get("organization")
        client = request.query_params.get("client")

        if organization:
            organization = Organization.objects.get(name=organization)
            bills = Bill.objects.filter(client_org_id=organization.id)
        elif client:
            client = Client.objects.get(name=client)
            organizations = Organization.objects.filter(client_name=client.id)
            bills = []
            for organization in organizations:
                bills.extend(Bill.objects.filter(
                    client_org_id=organization.id
                ))

        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)
