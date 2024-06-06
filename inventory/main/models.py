from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField(primary_key=True)
    prod_name=models.CharField(max_length=50,blank=False,null=False)
    description=models.TextField(max_length=50)
    category=models.CharField(max_length=20)
    quantity=models.IntegerField()
    cost=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.prod_name
    
class Supplier_List(models.Model):
    supplier_id=models.AutoField(primary_key=True)
    supplier_name=models.CharField(max_length=30)
    address=models.TextField()
    action=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    contact=models.IntegerField()
    
    def __str__(self):
        return self.supplier_name

class Warehouse(models.Model):
    warehouse_id=models.AutoField(primary_key=True)
    warehouse_name=models.CharField(max_length=40)
    location=models.CharField(max_length=30)
    manager_name=models.CharField(max_length=30)
    capacity=models.IntegerField()
   
    def __str__(self):
        return self.warehouse_name
    

class Stock(models.Model):
    warehouse_name=models.ForeignKey(Warehouse,on_delete=models.CASCADE)
    supplier_name=models.CharField(max_length=30)
    address=models.TextField()
    action=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    contact=models.IntegerField()
    
    def __str__(self):
        return self.status
    
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    password=models.CharField(max_length=20,help_text="Enter a strong password")
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    role=models.CharField(max_length=20)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.username
    
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=20)
    quantity=models.IntegerField()
    action=models.CharField(max_length=20)
    order_date=models.DateTimeField()
    cost=models.IntegerField()

    def __str__(self):
        return self.status
    
class Payment(models.Model):
    pay_id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    payment_date=models.DateTimeField()
    amount=models.IntegerField()
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.amount

class ReturnOrder(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    return_id=models.AutoField(primary_key=True)
    status=models.CharField(max_length=20)
    quantity=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='return_quantity')
    cost=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='return_cost')

    def __str__(self):
        return self.status
    
class SalesList(models.Model):
    sales_id=models.AutoField(primary_key=True)
    prod_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    cost=models.DecimalField(max_digits=6,decimal_places=4)
    
    def __str__(self):
        return str(self.quantity)