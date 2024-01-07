# AWS S3 MEDIA FILES UPLOAD PROJECT

This project is designed to upload media files to Amazon Simple Storage Service. Django was used to build the application that seamlessly implements this feature. Note that Python must be installed on the host system

## Getting Started

Follow these steps to get your development environment set up:

### 1. Clone the Repository

```bash
git clone https://github.com/blackxavier/AWS_S3_Photo_Upload.git
```

### 2. Change Directory

```
cd AWS_S3_Photo_Upload
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add environment variables in the project root directory

Create a file called .env and add AWS S3 required environment variables generated from AWS IAM console. See example below:

```
AWS_ACCESS_KEY_ID=AKIAuseyourown
AWS_SECRET_ACCESS_KEY=Pfh+useyourownUbYEuv1SjHzt2Y+at
AWS_STORAGE_BUCKET_NAME=project1-bucuseyourownket-123456
AWS_S3_REGION_NAME=us-east-1
AWS_S3_CUSTOM_DOMAIN=%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
```

### 5. Install Dependencies

```
python manage.py runserver
```

### 6. Test Application

Access server at localhost:8000
