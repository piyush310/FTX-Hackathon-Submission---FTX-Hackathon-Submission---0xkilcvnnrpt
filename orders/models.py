from django.db import models

# Create your models here.
class Order(models.Model):
    txn_order_id = models.CharField(max_length=30, unique=True)
    txn_oder_amnt = models.DecimalField(decimal_places=4, max_digits=12)
    txn_pmnt_id = models.CharField(max_length=30, unique=True)
    txn_signature = models.CharField(max_length=256)

    def __str__(self):
        return self.txn_order_id
