# INSTACLONE

## Author

[Joy Kolia](https://github.com/jLuseno161)

## Description

A sample replica of the instagram application made using Django where a user can upload their images/posts and also view posts made by other people.

## Live Link

[View Site](https://instaclone0.herokuapp.com)

## Admin Dashboard

[Admin Dashboard Login](https://instaclone0.herokuapp.com/admin/)  with credentials
    username : `moringa`
    password : `@Moringa20`

## User Story
* User can signup & signin to the application
* User can upload their photos
* User can comment on posts made by other users
* User is able to edit there profile
* Current user is able to view their profile with the photos they posted
* User is able to view other users pictures on their timeline
* When user clicks on a single photo it expands it and user is able to view the details of the photo in a modal.

## Prerequisites

You need the following to start working on this project: On your local system; 

1. Python3.8
2. Django
3. Pip
4. Virtual Environment(venv)
5. A text editor

## Development Installation

To get the code..

1. Clone the repository:
 `git clone  https://github.com/jLuseno161/InstaClone.git`

2. Move to the folder and install requirements
 ` cd InstaClone`

3. In the projects root directory, install the virtualenv library using pip and create a virtual environment. Run the following commands respectively:
    - **`pip install virtualenv`**
    - **`virtualenv venv`**
    - **`. venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
4. Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
5. Launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    - To upload photos as admin, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.

## Technology used

* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* Git
* Bootstrap 4.3.1

## Known Bugs

* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [joyluseno0@gmail.com]

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright © 2021  [JOY L. KOLIA](https://github.com/jLuseno161)
