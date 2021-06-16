from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers

from account.send_mail import send_confirmation_email


User = get_user_model()

class RegisterApiView(APIView):

    def post(self, request):
        serializer = serializers.RegisterApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ActivationView(APIView):

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message': 'Successfully activated!!!'}, status=status.HTTP_200_OK)

        except User.DoesNotExists:
            return Response({'message': 'Link expired!!!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer
#


#
# from django.contrib.auth import get_user_model
# from django.shortcuts import render, get_object_or_404
#
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from . import serializers
# from account.serializers import RegisterSerializer
#
#
# User = get_user_model()
#
# class RegisterView(APIView):
#     def post(self, request):
#         # data = request.data
#         serializer = serializers.RegisterSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.save()
#             return Response('succesfull!', status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# class ActivateView(APIView):
#     def get(self, request, activation_code):
#         try:
#             user = get_object_or_404(User, activation_code=activation_code)
#             user.is_active = True
#             user.activation_code = ''
#             user.save()
#             return Response('Your account successfully activated!', status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({'message':'link expired'}, status=status.HTTP_200_OK)
#
