from django import forms

from .models import PicnicReservation

class PicnicReservationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        self.fields['middle_initial'].widget.attrs.update({'class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control'})
        self.fields['comments'].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = PicnicReservation
        fields = '__all__'
