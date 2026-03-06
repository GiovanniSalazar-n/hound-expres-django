from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Guide
from .serializers import GuideSerializer


class GuideViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = GuideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            guide = Guide.objects.get(id=pk)
        except Guide.DoesNotExist:
            return Response(
                {"error": "Guía no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GuideSerializer(guide)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            guide = Guide.objects.get(id=pk)
        except Guide.DoesNotExist:
            return Response(
                {"error": "Guía no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GuideSerializer(guide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            guide = Guide.objects.get(id=pk)
        except Guide.DoesNotExist:
            return Response(
                {"error": "Guía no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        guide.delete()
        return Response(
            {"message": "Guía eliminada correctamente"},
            status=status.HTTP_204_NO_CONTENT
        )