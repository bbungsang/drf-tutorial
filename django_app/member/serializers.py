from django.contrib.auth.models import User

from rest_framework import serializers
from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    """
    'snippets'는 사용자 모델과 반대 방향으로 이어져 있기 때문에 ModelSerializer 에 기본적으로 추가되지 않는다.
    따라서 명시적으로 필드 지정
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')