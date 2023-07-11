from django.shortcuts import render
from .serializers import diseaseSerializer, imageSerializer
from .models import disease, image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


# Diseases APIViews
class diseaseIdentifiers(APIView):
    def get(self, request):
        identifiers = disease.objects.values_list("identifier", flat=True).distinct()
        return Response(identifiers, status=status.HTTP_200_OK)


class diseaseListView(APIView):
    def post(self, request):
        serializer = diseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, identifier, language):
        try:
            disease_obj = disease.objects.get(identifier=identifier, language=language)
            serializer = diseaseSerializer(disease_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except disease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, identifier, language):
        try:
            disease_obj = disease.objects.get(identifier=identifier, language=language)
            serializer = diseaseSerializer(disease_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except disease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, identifier, language):
        try:
            disease_obj = disease.objects.get(identifier=identifier, language=language)
            disease_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except disease.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Disease Images Illustratons
class imageListView(APIView):
    # Adding new image based disease identifier details
    def post(self, request):
        serializer = imageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve sepecific image using default image pk
    def get(self, request, pk):
        try:
            image_obj = image.objects.get(pk=pk)
            serializer = imageSerializer(image_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Updating or changing image or image description
    def put(self, request, pk):
        try:
            image_obj = image.objects.get(pk=pk)
            serializer = imageSerializer(image_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Deleting speific image
    def delete(self, request, pk):
        try:
            image_obj = image.objects.get(pk=pk)
            image_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
