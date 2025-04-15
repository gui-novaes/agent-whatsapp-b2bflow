# 📲 Projeto B2BFlow – Disparador de Mensagens WhatsApp com Python

Este projeto consiste em um **disparador automático de mensagens via WhatsApp**, desenvolvido em Python utilizando:

- **[Supabase](https://supabase.com/)**: Banco de dados como serviço (PostgreSQL).
- **[Z-API](https://app.z-api.io/)**: API para integração com o WhatsApp.
- **Python** com as bibliotecas `requests`, `supabase`, e `dotenv`.

O objetivo é permitir o envio automático de mensagens via WhatsApp com base em dados armazenados no Supabase.

---

## ✅ Pré-requisitos

Antes de começar, você precisará:

- Conta gratuita no [Supabase](https://supabase.com/)
- Conta gratuita no [Z-API](https://app.z-api.io/)
- Python 3.x instalado na máquina
- Visual Studio Code ou outro editor de código
- Git (opcional, mas recomendado)

---

## 🔧 Passo a Passo

### 1. Criando conta no Supabase
- Acesse [supabase.com](https://supabase.com/) e crie uma conta gratuita.
- Crie um novo projeto em **US East (North Virginia)**.
- Vá até o menu lateral esquerdo → **Table Editor** → **New Table** e crie a tabela `mensagens` com os seguintes campos:

| Campo   | Tipo      |
|---------|-----------|
| id      | int8 (PK) |
| name    | text      |
| phone   | text      |
| message | text      |
| status  | text      |

### 2. Recuperando as credenciais
- No menu lateral, vá até **Settings > API**.
- Copie:
  - A **URL do projeto**
  - A **API Key privada (service_role)**

---

### 3. Configurando conta na Z-API
- Acesse [app.z-api.io](https://app.z-api.io/), crie uma conta e conecte seu WhatsApp ao escanear o QR Code.
- Na dashboard da instância criada:
  - Copie a **Instance ID**
  - Copie o **Token da Instância**
- Vá em **Segurança** e ative o **Client Token**, que será necessário para enviar mensagens.

---

## 📁 Estrutura do Projeto

Crie uma pasta do projeto e abra no VSCode.

### 4. Instale as bibliotecas

```bash
pip install supabase requests python-dotenv
```

### 5. Crie o arquivo `.env`

```dotenv
SUPABASE_URL=https://<SEU_PROJETO>.supabase.co
SUPABASE_KEY=<SUA_SERVICE_ROLE_KEY>
ZAPI_INSTANCE_ID=<SEU_ID_INSTANCIA>
ZAPI_TOKEN=<SEU_TOKEN_INSTANCIA>
CLIENT_TOKEN_ZAPI=<SEU_CLIENT_TOKEN>
```

> ⚠️ Nunca compartilhe este arquivo em repositórios públicos.

---

## 🧠 Funcionamento do Script

### 6. Crie o arquivo `app.py`

Neste arquivo ficará o script responsável por:

- Consultar mensagens com status "pendente" no Supabase
- Enviar automaticamente as mensagens usando a API do Z-API
- Atualizar o status da mensagem no banco de dados

> 💡 **[Clique aqui](https://github.com/seuusuario/seurepositorio)** para acessar o código completo no GitHub.

---

## ✍️ Testando o envio

### 7. Adicione uma mensagem de teste no Supabase

Insira uma linha manualmente na tabela `mensagens`:

- **name**: João  
- **phone**: 5511987654321  
- **message**: Olá, tudo bem? Essa é uma mensagem automática!  
- **status**: pendente

> ⚠️ O número deve estar no formato internacional (ex: 55 + DDD + número)

---

## 🚀 Executando

### 8. Rode o script

```bash
python app.py
```

Se tudo estiver certo, você verá um retorno com **Status 200** e a confirmação do envio. A mensagem será entregue automaticamente via WhatsApp.

---

## 📬 Suporte

Em caso de dúvidas ou melhorias, entre em contato ou envie uma *issue* neste repositório.