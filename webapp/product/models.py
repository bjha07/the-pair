from django.db import models
from authentication.models import EmployeeMaster
# Create your models here.

PRODUCT_TYPES = (
        ('SPORT','SPORT'),
        ('CASUAL','CASUAL')
      )

IDEAL_FOR = (
        ('MEN','MEN'),
        ('WOMEN','WOMEN')
      )


class ReferralEmployee(models.Model):
    added_on=models.DateTimeField(auto_now_add = True)
    name_referral_by = models.CharField(max_length=50,null=True, blank=True)
    name_referral_to = models.CharField(max_length=50,null=True, blank=True)
    code_referral_by = models.CharField(max_length=50,null=True, blank=True)
    code_referral_to = models.CharField(max_length=50,null=True, blank=True)
    status = models.BooleanField(default=True)

class WalletMoney(models.Model):
    added_on=models.DateTimeField(auto_now_add = True)
    value = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    comment = models.CharField(max_length=100,null=True, blank=True)
    employee_code = models.ForeignKey(EmployeeMaster, null=True, blank=True,related_name="walletmoney")
    referralemployee = models.ForeignKey(ReferralEmployee, null=True, blank=True)

class OfferDiscount(models.Model):
    updated_on = models.DateTimeField(null=True, blank=True) 
    discount = models.IntegerField(default=0, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    status = models.IntegerField(default=0, null=True, blank=True) # 0 means normal , 1 means discount all 
    def __unicode__(self):
        return str(self.discount)

class ProductSize(models.Model):
    updated_on = models.DateTimeField(null=True, blank=True)
    size_from = models.IntegerField(default=0, null=True, blank=True)
    size_to = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)

    def __unicode__(self):
        return str(self.name)

class DashboardDetails(models.Model):
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(null=True, blank=True)
    dashboard_image1 = models.FileField(upload_to='dashboard', null=True,blank=True)
    dashboard_image2 = models.FileField(upload_to='dashboard', null=True,blank=True)
    dashboard_image3 = models.FileField(upload_to='dashboard', null=True,blank=True)
    dashboard_image4 = models.FileField(upload_to='dashboard', null=True,blank=True)
    dashboard_image5 = models.FileField(upload_to='dashboard', null=True,blank=True)
    referral_image = models.FileField(upload_to='dashboard', null=True,blank=True)
    other_image = models.FileField(upload_to='dashboard', null=True,blank=True)
    other = models.CharField(max_length=500,null=True, blank=True)

class ProductType(models.Model):
    updated_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    image = models.FileField(upload_to='dashboard', null=True,blank=True)
    status = models.BooleanField(default=True)
    dashboard_details = models.ForeignKey(DashboardDetails, null=True, blank=True)

    def __unicode__(self):
        return str(self.name)

class BrandName(models.Model):
    added_on = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=100,null=True, blank=True)
    image = models.FileField(upload_to='dashboard', null=True,blank=True)
    status = models.BooleanField(default=True)
    dashboard_details = models.ForeignKey(DashboardDetails, null=True, blank=True)

    def __unicode__(self):
        return str(self.name)

class ProductColor(models.Model):
    added_on = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=100,null=True, blank=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.name)
    
class Product(models.Model):
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(null=True, blank=True)
    code = models.CharField(max_length=50,null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    #color = models.CharField(max_length=50,null=True, blank=True)
    color = models.ManyToManyField(ProductColor,blank=True,null=True)
    model_name = models.CharField(max_length=100,null=True, blank=True)
    warranty = models.CharField(max_length=50,null=True, blank=True)
    ideal_for = models.CharField(max_length = 50, choices=IDEAL_FOR, blank=True, default='MEN')
    description = models.CharField(max_length=500,null=True, blank=True)
    product_type = models.CharField(max_length = 50, choices=PRODUCT_TYPES, blank=True, default='SPORT') 
    orignal_price = models.IntegerField(default=0, null=True, blank=True)
    actual_price = models.IntegerField(default=0, null=True, blank=True)
    discount = models.IntegerField(default=0, null=True, blank=True)
    product_image = models.CharField(max_length=200,null=True, blank=True)
    image = models.FileField(upload_to='product_images', null=True,blank=True)
    status = models.BooleanField(default=True) 
    offer_discount = models.ForeignKey(OfferDiscount, null=True, blank=True)
    product_size = models.ForeignKey(ProductSize, null=True, blank=True)
    brand_name = models.ForeignKey(BrandName, null=True, blank=True)

    def __unicode__(self):
        return str(self.name)

class ProductImage(models.Model):
    added_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(null=True, blank=True)
    image1 = models.CharField(max_length=200,null=True, blank=True) 
    image2 = models.CharField(max_length=200,null=True, blank=True)
    image3 = models.CharField(max_length=200,null=True, blank=True)
    image4 = models.CharField(max_length=200,null=True, blank=True)
    image5 = models.CharField(max_length=200,null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True) 

 
 
