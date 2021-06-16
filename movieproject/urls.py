
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movieproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)