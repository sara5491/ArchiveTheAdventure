# ARCHIVE THE ADVENTURE

The live site can be found at the following link: https://archive-adventure.herokuapp.com

# 1. OVERVIEW

(am i responsive)

This is my 3rd Milestone Project for Code Institute's Diploma in Web Application Development course.

'Archive The Adventure' is a website designed for lovers of photography and travel.
The platform allows users to upload their photographs and to be inspired by others that do the same.

# 2. USER STORIES

## <em>As a first time user I want to be able to...</em>
* Navigate the site easily, so that I can find what I need effectively.
* Have the purpose of the website be clearly evident upon first visit.
* View images without having to register first, so I can decide whether the site interests me or not.
* Search the images by keyword or location.
* Visit a site that is visually appealing and clear to understand.
* Access the site across all devices and for it to be accessible, even on small screens.
* Register an account and have a profile where I can keep track of any images I’ve uploaded.
* Contact the site owner with any questions or comments I may have.
* Follow/view the various social media accounts of the site.

## <em>As a returning user I want to be able to...</em>

# 7. DEPLOYMENT

## DATABASE DEPLOYMENT
The site uses a Mongodb database for data storage.
- Navigate to Mongo DB and log in/sign up
- Navigate to your ‘Cluster'
- Click the ‘Connect’ button
- Select ‘Connect Your Application’
- Copy the connection string and paste it in your env.py file (include your dbname and password)
- To confirm you are connected use the command 'show collection'

Since the env.py file contains sensitive information, it should not be stored in the Github repo.
So you must create your own, and store the environment variables required to configure the application.

Create an env.py file, and add the following environment variables:
```
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "your secret key")
os.environ.setdefault("MONGO_URI", "your mongodb connection string")
os.environ.setdefault("MONGO_DBNAME", "your dbname")
os.environ.setdefault("MAIL_USERNAME", "your email")
os.environ.setdefault("MAIL_PASSWORD", "your password")
```
Add your env.py file and pycache directory to .gitignore.

## DEPLOYMENT TO HEROKU
The site is hosted using Heroku, deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.
* Create an account in Heroku
* Click New and choose Create New App from the dropdown menu
* Choose an App name, which must be unique and choose a region closest to you then click create app.
* Go to the Deploy tab and click Connect to GithHub.
* Search for the name of the repository and click Connect.
* In the list of deployment methods, click 'Github' and link Heroku to your Gitub repository.
* You can choose Enable Automatic Deploys which will automatically update Heroku each time you commit.
* Hidden variables such as IP address, SECRET_KEY, MONGO_URI and MONGO_DATABASE need to be recorded in Heroku.
* Go to Settings, click Reveal Config Vars and fill out the values.
* When the app is deployed by Heroku correctly, the message will appear saying 'Your app was successfully deployed.’


# 8. CREDITS
## A) CODE SNIPPETS
- The Code Institute's Mini Project (Task Manager)
- Hover and text overlay on gallery photos - [30SecondsofCode](www.30secondsofcode.org/css/s/image-overlay-hover)
- Horizontal line on either side of headings - [Stackoverflow](www.stackoverflow.com/questions/15557627/heading-with-horizontal-line-on-either-side)
- Cards for images/navbar/delete modal - [MaterializeCSS](https://materializecss.com/)

## B) MEDIA
- Mountain/sky logo was created on [Canva](https://www.canva.com/help/article/licenses-copyright-commercial-use/)
- Camera icon in nabber was obtained from [FreeSVG](freesvg.org)
- Button icons were from [Font Awesome](https://fontawesome.com/)
- Website’s favicon was from [Favicon](https://favicon.io/)
- All photographs were taken by myself

## C) CONTENT
- All text content was written by myself

## D) LIBRARIES/TOOLS USED
- [RemoveBG](https://www.remove.bg/) - to make the logo background transparent
- [RandomKeyGen](https://randomkeygen.com/0) - to create secure passwords
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - to hash passwords
- [AmIResponsive](http://ami.responsivedesign.is/) - to create a mock-up of the website on various devices
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/) - to send emails to my gmail account via the contact form
- HTML5
- CSS
- JavaScript
- MongoDB
- Python
- Flask
- GitHub
- GitPod
- Heroku

## E) ACKNOWLEDGEMENTS
- Tutors at Code Institute and members of the Slack community for their continued help and support.