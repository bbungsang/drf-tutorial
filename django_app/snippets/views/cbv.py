from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# 믹스인 클래스 사용하지 않을 경우 필요한 모듈
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# 믹스인 클래스 사용할 때 필요한 모듈
from rest_framework import mixins

# 믹스인, 제네릭 클래스 사용할 때 필요한 모듈
from rest_framework import generics


# 클래스 기반 뷰의 가장 큰 이점은 기능들을 손쉽게 조합할 수 있다는 것이다.
# 생성/조회/업데이트/삭제 는 일반적으로 모델을 사용 할 때의 뷰와 비슷하다 하지만 REST 프레임워크에서는 믹스인 클래스로 구현해뒀다.

# 믹스인 클래스 사용 전
# class SnippetList(APIView):
#     """
#     코드 조각을 모두 보여주거나 새 코드 조각을 만든다.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
#     """
#     코드 조각 조회, 업데이트, 삭제
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


###################################### 믹스인 클래스 사용 ######################################

# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     # GenericAPIView 가 핵심 기능을 제공, 나머지 믹스인들이 .retrieve(), .update(), .destroy() 기능 제공
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


###################################### 제네릭 클래스 사용 ######################################

"""
REST 는 특정 뷰에 제한을 걸 수 있는 권한 클래스를 제공한다.
그 중 한 가지인 IsAuthenticatedOrReadOnly 는 인증 받은 요청에 읽기와 쓰기 권한을 부여하고,
인증 받지 않은 요청에 대해서는 읽기 권한만 부여한다.
"""
from rest_framework import permissions


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
