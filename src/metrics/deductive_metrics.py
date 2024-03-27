
def compute_weak_relevance(matrix, total_props, y_hat):
    """Compute the weak relevance metric."""

    num_total_props = len(total_props)
    if num_total_props < 1:
        return 0

    num_paths = 0
    for p_i in total_props:
        if _has_path(matrix, p_i, y_hat):
            num_paths += 1

    return num_paths / num_total_props


def compute_strong_relevance(matrix, total_props, y_hat):
    """Compute the weak relevance metric."""

    num_total_props = len(total_props)
    if num_total_props < 1:
        return 0

    connected_to_y_hat = 0
    for p_i in total_props:
        if _has_direct_path(matrix, p_i, y_hat):
            connected_to_y_hat += 1

    return connected_to_y_hat / num_total_props


def compute_non_redundancy(matrix, total_props, y_hat):
    """Compute the non-redundancy metric."""

    num_total_props = len(total_props)

    components = _get_connected_components(matrix)
    if len(components) > 1:
        return 1

    non_redundancy = 0
    for p_i in total_props:
        non_redundancy += (p_i != y_hat) * 1 if p_i in components[0] else 0

    return 1 - non_redundancy / num_total_props



def _has_direct_path(matrix, start, target):
    return target in matrix[start] or start in target


def _has_path(matrix, start, target, visited=None):
    if start == target:
        return True

    if not visited:
        visited = set()
    visited.add(start)

    for start_neighbor in matrix[start]:
        if start_neighbor not in visited:
            if _has_path(matrix, start_neighbor, target, visited):
                return True

    return False


def _get_connected_components(matrix):
    visited = set()
    connected_components = []

    for node in matrix:
        if node not in visited:
            component = []
            _dfs(matrix, node, component, visited)
            connected_components.append(component)

    return connected_components


def _dfs(matrix, node, component, visited):
    visited.add(node)
    component.append(node)
    for neighbor in matrix[node]:
        if neighbor not in visited:
            _dfs(matrix, neighbor, component, visited)

