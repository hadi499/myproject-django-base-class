from django.urls import path
from . import views
from .views import (
    ShippingListView,
    ShippingCreateView,
    CategoryListView,
    CategoryCreateView,
    TarifListView,
    ChangeTarifView,
    ShippingDetailView,
    AllDataListView,

)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ShippingListView.as_view()), name='home'),
    path('all_data/', AllDataListView.as_view(), name='all-data'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('tarif/', TarifListView.as_view(), name='tarif'),
    path('shipping/new/', ShippingCreateView.as_view(), name='create'),
    path('category/new/', CategoryCreateView.as_view(), name='add-category'),
    path('tarif/new/', ChangeTarifView.as_view(), name='change-tarif'),
    path('post/<int:pk>/', ShippingDetailView.as_view(), name='detail'),
]
