import numpy as np
import numpy.typing as npt


def get_similarity(
  vec1: npt.NDArray[np.float64], vec2: npt.NDArray[np.float64], get_l2: bool = False, verbose: bool = False
) -> float:
  """Compute the normalized cosine similarity and L2 distance within [0, 1]."""

  # Get the L2 norm of vectors
  norm_vec1 = np.linalg.norm(vec1)  # L2 norm = sqrt(sum_k abs(vec1(k))**2)
  norm_vec2 = np.linalg.norm(vec2)

  if get_l2:
    # Compute the Euclidian similarity
    L2_distance = np.linalg.norm(vec1 - vec2)  # L2-distance = sqrt( sum_k ( vec1(k) - vec2(k))**2 )
    output = np.sqrt(L2_distance**2 / (norm_vec1**2 + norm_vec2**2))
  else:
    # Compute the cosine similarity
    dot_product = np.dot(vec1, vec2)  # dot_product = sum_k vec1(k) * vec2(k)
    output = dot_product / (norm_vec1 * norm_vec2)

  if verbose:
    print(f"""Norms of vectors are {norm_vec1} and {norm_vec2} respectively.""")
    print(f"""The similarity is is {output}.""")

  return output
