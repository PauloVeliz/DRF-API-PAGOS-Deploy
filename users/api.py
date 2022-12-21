from django.contrib.auth import authenticate
from rest_framework import status, generics,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import SignUpSerializer, GetUserSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from .tokens import create_jwt_pair_for_user
from .models import User


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "El usuario se creó correctamente",
                "data": serializer.data,
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Logeado correctamente", "email": email ,"tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Correo inválido o contraseña incorrecta"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)

class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        'create': SignUpSerializer,
        
    }
    default_serializer_class = UserSerializer 

    def get_serializer_class(self):
        print(self.action)
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create','retrieve']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[AllowAny]
        
        return [permission() for permission in permission_classes]
    