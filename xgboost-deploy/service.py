import bentoml
import numpy as np
import xgboost as xgb
import os

@bentoml.service(
    resources={"cpu": "2"},
    traffic={"timeout": 10},
)

class CancerClassifier:
    # Retrieve model from bentoML Model Store
    bento_model = bentoml.models.get("cancer:latest")

    def __init__(self):
        self.model = bentoml.xgboost.load_model(self.bento_model)

        if os.getenv()

        