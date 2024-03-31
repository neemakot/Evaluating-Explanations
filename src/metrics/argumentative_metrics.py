"""
    Implementation of circularity and dialectical acceptability metrics
    for argumentative explanations.
"""


def compute_circularity(args, attack_relations, support_relations):
    """
       Compute the circularity metric by checking if there is a cycle in the combined abstract argumentation framework.
       The lower the score, the fewer the number of cycles
       and therefore the better the argumentative explanation, in a rhetorical sense.

        Parameters:
            args (List[str]): list of arguments in the argumentative explanation.
            attack_relations (List[List[str]]: list of attacker-attacked argument pairs in the explanation.
            support_relations (List[List[str]]: list of supporter-support argument pairs in the explanation.

        Returns:
            score (float): circularity score, the more cycles, the higher the score.
    """
    num_nodes = len(args)
    af = {ind: [] for ind in range(num_nodes)}

    for attack_pair in attack_relations:
        attacker, attacked = attack_pair
        af[args.index(attacker)].append(args.index(attacked))

    for support_pair in support_relations:
        supported, supporter = support_pair
        af[args.index(supported)].append(args.index(supporter))

    visited, stack = [False] * num_nodes, [False] * num_nodes
    score = 0

    for node in range(num_nodes):
        if not visited[node]:
            if _dfs_cycle(af, node, visited, stack):
                score += 1

    return score / num_nodes


def compute_dialectical_acceptability(args, attack_relations, args_y_hat):
    """
        Compute dialectical acceptability for an argumentative explanation.

        Parameters:
            args (List[str]): list of arguments in the argumentative explanation.
            attack_relations (List[Tuple[str]]: list of attacker-attacked argument pairs in the explanation.
            args_y_hat (List[str]): list of arguments that have conclusion y_hat.

        Returns:
            score (float): acceptability score
    """

    num_nodes = len(args)

    # dict of attackers for each argument
    af_attacks = {ind: [] for ind in range(num_nodes)}

    # initialize False, if true acc score one as there are attacked y_hat conclusion args.
    is_yhat_attacked = False

    for attack_pair in attack_relations:
        attacker, attacked = attack_pair
        af_attacks[args.index(attacked)].append(args.index(attacker))

        if attacked in args_y_hat:
            is_yhat_attacked = True

    # no y_hat argument attackers to check
    if not is_yhat_attacked:
        return 1

    score = 0
    for arg_i in args_y_hat:
        score_a_i = 0
        arg_i_attackers = af_attacks[args.index(arg_i)]
        if arg_i_attackers:
            for a_j in arg_i_attackers:
                if af_attacks[a_j]:
                    score_a_i += 1
                else:
                    score_a_i += 0
            score_a_i /= len(arg_i_attackers)
        else:
            # if there are no attackers of a_i
            score_a_i = 1

        score += score_a_i

    return score / num_nodes


def _dfs_cycle(arg_framework, start, visited, stack):
    """Depth-first-search traversal of argumentation graph to check for the presence of a cycle."""
    visited[start] = True
    stack[start] = True

    for arg in arg_framework[start]:
        if not visited[arg]:
            if _dfs_cycle(arg_framework, arg, visited, stack):
                return True
        elif stack[arg]:
            return True

    stack[start] = False
    return False
