import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization
import numpy as np

def rank(scores, descending=True):
    order = np.argsort(scores)
    if descending:
        order = order[::-1]
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(scores) + 1)
    return ranks


matrix = np.array([
    # [cena, radość (1-10), wygląd (1-10), ilość elementów]

    # LEGO Star Wars Kanonierka Gwardii Coruscańskiej
    [650, 9, 7, 1083],
    # LEGO Star Wars Gwiezdny Niszczyciel Typu Venator
    [2800, 10, 9, 5374],
    # LEGO Star Wars Myśliwiec X-Wing
    [1050, 10, 10, 1953],
    # LEGO Star Wars Brzeszczot
    [2600, 3, 1, 6187],
])

weights = [0.4, 0.2, 0.1, 0.3]
types = [-1, 1, 1, 1]

normalized_matrix = minmax_normalization(matrix, types)

# TOPSIS
topsis = TOPSIS()
topsis_scores = topsis(normalized_matrix, weights, types)
topsis_ranks = rank(topsis_scores, descending=True)

# SPOTIS
bounds = np.array([
    [300, 1, 1, 1000],    # wartości minimalne
    [3000, 10, 10, 10000] # wartości maksymalne
]).T

spotis = SPOTIS(bounds)
spotis_scores = spotis(matrix, weights, types)
spotis_ranks = rank(spotis_scores, descending=False)

results = pd.DataFrame({
    'Alternatywa': ['Kanonierka', 'Venator', 'X-Wing', 'Brzeszczot'],
    'TOPSIS_score': topsis_scores,
    'TOPSIS_rank': topsis_ranks,
    'SPOTIS_score': spotis_scores,
    'SPOTIS_rank': spotis_ranks
})

print(results)
