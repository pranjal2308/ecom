from django.db  import models
# from .category import Category


# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50)
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="images",default="")
   
    def __str__(self):
        return self.product_name


# class Category(models.Model):
#    name=models.CharField(max_length=50)        
     
# def __str__(self):
#         return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."    