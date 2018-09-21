from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Product title',
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Your title'
                            }
                        ))
    # email       = forms.EmailField(label='Edgica email')
    description = forms.CharField(required=False, widget=forms.Textarea(
                            attrs={
                                'class': 'new-class-name two',
                                'id': 'my-id-foe-textares',
                                'rows': 5,
                                'cols': 60,
                                'placeholder': 'Your description'
                            }
                        ))
    price       = forms.DecimalField(initial='199.99')

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
            # 'summary',
            # 'featured'
        ]

    # Validation methods
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "p" in title.lower():
            raise forms.ValidationError("The titel must start from 'P'!")
        if "#" in title:
            raise forms.ValidationError("No # is allowed in the title!")
        return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("@edgica.com"):
    #         raise forms.ValidationError("This is not an Edgica valid email!")
    #     return email


class RawProductForm(forms.Form):
    title       = forms.CharField(label='Product title', widget=forms.TextInput(
                            attrs={
                                'placeholder': 'Your title'
                            }
                        ))
    description = forms.CharField(required=False, widget=forms.Textarea(
                            attrs={
                                'class': 'new-class-name two',
                                'id': 'my-id-foe-textares',
                                'rows': 5,
                                'cols': 60,
                                'placeholder': 'Your description'
                            }
                        ))
    price       = forms.DecimalField(initial='199.99')
