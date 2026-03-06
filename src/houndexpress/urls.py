from django.urls import path
from .views import GuideViewSet

guide_create = GuideViewSet.as_view({
    "post": "create"
})

guide_update = GuideViewSet.as_view({
    "put": "update"
})

guide_detail = GuideViewSet.as_view({
    "get": "retrieve"
})

guide_delete = GuideViewSet.as_view({
    "delete": "destroy"
})

urlpatterns = [
    path("crear-guia/", guide_create),
    path("actualizar-guia/<int:pk>/", guide_update),
    path("obtener-guia/<int:pk>/", guide_detail),
    path("eliminar-guia/<int:pk>/", guide_delete),
]