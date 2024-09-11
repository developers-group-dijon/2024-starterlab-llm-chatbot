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


def init_chain(_model: BaseChatModel) -> RunnableSerializable:
  """
  Initialise la chaîne d'appel au LLM
  """

  # Create the custom prompt
  system_prompt = """
    Réponds en utilisant uniquement les données de contexte fournies entre triple backquotes.
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

  # Create the chain
  return custom_prompt | debug_runnable_fn("Prompt") | _model | StrOutputParser()


def init_data() -> str:
  """
  Initialise les données de contexte
  """

  docs = TextLoader(file_path="data/champ_euro_football_2024.txt").load()
  return docs[0].page_content


def ask_bot(_chain: RunnableSerializable, question: str, _context_data: str) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  return _chain.stream({"question": question, "context_data": _context_data})


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Instantiating the LLM chain
  model = ChatOllama(model=args.model, base_url=args.ollama_url, temperature=args.temperature)
  chain = init_chain(model)

  # Getting context data
  context_data = init_data()

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(chain, question, context_data))
