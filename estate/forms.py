from django import forms
from estate.models import Estate


class EstateForm(forms.ModelForm):

    class Meta:
        
        model=Estate

        fields="__all__"

        widgets={

            "address":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "property_type":forms.Select(attrs={"class":"form-control form-select"}),
            "number_of_bedrooms":forms.NumberInput(attrs={"class":"form-control"}),
            "square_footage":forms.NumberInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "property_img":forms.FileInput(attrs={"class":"form-control"}),
            "contact_details":forms.TextInput(attrs={"class":"form-control"}), 

        }
