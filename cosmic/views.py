from cosmic.models import Phone, Coupon
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from .serializers import PhoneSerializer


@api_view(['GET'])
def getData(request):
    phones = Phone.objects.all()
    serializer = PhoneSerializer(phones,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPhone(request):
    serializer = PhoneSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)