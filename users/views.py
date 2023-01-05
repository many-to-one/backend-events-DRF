from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserSerializer


class RegisterApi(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginApi(APIView):
    def post(self, request):
        email = request.data['email'] 
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is not None:
            raise AuthenticationFailed ('User is not found!')    

        if not user.check_password(password) :
            raise AuthenticationFailed ('Incorrecr password!')

        return Response({
            'massage': 'Succes!'
        })           