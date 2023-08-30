from .models import Register
from .serializers import RegisterSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view

@api_view(['GET'])
def  registerapi  (request):

    all_jobs=Register.objects.all()
    data=RegisterSerializer(all_jobs , many=True).data
    return Response({'data':data})



@api_view(['GET'])
def lgoicl(request,id):

    h1=Register.objects.all()
    test=RegisterSerializer(h1 , many=True).data
    return Response({'test':test})




    
