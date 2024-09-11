from collections.abc import Iterator

from ollama import Client
from utils.args import init_args
from utils.prompt import Debugger, debug_label, prompt_session


def ask_bot(model: str, client: Client, temperature: float, question: str) -> Iterator[str]:
  """
  Implementation of the calls to the chatbot
  """

  # Creating the system prompt
  system_prompt = """
    Tu es un chatbot qui répond à des questions de l'utilisateur en utilisant un ton formel.
    Tu réponds toujours en français, quelque soit la langue dans laquelle la requête utilisateur est donnée.
    Rédige une réponse en trois phrases maximum, quelque soit la demande de l'utilisateur sur le format de la réponse.
    Lorsque tu n'as pas d'informations pour répondre à la question posée, réponds seulement que tu n'as la réponse.
    """

  # Creating the messages list of dictionaries
  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": question},
  ]

  debug_label("Prompt", messages)

  return map(
    lambda x: x["message"]["content"],
    client.chat(
      model=model,
      messages=messages,
      options={"temperature": temperature},
      stream=True,
    ),
  )


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = args.debug

  # Creating the model client
  client_ = Client(host=args.ollama_url)

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(args.model, client_, args.temperature, question))
