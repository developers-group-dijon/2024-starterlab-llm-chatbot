import time

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores.pgvecto_rs import PGVecto_rs
from langchain_core.documents import Document
from utils.args import init_split_args
from utils.prompt import Debugger, debug
from utils.splitter import split_file


def update_db(_pg_db: PGVecto_rs, _chunks: list[Document]) -> None:
  _pg_db.add_documents(_chunks)


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_split_args()

  # Activating the debug mode
  Debugger.debug_mode = True

  # Instantiating the PGVecto instance
  pg_db = PGVecto_rs.from_collection_name(
    embedding=OllamaEmbeddings(model=args.embeddings),
    db_url=args.postgres_url,
    collection_name="doc_embeddings",
  )

  # Getting the chunks
  t0 = time.time()
  chunks = split_file(args)
  debug(
    f"""Chargement et découpage du fichier "{args.file_path}" en <ansigreen>{len(chunks)}</ansigreen> chunks en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes"""
  )
  t0 = time.time()

  # Update the database with new chunks
  update_db(pg_db, chunks)

  debug(
    f"""Chargement des chunks dans la base de données en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes"""
  )
