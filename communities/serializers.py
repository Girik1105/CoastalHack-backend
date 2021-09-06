from rest_framework import serializers

from users.serializers import UserSerializer
from . import models 

class post_serializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = models.Post
        fields = ("author", "image", "content",  "community", "timestamp", "id")
    
        # read_only_fields = ['user']
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


    def validate_content(self, value):
        if len(value) > 240:
            raise serializers.ValidationError("This is way to long")
        return value
    
    def validate(self, data):
        content = data.get("content", None)
        image = data.get("image", None)

        if content == None and image == None:
            raise serializers.ValidationError("Image or content is required")
        
        return data 

class community_serializer(serializers.ModelSerializer):    
    class Meta:
        model = models.community
        fields = ("name", "slug", "description",  "owner", "members", "cover", "created_on")
    