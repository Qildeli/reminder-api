from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
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


class LoginAPI(APIView):
    """
    An endpoint to authenticate existing users.
    """
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            return Response()


class UserDetail(APIView):
    """
    An endpoint to retrieve, update and delete existing users.
    """
    serializer_class = UserSerializer

    def get(self, request, pk):
        pass


    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
