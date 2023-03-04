# ocr_google_vision_cloud

`pip install -r requirements.txt`  <br>
`python ocr1.py --image path/to/your/image.jpg --creds credentials_file.json`

<br>

to test with sample image    <br>
`python ocr1.py --image Car-Number-Plate.jpg --creds credentials_file.json`

<br>


---

<br> 
<br> 

## To get a JSON file containing your Google Cloud Vision API credentials, follow these steps:

1. Go to the Google Cloud Console and navigate to the project you want to use with the Vision API.

2. In the left-hand navigation menu, select "APIs & Services" and then "Credentials."

3. Click on the "Create credentials" button and select "Service account key."

4. Fill out the form with the following details:

Service account name: Choose a name for your service account.
Role: Select "Project" > "Editor" or another appropriate role for your use case.
Key type: Select "JSON."
Click "Create" to download the JSON file containing your credentials.