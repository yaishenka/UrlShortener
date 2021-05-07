from django.urls import path
from . import views

urlpatterns = [
    path('<link>', views.goto),
    path('<link>/', views.goto),
    path('api/manage', views.UrlManagerView.as_view()),
    path('api/urls', views.ListAllUrls.as_view()),
    path('', views.goodby),
]