from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include("base.urls")),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls'))
]
