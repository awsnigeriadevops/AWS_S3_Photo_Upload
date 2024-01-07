from django.shortcuts import render, redirect
from .forms import S3FileForm


def upload_file(request):
    if request.method == "POST":
        form = S3FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_file")  # Redirect to a success page or another view
    else:
        form = S3FileForm()

    return render(request, "s3upload/index.html", {"form": form})
