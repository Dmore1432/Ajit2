from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course,CourseSerializer
from django.http import Http404
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet

class CourseListView(APIView):
    def get(self,request):
        course=Course.objects.all()
        serializer=CourseSerializer(course,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class CourseDetailView(APIView):
    def get_put_delete(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        course = self.get_put_delete(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)

    def put(self,request,pk):
        course=self.get_put_delete(pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk):
        self.get_put_delete(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#mixin base

class CourseListView1(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class CourseListDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

#genericsAPI
class GenericView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request):
        return self.list(request)

    def post(self,requset):
        return self.create(requset)


class GenericDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class PowerGenerics(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class = CourseSerializer

class PowerGenerics1(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class = CourseSerializer


#Viewsets
#not working
class CourseViewSet(ViewSet):
    def list(self,request):
        course=Course.objects.all()
        serializers=CourseSerializer(course,many=True)
        return Response(serializers.data)

    def create(self,request):
        serializers=CourseSerializer(request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    def retrive(self, request,pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializers = CourseSerializer(course)
        return Response(serializers.data)


#nested serializers
from .models import Intructor,Course1,IntructorSeri1
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.authentication import BasicAuthentication,TokenAuthentication

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return True

class IntructorListView(generics.ListCreateAPIView):
     authentication_classes = [TokenAuthentication]
     permission_classes = [WriteByAdminOnlyPermission]

     serializer_class = IntructorSeri1
     queryset = Intructor.objects.all()









# class IntructorListView(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [WriteByAdminOnlyPermission]
#     serializer_class = IntructorSeri1
#     queryset = Intructor.objects.all()
