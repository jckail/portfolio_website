# resume_app

Hi there.
This is a Django web app to help me showcase my tech skills.

I deployed this to google cloud run via:
docker build -t gcr.io/MY_PROJECT/resume_app:v2 --platform linux/amd64 .
docker push gcr.io/MY_PROJECT/resume_app:v2
gcloud run deploy portfloliowebsite --image gcr.io/MY_PROJECT/resume_app:v2 --platform managed --region us-central1 --allow-unauthenticated
