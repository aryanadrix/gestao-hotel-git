## Projeto: Gestão de Reservas de Hotel com Git e GitHub
Autores: Tito Adriano (Áryan Adrix) & Lucas Almeida (Lucasiefp)

Descrição Geral
Este projeto foi desenvolvido como parte de um exercício de avaliação sobre controlo de versões com Git e GitHub, aplicando práticas de trabalho colaborativo em equipa no contexto de um sistema simples de gestão de reservas de hotel.

O sistema permite:
Visualizar clientes registados
Consultar quartos disponíveis ou ocupados
Ver reservas efetuadas
Também exibe os dados através de uma interface HTML

## Estrutura do projecto

gestao-hotel-git/

│── app.py                
│── clientes.py           
│── quartos.py           
│── reservas.py          
│── templates/ interface.html 

│── README.md    


## Funcionalidades

### MÓDULOS 

Registo e listagem de clientes: 
clientes.py  —— Responsável: Tito Adriano

Gestão de quartos: 
quartos.py —— Responsável: Lucas Almeida

Criação e listagem de reservas: 
reservas.py —— Responsável: Lucas Almeida

Interface visual em HTML: 
templates/interface.html —— Responsável: Tito Adriano

Integração Flask + módulos do sistema: 
app.py —— Responsável: Lucas Almeida


## Como Executar o Sistema

1. Clonar o Repositório
git clone https://github.com/aryanadrix/gestao-hotel-git.git 
cd gestao-hotel-git

2. Instalar Dependências
- pip install flask

3. Executar a Aplicação
- python app.py

4. Aceder ao Sistema
- Abra no navegador: http://127.0.0.1:5000/

Aqui verás:
- A lista de clientes,
- Os quartos com seu estado (disponível/ocupado),
- E as reservas realizadas.

## Exemplo de Dados Padrão
Os dados iniciais são carregados diretamente dos módulos:

clientes.py
clientes = [ {"nome": "Adriano", "telefone": "912345678"}, {"nome": "Lucas", "telefone": "923456789"} ]

quartos.py
quartos = [ {"numero": 101, "tipo": "Solteiro", "disponivel": True}, {"numero": 102, "tipo": "Casal", "disponivel": False} ]

reservas.py
reservas = [ {"cliente": "Adriano", "quarto": 101} ]


## Etapa, Ação e	Responsáveiss

- Criação do repositório: gestao-hotel-git	- Tito Adriano
- Adição de colaborador:	Tito Adriano
- Estrutura inicial e commit base:	Ficheiros base + README	- Tito Adriano
- Branch feature-clientes:	Funções de clientes -	Tito Adriano
- Branch feature-quartos:	Gestão de quartos	- Lucas Almeida
- Branch feature-reservas:	Módulo Flask + reservas	- Lucas Almeida
- Branch feature-template:	Interface HTML -	Tito Adriano
- Pull Requests e Revisões:	Avaliação cruzada -	Ambos
- Tag final	v1.2	Ambos

## Tag Final

git tag -a v1.2 -m "Versão final com Flask e interface HTML"
git push origin v1.2

## Tecnologias Utilizadas
* Python 3
* Flask
* HTML + CSS inline
* Git e GitHub


