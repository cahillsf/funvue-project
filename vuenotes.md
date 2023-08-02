# Theme
* default UIkit theme is in node_modules/@vuikit/theme/dist/vuikit.css


## Git 
* add remote repo to track origin
`
git remote add origin https://github.com/cahillsf/funvue-project.git
git branch -M main
git push -u origin main
`

## Flask App
from /Users/scahill/Desktop/funvue-project/flask-server
- activate virtual environment: `source .venv/bin/activate`
- install deps: `python3.9 -m pip install -r requirements.txt`
run the app:
- python3.9 app.py
- ddtrace-run python3.9 app.py

to get idle: `idle` from terminal

https://github.com/tensorflow/tensorboard/issues/1566

- `/bin/bash ./docker_push.sh -t 0.0.1 -r cahillsf -i fv-vue -p ./funvue -d '/Users/stephen.cahill/Desktop/dev-projects/funvue-pr/funvue-project/funvue/Dockerfile-apm'`
## Mongodb 
cd docker-entrypoint-initdb.d


mongoimport -u "root" -p "example" --type csv --authenticationDatabase admin -d sitecontent -c cards --headerline homepage.csv

./mongo-db/mongo-db-init-files
* mongo -uroot -pexample

from the container bash: `mongosh --username root --password example --authenticationDatabase admin`

`mongosh --username flask-role --password toor --authenticationDatabase sitecontent`

use sitecontent
var col = db.cards
col.find()


#  db.getCollection('cards').find()

use sitecontent
db.createCollection('cards')
var myCards=
	[
		{
            '_id': 0,
            'title':'CardOne',
            'msg':'testOne',
            'animation':'fade-up'
          },
          {
            '_id': 1,
            'title':'CardTwo',
            'msg':'testTwo',
            'animation':'fade-up'
          },
          {
            '_id': 2,
            'title':'CardThree',
            'msg':'testTwo',
            'animation':'fade-up'
          },
          {
            '_id': 3,
            'title':'CardFour',
            'msg':'testTwo',
            'animation':'fade-up'
          },

	];

	db.cards.insert(myCards);

- `/bin/bash ./docker_push.sh -t 0.0.1 -r cahillsf -i fv-mongo -p ./mongo-db -d '/Users/stephen.cahill/Desktop/dev-projects/funvue-pr/funvue-project/mongo-db/Dockerfile'`
## ToDo

* better routing--> can i create a router-link within a different element?

* styling-- figure out a way to keep theming (currently in nodemodules which are in the .gitignore)

* hide dropdown menu after user has returned to full page view so that when the browser size is reduced below the breakpoint, it will not be visible



2023-07-25 21:20:15] [init] Using Kubernetes version: v1.26.0
[2023-07-25 21:20:15] [preflight] Running pre-flight checks
[2023-07-25 21:20:20] error execution phase preflight: [preflight] Some fatal errors occurred:
[2023-07-25 21:20:20]   [ERROR NumCPU]: the number of available CPUs 1 is less than the required 2
[2023-07-25 21:20:20] [preflight] If you know what you are doing, you can make a check non-fatal with `--ignore-preflight-errors=...`


### locust for load testing
- https://github.com/deliveryhero/helm-charts/tree/master/stable/locust
- https://docs.locust.io/en/1.5.2/running-locust-docker.html
- `docker-compose up --scale worker=4`

---
- kind get kubeconfig -n capd > mgmt.kubeconfig
- for workload cluster autoscaler: `kubectl create configmap mgmt-kube --from-file=mgmt.kubeconfig --kubeconfig=./capi-quickstart.kubeconfig -n kube-system`

- swap out the server address host in the kubeconfig to resolve to `host.docker.internal` for docker deployment
- for mgmt cluster autoscaler: `kubectl create configmap wkld-kube --from-file=capi-quickstart.kubeconfig -n kube-system`
- in mgmt cluster: `k apply -f /Users/stephen.cahill/Desktop/dev-projects/funvue-pr/funvue-project/local-kind/autoscaler.yaml`


  export AWS_REGION=us-east-2
  export AWS_CONTROL_PLANE_MACHINE_TYPE=m4.large
  export AWS_NODE_MACHINE_TYPE=m4.large
  export AWS_SSH_KEY_NAME=aws-ec2
  export X_AWS_PROFILE=cahillsf-account-admin
  export AWS_B64ENCODED_CREDENTIALS=$(aws-vault exec $X_AWS_PROFILE -- clusterawsadm bootstrap credentials encode-as-profile)