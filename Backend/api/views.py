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
        'Listar todos produtos': '/api/mostrar-produtos/',
        'Mostrar um produto': '/api/mostrar-produto/id',
        'Criar um produto': '/api/criar-produto/',
        'Atualizar um produto': '/api/atualizar-produto/id',
        'Excluir um produto': '/api/excluir-produto/id',
        'Listar todos clientes': '/api/mostrar-clientes/',
        'Mostrar um cliente': '/api/mostrar-cliente/id',
        'Criar um cliente': '/api/criar-cliente/',
        'Atualizar um cliente': '/api/atualizar-cliente/id',
        'Excluir um cliente': '/api/excluir-cliente/id',

    }
    return Response(api_urls)


@api_view(['GET'])
def showProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializers = ProductSerializer(instance=product, data=request.data)

    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['DELETE'])
def excludeProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    
    return Response("Produto excluído com sucesso")

@api_view(['GET'])
def showCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showCustomer(request, pk):
    customers = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customers,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializers = CustomerSerializer(instance=customer, data=request.data)

    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['DELETE'])
def excludeCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    
    return Response("Cliente excluído com sucesso")

@api_view(['GET'])
def showCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showCustomer(request, pk):
    customers = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customers,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializers = CustomerSerializer(instance=customer, data=request.data)

    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['DELETE'])
def excludeCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    
    return Response("Cliente excluído com sucesso")