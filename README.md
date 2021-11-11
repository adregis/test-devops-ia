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

O ambinete possui um node com kubernetes 1.21.4, uma VPC e tres sub-redes privadas, tres públicas e um Gateway NAT

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



