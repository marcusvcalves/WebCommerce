from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



@api_view(['GET'])
def apiOverview(request):
    api_urls = {

    }
    return Response(api_urls)

@api_view(['GET'])
def productsList(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products,many=True)
    return Response(serializers.data)