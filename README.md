# Elite Lab 3: Views

## Intro
In order to flex your newly learned responsive design skills, we will be creating a basic personal portfolio web site.

There are two pages:
* The Home page
* The Lab Exercise page

The Lab Exercise page will be a sandbox for us to throw some HTML and CSS around.

The Home page will eventually be copied into your final project. Feel free to continue customizing this page after the lab is over.

### Quick References
Read up on Flask Templates: https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/
HTML Intro and mega reference: https://www.w3schools.com/html/html_intro.asp
CSS Intro and mega reference: https://www.w3schools.com/css/css_intro.asp

## Set Up
* Fork and clone the repository to your local dev environment
```
git clone <url of your forked repository>
cd elite-lab-views
```

* Activate your virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

* Install the dependencies to your virtual environment
```
pip3 install -r requirements.txt
```

* Spin up the local web server with:
```
python3 -m flask run
```

## Lab Steps

Lab today will have 2 sections:

* Section 1: I will be sharing my screen and we will be going through section 1 together.
* Section 2: You will have time to fill in your portfolio site with details from your resume. This will eventually be used for your final project, so feel free to keep working on it afterwards.


### Section 1

* Edit the `exercise.css` file to move the text that says `Move me to the left!` to the left.
  * Quick hint, if you make changes to css files, you may need to hard refresh.
    * For Mac Users, you can do this with `Cmd + Shift + R`
    * For Windows Users, you can do this with `Ctrl + F5`

* Now move over into `exercise.html`

* Add a row with your contact info in 3 columns
  * Name
  * Contact Email
  * Where you are based from

* Add 3 rows with 3 projects you worked on
  * 1 column should be a title
  * 1 column should be a description

* The contact info row should break at the small breakpoint
* The project rows should break at the medium breakpoint

* Move over into `index.html`
* Add a personal image into the `/img/` folder
* Update one of the image cards at the bottom to show the newly added image

### Section 2

In this section, you will edit the contents of `index.html` to fill in your personal accomplishments, information, etc.

Use the information from the resume assignment to help fill in the home page.

Basic steps you should complete:
* Fill in the Experience/Projects/Accomplishments content
* Replace the image cards with your own images and provide some sort of title or caption
* Replace the blurb, banner, and footer with your details.

You guys are completely free to remove, move around, edit, change, and add content. I've attempted to make as blank of a personal resume website for you as possible. In the end, it's up to you on how much you want to make it yours.

Reach out if you are stuck, don't know how to do something, or have any questions in general.

Your content here will eventually end up on your final project (which will be deployed to the web). Feel free to keep tweaking and adding to this throughout the rest of our course! I'm always happy to help outside of class hours.
