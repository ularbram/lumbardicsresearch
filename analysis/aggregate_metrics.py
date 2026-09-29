"""Four scalar metrics only; read private predictions locally, publish none."""
import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, cohen_kappa_score, roc_auc_score

PROBS = ['p_normal_mild', 'p_moderate', 'p_severe']
GRADES = {'normal_mild': 0, 'moderate': 1, 'severe': 2}


def aggregate_metrics(frame):
    y = frame['grade'].map(GRADES)
    if y.isna().any():
        raise ValueError('Unknown or missing reference grade')
    y = y.to_numpy(dtype=int)
    p = frame[PROBS].to_numpy(dtype=float)
    if not (np.isfinite(p).all() and (p >= 0).all() and (p <= 1).all()
            and np.allclose(p.sum(axis=1), 1, atol=2e-7, rtol=0)):
        raise ValueError('Invalid class probabilities')
    if len(np.unique(y == 2)) != 2:
        raise ValueError('Severe metrics require both severe and non-severe targets')
    return {
        'quadratic_weighted_kappa': float(cohen_kappa_score(y, p.argmax(axis=1), labels=[0, 1, 2], weights='quadratic')),
        'severe_auprc': float(average_precision_score(y == 2, p[:, 2])),
        'severe_auroc': float(roc_auc_score(y == 2, p[:, 2])),
        'multiclass_brier': float(np.mean(np.sum((p - np.eye(3)[y]) ** 2, axis=1))),
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recompute scalar metrics without publishing private inputs')
    parser.add_argument('private_prediction_csv')
    args = parser.parse_args()
    import json
    print(json.dumps(aggregate_metrics(pd.read_csv(args.private_prediction_csv)), indent=2))
