from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.


class ArticleView(APIView):
    """ Метод get служит для получения всех артиклей из БД """
    def get(self, request):
        articles = Article.objects.all()
        # Параметр many сообщает сериализатору,что он будет сериализовать несколько статей
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    """ Метод post служит для создания нового артикля в БД """
    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    """ Метод put служит для изменения артикля в БД """
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' update successfully".format(article_saved.title)})

    """ Метод delete служит для удаления артикля из БД """
    def delete (self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id '{}' deleted".format(pk)}, status=204)






