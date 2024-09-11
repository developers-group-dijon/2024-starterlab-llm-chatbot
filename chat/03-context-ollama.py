from collections.abc import Iterator
from pathlib import Path

from ollama import Client
from utils.args import init_args
from utils.prompt import Debugger, debug_label, prompt_session


# TODO: - 001 :  Charger les données de contexte (champ_euro_fottball_2024.txt)
#       - 002 :  Ajouter context_data dans ask_bot
#       - 003 :  Créer le system prompt et le user prompt pour n'utiliser que le contexte
#       - 004 : Appel au model via le client Ollama (en mode stream)
def init_data() -> str:
  """
  Initialise les données de contexte
  """

  # TODO 001
  return ...


def ask_bot(model: str, client: Client, temperature: float, question: str, context_data: str) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  # TODO 003
  system_prompt = ...
  user_prompt = ...

  messages = [
    {...},
    {...},
  ]

  debug_label("Prompt", messages)

  # TODO 004
  return ...


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Creating the model client
  client = Client(host=args.ollama_url)

  # TODO 002
  # Getting context data
  context_data = ...

  # Starting the prompt session
  prompt_session(...)
