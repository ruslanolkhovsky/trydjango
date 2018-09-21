from django import forms

from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'topic',
            'author',
            'text',
        ]

    # Validation methods
    def clean_topic(self, *args, **kwargs):
        topic = self.cleaned_data.get("topic")
        if "#" in topic:
            raise forms.ValidationError("No # is allowed in the topic!")
        return topic
