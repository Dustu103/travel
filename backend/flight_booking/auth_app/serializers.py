from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    profile_pic = serializers.URLField(required=False, default="https://drive.google.com/uc?id=1USSc1D8fjYqOHt7VbQmv3CK1njV2jGHR")  

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'name', 'profile_pic']

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            profile_pic=validated_data.get('profile_pic'),
            password=validated_data['password']  
        )
