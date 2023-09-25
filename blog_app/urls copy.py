

from django.urls import path
from blog_app import views

urlpatterns = [
    

    path('', views.post_list, name="post-list"),
    path('post-detail/<int:pk>/', views.post_detail, name="post-detail"),
    path('draft-detail/<int:pk>/', views.draft_detail, name="draft-detail"),
    path('draft-publish/<int:pk>/', views.draft_publish, name="draft-publish"),
    path("draft-list", views.draft_list, name="draft-list"),
    path('draft-delete/<int:pk>/', views.draft_delete, name="draft-delete"),
    path('post-delete/<int:pk>/', views.post_delete, name="post-delete"),
    path('post-update/<int:pk>/', views.post_update, name="post-update"),
    path("post-create/", views.Post_create,name="post-create")
]
