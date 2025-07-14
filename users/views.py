from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
# users/views.py

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')
        phone_number = request.data.get('phone_number')
        user_type = request.data.get('user_type')  # e.g. 'tenant' or 'landlord'
        nin = request.data.get('nin', '')
        bvn = request.data.get('bvn', '')

        # Basic validation
        if not username or not password or not phone_number or not user_type:
            return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'Phone number already in use'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                phone_number=phone_number,
                user_type=user_type,
                nin=nin,
                bvn=bvn
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)





class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
            'user_type': user.user_type,
            'nin': user.nin,
            'bvn': user.bvn
        })
