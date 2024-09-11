import argparse
from argparse import ArgumentParser


def add_embedding_arg(parser: ArgumentParser) -> None:
  parser.add_argument(
    "--embeddings",
    help="le nom du modèle à utiliser pour les embeddings",
    default="all-minilm",
    choices=["all-minilm", "nomic-embed-text", "mxbai-embed-large"],
  )


def add_debug_arg(parser: ArgumentParser) -> None:
  parser.add_argument("--debug", help="affiche des informations de debug", action="store_true")


def add_postgres_arg(parser: ArgumentParser) -> None:
  parser.add_argument(
    "--postgres-url",
    help="l'url d'accès à la BDD Postgres/PgVecto.rs",
    default="postgresql+psycopg://pgvectors:pgvectors@localhost:5432/pgvectors",
  )


def add_text_splitter_arg(parser: ArgumentParser) -> None:
  parser.add_argument(
    "--text-splitter",
    help="le nom du splitter à utiliser",
    default="RecursiveCharacterTextSplitter",
    choices=["RecursiveCharacterTextSplitter", "HTMLHeaderTextSplitter", "MarkdownHeaderTextSplitter"],
  )
  # Splitter parameters
  parser.add_argument("--chunk-size", help="taille des chunks", default=1000, type=int)
  parser.add_argument("--chunk-overlap", help="overlap entre les chunks", default=100, type=int)
  parser.add_argument(
    "--apply-recursive-text-splitter",
    help="applique RecursiveCharacterTextSplitter en plus des autres splitter",
    action="store_true",
  )


def add_model_arg(parser: ArgumentParser) -> None:
  parser.add_argument(
    "--model",
    help="le nom du modèle à utiliser",
    default="llama3:8b",
    choices=["llama2", "llama3:8b", "mistral", "phi3"],
  )
  parser.add_argument("--ollama-url", help="l'url d'accès à ollama", default="http://localhost:11434")
  parser.add_argument("--temperature", help="la température du LLM", default=0.8, type=float)


def add_training_arg(parser: ArgumentParser) -> None:
  parser.add_argument(
    "--raw_model_name",
    help="le nom du modèle brut à entrainer",
    default="distilbert/distilbert-base-uncased",
  )
  parser.add_argument(
    "--dataset_name",
    help="le nom du jeu de données pour la supervision de l'entrainement",
    default="stanfordnlp/sst2",
  )


class ChatNamespace(argparse.Namespace):
  model: str
  ollama_url: str
  temperature: float
  embeddings: str
  debug: bool
  text_splitter: str
  chunk_size: int
  chunk_overlap: int
  apply_recursive_text_splitter: bool
  postgres_url: str


class SplitNamespace(argparse.Namespace):
  embeddings: str
  debug: bool
  text_splitter: str
  chunk_size: int
  chunk_overlap: int
  apply_recursive_text_splitter: bool
  file_path: str
  postgres_url: str


class TrainingNamespace(argparse.Namespace):
  raw_model_name: str
  dataset_name: str


def init_args() -> ChatNamespace:
  """
  Initialisation du programme avec récupération des paramètres
  """

  parser = argparse.ArgumentParser(prog="Chatbot")

  add_model_arg(parser)
  add_embedding_arg(parser)
  add_debug_arg(parser)
  add_text_splitter_arg(parser)
  add_postgres_arg(parser)

  return parser.parse_args(namespace=ChatNamespace())


def init_split_args() -> SplitNamespace:
  """
  Initialisation du programme avec récupération des paramètres
  """

  parser = argparse.ArgumentParser(prog="Load n split")
  add_debug_arg(parser)
  add_text_splitter_arg(parser)
  add_postgres_arg(parser)
  add_embedding_arg(parser)

  parser.add_argument(
    "file_path",
    help="le fichier à charger et découper",
    default="data/NIPS-2017-attention-is-all-you-need-Paper.pdf",
    type=str,
  )

  return parser.parse_args(namespace=SplitNamespace())


def init_train_args() -> TrainingNamespace:
  """
  Initialisation du programme avec récupération des paramètres
  """
  parser = argparse.ArgumentParser(prog="Train and Evaluate")
  add_training_arg(parser)

  return parser.parse_args(namespace=TrainingNamespace())
