from django import forms
from .models import S3File


class S3FileForm(forms.ModelForm):
    class Meta:
        model = S3File
        fields = ["file", "description"]

    def clean_file(self):
        file = self.cleaned_data.get("file")

        # Check if the file size is within acceptable limits
        if file:
            max_size = 5 * 1024 * 1024  # 5 MB
            if file.size > max_size:
                raise forms.ValidationError("File size must be no more than 5 MB.")

        return file
