# 2024-starterlab-llm-chatbot

# Contexte

Ce dépôt contient le code sources ainsi que de le [support de présentation](./Support%20présentation%20-%20Starterlab%20LLM%20Chatbot.pdf) de l'atelier organisé par le Developers Group Dijon le 3 octobre 2024.

Le dépôt Git propose 2 branches :
- main : socle applicatif et exercices _à trous_
- solutions : les exercices complétés

# Pré-requis

## Git

### Installation

- Sur le poste : https://git-scm.com/downloads

### Téléchargement du dépôt

*Pour éviter le téléchargement pendant le starter lab*

```
git clone git@github.com:developers-group-dijon/2024-starterlab-llm-chatbot.git
```

## Python - poetry

### Installation

- Sur le poste : https://python-poetry.org/docs/#installation

### Téléchargement des dépendances

*Pour éviter le téléchargement pendant le starter lab*

À la racine du dépôt Git :

```
POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
```

## Ollama

### Installation

- Sur le poste : https://ollama.com/download

### Téléchargement des modèles

*Pour éviter le téléchargement pendant le starter lab*

```
ollama pull llama3:8b
ollama pull llama2
ollama pull mistral
ollama pull phi3
ollama pull nomic-embed-text
ollama pull mxbai-embed-large
ollama pull all-minilm
```

## Docker et Docker compose

### Installation

- Sur le poste : https://docs.docker.com/engine/install/ https://docs.docker.com/compose/install/

### Téléchargement des images

À la racine du dépôt Git :

```
docker compose pull
```

# Organisation du code

Les scripts python sont dans le dossier `chat`.
Les répertoire `data` contient des données utilisées par les scripts.

## Exécution des commandes via poetry

Exemple de commande pour lancer le script "chat.rag-langchain"
```
poetry run python chat/07-rag-langchain.py
```
