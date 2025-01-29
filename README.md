# Hella Webinar 2025

Code Repository for the webinar

# Setting Up the Project

Step 1: Clone the Starter Code

git clone <repo-link>

Step 2: Install Dependencies

pip install -r backend/requirements.txt

Step 3: Run Locally

python backend/app.py


# Deploy Backend using AWS Lambda & API Gateway

Step 1: Package & Deploy Python Flask App

zip -r function.zip backend/*

Step 2: Upload to AWS Lambda 

Deploy the backend as a Lambda function.

# Deploy Frontend on AWS S3

Step 1: Enable S3 Static Website Hosting

Upload frontend files to an S3 bucket.

Modify bucket policy for public access.

Step 2: Configure CloudFront (Optional for HTTPS)

Set up CloudFront to serve S3 content securely.
