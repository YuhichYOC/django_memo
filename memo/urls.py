from django.urls import path

from memo import views

app_name = 'memo'
urlpatterns = [
    path('<int:node_id>', views.browse_node),
    path('', views.browse),
]
