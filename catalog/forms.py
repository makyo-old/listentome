from django import forms
from listentome.catalog.models imort *

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['performers']

class PerformerForm(forms.ModelForm):
    class Meta:
        model = Performer

class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece

class MovementForm(forms.ModelForm);
    class Meta:
        model = Movement
