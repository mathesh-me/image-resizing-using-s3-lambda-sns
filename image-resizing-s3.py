import os
import boto3
from PIL import Image
from io import BytesIO

# Initialize AWS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Define the S3 buckets and SNS topic
bucket_1 = 'image-non-sized-1' # your-source-bucket
bucket_2 = 'image-sized-1' # your-destination-bucket
sns_topic_arn = 'arn:aws:sns:ap-south-1:804937851364:image-resizing-topic' # your-sns-topic

def lambda_handler(event, context):
    if 'Records' in event:
        # Handle S3 batch event
        for record in event['Records']:
            handle_s3_record(record)
    else:
        # Handle single S3 event
        handle_s3_record(event)

def handle_s3_record(record):
    # Ensure the event record structure is correct
    if 's3' in record and 'bucket' in record['s3'] and 'name' in record['s3']['bucket'] and 'object' in record['s3'] and 'key' in record['s3']['object']:
        # Get the bucket name and object key from the S3 event record
        source_bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        # Download the file from S3 bucket_1
        response = s3.get_object(Bucket=source_bucket, Key=object_key)
        content_type = response['ContentType']
        image_data = response['Body'].read()

        # Resize and compress the image
        resized_image = resize_and_compress_image(image_data)

        # Upload the resized and compressed image to S3 bucket_2
        destination_key = f"resized/{object_key}"
        s3.put_object(Bucket=bucket_2, Key=destination_key, Body=resized_image, ContentType=content_type)

        # Send a notification to the SNS topic
        message = f"Image {object_key} has been resized and uploaded to {bucket_2}"
        sns.publish(TopicArn=sns_topic_arn, Message=message)
    else:
        # Log an error message if the event record structure is unexpected
        print("Error: Invalid S3 event record structure")


def resize_and_compress_image(image_data, quality=75):
    # Open the image using PIL
    image = Image.open(BytesIO(image_data))

    # Compress the image
    image_io = BytesIO()
    image.save(image_io, format=image.format, quality=quality)

    return image_io.getvalue()
