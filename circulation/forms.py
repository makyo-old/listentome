from django import forms
from listentome.circulation.models import CheckoutRecord

class CheckoutForm(models.ModelForm):
    class Meta:
        model = CheckoutRecord

class ReservationForm(models.ModelForm):
    class Meta:
        model = ReservationRecord(models.Model):

