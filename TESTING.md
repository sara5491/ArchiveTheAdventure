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
 

## KNOWN ISSUES

* On mobile devices, the search label currently covers two lines.
![Screenshot of search label](documentation/search-issue.png)

* The calendar cuts off the last letter of some months.
![Screenshot of calendar dropdown](documentation/calendar-cutoff.png)

