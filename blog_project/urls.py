from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# ✅ API Homepage (Root `/` URL)
@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Welcome to the Blog API!",
        "endpoints": {
            "posts": "/api/posts/",
            "comments": "/api/comments/",
            "token_obtain": "/api/token/",
            "token_refresh": "/api/token/refresh/"
        }
    })

urlpatterns = [
    path('', api_root),  # ✅ Returns JSON response when visiting `/`
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # Include blog app URLs

    # ✅ JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
