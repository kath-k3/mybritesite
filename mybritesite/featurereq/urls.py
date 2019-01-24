from django.urls import path

from . import views

app_name = 'featurereq'
urlpatterns = [
    path('', views.FeatureRequestListView.as_view(), name='index'),
    path('requests/create/', views.FeatureRequestCreateView.as_view(), name='create'),
    path('requests/update/<int:pk>/', views.FeatureRequestUpdateView.as_view(), name='update'),
    path('requests/detail/<int:pk>/', views.FeatureRequestDetailView.as_view(), name='detail'),
    path('requests/delete/<int:pk>/', views.FeatureRequestDeleteView.as_view(), name='delete'),

    #path('<int:featurerequest_id>/', views.featurerequest_detail, name='detail'),

    #path('requests/', views.featurerequest_list, name='list'),
]