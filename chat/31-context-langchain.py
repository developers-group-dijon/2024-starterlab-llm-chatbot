from collections.abc import Iterator

from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import TextLoader
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables.base import RunnableSerializable
from utils.args import init_args
from utils.prompt import Debugger, debug_runnable_fn, prompt_session


# TODO: - 001 : Initialiser la chaine en utilisant le retriever de la BDD
#       - 002 : Récupérer les données de contexte et démarrer la session de prompt
#       - 003 : Créer le template de prompt en associant le system prompt et le human prompt
#       - 004 : Créer la chaine de traitement
#       - 005 : Compléter la fonction init_data pour charger les données
#       - 006 : Compléter le retour de la fonction ask_bot
def init_chain(model: BaseChatModel) -> RunnableSerializable:
  """
  Initialise la chaîne d'appel au LLM
  """

  # Create the custom prompt
  # TODO 003 - Tips : utiliser la fonction ChatPromptTemplate.from_messages
  system_prompt = ...
  human_template = ...
  custom_prompt = ...

  # Create the chain
  # TODO 004
  return (
    {...: ... | format_docs, ...: ...}
    | debug_runnable_fn("Données initiales")
    | ...
    | debug_runnable_fn("Prompt")
    | ...
    | ...
  )


def init_data() -> str:
  """
  Initialise les données de contexte
  """

  # TODO 005 - Tips : utliser la fonction UnstructuredHTMLLoader
  docs = ...(file_path="data/champ_euro_football_2024.html").load()
  return docs[0].page_content


def ask_bot(chain: RunnableSerializable, question: str, context_data: str) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  # TODO 006 - Tips : utiliser la fonction stream
  return ...


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Instantiating the LLM chain
  # TODO 001
  model = ChatOllama(model=..., base_url=...)
  chain = init_chain(..., ...)

  # Getting context data
  # TODO 002
  context_data = ...
  # Starting the prompt session
  prompt_session(...)
