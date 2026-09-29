import numpy as np
import pandas as pd
from aggregate_metrics import aggregate_metrics


def test_synthetic_perfect_ranking_and_classes():
    frame = pd.DataFrame({
        'grade': ['normal_mild', 'moderate', 'severe', 'normal_mild', 'severe'],
        'p_normal_mild': [.8, .1, .1, .8, .1],
        'p_moderate': [.1, .8, .1, .1, .1],
        'p_severe': [.1, .1, .8, .1, .8],
    })
    result = aggregate_metrics(frame)
    assert np.isclose(result['quadratic_weighted_kappa'], 1)
    assert np.isclose(result['severe_auroc'], 1)
    assert np.isclose(result['severe_auprc'], 1)
    assert np.isclose(result['multiclass_brier'], .06)
