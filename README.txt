===================================
SISTEMA DE AGENDAMENTO DE BARBEARIA
===================================

--- Integrantes ---
- Gedian Gabriel Funka
- Kauã Miguel Neuenfeld
- Weslley Kuhne

--- Descrição do projeto --- 
sistema web desenvolvido em Python com Flask e MySQL para gestão e agendamentos de horarios e serviços de uma barbearia 

--- Instruções para rodagem do projeto ---
1. Configurar o Banco de dados
    - Importe e execute o arquivo "Banco de dados Trabalho SA Python.sql" no seu MySql Workbench 

2. Configuração do seu ambiente Python
    - Abra o terminal na pasta raiz do projeto
    -Crie e ative um ambiente virtual

    No Windows:
     python -m venv venv
     .\venv\Scripts\activate

3. INSTALAÇÃO DAS DEPENDÊNCIAS:
   - Execute o comando para instalar as bibliotecas necessárias:
     pip install flask
     pip install mysql-connector-python

4. EXECUÇÃO DA APLICAÇÃO:
   - Navegue até a pasta da aplicação e execute o arquivo app.py:
     cd Trabalho_Barbearia
     python app.py

   - Abra o navegador e acesse o endereço indicado no terminal 
     (geralmente http://127.0.0.1:5000).

--- Estrutura do projeto ---
TrabalhoSA_Python/
├──Trabalho_Barbearia/
|  ├──  templates/ #Paginas HTML
|  |    ├──agendamentos.html #Mostrando todos os agendamentos da barbearia
|  |    ├──detalhe.html #Mostra o detalhe do agendamento X
|  |    └──index.html #Incio descrevendo um pouco da barbearia
|  ├──agendamentos.py #Logica e rotas de agendamento
|  ├──app.py #Ponto de entrada da aplicação, com as rotas necessarias
|  ├──banco.py #configuração e aplicação do banco de dados da barbearia
|  ├──config.py #configuração do ambiente/aplicação
|  └──models.py #Modelo de dados
├──Banco de dados Trabalho SA Python.sql #Script de criação do banco de dados da barbearia
├──README.txt
└──.gitignore
