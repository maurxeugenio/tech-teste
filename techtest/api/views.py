from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from techtest.regions.models import Region
from techtest.articles.models import Author, Article
from techtest.articles.serializers import AuthorSerializer, ArticleSerializer
from techtest.regions.serializers import RegionSerializer


class ArticleListView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Article.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.author = None
            serializer.save()
            return Response({"status": "sucess remove author", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error remove author", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, id=None):
        object = get_object_or_404(Article, id=id)
        serializer = self.serializer_class(object)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        object = get_object_or_404(Article, id=id)
        serializer = self.serializer_class(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        object = get_object_or_404(Article, id=id)
        object.delete()
        return Response({'status': 'item deleted'}, status=status.HTTP_204_NO_CONTENT)


class AuthorListView(APIView):
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Author.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AuthorDetailView(APIView):
    serializer_class = AuthorSerializer

    def get(self, request, id=None):
        object = get_object_or_404(Author, id=id)
        serializer = self.serializer_class(object)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        object = get_object_or_404(Author, id=id)
        serializer = self.serializer_class(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        object = get_object_or_404(Region, id=id)
        object.delete()
        return Response({'status': 'item deleted'}, status=status.HTTP_204_NO_CONTENT)


class RegionListView(APIView):
    serializer_class = RegionSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(Region.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class RegionDetailView(APIView):
    serializer_class = RegionSerializer

    def get(self, request, id=None):
        object = get_object_or_404(Region, id=id)
        serializer = self.serializer_class(object)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        object = get_object_or_404(Region, id=id)
        serializer = self.serializer_class(object, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        object = get_object_or_404(Region, id=id)
        object.delete()
        return Response({'status': 'item deleted'}, status=status.HTTP_204_NO_CONTENT)
