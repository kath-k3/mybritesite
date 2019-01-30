from django import forms

from .models import FeatureRequest


class FeatureRequestForm(forms.ModelForm):

    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority',
                  'product_area', 'target_date']
        widgets = {
            'target_date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }

    def save(self, commit=True):
        priority = self.cleaned_data['client_priority']
        if FeatureRequest.objects.filter(client_priority=priority).exists():

            self.instance.client_priority = None

            # TODO move other feature requests for the client
            #self.instance.to(priority)
        else:
            self.instance.client_priority = priority
        if commit:
            self.instance.save()
        return self.instance
