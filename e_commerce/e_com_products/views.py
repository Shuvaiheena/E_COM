import email
from os import name
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from datetime import datetime
from django.db import transaction
from e_com_customer.models import CustomerDetails


# Create your views here.

class ProductApi(APIView):
    # creating ,updating ,listing and deleting product to customer
    def post(self, request):
        try:
            with transaction.atomic():
                # import pdb;pdb.set_trace()
                date_format = "%Y-%m-%d"
                a = datetime.strptime(str(datetime.now().date()), date_format)
                b = datetime.strptime(str(request.data.get('Date')), date_format)
                delta = b - a
                age_days =delta.days
                if abs(age_days) >= 60:
                    prod_active_status = 0
                else:
                    prod_active_status = 1
                if request.data.get('Customer_mobile'):
                    customer_instant = CustomerDetails.objects.filter(mobile = request.data.get('Customer_mobile')).first()
                ProductDetails.objects.create(
                    prod_name = request.data.get('Name'),
                    prod_code = request.data.get('Code'),
                    prod_date=request.data.get('Date'),
                    prod_age = abs(age_days),
                    prod_active = prod_active_status,
                    customer = customer_instant

                )
                return Response({'status' : 1, 'message' : 'Successfully created'})
        except:
            return Response({'status' : 0})
    
    def get(self, request):
        try:
            # import pdb;pdb.set_trace()
            if request.objects.data('Customer_mobile'):
                data = ProductDetails.objects.filter(customer_mobile=request.objects.data('Customer_mobile'),prod_active=1).values()
            else:
                data = ProductDetails.objects.filter(prod_active =1).values()
            return Response({'status' : 1, 'data':data})
        except:
            return Response({'status' : 0})
    def put(self, request):
        try:
            if request.data.get('Id'):
                # import pdb;pdb.set_trace()
                date_format = "%Y-%m-%d"
                a = datetime.strptime(str(datetime.now().date()), date_format)
                b = datetime.strptime(str(request.data.get('Date')), date_format)
                delta = b - a
                age_days =delta.days
                if abs(age_days) >= 60:
                    prod_active_status = 0
                else:
                    prod_active_status = 1
                if request.data.get('Customer_mobile'):
                    customer_instant = CustomerDetails.objects.filter(mobile = request.data.get('Customer_mobile')).first()
                ProductDetails.objects.create(
                    prod_name = request.data.get('Name'),
                    prod_code = request.data.get('Code'),
                    prod_date=request.data.get('Date'),
                    prod_age = abs(age_days),
                    prod_active = prod_active_status,
                    customer = customer_instant

                )
                return Response({'status' : 1, 'message' : 'Succesfully updated'})
            return Response({'status' : 0})
        except:
            return Response({'status' : 0})
    
    def patch(self, request):
        try:
            if request.data.get('Id'):
                # {
                #     "Id" : 3
                # }
                ProductDetails.objects.filter(prod_id = request.data.get('Id')).delete()
                return Response({'status' : 1, 'message' : 'Succesfully deleted'})
            return Response({'status' : 0})
        except:
            return Response({'status' : 0})
    def delete(self, request):
        try:
            ProductDetails.objects.all().delete()
            return Response({'status' : 1, 'message' : 'Succesfully deleted all records'})
        except:
            return Response({'status' : 0})


class ProductStatusApi(APIView):
    # to check the age of a product and update the product to active or inactive based on the age
    def put(self, request):
        try:
            with transaction.atomic():
                # import pdb;pdb.set_trace()
                date_format = "%Y-%m-%d"
                date_today = datetime.strptime(str(datetime.now().date()), date_format)
                currently_active_prod_data = ProductDetails.objects.filter(prod_active=1).values_list('prod_id',flat=True)
                for id in currently_active_prod_data:
                    prod_date = ProductDetails.objects.filter(prod_id =id).values('prod_date').first()['prod_date']
                    delta = date_today - prod_date
                    age_days = delta.days

                    if abs(age_days) >= 60:
                        prod_active_status = 0
                    else:
                        prod_active_status = 1
                    ProductDetails.objects.filter(prod_id = id).update(
                        prod_age = abs(age_days),
                        prod_active = prod_active_status
                    )

                
                return Response({'status' : 1, 'message' : 'Product Status Updated Succesfully'})
        except:
            return Response({'status' : 0})
    