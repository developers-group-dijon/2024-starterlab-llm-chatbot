from collections.abc import Iterator

from ollama import Client
from utils.args import init_args
from utils.prompt import Debugger, debug_label, prompt_session
from datasets import load_dataset


# TODO: - 001 : Créer l'appel au client dans le main
#       - 002 : Charger le dataset python_code_instructions_18k_alpaca (train) et sélectionner les 100 premières lignes
#       - 003 : Formatter les données Créer un system prompt avec les exemples
#       - 004 : Construire le dict messages avec
#         - 1 prompt de rôle system
#         - 1 prompt de rôle user dont le contenu est question
#       - 005 : Appel au modèle (mode stream) et retourner le "message.content" de la réponse
def ask_bot(model: str, client: Client, temperature: float, question: str, n_rows: int = 100) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  # load data using HuggingFace datasets API
  # TODO 002 - Charger le dataset python_code_instructions_18k_alpaca (train) et sélectionner les 100 premières lignes
  ds = ...

  # TODO 003 - Formatter les données Créer un system prompt avec des exemples
  system_prompt = ...

  # TODO 004 - Same as previous exercise with an enriched system_prompt
  messages = [...]

  debug_label("Prompt", messages)

  # TODO 005 - Tips : Use the chat method of the client object
  return ...


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activation du mode debug
  Debugger.debug_mode = args.debug

  # Creating the model client
  client = ...

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(args.model, client, args.temperature, question))
