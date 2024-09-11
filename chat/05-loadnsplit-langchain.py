import difflib
from typing import List

from langchain_core.documents import Document
from utils.args import init_split_args
from utils.prompt import Debugger, debug_label
from utils.splitter import split_file


# TODO: - 001 : Consulter et appeler la fonction split_file dans utils puis la fonction log_chunks_stats
#       - 002 : Compléter la fonction get_overlap
#       - 003 : Créer le template de prompt en associant le system prompt et le human prompt
#       - 004 : Compléter les messages d'analyse des chunks
def log_chunks_stats(chunks: List[Document]) -> None:
  """ Analyse la taille et l'overlap des chunks"""

  # Evaluate chunks length and overlap
  # TODO 002 - Tips : utiliser la fonction SequenceMatcher de difflib
  def get_overlap(s1: str, s2: str) -> str:
    s = ...
    pos_a, pos_b, size = s.find_longest_match(...)

    # Getting overlaps at the start or end of chunks
    _overlap = s1[pos_a: pos_a + size]
    if (s1.startswith(_overlap) and s2.endswith(_overlap)) or (s1.endswith(_overlap) and s2.startswith(_overlap)):
      return _overlap

    return ""

  n_chunks = len(chunks)
  overlap = []
  for k in range(n_chunks - 1):
    # TODO 003 - Tips : Use  page_content attribut
    tmp = get_overlap(..., ...)
    overlap.append(...)

  # TODO 004
  debug_label(
    f"Taille des <ansigreen>{len(chunks)}</ansigreen> chunks", f"{[len(...) for ... in ...]}"
  )
  debug_label("Overlap des chunks", f"{...}")


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_split_args()

  # Activating the debug mode
  Debugger.debug_mode = True

  # Splitting the files
  # TODO 001
  chunks = ...

  # Analyzing the chunks
  log_chunks_stats(...)
