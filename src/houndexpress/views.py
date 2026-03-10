from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Guide, StatusHistory
from .serializers import GuideSerializer, StatusHistorySerializer


class GuideViewSet(viewsets.ViewSet):

    def list(self, request):
        guides = Guide.objects.all().order_by("-createdAt")
        serializer = GuideSerializer(guides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GuideSerializer(data=request.data)
        if serializer.is_valid():
            guide = serializer.save()
            StatusHistory.objects.create(
                guide=guide,
                status=guide.currentStatus,
                updatedBy="sistema"
            )
            return Response(GuideSerializer(guide).data, status=status.HTTP_201_CREATED)
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

        previous_status = guide.currentStatus
        serializer = GuideSerializer(guide, data=request.data)
        if serializer.is_valid():
            updated_guide = serializer.save()
            if previous_status != updated_guide.currentStatus:
                StatusHistory.objects.create(
                    guide=updated_guide,
                    status=updated_guide.currentStatus,
                    updatedBy="sistema"
                )
            return Response(GuideSerializer(updated_guide).data, status=status.HTTP_200_OK)
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

    def history(self, request, pk=None):
        try:
            guide = Guide.objects.get(id=pk)
        except Guide.DoesNotExist:
            return Response(
                {"error": "Guía no encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )

        history = guide.statusHistory.all().order_by("-timestamp")
        serializer = StatusHistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)