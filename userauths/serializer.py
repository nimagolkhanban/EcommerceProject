from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauths.models import User,Profile


#jwtserializers
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["full_name"] = user.full_name
        token["email"] = user.email
        token["username"] = user.username
        try:
            token["vendor_id"] = user.vendor.id
        except:
            token["vendor_id"] = 0
        return token

        


#model serializers
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"
    
    def to_representation(self, instance):
        responce = super().to_representation(instance)
        responce["user"] = UserSerializer(instance.user).data  
        #this line of code above is very important "instance.user" refrence the user field in profile model that have a 1to1 relationship
        #to user model that return a whole instance data and the ".data" return a dictionary full of that spesefic instance model data
        return responce