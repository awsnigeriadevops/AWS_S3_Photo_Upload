# from django.shortcuts import render
# import boto3
# from botocore.exceptions import NoCredentialsError
# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.contrib import messages

# # from urllib3 import request


# def index(request):
#     return render(request, "s3upload/index.html")


# def upload_to_s3(file, bucket_name, object_name=None, request=None):
#     """
#     Upload a file to an S3 bucket

#     :param file: File-like object to be uploaded
#     :param bucket_name: Name of the S3 bucket
#     :param object_name: S3 object name (key)
#     :return: True if successful, else False
#     """
#     storage_config = getattr(settings, "STORAGES", {}).get("default", {})
#     AWS_ACCESS_KEY_ID = storage_config.get("OPTIONS", {}).get("AWS_ACCESS_KEY_ID", None)
#     AWS_SECRET_ACCESS_KEY = storage_config.get("OPTIONS", {}).get(
#         "AWS_SECRET_ACCESS_KEY", None
#     )
#     try:
#         s3_client = boto3.client(
#             "s3",
#             aws_access_key_id=AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#         )

#         if object_name is None:
#             object_name = file.name
#             print(f"object_name: {object_name}")

#         s3_client.upload_file(file, bucket_name, object_name)
#         print(f"s3_client: {s3_client}")
#         print(f"Successfully uploaded {object_name} to {bucket_name}")
#         return True

#     except NoCredentialsError:
#         messages.error(request, "AWS credentials not available.")
#         return False
#     except Exception as e:
#         messages.error(request, f"Error uploading to S3: {str(e)}")
#         return False


# def upload_file(request):
#     if request.method == "POST":
#         file = request.FILES["image"]
#         storage_config = getattr(settings, "STORAGES", {}).get("default", {})
#         bucket_name = storage_config.get("OPTIONS", {}).get(
#             "AWS_STORAGE_BUCKET_NAME", None
#         )
#         # bucket_name = settings.AWS_STORAGE_BUCKET_NAME
#         if upload_to_s3(file, bucket_name, request=request):
#             print("Passed this area,upload_file")
#             messages.success(request, "File uploaded successfully to S3!")
#         else:
#             messages.error(request, "Failed to upload file to S3.")

#     return redirect("index")


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
