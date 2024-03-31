from src.metrics.deductive_metrics import compute_redundancy, compute_strong_relevance, compute_weak_relevance

if __name__ == '__main__':
    # Explanation
    matrix = {'A1': ['A2'],
              'A2': ['A3', 'A4'],
              'A3': [],
              'A4': ['A3']
              }
    propositions = ['A1', 'A2', 'A3', 'A4']
    y_hat = 'A3'

    weak_relevance_score = compute_weak_relevance(matrix, propositions, y_hat)
    strong_relevance_score = compute_strong_relevance(matrix, propositions, y_hat)
    redundancy_score = compute_redundancy(matrix, propositions, y_hat)

    print('-' * 50)
    print(f'Explanation: {matrix}')
    print(f'Prediction: {y_hat}')
    print('-' * 17 + '   Evaluation   ' + '-' * 17)
    print(f'Weak Relevance Score: {weak_relevance_score:.2f}')
    print(f'Strong Relevance Score: {strong_relevance_score:.2f}')
    print(f'Redundancy Score: {redundancy_score:.2f}')
