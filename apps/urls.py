from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),  # entry point to other project app urls
]
