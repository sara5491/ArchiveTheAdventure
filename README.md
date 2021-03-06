- [ARCHIVE THE ADVENTURE](#archive-the-adventure)
- [1. OVERVIEW](#1-overview)
- [2. UX](#2-ux)
  * [USER STORIES](#user-stories)
    + [<em>As a first time user (or as someone who has not registered) I want to be able to...</em>](#-em-as-a-first-time-user--or-as-someone-who-has-not-registered--i-want-to-be-able-to--em-)
    + [<em>As a returning user I want to be able to...</em>](#-em-as-a-returning-user-i-want-to-be-able-to--em-)
    + [<em>As an admin user I want to be able to...</em>](#-em-as-an-admin-user-i-want-to-be-able-to--em-)
  * [STRATEGY](#strategy)
    + [SITE OWNER GOALS](#site-owner-goals)
    + [TARGET AUDIENCE](#target-audience)
  * [SCOPE](#scope)
    + [FUNCTIONAL REQUIREMENTS](#functional-requirements)
    + [CONTENT REQUIREMENTS](#content-requirements)
  * [STRUCTURE](#structure)
    + [DATABASE](#database)
  * [SKELETON](#skeleton)
    + [WIREFRAMES](#wireframes)
  * [SURFACE](#surface)
    + [DESIGN](#design)
      - [COLOUR PALETTE](#colour-palette)
      - [TYPOGRAPHY](#typography)
      - [ICONS & LOGO](#icons---logo)
- [3. FEATURES](#3-features)
  * [EXISTING FEATURES](#existing-features)
    + [Home](#home)
    + [About Us](#about-us)
    + [Contact Us](#contact-us)
    + [Browse Gallery](#browse-gallery)
    + [Profile](#profile)
    + [Add Photo](#add-photo)
    + [Edit Photo](#edit-photo)
    + [Log Out](#log-out)
    + [Admin](#admin)
    + [404 Error](#404-error)
  * [FUTURE IMPLEMENTATION](#future-implementation)
- [4. TESTING](#4-testing)
- [5. DEPLOYMENT](#5-deployment)
  * [DATABASE DEPLOYMENT](#database-deployment)
  * [DEPLOYMENT TO HEROKU](#deployment-to-heroku)
- [6. CREDITS](#6-credits)
  * [CODE SNIPPETS](#code-snippets)
  * [MEDIA](#media)
  * [CONTENT](#content)
  * [LIBRARIES/TOOLS USED](#libraries-tools-used)
  * [ACKNOWLEDGEMENTS](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# ARCHIVE THE ADVENTURE

The live site can be found at the following link: https://archive-adventure.herokuapp.com

# 1. OVERVIEW

![Am I Responsive?](documentation/readme-images/amiresponsive.png)

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
* Register an account and have a profile where I can keep track of any images I???ve uploaded.
* Contact the site owner with any questions or comments I may have.
* Follow/view the various social media accounts of the site.

### <em>As a returning user I want to be able to...</em>
* Log in to the site and view my profile.
* Edit and/or delete my images that I???ve previously uploaded to the site.
* Be prompted as to whether I want to delete my image or not, so I don???t do so by mistake.
* Be able to see all images I???ve uploaded under my profile.
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

- **CREATE** ??? A function we can call when a new image is being added to the database. The user can supply the values for category_name (continent), photo_name, photo_description, date_taken and image_url.

- **READ** ??? A function we can call to retrieve information from the database and display the results of all the images currently available to read in our database. All visitors to the website can browse all images without having to sign up for an account.

- **UPDATE** ??? A function we can call when information about an image needs to be changed. The user can edit the values for category_name (continent), photo_name, photo_description, date_taken and image_url. After the function is called, the corresponding entry in the image database will contain the updated fields. This option is only available to the uploader of the image. The admin user can edit and delete anyone???s images.

- **DELETE** ??? A function we can call to remove a particular image from the database. This option is only available to the uploader of the image.

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

### CONTENT REQUIREMENTS
* Most of the site content is provided by its users.
* All images are shown on the home page so it is clear what the purpose of the site is when a user first enters it.

## STRUCTURE

- **HOME/PHOTOS PAGE** (get_photos.html) - The Home Page of the website contains all image cards for all users to view. There is a sticky navbar at the top which is shown on all pages and contains the logo and links to all other pages of the site. At the bottom of the page there is a footer that is also placed on all other pages, which contains social media links.

- **ABOUT US** (about.html) - This clearly outlines the purpose of the site and encourages users to sign up.

- **BROWSE IMAGES PAGE** - (browse.html) - This page allows users to easily see all images that have been uploaded to the site. The name of the photo and the username of who uploaded it is shown when the image is hovered over.

- **LOG IN PAGE** (login.html) - The Log In page allows users who already have an account to log in to their profile. When the user logs in successfully, they are redirected to their unique profile page where they can view, edit and delete their images. A 'Log Out??? tab is visible and the Register is hidden once a user logs in.

- **REGISTER PAGE** (register.html) - The Register page allows users to create an account by entering a unique username and password. When the user registers successfully, they are redirected to their profile page where they can add, edit, delete and view existing images.

- **PROFILE PAGE** (profile.html) - The Profile Page is unique to each user and is available after the user registers and logs in successfully. They can add, edit, delete and view their existing images. An ???Add New Photo??? button is available at the top of the screen which takes users to the add_photo page.

- **ADD PHOTO PAGE** (add_photo.html) - The Add Photo page allows users to add a new image by submitting a form. The user needs to enter the required fields for photo_name, photo_description, category_name, date_taken and image_url. The photo is displayed on the Home page, the Browse Gallery page and the Profile page.

- **EDIT PHOTO PAGE** (edit_photo.html) - The Edit Photo page allows users to edit or delete any of their uploaded photos. The Cancel button takes them back to the home page.

- **ADMIN PAGE** (admin.html) - The Admin Page allows the website administrator to add, edit and delete any photos. Only the admin user has access to this page via a link in the navbar.

- **CONTACT PAGE** (contact.html) - The Contact Page allows users send a form to the site owner which contains: an email and message field that are required to be filled in.

### DATABASE

MongoDB will handle all data and collections and a diagram of the structure can be seen below:
![MongoDB database collections](documentation/readme-images/mongodb.png)

## SKELETON

### WIREFRAMES
* [Home page](documentation/wireframes/home.png)
* [About Us](documentation/wireframes/about.png)
* [Browse](documentation/wireframes/browse.png)
* [Profile](documentation/wireframes/profile.png)
* [Log In](documentation/wireframes/login.png)
* [Register](documentation/wireframes/register.png)
* [Contact](documentation/wireframes/contact.png)

## SURFACE

### DESIGN
I wanted the feel of the website to be relaxed with no overly bright colours. I also wanted the tones to be muted as to not distract too much from the images. 

#### COLOUR PALETTE
![Colour palette used for website](documentation/readme-images/colours.png)

#### TYPOGRAPHY
I chose the font 'JetBrains Mono' from Google Fonts for all typography on the site. 

#### ICONS & LOGO
I have used a line drawing of a camera as an icon in the navbar which takes the user to the homepage when clicked on. I overlayed this same icon onto the main logo of the site to create consistency. The logo brings together the two main elements of the platform - travel (or adventure) and photography.

* [Logo mockups](documentation/readme-images/logos.png)

# 3. FEATURES

## EXISTING FEATURES

### Home
The landing page. Navbar in image shows what the admin user sees when they are logged in.
![Homepage](documentation/readme-images/features/01homepage.png)
Footer has links to all social media accounts.
![Homepage footer](documentation/readme-images/features/02homepage.png)

### About Us
![About Us](documentation/readme-images/features/03aboutus.png)

### Contact Us
Contact Us form which is set up to send an email to archivetheadventure@gmail.com (an email address I made for this project).
![Contact Us](documentation/readme-images/features/04contactus.png)
![Email Account](documentation/readme-images/features/15gmail.png)

### Browse Gallery
Name of the image is shown when hovered over - or tapped when on mobile.
![Browse the Gallery](documentation/readme-images/features/05gallery.png)

### Profile
Users can either edit/delete from the main photos page or from their profile.
![Profile Page](documentation/readme-images/features/06profile.png)

### Add Photo
![Add Photo](documentation/readme-images/features/07addphoto.png)
Calendar doesn't allow users to choose a future date.
![Date Taken](documentation/readme-images/features/08calendar.png)

Users must choose a continent from the dropdown where the image was taken.
![Category Dropdown](documentation/readme-images/features/09continent.png)

### Edit Photo
![Edit Photo](documentation/readme-images/features/13editphoto.png)
A modal is triggered when user clicks 'delete' so they are prompted to confirm deletion or they can exit back to the homepage.
![Delete Modal Trigger](documentation/readme-images/features/10deletemodal.png)

### Log Out
![Log Out](documentation/readme-images/features/11logout.png)

### Admin
The admin user can edit/delete all users' photos.
![Admin](documentation/readme-images/features/12admin-all.png)

### 404 Error
404 error page when incorrect link is clicked.
![404 Error](documentation/readme-images/features/14error.png)

## FUTURE IMPLEMENTATION
* Enable users to comment on images.
* Enable users to rate images.
* Enable file upload rather than using an image URL.
* Enable users to change their username and/or password if they wish.
* Enable a 'forgotten your password' system.
* Confirmation of password when a user registers or logs in to the site.
* Pagination on home page and gallery page to stop endless scrolling.
* Inappropriate/offensive image filter. Rejects the image and stops users adding it to the database.
* Allow users to click on a photo and it will take them to a page which shows the photo at its full size.
* Allow admin to manage user accounts.
* A more comprehensive search function.
* Allow users to crop/resize their image so they can change the focus point.


# 4. TESTING

Testing information can be found in the [TESTING.md](TESTING.md) file.

# 5. DEPLOYMENT

## DATABASE DEPLOYMENT
The site uses a Mongodb database for data storage.
- Navigate to Mongo DB and log in/sign up
- Navigate to your ???Cluster'
- Click the ???Connect??? button
- Select ???Connect Your Application???
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
![Heroku deployment](documentation/readme-images/deployment1.png)
* Choose an App name, which must be unique and choose a region closest to you then click create app.
![Heroku deployment](documentation/readme-images/deployment2.png)
* Go to the Deploy tab and click Connect to GithHub.
* Search for the name of the repository and click Connect.
* In the list of deployment methods, click 'Github' and link Heroku to your Gitub repository.
* You can choose Enable Automatic Deploys which will automatically update Heroku each time you commit.
* Hidden variables such as IP address, SECRET_KEY, MONGO_URI and MONGO_DATABASE need to be recorded in Heroku.
* Go to Settings, click Reveal Config Vars and fill out the values.
* When the app is deployed by Heroku correctly, the message will appear saying 'Your app was successfully deployed.???


# 6. CREDITS
## CODE SNIPPETS
- The Code Institute's Mini Project (Task Manager)
- Hover and text overlay on gallery photos - [30SecondsofCode](www.30secondsofcode.org/css/s/image-overlay-hover)
- Horizontal line on either side of headings - [Stackoverflow](www.stackoverflow.com/questions/15557627/heading-with-horizontal-line-on-either-side)
- Cards for images/navbar/delete modal - [MaterializeCSS](https://materializecss.com/)

## MEDIA
- Mountain/sky logo was created on [Canva](https://www.canva.com/help/article/licenses-copyright-commercial-use/)
- Camera icon in nabber was obtained from [FreeSVG](freesvg.org)
- Button icons were from [Font Awesome](https://fontawesome.com/)
- Website???s favicon was from [Favicon](https://favicon.io/)
- Google Fonts library
- All photographs were taken by myself

## CONTENT
- All text content was written by myself

## LIBRARIES/TOOLS USED
- [RemoveBG](https://www.remove.bg/) - to make the logo background transparent
- [RandomKeyGen](https://randomkeygen.com/0) - to create secure passwords
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - to hash passwords
- [AmIResponsive](http://ami.responsivedesign.is/) - to create a mock-up of the website on various devices
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/) - to send emails to my gmail account via the contact form
- [ImgBB](https://imgbb.com/) - image hosting
- HTML5
- CSS
- JavaScript
- MongoDB
- Python
- Flask
- GitHub
- GitPod
- Heroku

## ACKNOWLEDGEMENTS
- Tutors at Code Institute for dealing with my <s>stupid</s> questions and members of the Slack community for their continued help and support.