from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_page, name='gallery'),
    path('photo/<str:pk>', views.view_image, name='photo'),
    path('add/', views.add_image, name='add'),
]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
