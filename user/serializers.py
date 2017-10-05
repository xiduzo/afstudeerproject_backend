from rest_framework import serializers

from .models import (
    User,
)

from world.models import (
    World,
    UserInWorld,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'created_at',
            'uid',
            'student_number',
            'email',
            'avatar_hash',
            'initials',
            'first_name',
            'surname_prefix',
            'surname',
            'gender',
            'is_staff',
            'is_superuser',
        )

class PlainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'uid',
            'email',
            'avatar_hash',
            'first_name',
            'surname_prefix',
            'surname',
        )

class GamemasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'email',
            'avatar_hash',
            'first_name',
            'surname_prefix',
            'surname',
        )

# V2
class V2UserWorldsSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserInWorld
        depth = 1
        fields = (
            'id',
            'user',
            'world'
        )
