from django.contrib import admin
from django.urls import path
from .views import hellorworldfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/', hellorworldfunc),
    path('helloworldurl2/', HelloWorldClass.as_view()),
]
