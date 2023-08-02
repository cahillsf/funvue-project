DATADOG_API_SECRET_NAME=datadog-api-secret
kubectl create secret generic $DATADOG_API_SECRET_NAME --from-literal api-key=$DD_API_KEY --kubeconfig=./capi-quickstart.kubeconfig
kubectl create configmap my-loadtest-locustfile --from-file ../locust-loadtest/locustfile.py --kubeconfig=./capi-quickstart.kubeconfig
kubectl --kubeconfig=./capi-quickstart.kubeconfig \
  apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.1/manifests/calico.yaml
helm install ddagent -f ../local-kind/dd-values.yaml  --set datadog.apiKeyExistingSecret=datadog-api-secret datadog/datadog --kubeconfig=./capi-quickstart.kubeconfig
helm install locust deliveryhero/locust -f ../local-kind/locust-values.yaml --kubeconfig=./capi-quickstart.kubeconfig
helm install metrics-server metrics-server/metrics-server -f ../local-kind/metrics-server-values.yaml --kubeconfig=./capi-quickstart.kubeconfig
kubectl create configmap mgmt-kube --from-file=mgmt.kubeconfig --kubeconfig=./capi-quickstart.kubeconfig -n kube-system
kubectl apply -f ../k8s-config -R --kubeconfig=./capi-quickstart.kubeconfig