from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


user = get_user_model()


class RegisterAPI(APIView):
    """
    An endpoint to create a new user.
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)


class LoginAPI(APIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    serializer_class = LoginSerializer

    def post(self, request):
        pass


class LogoutAPI(APIView):
    """
    An endpoint to logout users.
    """
    def post(self, request):
        pass