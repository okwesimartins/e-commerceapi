from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Article
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','password','phonenumber','first_name','email']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=255,min_length=4),
#     first_name = serializers.CharField(max_length=255,min_length=2)
#     last_name = serializers.CharField(max_length=255,min_length=2)

#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email']
    
#     def validate(self, attrs):
#         if User.objects.filter(email=attrs['email']).exists():
#             raise serializers.ValidationError({'email',('Email already exist')})
#         return super().validate(attrs)

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author','email']
         


        

