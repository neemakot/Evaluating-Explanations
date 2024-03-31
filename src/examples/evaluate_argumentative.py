from src.metrics.argumentative_metrics import compute_circularity, compute_dialectical_acceptability


if __name__ == '__main__':
    # Explanation 1
    ex1_arguments = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']
    ex1_attack_relations = [('A1', 'B1'), ('A2', 'B1'), ('A3', 'B2'), ('A3', 'B3'),
                            ('B1', 'A1'), ('B2', 'A3'), ('B3', 'A3')]
    ex1_support_relations = [('A1', 'A2'), ('A1', 'A3'), ('B1', 'B2'), ('B1', 'B3')]
    ex1_y_hat_args = ['B3']
    ex1_circ_score = compute_circularity(ex1_arguments, ex1_attack_relations, ex1_support_relations)
    ex1_acc_score = compute_dialectical_acceptability(ex1_arguments, ex1_attack_relations, ex1_y_hat_args)

    print('-' * 50)
    print('Example 1:')
    print(f'Arguments: {ex1_arguments}')
    print(f'Attack Relations: {ex1_attack_relations}')
    print(f'Support Relations: {ex1_support_relations}')
    print('-' * 17 + '   Evaluation   ' + '-' * 17)
    print(f'Circularity Score: {ex1_circ_score:.2f}')
    print(f'Acceptability Score: {ex1_acc_score:.2f}')

