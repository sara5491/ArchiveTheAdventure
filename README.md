# ARCHIVE THE ADVENTURE

The live site can be found at the following link: https://archive-adventure.herokuapp.com

# 1. OVERVIEW

(am i responsive)

This is my 3rd Milestone Project for Code Institute's Diploma in Web Application Development course.

'Archive The Adventure' is a website designed for lovers of photography and travel.
The platform allows users to upload their photographs and to be inspired by others that do the same.

# 2. UX

## USER STORIES

### <em>As a first time user (or as someone who has not registered) I want to be able to...</em>
* Navigate the site easily, so that I can find what I need effectively.
* Have the purpose of the website be clearly evident upon first visit.
* View images without having to register first, so I can decide whether the site interests me or not.
* Search the images by keyword or location.
* Visit a site that is visually appealing and clear to understand.
* Access the site across all devices and for it to be accessible, even on small screens.
* Register an account and have a profile where I can keep track of any images I’ve uploaded.
* Contact the site owner with any questions or comments I may have.
* Follow/view the various social media accounts of the site.

### <em>As a returning user I want to be able to...</em>
* Log in to the site and view my profile.
* Edit and/or delete my images that I’ve previously uploaded to the site.
* Be prompted as to whether I want to delete my image or not, so I don’t do so by mistake.
* Be able to see all images I’ve uploaded under my profile.
* Browse all images uploaded by other users.

### <em>As an admin user I want to be able to...</em>
* Add my own images onto the site.
* Edit/Delete the images others have uploaded in case they are not appropriate.

## STRATEGY

### SITE OWNER GOALS
* Create a user-friendly platform which allows photography and travel enthusiasts to inspire each other with their images.
* Allow users to easily sign up for an account/log in and access their profile.
* Create a loyal following and community of users who will continuously use the platform.
* Create an application that is easy to use and fully responsive on all major screen sizes.
* Implement CRUD (Create, Read, Update, Delete) functionality which allows users to add, edit and delete their images.
* Implement defensive design through data validation and authentication.
* Allow for simple design and navigation of the application.

### TARGET AUDIENCE
The target audience of the site are people who enjoy travelling and taking photos, whether as a casual hobby or as a profession. 
Potential visitors could also include those that only want to browse images, and not upload their own. The target visitor is not limited by their level of knowledge or skill, or whether they use a top of the range camera or their mobile phone.

## SCOPE

### FUNCTIONAL REQUIREMENTS

CRUD functionality (Create, Read, Update, and Delete) is required for this project so these are implemented as a part of the essential features.

- CREATE — A function we can call when a new image is being added to the database. The user can supply the values for category_name (continent), photo_name, photo_description, date_taken and image_url.

- READ — A function we can call to retrieve information from the database and display the results of all the images currently available to read in our database. All visitors to the website can browse all images without having to sign up for an account.

- UPDATE — A function we can call when information about an image needs to be changed. The user can edit the values for category_name (continent), photo_name, photo_description, date_taken and image_url. After the function is called, the corresponding entry in the image database will contain the updated fields. This option is only available to the uploader of the image. The admin user can edit and delete anyone’s images.

- DELETE — A function we can call to remove a particular image from the database. This option is only available to the uploader of the image.

* Responsive on all devices.
* Ability to register, login and logout.
* Full CRUD functionality to Add, Read, Edit and Delete images.
* A page for users to add images to the platform.
* A page for users to edit/delete images to the platform.
* Search by a keyword function so users can search for specific images or locations.
* 404 page that appears for an invalid URL and a button that takes users back to the Home page.
* Contact page where users can email the site owner.
* Admin privileges to edit/delete any images that are offensive/inappropriate.
* Profile page where users can see all their previously uploaded images.




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