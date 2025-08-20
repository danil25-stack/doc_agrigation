import os 


AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME', 'raw-article')
AWS_REGION = os.getenv('AWS_REGION', 'eu-central-1')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
