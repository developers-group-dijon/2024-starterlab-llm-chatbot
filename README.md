# 2024-starterlab-llm-chatbot


# Pré-requis

## Python - poetry

### Installation

- Sur le poste : https://python-poetry.org/docs/#installation

### Téléchargement des dépendances

*Pour éviter le téléchargement pendant le starter lab*

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

```
docker compose pull
```

# Organisation du code

Les scripts python sont dans le dossier `chat`.
Les répertoire `data` contient des données utilisées par les scripts.

## Exécution des commandes via poetry

Exemple de commande pour lancer le script "chat.rag-langchain"
```
poetry run python chat/rag-langchain.py
```
