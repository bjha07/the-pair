from django.db import models
from django.contrib.auth.models import User
# Create your models here.

USER_TYPES = (
        ('Manager', 'Manager '),
        ('CS Team','CS Team'),
        ('Admin', 'Admin'),
        ('User','User')
      )

DEPARTMENT_LIST = (
        ('IT','IT'),
        ('Operations','Operations'),
        )

class Department(models.Model):
    name = models.CharField(max_length=150, choices=DEPARTMENT_LIST)
    added_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.name


class EmployeeMaster(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    employee_code = models.CharField(max_length=20, null=True, blank=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60,null=True, blank=True)
    user_type = models.CharField(max_length = 50, choices=USER_TYPES, blank=True, default='User',)
    email = models.CharField(max_length=100, null=True, blank=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    address3 = models.CharField(max_length=200, null=True, blank=True)
    mobile_no = models.CharField(max_length=60)
    department = models.ForeignKey(Department)
    login_active = models.IntegerField(default=0)
    staff_status = models.IntegerField(default=0) #0:perm, 1:temp, 2:deact
    refferal_code = models.CharField(max_length=60,null=True, blank=True)

    def __unicode__(self):
        return str(self.firstname) + " - " + str(self.lastname) + " - "+ str(self.employee_code)


