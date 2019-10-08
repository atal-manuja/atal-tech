from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView


class CheckView(APIView):



    def get(self,request):
        print('in da view')
        return Response({'data':"you are into atal's api"})