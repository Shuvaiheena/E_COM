from django.db import models


# Create your models here.
class CustomerDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    active_state = models.IntegerField(blank=True, null=True,default=0)
    date_created = models.DateField(blank=True, null=True)
    customer_age = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'customer_details'

    def __str__(self):
        return str(self.Name)