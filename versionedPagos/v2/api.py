from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from services.models import Service
from users.models import User
from expired_payments.models import ExpiredPayment
from .serializers import ServiceSerializer,UserSerializer, ExpiredPaymentSerializer
from users.serializers import SignUpSerializer

class ServiceViewSet(ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #http_method_names = ['get', 'post', 'head']
    # permission_classes=[IsAuthenticated]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update','create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[AllowAny]
        
        return [permission() for permission in permission_classes]


class ExpiredPaymentViewSet(ModelViewSet):

    queryset = ExpiredPayment.objects.all()
    serializer_class = ExpiredPaymentSerializer
    #http_method_names = ['get', 'post', 'head']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['destroy','partial_update','update']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes=[AllowAny]
        return [permission() for permission in permission_classes]


class UsersViewSet(ModelViewSet):
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
    