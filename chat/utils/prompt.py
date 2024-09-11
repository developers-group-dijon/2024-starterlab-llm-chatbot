from collections.abc import Iterator
import time
from typing import Any, Callable, Tuple

from langchain_core.runnables.base import RunnableLambda
from prompt_toolkit import HTML, PromptSession, print_formatted_text as print
from prompt_toolkit.history import FileHistory


class Debugger:
  debug_mode = False

  @classmethod
  def debug(cls, input: Any) -> None:
    if cls.debug_mode:
      print(HTML(f"<ansired> » </ansired> <ansibrightblack>{input}</ansibrightblack>"))

  @classmethod
  def debug_label(cls, label: str, input: Any) -> Any:
    cls.debug(f"<ansigreen>[{label}]</ansigreen>")
    cls.debug(f"{input}")
    return input

  @classmethod
  def debug_runnable_fn(cls, label: str) -> RunnableLambda:
    return RunnableLambda(lambda i: cls.debug_label(label, i))


def debug_label(label: str, input: Any) -> None:
  Debugger.debug_label(label, input)


def debug(input: Any) -> None:
  Debugger.debug(input)


def debug_runnable_fn(label: str) -> RunnableLambda:
  return Debugger.debug_runnable_fn(label)


def prompt_session(callback: Callable[[str], Iterator[str]]) -> None:
  session = PromptSession(history=FileHistory(".history"))

  while True:
    message = session.prompt(">>> ")
    if message in ["bye", "exit", "quit", "q"]:
      exit("À bientôt")

    t0 = time.time()

    n_words, n_char = print_response(callback(message))
    feedback = f"""Réponse générée en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes avec <ansigreen>{n_words}</ansigreen> mots et <ansigreen>{n_char}</ansigreen> caractères."""
    debug(feedback)


def print_response(response: Iterator[str]) -> tuple[int, int]:
  first = True
  sentence = []
  n_char = 0
  n_words = 0
  for chunk in response:
    if first:
      print("")
      first = False
    print(chunk, end="", flush=True)
    sentence += chunk
  print("\n")

  sentence = "".join(sentence)[1:]
  n_char = len(sentence)
  n_words = len(sentence.split(" "))

  return n_words, n_char
