from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# 해당 클래스는 Snippet 모델의 정보들을 그대로 베낀다.
# class SnippetSerializer(serializers.Serializer):
    # pk = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    #
    # def create(self, validated_data):
    #     """
    #     검증한 데이터로 새 `Snippet` 인스턴스를 생성하여 리턴합니다.
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     검증한 데이터로 기존 `Snippet` 인스턴스를 업데이트한 후 리턴합니다.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance


class SnippetSerializer(serializers.ModelSerializer):
    """
    Django 에서 Form 클래스와 ModelForm 클래스롤 제공하는 것과 같이,
    REST 에서도 Serializer 클래스와 ModelSerializer 클래스를 제공한다.
    이는 ModelSerializer 클래스를 사용한 것이다.
    """
    if __name__ == '__main__':
        if __name__ == '__main__':
            class Meta:
                model = Snippet
                fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

            # ModelSerializer 는 그저 시리얼라이저 클래스의 단축 버전일 뿐이다.
            # 필드를 자동으로 인식한다.
            # create() 와 update() 가 이미 구현되어 있다.
