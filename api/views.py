from rest_framework import viewsets
from myapp.models import Role, Appraiser, Client, LoanStatus, Loan, Collateral, Payment
from .serializers import RoleSerializer, AppraiserSerializer, ClientSerializer, LoanStatusSerializer, LoanSerializer, CollateralSerializer, PaymentSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class AppraiserViewSet(viewsets.ModelViewSet):
    queryset = Appraiser.objects.all()
    serializer_class = AppraiserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class LoanStatusViewSet(viewsets.ModelViewSet):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class CollateralViewSet(viewsets.ModelViewSet):
    queryset = Collateral.objects.all()
    serializer_class = CollateralSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
