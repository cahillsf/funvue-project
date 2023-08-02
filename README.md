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
  >>> secrets.token_hex(16)
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
## Deploy in Self-Managed AWS K8s Cluster w/CAPI and CAPA
- based off of the [quickstart instructions](https://cluster-api.sigs.k8s.io/user/quick-start.html) for reference
- please review the [prereqs](https://cluster-api.sigs.k8s.io/user/quick-start.html#common-prerequisites) and install prior to moving forward 

### Create a local kind management cluster
- clone this repository and `cd` into the root directory
- run: `kind create cluster --config ./capi/kind-cluster-with-extramounts.yaml -n capm`

#### Set up the required AWS variables and credentials
- for this example I will be using [aws-vault](https://github.com/99designs/aws-vault) to securely manage my user credentials.  Replace <TARGET_PROFILE> with your intended profile in the envvar exports
- you will also need to [create an ssh key](https://cluster-api-aws.sigs.k8s.io/topics/using-clusterawsadm-to-fulfill-prerequisites.html#create-a-new-key-pair) for the EC2s we will be provisioning as nodes (replace <SSH_KEY> with your key name)
- create the following vars:
  ```
  export AWS_REGION=us-east-2
  export AWS_CONTROL_PLANE_MACHINE_TYPE=m4.large
  export AWS_NODE_MACHINE_TYPE=m4.large
  export AWS_SSH_KEY_NAME=<SSH_KEY>
  export X_AWS_PROFILE=<TARGET_PROFILE>
  export AWS_B64ENCODED_CREDENTIALS=$(aws-vault exec $X_AWS_PROFILE -- clusterawsadm bootstrap credentials encode-as-profile)
  ```

#### Initialize your local kind cluster to be used as a managament cluster
- run `clusterctl init --infrastructure aws`
- `aws:v2.0.2`
### Deploy the workload cluster
- `kubectl apply -f ./capi/capi-quickstart.yaml`

- this template was based off of the following cluster template with some modifications:
  ```
  clusterctl generate cluster capi-quickstart \
  --kubernetes-version v1.26.0 \
  --control-plane-machine-count=1 \
  --worker-machine-count=1 \
  --infrastructure=aws:v2.0.2 \
  > capi-quickstart.yaml
  ```
  - these modifications include:
    - ignoring preflight error messages from kubeadm to launch the cluster with fewer resources (CPU/Mem) than Kubeadm would typically allow.  We are launching this cluster with small instances to minimize costs
    - adding additional block storage to avoid node `DiskPressure` conditions
- it will take some time for the CAPA controller to provision the workload cluster, you can check the progress by running `clusterctl describe cluster capi-quickstart` 
### Configure the workload cluster
- export the kubeconfig: `clusterctl get kubeconfig capi-quickstart > capi-quickstart.kubeconfig`
- install the out of tree cloud provider:
  ```
  helm repo add aws-cloud-controller-manager https://kubernetes.github.io/cloud-provider-aws
  helm repo update
  helm upgrade --install aws-cloud-controller-manager --kubeconfig=./capi-quickstart.kubeconfig aws-cloud-controller-manager/aws-cloud-controller-manager
  ```

- install the AWS k8s CNI provider: `kubectl --kubeconfig=./capi-quickstart.kubeconfig apply -f https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/master/config/master/aws-k8s-cni.yaml`

### Deploy the workload

### Credentials Management
- using aws-vault you will receive a short-lived session token from STS, if the session token is expired and you attempt to perform changes to your AWS clusters, you will see errors like the following from your `capa-controller-manager`:
  - `status code: 400, request id: <ID>, ExpiredTokenException: The security token included in the request is expired`
- this means the token must be refreshed, here is how this can be accomplished:
  - regenerate the b64 encoded credentials: `export AWS_B64ENCODED_CREDENTIALS=$(aws-vault exec $X_AWS_PROFILE -- clusterawsadm bootstrap credentials encode-as-profile)`
  - `clusterawsadm controller update-credentials --namespace capa-system`
  - restart the `capa-controller-manager` deployment: `kubectl -n capa-system rollout restart deployment capa-controller-manager`
- note: this is for development use only, there is a way to [use IAM roles for management clusters](https://cluster-api-aws.sigs.k8s.io/topics/using-iam-roles-in-mgmt-cluster.html?highlight=credentials%20managemen#using-iam-roles-in-management-cluster-instead-of-aws-credentials) deployed in AWS

### Cleanup
- delete the workload cluster: `kubectl delete cluster capi-quickstart`
  - wait for this command to return, you can check the progress of the resource deletion by watching the logs from the `capa-controller-manager` manager pod
---
### Push your own images
- the k8s resources by default are set to pull the images from my dockerhub repo `cahillsf`.  If you'd like to build and push your own images, you can use the helper shell script `docker_push.sh` to do so
  - example command from current `README` dir: `/bin/bash ./docker_push.sh -t 0.0.1 -r cahillsf -i fv-flask -p ./flask-server -d '/Users/stephen.cahill/Desktop/dev-projects/funvue-pr/funvue-project/flask-server/Dockerfile'`
- you will then need to update the k8s deployment files `./k8s-config` accordingly to pull your images