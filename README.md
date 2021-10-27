# WIP
# Web app "funvue"

Using Datadog products APM, Continous Profiler, and RUM


## Database: MongoDB
* containerized -> from base directory `funvue-project` run `docker compose up --build`

## Back end: Flask
* from `flask-server` activate your virtual environment: https://docs.python.org/3/library/venv.html

* install dependencies: run `pip install -r requirements.txt` 

* run `ddtrace-run python3 app.py` to start the flask server

## Front end: Vue
* install depedendencies: from `funvue` directory run `npm install`

* from funvue directory: `npm run dev` to start the development server

* website will be running at http://localhost:8080

## Requirements: 
* python 3 - https://www.python.org/downloads/
* docker desktop - https://docs.docker.com/get-docker/
* Vue cli - https://cli.vuejs.org/
