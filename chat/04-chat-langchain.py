from collections.abc import Iterator

from langchain_community.chat_models import ChatOllama
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

  system_prompt = """
    Répond en 3 phrases maximum et utilise un ton neutre.
    Lorsque tu n'as pas d'informations pour répondre à la question posée, réponds que tu n'as la réponse.
    """
  human_template = "{question}"

  custom_prompt = ChatPromptTemplate.from_messages(
    [
      SystemMessage(system_prompt),
      HumanMessagePromptTemplate.from_template(human_template),
    ]
  )

  return custom_prompt | debug_runnable_fn("Prompt") | _model | StrOutputParser()


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

  # Instantiating the LLM chain
  model = ChatOllama(model=args.model, base_url=args.ollama_url, temperature=args.temperature)
  chain = init_chain(model)

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(chain, question))
