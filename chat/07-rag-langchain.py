from collections.abc import Iterator
import time

from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.base import RunnableSerializable
from langchain_core.vectorstores.base import BaseRetriever, VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.args import init_args
from utils.prompt import Debugger, debug, debug_runnable_fn, prompt_session


def format_docs(docs: list[Document]) -> str:
  """
  Met en forme le résultat d'une recherche de documents de contexte
  """

  return "\n\n".join(doc.page_content for doc in docs)


def init_chain(_model: BaseChatModel, retriever: BaseRetriever) -> RunnableSerializable:
  """
  Initialise la chaîne d'appel au LLM
  """

  system_prompt = """
    Réponds en utilisant uniquement les données de contexte fournies.
    Lorsque le contexte ne fournit pas d'informations pour répondre à la question posée, réponds que tu n'as pas la réponse.
    """
  human_template = """
    Contexte: {context_data}
    Question: {question}
    Réponse:
    """

  custom_prompt = ChatPromptTemplate.from_messages(
    [
      SystemMessage(system_prompt),
      HumanMessagePromptTemplate.from_template(human_template),
    ]
  )

  return (
    {"context_data": retriever | format_docs, "question": RunnablePassthrough()}
    | debug_runnable_fn("Données initiales")
    | custom_prompt
    | debug_runnable_fn("Prompt")
    | _model
    | StrOutputParser()
  )


def init_data(embedding: Embeddings, _store: VectorStore, _chunk_size: int, _chunk_overlap: int) -> VectorStore:
  """
  Initialise les données de contexte
  """

  t0 = time.time()

  # Define the splitter
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=_chunk_size, chunk_overlap=_chunk_overlap, add_start_index=True
  )
  # Chunk the data
  all_splits = TextLoader(file_path="data/champ_euro_football_2024.txt").load_and_split(text_splitter)

  debug(
    f"Contenu découpé en <ansigreen>{len(all_splits)} chunks</ansigreen> en <ansigreen>{(time.time() - t0):0.3} secondes</ansigreen>"
  )
  debug(f"Métadonnées du chunk n°<ansigreen>2</ansigreen> : {all_splits[2].metadata}")

  # Store the chunks
  t0 = time.time()
  _store = _store.from_documents(documents=all_splits, embedding=embedding)
  debug(f"Génération et sauvegarde des embeddings en <ansigreen>{(time.time() - t0):0.3} secondes</ansigreen>")

  return _store


def ask_bot(_chain: RunnableSerializable, question: str) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  return _chain.stream(question)


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Calculating and storing embeddings
  embeddings = OllamaEmbeddings(base_url=args.ollama_url, model=args.embeddings, temperature=args.temperature)
  store = init_data(embeddings, FAISS, args.chunk_size, args.chunk_overlap)

  # Instantiating the LLM chain
  model = ChatOllama(model=args.model, base_url=args.ollama_url)
  chain = init_chain(model, store.as_retriever())

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(chain, question))
