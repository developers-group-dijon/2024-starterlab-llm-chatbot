# Importing libraries
import time
from typing import List

import numpy as np
import numpy.typing as npt
import ollama
from utils.args import init_args
from utils.prompt import Debugger, debug, debug_label
from utils.similarity import get_similarity


def compute_embeddings(list_sentences: List[str], model: str) -> npt.NDArray[np.float64]:
  """Compute embeddings of each element of the input list."""

  # Evaluate the output dimension
  n_sentences = len(list_sentences)
  n_dim = len(ollama.embeddings(model=model, prompt="dummy")["embedding"])

  # Get embeddings
  t0 = time.time()
  _vectors = np.empty(shape=[n_sentences, n_dim], dtype=float)

  for i, sentence in enumerate(list_sentences):
    _vectors[i] = ollama.embeddings(model=model, prompt=sentence)["embedding"]

  debug(
    f"Vectorisation de <ansigreen>{n_sentences}</ansigreen> phrases en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes avec le modèle {model}"
  )
  return _vectors


def compute_cosine_matrix(_vectors: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
  n_sentences = len(_vectors)

  cos_matrix = np.empty(shape=[n_sentences, n_sentences], dtype=float)

  for k in range(n_sentences):
    for j in range(k, n_sentences):
      cos_matrix[k, j] = get_similarity(_vectors[k], _vectors[j])
      cos_matrix[j, k] = cos_matrix[k, j]

  return cos_matrix


def print_similarity(_sentences: list[str], _cosine_matrix: npt.NDArray[np.float64], i: int, j: int) -> None:
  similarity = _cosine_matrix[i][j]
  color = "ansiblue"
  if similarity < 0.4:
    color = "ansired"
  elif similarity > 0.6:
    color = "ansigreen"
  debug(
    f"""Similarité entre <ansigreen>{_sentences[i]:30s}</ansigreen> et <ansigreen>{_sentences[j]:30s}</ansigreen> : <{color}>{similarity:0.3}</{color}>"""
  )


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_args()

  # Activating the debug mode
  Debugger.debug_mode = True

  # Creating sentences
  sentences = [
    "J'aime le paté",
    "J'aime les courgettes",
    "La charcuterie, c'est la vie",
    "Je n'aime pas les légumes",
    "Le végétal c'est le mal",
    "Le paté est trop bon",
    "La vie est triste sans paté",
    "Je suis allergique au paté",
  ]

  # Calculating embeddings
  vectors = compute_embeddings(sentences, model=args.embeddings)

  # Calculating the similarity matrix
  cosine_matrix = compute_cosine_matrix(vectors)

  # Printing results
  with np.printoptions(precision=3) as opts:
    debug_label("La similarité cosinus entre les phrases est respectivement", f"""\n{cosine_matrix}""")

  for k in range(1, len(sentences)):
    print_similarity(sentences, cosine_matrix, 0, k)
