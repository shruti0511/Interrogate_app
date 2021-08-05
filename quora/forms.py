from django.forms import ModelForm
from .models import Answer

class addAnswer(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']        

     