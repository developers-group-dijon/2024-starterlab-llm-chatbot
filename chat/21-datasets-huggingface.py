from collections.abc import Iterator

from ollama import Client
from utils.args import init_args
from utils.prompt import Debugger, debug_label, prompt_session
from datasets import load_dataset


def ask_bot(model: str, client: Client, temperature: float, question: str, n_rows: int = 2) -> Iterator[str]:
  """
  Implémentation de l'appel au bot
  """

  # load data using HuggingFace datasets API
  ds = load_dataset("iamtarun/python_code_instructions_18k_alpaca", split="train")[0:n_rows]
  ds = "".join(
    ["{Question :\n" + ds["instruction"][x] + "\nAnswer :\n{" + ds["output"][x] + "}\n\n" for x in range(n_rows)]
  )

  system_prompt = f"""
    You are a Python instructor only that replies to questions and query about Python programming.
    Use the following examples within brackets to respond to the user's query
    {ds}
    """

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

  # Activation du mode debug
  Debugger.debug_mode = args.debug

  # Creating the model client
  client = Client(host=args.ollama_url)

  # Starting the prompt session
  prompt_session(lambda question: ask_bot(args.model, client, args.temperature, question))
