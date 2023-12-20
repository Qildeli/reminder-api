from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status


user = get_user_model()


class RegisterAPI(APIView):
    """
    An endpoint to create a new user.
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    serializer_class = LoginSerializer

    def post(self, request):
        pass
