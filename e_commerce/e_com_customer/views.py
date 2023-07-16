import email
from os import name
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from datetime import datetime
from django.db import transaction


# Create your views here.

class CustomerApi(APIView):
    def post(self, request):
        try:
            with transaction.atomic():
                # import pdb;pdb.set_trace()
                if CustomerDetails.objects.filter(mobile=request.data.get('Mobile')).exists():
                    return Response({"status":0,"message":"Customer Already Exist"})
                CustomerDetails.objects.create(
                    name = request.data.get('Name'),
                    email = request.data.get('Email'),
                    mobile=request.data.get('Mobile'),
                    address=request.data.get('Address'),
                    gender = request.data.get('Gender'),
                    date_created=request.data.get('Date'),
                    customer_age = request.data.get('Age'),
                    active_state = 1
                )
                return Response({'status' : 1, 'message' : 'Successfully created'})
        except:
            return Response({'status' : 0})
    
    def get(self, request):
        try:
            # import pdb;pdb.set_trace()
            data = CustomerDetails.objects.filter(active_state =1).values()
            return Response({'status' : 1, 'data':data})
        except:
            return Response({'status' : 0})
    def put(self, request):
        try:
            if request.data.get('Id'):
                # import pdb;pdb.set_trace()
                if CustomerDetails.objects.filter(mobile=request.data.get('Mobile')).exclude(id=request.data.get('Id')).exists():
                    return Response({"status":0,"message":"Customer Already Exist"})
                CustomerDetails.objects.filter(id=request.data.get('Id')).update(
                    name = request.data.get('Name'),
                    email = request.data.get('Email'),
                    mobile=request.data.get('Mobile'),
                    address=request.data.get('Address'),
                    gender = request.data.get('Gender'),
                    date_created=request.data.get('Date'),
                    customer_age = request.data.get('Age')
                )
                return Response({'status' : 1, 'message' : 'Succesfully updated'})
            return Response({'status' : 0})
        except:
            return Response({'status' : 0})
    
    def patch(self, request):
        try:
            if request.data.get('Id'):
                # import pdb;pdb.set_trace()
                CustomerDetails.objects.filter(id = request.data.get('Id')).delete()
                return Response({'status' : 1, 'message' : 'Succesfully deleted'})
            return Response({'status' : 0})
        except:
            return Response({'status' : 0})
    def delete(self, request):
        try:
            CustomerDetails.objects.all().delete()
            return Response({'status' : 1, 'message' : 'Succesfully deleted all records'})
        except:
            return Response({'status' : 0})
    