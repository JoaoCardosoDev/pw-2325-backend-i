from django.db import models

# Create your models here.

class Product(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=20, null=False, blank=False, help_text="Name of the product")
    price =models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=100)
    enabled=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
