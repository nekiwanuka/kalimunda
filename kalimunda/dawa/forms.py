# forms is an interface where a user creates dat, basing on the models we have created 
from django.forms import ModelForm

#Accessing our models such that  we link them to the forms
from .models import * 
class AddForm(ModelForm):
    class Meta:
        model = Product
        # this is a field for updating the already existing stock
        fields = ['recieved_quantity']
        
# were modelling a form basing on our model we shall use to record a given product sale.        
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_recieved','issued_to']
