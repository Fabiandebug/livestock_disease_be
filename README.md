# livestock_disease_be

Interview Test Task for livestock set of manuals in English and Kiswahili that contain livestock disease information. These manuals contains information in plain text, bullet points, pictures and illustration.

# App Setup

create your venv

# python -m venv venv

activate the windows venv using

# .\venv\Scripts\activate.

activate the linux venv using

# source venv/bin/activate

run

# pip install -r requirements.txt

create the config.ini file in the root DIR and copy the configuration setting from the config.ini.template file.
Populate the fields with your mysql database settings

Run

# python manage.py makemigrations

This will initiate db
Run

# python manage.py migrate

This will setup the db
run

# python manage.py runserver

This wil startup Django app server which will run on 'http://localhost:8000/'
