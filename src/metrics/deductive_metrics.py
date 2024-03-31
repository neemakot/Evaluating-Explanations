"""
    Implementation of redundancy, strong relevance and weak relevance metrics
    for deductive explanations.

    Parameters (for all three metrics):
        matrix (Dict[str, List[str]]): adjacency dictionary that represents the deductive explanation.
        propositions (List[str]): all propositions in the deductive explanation, i.e. all keys in matrix.
        y_hat (str): the prediction, which is an element of total_props.

    Returns:
        score (float): metric score in [0,1]

    Example input:

    matrix: { 'A': ['B', 'D', 'F', 'Y'],
              'B': ['C'],
              'C': ['A', 'D'],
              'D': [],
              'E': ['A', 'B', 'C'],
              'F': ['A']
            }
    y_hat:  'Y'

    For strong relevance, the best score is one, the worst score is zero.
    For weak relevance, the best score is one, the worst score is zero.
    For redundancy, the best score is zero, the worst score is one.

"""


def compute_redundancy(matrix, propositions, y_hat):
    """Compute the redundancy metric."""
    num_props = len(propositions)

    components = _get_connected_components(matrix)
    if len(components) > 1:
        return 1

    redundant_props = 0
    for p_i in propositions:
        redundant_props += (p_i != y_hat) * 1 if p_i in components[0] else 0

    return 1 - redundant_props / num_props


def compute_strong_relevance(matrix, propositions, y_hat):
    """Compute the weak relevance metric."""

    num_props = len(propositions)
    if num_props < 1:
        return 0

    connected_to_y_hat = 0
    for p_i in propositions:
        if _has_direct_path(matrix, p_i, y_hat):
            connected_to_y_hat += 1

    return connected_to_y_hat / num_props


def compute_weak_relevance(matrix, propositions, y_hat):
    """Compute the weak relevance metric."""

    num_total_props = len(propositions)
    if num_total_props < 1:
        return 0

    num_paths = 0
    for p_i in propositions:
        if _has_path(matrix, p_i, y_hat):
            num_paths += 1

    return num_paths / num_total_props


def _has_direct_path(matrix, start, target):
    """Return true if edge between start and target, else false."""
    return target in matrix[start] or start in target


def _get_connected_components(matrix):
    """Retrieve all connected components."""
    visited = set()
    connected_components = []

    for node in matrix:
        if node not in visited:
            component = []
            _dfs(matrix, node, component, visited)
            connected_components.append(component)

    return connected_components


def _dfs(matrix, node, component, visited):
    """Compute depth first search."""
    visited.add(node)
    component.append(node)
    for adjacent_node in matrix[node]:
        if adjacent_node not in visited:
            _dfs(matrix, adjacent_node, component, visited)


def _has_path(matrix, start, target, visited=None):
    """Compute whether there is a path between start and target."""
    if start == target:
        return True

    if not visited:
        visited = set()
    visited.add(start)

    for start_adjacent_node in matrix[start]:
        if start_adjacent_node not in visited:
            if _has_path(matrix, start_adjacent_node, target, visited):
                return True

    return False
