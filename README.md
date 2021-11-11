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
- Python
- Flask
- Helm
- Docker


Steps:

1 - Provisionar cluster EKS na AWS executando terraform;
2 - Configurar ambiente de monitoramento Dashboard, Prometheus e Grafana;
3 - Realizar deploy da aplicação Demo


### Step 1

Requisitos para a configuração:
- Terraform v0.14.4
- AWS CLI
- AWS IAM authenticator
- kubectl

O ambinete possui um node com kubernetes 1.21.4, uma VPC, tres sub-redes privadas, tres públicas e um Gateway NAT

Para iniciar a configuração do ambiente é necessario baixar o projeto do repositorio e executar os comandos do terraform:

>git clone https://github.com/adregis/test-devops-ia.git

>cd terraform

### Iniciar o terraform e os adicionar os arquivos de estado que ira controlar as alterações dos recursos:
>terraform init

### Validar o arquivo de configuração:
>terraform validate

### Realiza uma simulação detalhando todos os recursos que sera criado:
>terraform plan

### Para criar os recursos executar:
>terraform apply


![Alt text](https://github.com/adregis/test-devops-ia/blob/main/imagens/eks1.png?raw=true "Console EKS")


### Step 2

Requisitos para a configuração:
- kubernetes Dashboard
- Prometheus 
- Grafana
- Helm

Instalação e configuração do kubernetes Dashboard, ferramenta para verificar saude do cluster e consumo dos recursos:

### Download e unzip do metrics server:
>wget -O v0.3.6.tar.gz https://codeload.github.com/kubernetes-sigs/metrics-server/tar.gz/v0.3.6 && tar -xzf v0.3.6.tar.gz

### Deploy do metrics server no cluster
>kubectl apply -f metrics-server-0.3.6/deploy/1.8+/

### Deploy dos recursos necessarios para o Dashboard:kubectl 
>apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml

### Necessario criar proxy server para acessar o dashboard e configurar ClusterRoleBinding para visualizar o token e criar as permissões necessarias de autenticação:  
>kubectl proxy

>kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep service-controller-token | awk '{print $1}')

![Alt text](https://github.com/adregis/test-devops-ia/blob/main/imagens/eks-dash.png?raw=true "Dashboard")


Instalaçao e configuração da stack de monitoramento com Prometheus e Grafana

#### Prometheus

Um sistema de coleta de métricas de aplicações e serviços para armazenamento que utiliza banco de dados de séries temporais.

#### Grafana

Uma solução de análise e observabilidade que suporta vários sistemas de coleta e métricas. Quando integrada ao Prometheus, serve para exibir métricas em painéis úteis para diferentes áreas e necessiades.

A configuração foi realizada utilizando o helm com o pacote disponibilizado pela prometheus-community

Adicionar repositorio do helm atualizado:

>helm repo add stable https://charts.helm.sh/stable

Adicionar o Prometheus community helm chart ao Kubernetes:

>helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

Instalar o kube-prometheus-stack com o comando:

>helm install stable prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

Por padrão o service do Prometheus e Grafana são acessados somente na rede interna do cluster.

![Alt text](https://github.com/adregis/test-devops-ia/blob/main/imagens/service.jpeg?raw=true "Service prometheus e grafana")

É necessario alterar o tipo de serviço de ClusterIP para LoadBalancer no serviço do Grafana para liberar acesso externo ao sistema:

> kubectl edit svc prometheus-grafana -n monitoring 

Com o endereço disponibilizado pelo Kubernetes o serviço já pode ser acessado externamente:

![Alt text](https://github.com/adregis/test-devops-ia/blob/main/imagens/service-grafana.jpeg?raw=true "Service grafana")

























