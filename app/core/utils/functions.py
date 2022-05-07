from django.conf import settings

import pandas as pd

from core import models


def excel_to_database(bills, clients):

    bills_file_path = settings.MEDIA_ROOT + bills
    clients_file_path = settings.MEDIA_ROOT + clients

    clients_df = pd.read_excel(
        clients_file_path,
        sheet_name="client",
        header=None,
        skiprows=1
    )
    organizations_df = pd.read_excel(
        clients_file_path,
        sheet_name="organization",
        header=None,
        skiprows=1
    )
    bills_df = pd.read_excel(
        bills_file_path,
        header=None,
        skiprows=1
    )

    for _, client in clients_df.iterrows():
        client_model = models.Client(name=client.values[0])
        clients = [client.name for client in models.Client.objects.all()]
        if client_model.name not in clients:
            client_model.save()

    for _, organization in organizations_df.iterrows():
        client = models.Client.objects.get(name=organization.values[0])
        organization_model = models.Organization(
            name=organization.values[1],
            client_name=client
        )
        organizations = [org.name for org in models.Organization.objects.all()]
        if organization_model.name not in organizations:
            organization_model.save()

    for _, bill in bills_df.iterrows():
        organization = models.Organization.objects.get(name=bill.values[0])
        bill_model = models.Bill(
            client_org=organization,
            number=bill.values[1],
            sum=bill.values[2],
            date=bill.values[3],
        )
        bills = [
            (bill.number, bill.client_org)
            for bill in models.Bill.objects.all()
        ]
        if (bill_model.number, bill_model.client_org) not in bills:
            bill_model.save()
