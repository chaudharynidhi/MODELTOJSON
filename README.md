# MODELTOJSON

APP that shows the JSON format for the data stored in the db through custom management codebase.

APP is deployed for production using Heroku: https://modeltojsonapi.herokuapp.com/

To get the JSON format we can use: https://modeltojsonapi.herokuapp.com/?format=json
 
 Steps to go through the APP codebase:
 
 1. Check out the models.py file for the db structure for the 2 models: Users and Activity Period.
 2. Then for custom management codebase go to the management/commands/create_user file and check the data added to the db
 3. In Serializer.py file, converted the Model Data format to JSON Format.
 4. In views.py file used the serialized data to be displayed in the GET response for the API.
 5. In admin.py file registered the twop models to be accessible through the admin portal.
 
 For deploying the codebase to Heroku:
 
 1. Added a Procfile in the root directory.
 2. Installed gunicorn
 3. Installed django-heroku and added  ```django_heroku.settings(locals())```
 4. Build the requirements.txt for buildin the environment for the webapp to run.
 
 DB used is sqlite3
