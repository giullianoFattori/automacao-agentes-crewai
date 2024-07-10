# Automação de Agentes CrewAI

Este projeto é uma automação utilizando agentes AI para planejar itinerários de viagem e realizar outras tarefas. Abaixo estão as instruções para configurar o ambiente correto para executar o projeto em Windows, macOS e Linux.

## Estrutura de Pastas

    automacao-agentes-crewai/
    ├── tools/
    │ ├── calculator_tools.py
    │ ├── search_tools.py
    ├── .env
    ├── .gitignore
    ├── agents.py
    ├── main.py
    ├── pyproject.toml
    ├── tasks.py



## Pré-requisitos

- Python 3.10.x
- [Poetry](https://python-poetry.org/): Uma ferramenta de gerenciamento de dependências para Python.

## Configuração do Ambiente

### Windows

1. **Instale o Python:**
   - Baixe e instale o Python 3.10.x do site oficial: [Python.org](https://www.python.org/downloads/windows/)
   - Certifique-se de adicionar o Python ao PATH durante a instalação.

2. **Instale o Poetry:**
   - Abra o PowerShell como Administrador e execute o seguinte comando:
     ```powershell
     (Invoke-WebRequest -Uri https://install.python-poetry.org | python -)
     ```

3. **Clone o Repositório:**
   - Clone o repositório do projeto para o seu diretório desejado:
     ```sh
     git clone <url-do-repositorio>
     cd automacao-agentes-crewai
     ```

4. **Instale as Dependências:**
   - No PowerShell, execute:
     ```sh
     poetry install
     ```

5. **Configure o Ambiente:**
   - O arquivo `.env` esta na raiz do projeto as variáveis de ambiente necessárias para que você as coloque.

### macOS

1. **Instale o Python:**
   - Utilize o Homebrew para instalar o Python 3.10.x:
     ```sh
     brew install python@3.10
     ```

2. **Instale o Poetry:**
   - Execute o comando de instalação do Poetry:
     ```sh
     curl -sSL https://install.python-poetry.org | python3 -
     ```

3. **Clone o Repositório:**
   - Clone o repositório do projeto:
     ```sh
     git clone <url-do-repositorio>
     cd automacao-agentes-crewai
     ```

4. **Instale as Dependências:**
   - No terminal, execute:
     ```sh
     poetry install
     ```

5. **Configure o Ambiente:**
   - O arquivo `.env` esta na raiz do projeto as variáveis de ambiente necessárias para que você as coloque.

### Linux

1. **Instale o Python:**
   - Utilize o gerenciador de pacotes da sua distribuição para instalar o Python 3.10.x. Exemplo para Debian/Ubuntu:
     ```sh
     sudo apt-get update
     sudo apt-get install python3.10 python3.10-venv python3.10-dev
     ```

2. **Instale o Poetry:**
   - Execute o comando de instalação do Poetry:
     ```sh
     curl -sSL https://install.python-poetry.org | python3 -
     ```

3. **Clone o Repositório:**
   - Clone o repositório do projeto:
     ```sh
     git clone <url-do-repositorio>
     cd automacao-agentes-crewai
     ```

4. **Instale as Dependências:**
   - No terminal, execute:
     ```sh
     poetry install
     ```

5. **Configure o Ambiente:**
   - O arquivo `.env` esta na raiz do projeto as variáveis de ambiente necessárias para que você as coloque.

## Executando o Projeto

Depois de configurar o ambiente, você pode executar o projeto utilizando o seguinte comando:

```sh
poetry run python main.py
