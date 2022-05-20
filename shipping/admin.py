from django.contrib import admin
from .models import Category, Shipping, TarifPerKilo


admin.site.register(Category)


@admin.register(TarifPerKilo)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['id', 'harga', 'created_at', 'updated']


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['resi', 'nama_barang', 'kategori', 'nama_pengirim', 'alamat_pengirim',
                    'nama_penerima', 'alamat_penerima', 'berat', 'tarif_per_kilo', 'created_at']
