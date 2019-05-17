# wagtail-design-system

Proof-of-concept for a Wagtail-backed design system website with front-end
component code stored in the same repo (for now, simply copied over from
capital-framework with some minor modifications).


## Setup

1. If you're not set up to run Python 3 yet, go through our
   [guide to running both Python 2 and 3](https://github.com/cfpb/development/blob/master/guides/installing-python.md).
   You will need to be running Python 3 to test this project out.
1. Clone repo and go into its folder
1. Create a new Python virtualenv and activate it: `mkvirtualenv --python=python3 [virtualenv name]`
1. `pip install -r requirements.txt`
1. `./manage.py migrate`
1. `./manage.py runserver`
1. Visit http://localhost:8000/admin/ and login with `admin`/`admin`
