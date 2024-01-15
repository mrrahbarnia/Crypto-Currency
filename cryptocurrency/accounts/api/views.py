"""
API view for accounts app.
"""
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import (
    get_user_model,
    login
)
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    ChangePasswordSerializer
)

user = get_user_model()


class RegistrationApiView(GenericAPIView):
    """
    Registration view with specific validation
    in the serializer using email and password.
    """
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class LoginApiView(GenericAPIView):
    """
    Login view with email and password.
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            'detail': _('Logged in')
        })
    


class ChangePasswordApiView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    model = user
    serializer_class = ChangePasswordSerializer
    
    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):

        user_object = self.get_object()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_password = serializer.validated_data('old_password')

        if not user_object.check_password(old_password):
            return Response(
                {"old_password": _("Wrong password.")},
                status=status.HTTP_400_BAD_REQUEST)
        
        new_password = serializer.validated_data('new_password')
        user_object.set_password(new_password)
        user_object.save()

        return Response(
            {'detail': _('Your password changed successfully.')},
            status=status.HTTP_200_OK
        )



