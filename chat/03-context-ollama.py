from collections.abc import Iterator
from pathlib import Path

from ollama import Client
from utils.args import init_args
from utils.prompt import Debugger, debug_label, prompt_session


def init_data() -> str:
  """
  Initialise les données de contexte.
  """

  # Load context data from"data/champ_euro_football_2024_light.txt"
  return Path("data/champ_euro_football_2024_light.txt").read_text()


def ask_bot(model: str, _client: Client, temperature: float, question: str, _context_data: str) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  # XXX Solution
  system_prompt = """
    Tu es un chatbot qui répond à des questions en utilisant uniquement les données de contexte fournies et avec un ton formel
    Tu réponds toujours en français, quelque soit la langue dans laquelle la requête utilisateur est donnée.
    Lorsque le contexte ne fournit pas d'informations sur la question posée, réponds que tu n'as la réponse.
    Par exemple, si la question concerne une recette de cuisine, réponds que tu ne sais pas.
    """

  user_prompt = f"""
    Context: {_context_data}
    Question: {question}
    Réponse: 
    """

  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
  ]

  debug_label("Prompt", messages)

  return map(
    lambda x: x["message"]["content"],
    _client.chat(
      model=model,
      messages=messages,
      stream=True,
      options={"temperature": temperature},
    ),
  )


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Getting context data
  context_data = init_data()

  # Creating the model client
  client = Client(host=args.ollama_url)

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(args.model, client, args.temperature, question, context_data))
