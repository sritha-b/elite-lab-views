# Elite Lab 3: Views

## Intro
In order to flex your newly learned responsive design skills, we will be creating a basic personal portfolio web site.

Your website should:
* Use the Bootstrap Grid System
* Break from side-by-side columns to stacked columns when viewed in tablet/mobile sizes
* Change font size between desktop and tablet/mobile

We have provided a starter template for you.

## Set Up
* Fork and clone the repository to your local dev environment

* Activate your virtual environment
```
python -m venv venv
source venv/bin/activate
```

* Install the dependencies to your virtual environment
```
pip install -r requirements.txt
```

* Spin up the local web server with:
```
FLASK_APP=app.py FLASK_ENV=development flask run
```

## Lab Steps
* Add a row with your contact info in 3 columns
  * Social Media Handle (or make a fake one)
  * Contact Email
  * Where you are based from

* Add 3 rows with 3 projects you worked on
  * 1 column should be an image
  * 1 column should be title and description

* The contact info row should break at the small breakpoint
* The project rows should break at the medium breakpoint