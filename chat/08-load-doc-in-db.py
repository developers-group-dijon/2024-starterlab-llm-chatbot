import time

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.pgvecto_rs import PGVecto_rs
from utils.args import init_split_args
from utils.prompt import Debugger, debug
from utils.splitter import split_file


# TODO: - 001 : Initialiser une BDD (run docker compose up dans la racine du projet)
#       - 002 : Créer les chunks
#       - 003 : Mettre à jour la BDD
#       - 004 : Compléter la fonction update_db
def update_db(_pg_db: PGVecto_rs, _chunks: list[dict]) -> None:
  # TODO 004
  _pg_db.xxx(...)


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_split_args()

  # Activating the debug mode
  Debugger.debug_mode = True

  # Instantiating the PGVecto instance
  # TODO 001 -  Tips : Utiliser la méthode from_collection_name de PGVecto_rs
  pg_db = xxx.xxx(
    embedding=...,
    db_url=...,
    collection_name=...,
  )

  t0 = time.time()
  # TODO 002 -  Tips : Utiliser la fonction split_args
  chunks = ...

  debug(
    f"""Chargement et découpage du fichier "{args.file_path}" en <ansigreen>{len(chunks)}</ansigreen> chunks en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes"""
  )

  # Getting the chunks
  t0 = time.time()

  # Update the database with new chunks
  # TODO 003
  ...(..., ...)

  debug(
    f"""Chargement des chunks dans la base de données en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes"""
  )
