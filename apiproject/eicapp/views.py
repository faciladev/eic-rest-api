from django.http import HttpResponse, JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
import os
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination

from rest_framework import generics, status, permissions, routers, serializers, viewsets
from django.contrib.auth.models import User
from eicapp.models import Slide, Sector, Email, ChinesePage, NewsEvent, Incentive, CountryProfile, Service
from eicapp.serializers import SlideSerializer, SectorSerializer, UserSerializer, EmailSerializer, ChinesePageSerializer, NewsEventSerializer, IncentiveSerializer, CountryProfileSerializer, ServiceSerializer
from eicapp.permissions import IsStaff

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStaff]

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

class ChinesePageViewSet(viewsets.ModelViewSet):
    queryset = ChinesePage.objects.all()
    serializer_class = ChinesePageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

class NewsEventViewSet(viewsets.ModelViewSet):
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IncentiveViewSet(viewsets.ModelViewSet):
    queryset = Incentive.objects.all()
    serializer_class = IncentiveSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

class CountryProfileViewSet(viewsets.ModelViewSet):
    queryset = CountryProfile.objects.all()
    serializer_class = CountryProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        body = request.data
        response = super(EmailViewSet, self).create(request, *args, **kwargs)
        subject = f'{body["sender"]} > {body["subject"]}'
        message = body['message']
        recepient = os.getenv('EMAIL_HOST_USER')
        try:
            send_mail(subject, 
            message, os.getenv('EMAIL_HOST_USER'), [recepient], fail_silently = False)
        except Exception as e:
            print(e)
            
        return response

@csrf_exempt
def download(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        path_to_apk = os.path.abspath(os.path.dirname(__file__)) + "/../static/Invest_in_Ethiopia.apk"
        with open(path_to_apk, 'rb') as fh:
            response = HttpResponse(fh, content_type="application/vnd.android.package-archive") 
            response["Content-disposition"] = "attachment; filename={}".format("InvestInEthiopia.apk")
            return response

# TODO
# Remove EmailViewset from the API Root view
