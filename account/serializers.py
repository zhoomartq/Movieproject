

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterApiSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate(self, attrs):
        password_confirm = attrs.pop('password_confirm')
        if attrs.get('password') != password_confirm:
            raise serializers.ValidationError('Password and password_confirm did not match')
        if not attrs.get('password').isalnum():
            raise serializers.ValidationError('Password field must be contain alpha and numbers')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.pop('password', None)
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found')
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            refresh = self.get_token(user)
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)
        return attrs