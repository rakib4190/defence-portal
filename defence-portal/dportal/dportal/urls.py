from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/', include('admins.urls')),
    path('', include('student.urls')),
    path('', include('login.urls')),
    path('', include('teacher.urls')),
]
