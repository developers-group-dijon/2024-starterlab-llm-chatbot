from collections.abc import Iterator

from langchain_community.chat_models import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables.base import RunnableSerializable
from utils.args import init_args
from utils.prompt import Debugger, debug_runnable_fn, prompt_session


# TODO: - 001 :  Initier le modèle et la chaine de traitement
#       - 002 :  Créer la session prompt
#       - 003 :  Créer le template de prompt en associant le system prompt et le human prompt
#       - 004 : Créer la chaine de traitement
#       - 005 : Compléter le retour de la fonction ask_bot
def init_chain(_model: BaseChatModel) -> RunnableSerializable:
  """
  Initialise la chaîne d'appel au LLM
  """

  # TODO 003 - Tips : utiliser la fonction ChatPromptTemplate.from_messages
  system_prompt = """
    Répond en 3 phrases maximum et utilise un ton neutre.
    Lorsque tu n'as pas d'informations pour répondre à la question posée, réponds que tu n'as la réponse.
    """

  human_template = "{question}"

  custom_prompt = ChatPromptTemplate.from_messages(
    [
      ...,
      ...,
    ]
  )

  # TODO 004
  return ... | ... | ... | ...


def ask_bot(chain: RunnableSerializable, question: str) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  # TODO 005 - Tips : utiliser la fonction stream
  return ...


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Instantiating the LLM chain
  # TODO 001 - Tips : utiliser la classe ChatOllama de la bibliothèque langchain_community
  model = ChatOllama(...)
  chain = init_chain(...)

  # Starting the prompt session
  # TODO 002
  prompt_session(...)
