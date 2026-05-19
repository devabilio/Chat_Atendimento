# API de Atendimento/Chat

API REST desenvolvida em Python utilizando FastAPI para gerenciamento de contatos, conversas e mensagens em tempo real.

## Tecnologias Utilizadas

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Alembic
- Pytest

---

# Funcionalidades

## Contatos

- Criar contato
- Listar contatos
- Buscar contato por ID
- Atualizar contato
- Remover contato

## Conversas

- Criar conversa
- Listar conversas
- Buscar conversa específica
- Atualizar status da conversa

Status disponíveis:

- OPEN
- IN_PROGRESS
- CLOSED

## Mensagens

- Enviar mensagens
- Listar mensagens de uma conversa

Tipos de remetente:

- CUSTOMER
- AGENT

---

# Regras de Negócio

- Não permitir mensagens em conversas encerradas
- Não permitir mensagens vazias
- Toda conversa deve possuir um contato vinculado
- Retornar códigos HTTP apropriados
- Tratamento consistente de erros

---

# Estrutura do Projeto

```bash
app/
│
├── main.py
├── database.py
│
├── models/
├── schemas/
├── routes/
├── services/
├── repositories/
├── core/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md