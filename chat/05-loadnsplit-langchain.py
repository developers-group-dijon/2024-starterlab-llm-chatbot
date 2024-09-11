import difflib
from typing import List

from langchain_core.documents import Document
from utils.args import init_split_args
from utils.prompt import Debugger, debug_label
from utils.splitter import split_file


def log_chunks_stats(_chunks: List[Document]) -> None:
  # Evaluate chunks length and overlap
  def get_overlap(s1: str, s2: str) -> str:
    s = difflib.SequenceMatcher(None, s1, s2, False)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2))

    # Getting overlaps at the start or end of chunks
    _overlap = s1[pos_a : pos_a + size]
    if (s1.startswith(_overlap) and s2.endswith(_overlap)) or (s1.endswith(_overlap) and s2.startswith(_overlap)):
      return _overlap

    return ""

  n_chunks = len(_chunks)
  overlap = []
  for k in range(n_chunks - 1):
    tmp = get_overlap(_chunks[k].page_content, _chunks[k + 1].page_content)
    overlap.append(len(tmp))

  debug_label(
    f"Taille des <ansigreen>{len(_chunks)}</ansigreen> chunks", f"{[len(chunk.page_content) for chunk in _chunks]}"
  )
  debug_label("Overlap des chunks", f"{overlap}")


if __name__ == "__main__":
  # Getting arguments from CLI
  args = init_split_args()

  # Activating the debug mode
  Debugger.debug_mode = True

  # Splitting the files
  chunks = split_file(args)

  # Analyzing the chunks
  log_chunks_stats(chunks)
