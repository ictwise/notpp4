Back to [README](../../README.md)

# Deployment Steps

## **Contents**

- [**Heroku Deployment**](#heroku-deployment)
- [**Connecting to Heroku**](#connecting-to-heroku)
- [**AWS**](#amazon-aws)
- [**GMail Client**](#gmail-client)
- [**Config Vars**](#config-vars)
- [**How to contribute to the site**](#how-to-contribute-to-the-site)
- [**How to run the project locally**](#how-to-run-the-project-locally)


### **Heroku Deployment**



The project was developed using [GitPod](https://gitpod.io/) and pushed to [GitHub](https://github.com/) then deployed on Heroku using these instructions:

Deployment

### **Setting up Database**
Create an ElephantSQL account
Log in to ElephantSQL.com to access your dashboard
Click “Create New Instance”
Set up your plan
•	Give your plan a Name (this is commonly the name of the project)
•	Select the Tiny Turtle (Free) plan
•	You can leave the Tags field blank
Select “Select Region”
Select a data center near you
click “Create instance”
Log into Heroku
Click New to create a new app
Give your app a name and select the region closest to you. When you’re done, click Create app to confirm
Open the Settings tab
Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL.
Open up your Gitpod tab
In the terminal, install dj_database_url and psycopg2
pip3 install dj_database_url==0.5.0 psycopg2
Update your requirements.txt
pip freeze > requirements.txt
In your settings.py file, import dj_database_url underneath the import for os
import os
 import dj_database_url

Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated

# DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }

In the terminal, run the showmigrations command to confirm you are connected to the external database
python3 manage.py showmigrations

Migrate your database models to your new database

 python3 manage.py migrate

Create a superuser for your new database

python3 manage.py createsuperuser

login to your app admin, go to categories and create the categories of repair and service.
You might want to add some Products but there will be opportunity to create these later through the add_product page.
Finally, to prevent exposing our database when we push to GitHub, we will delete it again from our settings.py
For now, your DATABASE setting in the settings.py file should look like this

 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }

Confirm that the data in your database on ElephantSQL has been created
On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”

Click the Table queries button, select auth_user(public)

When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database

To prevent 500 errors during login on a deployed site you need to make a one line addition to your settings file.
ACCOUNT_EMAIL_VERIFICATION = 'none'
#### **Connecting to Heroku**Install gunicorn
Pip3 install gunicorn
Pip3 freeze > requirements.txt
Create a Procfile
web: gunicorn ecobiketech.wsgi:application (ensure there are no empty spaces or blank lines)
disable collectstatic.
By using Heroku config:set  DISABLE_COLLECTSTATIC = 1 –app
add the hostname of our Heroku app and local host to ALLOWED_HOSTS in settings.py
ALLOWED_HOSTS =[‘ecobiketech’, ‘localhost’]
Commit changes to GitHub using *git add .*, *git commit -m <commit message>*, *git push*.
Then deploy to Heroku using *git push heroku main*
If the git remote isn't initialised you may have to do that first by running *heroku git:remote -a <heroku-app-name>
From Heroku dashboard click "Deploy" -> "Deployment Method" and select "GitHub"
Search for your GitHub repo and connect then Enable Automatic Deploys.
Generate secret key. Strong secret keys can be obtained from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/). This automatically generates a secret key 50 characters long with alphanumeric characters and symbols.
Add secret key to GitPod variables and Heroku config vars

#### **Amazon AWS**

1. Create Amazon AWS account and create a new bucket in the S3 services and choose your closest region.
2. Uncheck block all public access and create bucket. 
3. From Properties tab turn on static website hosting using default values of index.html and errors.html.
4. On permissions tab include CORS configuration:
```python
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Create security policy: S3 Bucket Policy, allow all principles by adding a * and Amazon S3 services and selecting Get Object action. Paste ARN from Bucket Policy, add statement, generate policy and copy and paste into Bucket Policy. Also add /* at end of resource key to allow use of all pages. 
6. Under public access select access to all List Objects. 

7. Create Group for the bucket through IAM. Create policy by importing AWS S3 Full Access policy and add ARN from bucket to the policy resources. Attach policy to group. 
8. Create user, give programmatic access and add user to the group. Download CSV file when prompted to save access key ID an secret access key to save to environment and config [variables](#config-vars).
9. Add AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME = 'eu-west-2' to settings.py.
10. Add, commit and push to GitHub then navigate to Heroku to confirm static files collected successfully on the Build Log. The DISABLE_COLLECTSTATIC variable can now be deleted.
#### **GMail Client**

In `settings.py` change the `DEFAULT_FROM_EMAIL` to your own email address.

1. Go to your Gmail account and navigate to the 'Settings' tab.
2. Go to 'Accounts and Imports', 'Other Google Account Settings'.
3. Go to the 'Security' tab, and scroll down to 'Signing in to Google'.
4. If required, click to turn on '2-step Verification**', then 'Get Started', and enter your password.
5. Verify using your preferred method, and turn on 2-step verification.
6. Go back to 'Security', 'Signing in to Google', then go to 'App Passwords'.
7. Enter your password again if prompted, then set 'App' to `Mail`, 'Device' to `Other`, and type in `Django`.
8. Copy and paste the passcode that shows up, this is your '**EMAIL_HOST_PASS**' variable to add to your environment/config variables. '**EMAIL_HOST_USER**' is the Gmail email address.

### **Config Vars**

The config/environment variables should be set up as follows:

| Key                    | Value                      |
| ---------------------- |--------------------------- |
| PORT                   | 8000                       |
| IP                     | 0.0.0.0                    |
| SECRET_KEY             | YOUR_SECRET_KEY            |
| STRIPE_PUBLIC_KEY      | STRIPE_PUBLIC_KEY          |
| STRIPE_SECRET_KEY      | YOUR_STRIPE_SECRET_KEY     |
| STRIPE_WH_SECRET       | STRIPE_WEBHOOKS_KEY        |
| DATABASE_URL           | YOUR_POSTGRES_URL          |
| AWS_ACCESS_KEY_ID      | YOUR_AWS_ACCESS_KEY_ID     |
| AWS_SECRET_ACCESS_KEY  | YOUR_AWS_SECRET_ACCESS_KEY |   
| USE_AWS                | True                       |
| EMAIL_HOST_PASS        | YOUR_EMAIL_HOST_PASSCODE   |
| EMAIL_HOST_USER        | YOUR_EMAIL_HOST_USERNAME   |


#### Where to find Config Var Key-value Pairs 

To find the values of each key:

- SECRET_KEY: This is a random string provided when creating the Django project and can easily be changed to ensure extra security. 
- DATABASE_URL: This is temporary.
- STRIPE_PUBLIC_KEY: Retrived from Stripe Dashboard in the Developer's API section (Publishable key).
- STRIPE_SECRET_KEY: Retrived from Stripe Dashboard in the Developer's API section (Secret key)
- STRIPE_WH_SECRET: Retrived from Stripe Dashboard in the Developer's after creating an endpoint for your webhook (Signing secret).
- EMAIL_HOST_USER: Your email address or username. [See below for instructions](#smtp-setup).
- EMAIL_HOST_PASS: Your passcode from your email client. [See below for instructions](#smtp-setup).
- AWS_SECRET_ACCESS_KEY: From the CSV file that you download having created a User in Amazon AWS S3. [See below for instructions](#amazon-aws).
- AWS_ACCESS_KEY_ID: From the CSV file that you download having created a User in Amazon AWS S3. [See below for instructions](#amazon-aws).


### How to contribute to the site

1. Navigate to [GitHub](https://github.com/) and log in
2. Locate my [repo](https://github.com/ictwise/notpp4/)
3. On the right side of the screen click Fork
4. This creates a copy in your own repository to make changes in [GitPod](https://gitpod.io/)
5. Once finished with changes add, commit and push to your own [GitHub](https://github.com/)
6. Click Pull Requests and select "New Pull Request" button.


### How to run the project locally

To clone this project from GitHub follow the instructions taken from [GitHub Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) explained here:
1. Navigate to the [GitHub Repository](https://github.com/ictwise/notpp4/)
3. To clone using HTTPS click the clipboard symbol under "Clone with HTTPS". To clone using SSH key click Use SSH then click the clipboard symbol. To clone using GitHub CLI select Use GitHub CLI and click the clipboard symbol. 
4. Open Git Bash
5. Change the working directory to the location you want the cloned directory to be.
6. Type 'git clone' and paste the url copied from step 3. 
7. Press 'enter' to create your clone.

[Back to contents](#contents)

