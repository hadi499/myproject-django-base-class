from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,

)
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Shipping, Category, TarifPerKilo
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class ShippingListView(LoginRequiredMixin, ListView):
    model = Shipping
    template_name = 'shipping/home.html'
    context_object_name = 'shipping'
    ordering = ['-id']

    def get_queryset(self):
        today = datetime.today()
        return Shipping.objects.filter(date=today)


class AllDataListView(LoginRequiredMixin, ListView):
    model = Shipping
    template_name = 'shipping/allData.html'
    context_object_name = 'shipping'
    ordering = ['-id']


class ShippingDetailView(LoginRequiredMixin, DetailView):
    model = Shipping


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'shipping/category.html'
    context_object_name = 'category'


class TarifListView(LoginRequiredMixin, ListView):
    model = TarifPerKilo
    template_name = 'shipping/tarif.html'
    context_object_name = 'tarif'
    ordering = ['-id']


class ShippingCreateView(LoginRequiredMixin, CreateView):
    kategori = Category.objects.all()
    tarif_per_kilo = TarifPerKilo.objects.all().last()
    model = Shipping
    fields = ['nama_barang', 'kategori', 'nama_pengirim', 'alamat_pengirim', 'nama_penerima', 'alamat_penerima',
              'berat', 'tarif_per_kilo']
    context = {
        'kategori': kategori,
        'tarif_per_kilo': tarif_per_kilo

    }
    extra_context = context
    template_name = 'shipping/create.html'
    success_url = '/'


class CategoryCreateView(LoginRequiredMixin, CreateView):

    model = Category
    fields = ['nama']
    template_name = 'shipping/addCategory.html'
    success_url = '/category'


class ChangeTarifView(LoginRequiredMixin, CreateView):

    model = TarifPerKilo
    fields = ['harga']
    template_name = 'shipping/changeTarif.html'
    success_url = '/tarif'
