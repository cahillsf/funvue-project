# WIP
# Web app "funvue"

Using Datadog products APM, Continous Profiler, and RUM


## Database: MongoDB
* containerized -> from base directory `funvue-project` run `docker compose up --build`

## Back end: Flask
* from `flask-server` activate your virtual environment: https://docs.python.org/3/library/venv.html

* run `pip install requirements.txt` to install dependencies

* run `ddtrace-run python3 app.py` to start the flask server

## Front end: Vue
* from funvue directory: `npm run dev` to start the development server
* website will be running at http://localhost:8080
