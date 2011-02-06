from django.db import models
from django.contrib.auth.models import User
from listentome.catalog.models import Record

class CheckoutRecord(models.Model):
    record = models.ForeignKey(Record)
    user = models.ForeignKey(User)
    date_out = models.DateField(auto_now_add = True)
    date_due = models.DateField()
    date_in = models.DateField(blank = True, null = True)

class ReserveRecord(models.Model):
    record = models.ForeignKey(Record)
    reserved_by = models.ForeignKey(User, related_name = 'records_reserved_by')
    reserved_for = models.ForeignKey(User, related_name = 'records_reserved_for')
    date_reserved = models.DateField(auto_now_add = True)
    date_expires = models.DateField()
