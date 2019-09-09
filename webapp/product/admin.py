from django.contrib import admin
from product.models import Product , ProductSize , OfferDiscount , BrandName , ProductColor , DashboardDetails , ProductType

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(OfferDiscount)
admin.site.register(BrandName)
admin.site.register(ProductColor)
admin.site.register(DashboardDetails)
admin.site.register(ProductType)
