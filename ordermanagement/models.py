from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    customer_places = models.CharField(max_length=200, null=True)
    customer_price = models.FloatField(default=0.0)
    customer_emailid = models.EmailField(max_length=254, null=True, blank=True)  # Use EmailField for emails
    customer_contactno = models.CharField(max_length=15, null=True, blank=True)  # Use CharField for phone numbers

    def __str__(self):
        return f"{self.customer_name}" if self.customer_name else "Unnamed Customer"
