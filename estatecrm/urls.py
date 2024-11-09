"""
URL configuration for estatecrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estate import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('estate/add/',views.EstateCreateView.as_view(),name="estate-add"),
    path('estate/all/',views.EstateListView.as_view(),name="estate-list"),
    path('estate/<int:pk>/',views.EstateDetailView.as_view(),name="estate-details"),
    path('estate/<int:pk>/delete/',views.EstateDeleteView.as_view(),name="estate-delete"),
    path('estate/<int:pk>/update/',views.EstateUpdateView.as_view(),name="estate-update"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

