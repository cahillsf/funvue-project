cat kind-cluster.yaml | envsubst > kind-cluster-final.yaml
cat fortune-teller-ng.yaml | envsubst > ../k8s-config/fortune-teller-ng.yaml
kind create cluster --config kind-cluster-final.yaml
kind export kubeconfig --name fv-kind
DATADOG_API_SECRET_NAME=datadog-api-secret
kubectl create secret generic $DATADOG_API_SECRET_NAME --from-literal api-key=$DD_API_KEY
kubectl create configmap my-loadtest-locustfile --from-file ../locust-loadtest/locustfile.py
helm install ddagent -f dd-values.yaml  --set datadog.apiKeyExistingSecret=datadog-api-secret datadog/datadog
helm install locust deliveryhero/locust -f locust-values.yaml
kubectl apply -f ../k8s-config -R
