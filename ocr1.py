import argparse
import io
import os

from google.cloud import vision_v1
from google.oauth2 import service_account

# Create an argument parser to receive the file paths
parser = argparse.ArgumentParser()
parser.add_argument('--creds', help='Path to the credentials JSON file',default='focus-skein-304910-8d3e63c5dc1c.json')
parser.add_argument('--image', help='Path to the image file')
args = parser.parse_args()

# Set the path to your credentials JSON file
creds_path = args.creds

# Create a client object for the Vision API
creds = service_account.Credentials.from_service_account_file(creds_path)
client = vision_v1.ImageAnnotatorClient(credentials=creds)

# Set the path to your image file
image_path = args.image

# Load the image file into memory
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# Create an image object
image = vision_v1.types.Image(content=content)

# Set the type of annotation you want to perform (in this case, OCR)
feature = vision_v1.types.Feature(type=vision_v1.types.Feature.Type.TEXT_DETECTION)

# Create a request object containing the image and the feature
request = vision_v1.types.AnnotateImageRequest(image=image, features=[feature])

# Send the request to the Vision API and store the response
response = client.annotate_image(request=request)

# Extract the OCR text from the response
ocr_text = response.text_annotations[0].description

# Print the OCR text
print(ocr_text)

