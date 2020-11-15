from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
#from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializers
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.RetrieveModelMixin, 
                        mixins.DestroyModelMixin ):
    serializer_class=PostSerializers
    queryset=Post.objects.all()

    lookup_field='id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request,id=None):
        
        return self.create(request, id)

    def put(self, request, id=None):
        return self.update(request, id) 

    def delete(self,request, id):
        return self.destroy(request, id)    


class PostAPIView(APIView):
    def get(self,request):
        post= Post.objects.all()
        serializers=PostSerializers(post, many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers=PostSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

'''
class PostDetails(APIView):

    def get_objects(self,id):
        try:
            return Post.objects.get(id=id)

        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

    def get(self,request,id):
        post= self.get_objects(id)
        serializers=PostSerializers(post)
        return Response(serializers.data)

    def put(self,request,id):
        post= self.get_objects(id)
        serializers= PostSerializers(post,data=request.data)
    
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,id):
        post= self.get_objects(id)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


'''

'''
@api_view(['GET','POST'])
def post_details(request):
    if request.method =='GET':
        articles= Article.objects.all()
        serializers=ArticleSerializers(articles, many=True)
        return Response(serializers.data)

    elif request.method=='POST':
        serializers=ArticleSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT','DELETE'])
def article_details(request, pk):
    try:
        article= Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)    

    if request.method =='GET':
        serializers=ArticleSerializers(article)
        return Response(serializers.data)

    elif request.method =='PUT':
        serializers= ArticleSerializers(article,data=request.data)
    
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)  

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_NO_CONTENT)      '''  

# POSTS VIEW ENDPOINT
def posts(request):
    return render(request, 'blog-listing.html')


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')