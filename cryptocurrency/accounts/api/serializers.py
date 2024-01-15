"""
Serializers for accounts app.
"""
from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
    authenticate
)
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password

user = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        password = attrs.get('password')
        password1 = attrs.get('password1')

        if password != password1:
            raise serializers.ValidationError(
                {'detail':_("Passwords must be match.")}
            )
        
        errors = {}
        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        
        return super(RegistrationSerializer, self).validate(attrs)

    def create(self, validated_data):
        """Create user with encrypted password."""
        validated_data.pop('password1', None)
        return user.objects.create_user(**validated_data)
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code="authorization")
        
        if not user.is_verified:
            raise serializers.ValidationError(
                {'detail': _('User is not verified.')}
            )
        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        """Validating new passwords."""
        new_password = attrs.get('new_password')
        new_password1 = attrs.get('new_password1')
        if new_password != new_password1:
            raise serializers.ValidationError(
                {"detail": _("Passwords must be match.")}
            )

        errors = dict()
        try:
            validate_password(new_password)
        except exceptions.ValidationError as e:
            errors['new_password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)

        return super(ChangePasswordSerializer, self).validate(attrs)

        
