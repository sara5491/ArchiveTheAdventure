- [Encountered Issues](#ecountered-issues)
- [Testing User Stories](#testing-user-stories)
- [Testing Accessibility](#testing-accessibility)
- [Code Validation](#code-validation)
- [Known Issues](#known-issues)

## ENCOUNTERED ISSUES

I came across many(!) issues during the creation of my site. Most that have been dealt with but there are some still ongoing which are noted at the end of this section.

- After using Flask Mail to try and connect the contact form with my gmail account, I kept getting this issue -

![Screenshot of error page](documentation/flask-mail.png)

I discovered it was because I needed to have MFA with my gmail account. After setting this up, I was able to receive emails in my account.

- I had issues with the layout of my image cards after logging in and once the edit/delete buttons appeared.

![Screenshot of image cards layout issue](documentation/card-issue.png)

I (finally) worked out it was due to Materialize setting the width at 50% and I needed to overwrite this and once I changed the width to 33%, the cards looked fine.

![Screenshot of image cards fixed layout](documentation/cards-fixed-size.png)

- I had a few issues of some of the cards being in the wrong place. I found this was due to a couple of stray 'end div' tags.


## TESTING USER STORIES

### First Time User
* Navigate the site easily, so that I can find what I need effectively.

![Screenshot of navbar](documentation/user-stories/first-navbar.png)

* View images without having to register first, so I can decide whether the site interests me or not.

![Screenshot of gallery page](documentation/user-stories/first-view.png)

* Search the images by keyword or location.

![Screenshot of search bar](documentation/user-stories/first-search.png)

* Visit a site that is visually appealing and clear to understand.

![Screenshot of homepage](documentation/user-stories/first-visual.png)

![Screenshot of about us page](documentation/user-stories/first-clear.png)

* Access the site across all devices and for it to be accessible, even on small screens.

![Screenshot of site on mobile device](documentation/user-stories/first-responsive.png)

* Register an account and have a profile where I can keep track of any images I’ve uploaded.

![Screenshot of account signup page](documentation/user-stories/first-register.png)

* Contact the site owner with any questions or comments I may have.

![Screenshot of contact us form](documentation/user-stories/first-contact.png)

* Follow/view the various social media accounts of the site.

![Screenshot of footer with social links](documentation/user-stories/first-socials.png)


### Returning User
* Log in to the site and view my profile.

![Screenshot of user profile](documentation/user-stories/returning-profile.png)

* Edit and/or delete my images that I’ve previously uploaded to the site.

![Screenshot of edit/delete image buttons](documentation/user-stories/returning-edit.png)

* Be prompted as to whether I want to delete my image or not, so I don’t do so by mistake.

![Screenshot of delete modal](documentation/user-stories/returning-delete.png)

* Be able to see all images I’ve uploaded under my profile.

![Screenshot of profile](documentation/user-stories/returning-images.png)

* Browse all images uploaded by other users.

![Screenshot of all images uploaded by others](documentation/user-stories/returning-view.png)

![Screenshot of gallery](documentation/user-stories/returning-gallery.png)


### Admin User
* Add my own images onto the site.

![Screenshot of admin profile](documentation/user-stories/admin-add.png)

* Edit/Delete the images others have uploaded in case they are not appropriate.

![Screenshot of all photos that admin can edit/delete](documentation/user-stories/admin-add.png)

## TESTING ACCESSIBILITY

### Home Page Results
![Screenshot of lighthouse results for Home Page](documentation/lighthouse-screenshots/home.png)

The performance rating was low for the home page and Lighthouse suggested saving images in a file format other than .png or .jpg but this is not ideal as these formats are what most people save their photos as.

### About Us Results
![Screenshot of lighthouse results for About Us](documentation/lighthouse-screenshots/about.png)

### Browse Photos Results
![Screenshot of lighthouse results for Browse Photos](documentation/lighthouse-screenshots/browse.png)

### Contact Us Results
![Screenshot of lighthouse results for Contact Us](documentation/lighthouse-screenshots/contact.png)

### Log In Results
![Screenshot of lighthouse results for Log In](documentation/lighthouse-screenshots/login.png)

### Admin Page Results
![Screenshot of lighthouse results for Profile Page](documentation/lighthouse-screenshots/admin.png)

### Add Photo Results
![Screenshot of lighthouse results for Add Photo](documentation/lighthouse-screenshots/addphoto.png)


## CODE VALIDATION

### CSS VALIDATION
Passed The W3C CSS Validation Service without any issues.

### HTML VALIDATION
There were a couple of issues when using The W3C Markup Validation Service however these were seen as warnings rather than major errors.
 * [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Farchive-adventure.herokuapp.com%2F)
 * [Browse](https://validator.w3.org/nu/?doc=https%3A%2F%2Farchive-adventure.herokuapp.com%2Fbrowse)
 * [About](https://validator.w3.org/nu/?doc=https%3A%2F%2Farchive-adventure.herokuapp.com%2Fabout)
 * [Contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Farchive-adventure.herokuapp.com%2Fcontact)

## KNOWN ISSUES

* On some smaller devices, the search label currently covers two lines.

![Screenshot of search label](documentation/search-issue.png)

* The calendar cuts off the last letter of some months.

![Screenshot of calendar dropdown](documentation/calendar-cutoff.png)

