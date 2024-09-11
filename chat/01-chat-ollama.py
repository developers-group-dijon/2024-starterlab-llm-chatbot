from collections.abc import Iterator

from ollama import Client
from utils.args import init_args
from utils.prompt import Debugger, debug_label, prompt_session


# TODO: - 001  : Créer l'appel au client dans le main
#       - 002 : Construire le dict messages avec
#         - 1 prompt de rôle system dont le contenu est system_prompt
#         - 1 prompt de rôle user dont le contenu est question
#       - 003 : Appel au modèle(mode stream) et retourner le "message.content" de la réponse
def ask_bot(model: str, client: Client, temperature: float, question: str) -> Iterator[str]:
  """
    Implementation of the calls to the chatbot
  """

  system_prompt = """
    Tu es un chatbot qui répond à des questions de l'utilisateur en utilisant un ton formel.
    Tu réponds toujours en français, quelque soit la langue dans laquelle la requête utilisateur est donnée.
    Rédige une réponse en trois phrases maximum, quelque soit la demande de l'utilisateur sur le format de la réponse.
    Lorsque tu n'as pas d'informations pour répondre à la question posée, réponds seulement que tu n'as la réponse.
    """

  # TODO 002 - Tips : Provide a dict with role and content fields for system and user instructions
  messages = [...]

  debug_label("Prompt", messages)

  # TODO 003 - Tips : Use the chat method of the client object
  return ...


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # TODO 001
  client = ...

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(args.model, client_, args.temperature, question))
