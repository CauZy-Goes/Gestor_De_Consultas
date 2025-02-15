# Gestão de Pacientes - Clínica de Psicologia

Este é um sistema web **Full Stack em Django** para gestão de pacientes em uma clínica de psicologia. O sistema permite cadastrar pacientes, agendar consultas e atribuir tarefas terapêuticas aos pacientes.

## ✨ Funcionalidades
- Cadastro e listagem de pacientes.
- Visualização do perfil do paciente e agendamento de consultas.
- Registro de consultas com campos para humor, anotações e vídeos.
- Atribuição de tarefas terapêuticas aos pacientes.
- Geração de um link público para consulta.

  ## 🌟 Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite
- **Front-end:** HTML, CSS (TailWindCSS)
- **Outros:** Django ORM, Django Admin

## 📢 Possíveis Melhorias
- Implementar autenticação e controle de usuários.
- Melhorar a interface utilizando frameworks como React ou Vue.js.
- Migrar para um banco de dados mais robusto (PostgreSQL ou MySQL).
- Criar uma API REST para integração com outras aplicações.

## 🗓 Telas do Sistema
### **1. Tela de Cadastro e Exibição de Pacientes**
![Tela de Cadastro e Exibição de Pacientes](https://github.com/CauZy-Goes/Gestor_De_Consultas/blob/main/clinica_img/pacientes.png)

### **2. Cadastro e Exibição das Consultas do Paciente**
![Cadastro e Exibição das Consultas do Paciente](https://github.com/CauZy-Goes/Gestor_De_Consultas/blob/main/clinica_img/paciente_.png)

### **3. Detalhes da Consulta do Paciente**
![Detalhes da Consulta do Paciente](https://github.com/CauZy-Goes/Gestor_De_Consultas/blob/main/clinica_img/consulta.png)

## 🛠️ Instalação e Execução
### **1. Clonar o Repositório**
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### **2. Criar e Ativar um Ambiente Virtual**
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### **3. Instalar Dependências**
```sh
pip install -r requirements.txt
```

### **4. Aplicar Migrações ao Banco de Dados**
```sh
python manage.py migrate
```

### **5. Criar um Superusuário (Opcional, para acessar o admin)**
```sh
python manage.py createsuperuser
```

### **6. Iniciar o Servidor**
```sh
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/** no navegador.

## 👥 Autor
Desenvolvido por **Cauã Farias**.


