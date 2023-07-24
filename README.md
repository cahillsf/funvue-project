# WIP
# Web app "funvue"


## Local Testing

### Database: MongoDB
* containerized -> from base directory `funvue-project` run `docker compose up --build`

### Back end: Flask
* from `flask-server` activate your virtual environment: https://docs.python.org/3/library/venv.html

* install dependencies: run `pip install -r requirements.txt` 

* create your `SECRET_KEY` as an envvar in your virtualenv using the secrets package ([ref](https://www.bacancytechnology.com/blog/flask-jwt-authentication)):
  - activate your local interpreter and run:
  ```
  >>> import secrets
  >>> secrets.toxen_hex(16)
  ```
  - export the resulting secret key `export SECRET_KEY='<SECRET_KEY>'`



* run `ddtrace-run python3 app.py` to start the flask server

### Front end: Vue
* install depedendencies: from `funvue` directory run `npm install`

* from funvue directory: `npm run dev` to start the development server

* website will be running at http://localhost:8080

### Requirements: 
* python 3 - https://www.python.org/downloads/
* docker desktop - https://docs.docker.com/get-docker/
* Vue cli - https://cli.vuejs.org/

--- 
## Deploy in Self-Managed AWS K8s Cluster
- 

---
### Push your own images
- the k8s resources by default are set to pull the images from my dockerhub repo `cahillsf`.  If you'd like to build and push your own images, you can use the helper shell script `docker_push.sh` to do so
  - example command from current `README` dir: `/bin/bash ./docker_push.sh -t 0.0.1 -r cahillsf -i fv-flask -p ./flask-server -d '/Users/stephen.cahill/Desktop/dev-projects/funvue-pr/funvue-project/flask-server/Dockerfile'`
- you will then need to update the k8s deployment files `./k8s-config` accordingly to pull your images