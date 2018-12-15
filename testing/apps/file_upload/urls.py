from django.urls import path, include
from . import views

app_name = 'file_upload'
urlpatterns = [
    # path('', views.SnippetListView.as_view(), name='snippets-list'),
    path('upload', views.FileUploadCreate.as_view(), name='FileUploadCreate'),
    # path('detail/<int:pk>/', views.SnippetDetailView.as_view(), name='snippets-detail'),
    # path('update/<int:pk>', views.SnippetUpdate.as_view(), name='snippets-update'),
    # path('delete/<int:pk>', views.SnippetDelete.as_view(), name='snippets-delete'),
    
]
