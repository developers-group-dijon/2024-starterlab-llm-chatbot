# Importing libraries
import time
from typing import List

import ollama
import numpy as np
import numpy.typing as npt
from utils.args import init_args
from utils.prompt import Debugger, debug, debug_label
from utils.similarity import get_similarity


# TODO: - 001 : Définir une liste de phrases
#       - 002 : Vectoriser les phrases et calculer la matrices de similarité
#       - 003 : Afficher les résultats du calcul de similarité
#       - 004 : Initialiser la matrice vectors
#       - 005 : Vectoriser chaque phrase avec le même modèle.
#       - 006 : Remplir la matrice de similarité
def compute_embeddings(list_sentences: List[str], _model: str) -> npt.NDArray[np.float64]:
  """Compute embeddings of each element of the input list."""

  # Evaluate the output dimension
  # TODO 004 - Tips : inférer le modèle d'embeddings avec un prompt pour connaitre la dimension de l'espace vectoriel
  n_sentences = ...
  n_dim = ...

  t0 = time.time()
  _vectors = np.empty(shape=[n_sentences, n_dim], dtype=float)

  # TODO 005 - Tips : utiliser la méthode embeddings de la classe ollama
  for i, sentence in enumerate(list_sentences):
    _vectors[i] = ...

  debug(
    f"Vectorisation de <ansigreen>{n_sentences}</ansigreen> phrases en <ansigreen>{(time.time() - t0):0.3}</ansigreen> secondes avec le modèle {_model}"
  )
  return _vectors


def compute_cosine_matrix(_vectors: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
  """Calcule la matrice de similarité entre deux vecteurs"""

  n_sentences = len(_vectors)
  cos_matrix = np.empty(shape=[n_sentences, n_sentences], dtype=float)

  # TODO 006
  for k in range(n_sentences):
    for j in range(k, n_sentences):
      cos_matrix[k, j] = ...
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

  # Calculating embeddings
  # TODO 001
  sentences = [
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
  ]

  # Calculating the similarity matrix
  # TODO 002
  vectors = ...
  cosine_matrix = ...

  # Printing results
  # TODO 003
  with np.printoptions(precision=3) as opts:
    debug_label("La similarité cosinus entre les phrases est respectivement", f"""\n{...}""")
  for n in range(1, len(sentences)):
    print_similarity(..., ..., 0, n)
