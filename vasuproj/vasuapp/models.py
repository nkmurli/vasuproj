from django.db import models
from _overlapped import NULL


# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    
    
class StaffingMaster(models.Model):
    Eno         =models.CharField(max_length=64)
    Ename       =models.CharField(max_length=64)
    DMName      =models.CharField(max_length=64,null=True,default='Dummy Manager')
    BudgetArea  =models.CharField(max_length=64,null=True,default='Dummy Area')
    IBMMailID   =models.CharField(max_length=64,null=True,default='Dummy@in.ibm.com')
    OfficeNumber=models.CharField(max_length=64,default='080-417-72392',null=True)
    MobileNumber=models.CharField(max_length=64,default='999999999',null=True)
    ClientMailID=models.CharField(max_length=64,default='Anthem@Anthem.com',null=True)
    

     
