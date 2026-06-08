"""Vertex AI training pipeline with automated evaluation."""
from kfp import dsl
from kfp.v2 import compiler
from google.cloud import aiplatform

@dsl.component(base_image="python:3.11", packages_to_install=["scikit-learn","pandas","google-cloud-bigquery"])
def train_model(project: str, dataset: str, model_name: str, output_path: dsl.Output[dsl.Model]):
    """Train and evaluate model with automated quality gates."""
    import pandas as pd, joblib
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import cross_val_score
    from google.cloud import bigquery
    bq = bigquery.Client(project=project)
    df = bq.query(f"SELECT * FROM `{dataset}`").to_dataframe()
    X, y = df.drop("target", axis=1), df["target"]
    model = GradientBoostingClassifier(n_estimators=500, learning_rate=0.05)
    scores = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
    assert scores.mean() > 0.85, f"Model quality gate failed: AUC={scores.mean():.3f}"
    model.fit(X, y)
    joblib.dump(model, output_path.path)
    print(f"Model trained. CV AUC: {scores.mean():.4f} ± {scores.std():.4f}")
