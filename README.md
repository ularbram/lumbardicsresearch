# Lumbar neural foraminal stenosis: selected aggregate research results

This is a deliberately selective public release. Only aggregate performance tables, six main vector figures, a small metric-recomputation helper, and its synthetic test are included. Full training/architecture code, internal tools, working manuscript, MRI, patient-level records, target-level predictions, checkpoints, credentials, and original datasets are NOT published here.

## Study and results

Exploratory source-only lumbar MRI ordinal grading. Five patient-separated outer folds and 30 completed training stages; 1,972 patients and 19,690 observed targets. LumbarDISC supplied severity development; SPIDER supplied anatomy pretraining. No AISSLab/external severity labels were used for nested selection. Earlier candidate development used this cohort; nested reanalysis therefore remains exploratory, not independent confirmation.

Raw selected-procedure QWK: 0.354 (95% CI 0.338-0.371), versus baseline 0.328 (0.312-0.344). Severe AP: 0.183 (0.162-0.208); severe AUROC: 0.847 (0.834-0.859); multiclass Brier: 0.418 (0.409-0.427). The selected-minus-baseline severe AP interval spans zero. Selected severe sensitivity at argmax was 60.8%, below baseline 73.6%, while severe PPV was 15.2% versus 12.8%. Better QWK does not mean improved safety at every operating point. Temperature transfer did not consistently improve probability accuracy.

Intervals use 2,000 paired patient-clustered bootstrap replicates, stratified by outer fold, conditional on fitted models. They do not quantify retraining or prior development uncertainty. Raw and inner-calibrated outcomes are both reported. Class decisions use argmax, not a clinically selected threshold. Brier is summed over classes (range 0-2); AP is non-interpolated average precision, with grouped score ties.

See [aggregate tables](results/nested_source_2026-09-29/tables), [main figures](results/nested_source_2026-09-29/figures), and [captions](results/nested_source_2026-09-29/figure_inventory.csv). CSVs retain full precision. ROC/PR and calibration plots are point curves without curve/bin confidence bands. Supplementary DCA, subgroup exploration, and internal patient-burden records are intentionally not published in this selective release.

## Limited public code

analysis/aggregate_metrics.py recomputes four scalar metrics from a privately supplied prediction CSV. It does not train a model, reproduce the full bootstrap pipeline, process MRI, or constitute a clinical application. Its synthetic test contains no patient information. Dependencies: numpy, pandas, scikit-learn, pytest. Test with `python -m pytest analysis/test_aggregate_metrics.py -q`. Do not upload your private prediction CSV.

The full implementation and working manuscript remain in the author's local project. This public subset is NOT a complete end-to-end reproducibility package; no such claim is made.

## Evidence, privacy, and licenses

These results are not geographic or confirmatory external validation and do not establish clinical or commercial readiness. Orientation provenance, independent cohort testing, final checkpoint lock, and human author/ethics review remain outstanding. No dataset or checkpoint redistribution is authorized by this repository. Original conditions apply: [LumbarDISC](https://pubs.rsna.org/doi/full/10.1148/ryai.250480), [SPIDER](https://www.nature.com/articles/s41597-024-03090-w). AI-assisted outputs require human verification. This is a working aggregate research record, not a final submitted manuscript.
