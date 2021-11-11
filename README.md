Teste Devops IA 

Autor Adriano Regis

Recursos:
- Terraform v0.14.3
- Kubernetes 1.21
- EKS
- Github
- kubernetes Dashboard
- Prometheus 
- Grafana
- AWS
- Pthon
- Flask


Steps:

1 - Provisionar cluster EKS na AWS executando terraform
2 - Configurar ambiente de monitoramento


### Step 1

Requisitos para a configuração:
- Terraform v0.14.4
- AWS CLI
- AWS IAM authenticator
- kubectl

O ambinete possui um node com kubernetes 1.21.4, uma VPC, tres sub-redes privadas, tres públicas e um Gateway NAT

Para iniciar a configuração do ambiente é necessario baixar o projeto do repositorio e executar os comandos do terraform:

git clone https://github.com/adregis/test-devops-ia.git

cd terraform

### Iniciar o terraform e os adicionar os arquivos de estado que ira controlar as alterações dos recursos:
terraform init

### Validar o arquivo de configuração:
terraform validate

### Realiza uma simulação detalhando todos os recursos que sera criado:
terraform plan

### Para criar os recursos executar:
terraform apply


![Alt text](https://github.com/adregis/test-devops-ia/blob/main/eks1.png?raw=true "Console EKS")


### Step 2

Requisitos para a configuração:
- kubernetes Dashboard
- Prometheus 
- Grafana

Instalação e configuração do kubernetes Dashboard, ferramenta para verificar saude do cluster e consumo dos recursos:

### Download e unzip do metrics server:
wget -O v0.3.6.tar.gz https://codeload.github.com/kubernetes-sigs/metrics-server/tar.gz/v0.3.6 && tar -xzf v0.3.6.tar.gz

### Deploy do metrics server no cluster
kubectl apply -f metrics-server-0.3.6/deploy/1.8+/

### Deploy dos recursos necessarios para o Dashboard:kubectl 
apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml

### Necessario criar proxy server para acessar o dashboard e gerar ClusterRoleBinding que dar acesso ao token e e cria as permissões necessarias de autenticação:  
kubectl proxy

kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep service-controller-token | awk '{print $1}')

![Alt text](https://github.com/adregis/test-devops-ia/blob/main/imagens/eks-dash.png?raw=true "Dashboard")



