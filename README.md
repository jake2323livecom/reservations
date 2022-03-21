# reservations

## Purpose
This repo contains a full dev environment for the containerized reservations app.

- the .dockerignore file ensures that files used to build the docker images aren't copied into the images themselves at buildtime.
- The .gitignore file ignores .docker files so that you can create local docker images without them being copied into the repo. This simply saves space.
- There are two docker-compose files:
    - docker-compose.yml
        - Used for development
        - This docker compose file maps the web containers project directory to the repo so that you can make live changes during development.
    - docker-compose.prod.yml
        - Used for production
        - This compose file removes persistent storage for the web container altogether. The entire project directory is copied into the container image at buildtime.  Therefore, file changes in the web container aren't persistent, but they shouldn't need to be. 
        - You could optionally create a docker volume for the web container.

- The django project is called reservations and has three apps:
    - accounts
        - used to manage user accounts.  
        - uses the existed User model provided by Django, but has custom forms for user management
    - jcu_ball
        - for managing jcu_ball reservations
        - has a custom model for jcu ball reservations
    - summer_picnic
        - for managing picnic reservations
        - has separate model for picnic reservations

- The Django project has a templates directory located at the project root and this directory has been added to settings.py.  This is where the base template is located.

- The static_root is the staticfiles directory at the project root.  The web container and nginx container share a docker volume which maps to that directory.  URL aliasing is setup in the nginx.conf file so that requests to the /static/ url are actually redirected to the docker volume for static files.  Therefore, the nginx container is actually serving static files, not the web container.

- The scripts directory at the project root holds python scripts that act like jobs did in Nautobot.
    - each script must have a run() function to execute some code
    - running these scripts within the django environment requires you to install the django-extensions module in the web container (included in requirements.txt already) and to add it to the installed_applications variable in settings.py
    - the django-extensions module allows you to run a myriad of other commands with the manage.py script.
    - to run a script, use this syntax: python manage.py runscript PYTHON_FILE_NAME
    - 
    
- The requirements.txt file is copied to the web container during buildtime and determines which python modules are installed. This is the first step in the Dockerfile

- 
