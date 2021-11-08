from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from applications.account.serializers import RegisterSerializers

User = get_user_model()

class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Succesfully signed up', status=status.HTTP_201_CREATED)

