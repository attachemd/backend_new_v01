from rest_framework import generics, authentication, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from selenium.webdriver.common.devtools.v85.network import Response

from user.serializers import UserSerializer, MyTokenObtainPairSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


# @api_view(['POST', ])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#
#         data = {}
#
#         if serializer.is_valid():
#             account = serializer.save()
#
#             data['response'] = "Registration Successful!"
#             # data['username'] = account.username
#             data['email'] = account.email
#
#             # token = Token.objects.get(user=account).key
#             # data['token'] = token
#
#             refresh = RefreshToken.for_user(account)
#             data['token'] = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#
#         else:
#             data = serializer.errors
#
#         return Response(data, status=status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
