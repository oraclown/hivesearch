### How to deploy Elasticsearch on a Kubernetes cluster on AWS using Kops & Helm

## Configure Kubernetes on AWS using Kops
1. Do steps 1-5 from this guide: https://medium.appbase.io/deploy-elasticsearch-with-kubernetes-on-aws-in-10-steps-7913b607abda

## Install Elasticsearch on your deployed cluster using Helm
1. Install Helm
2. Check `helm env` and see if your `HELM_KUBECONTEXT` is set. If not, create that environmental variable and set it to the name of your deployed cluster. For example, `set HELM_KUBECONTEXT=example.k8s.local` (on Windows)
3. Find an Elasticsearch Helm chart. I used this one: https://hub.helm.sh/charts/bitnami/elasticsearch
4. Follow the instructions given to use the chart. For example, `helm repo add...`, then `helm install...`

## Expose your app's IP address / add a LoadBalancer
1. Get name of your Elasticsearch deployment `kubectl get deployments`
2. Create LoadBalancer to expose the deployment `kubectl expose deployment blah --type=LoadBalancer --name=blahblah`. More guidance: https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
3. 

## Useful tips:
1. Shut down cluster & avoid autoscaling: https://perrohunter.com/how-to-shutdown-a-kops-kubernetes-cluster-on-aws/
2. More on load balancers *shrug: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/