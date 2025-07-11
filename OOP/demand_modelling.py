"""
Advanced Data Science Module:
- Scikit-learn pipeline
- Feature engineering
- Model serialization
- Type-safe predictions
"""
import json
from datetime import datetime
from pathlib import Path
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from pydantic import BaseModel

class SalesData(BaseModel):
    item_id: int
    day_of_week: Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    is_holiday: bool
    temperature: float
    historical_sales: float

class DemandPredictor:
    def __init__(self):
        self.model = self._build_pipeline()
        self.features = ["item_id", "day_of_week", "is_holiday", "temperature"]
        
    def _build_pipeline(self) -> Pipeline:
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), ['day_of_week']),
                ('num', 'passthrough', ['item_id', 'is_holiday', 'temperature'])
            ])
        
        return Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(n_estimators=100))
        ])
    
    def train(self, data: list[SalesData]) -> None:
        df = pd.DataFrame([d.model_dump() for d in data])
        X = df[self.features]
        y = df['historical_sales']
        self.model.fit(X, y)
    
    def predict(self, item_id: int, **conditions) -> float:
        input_data = {"item_id": item_id, **conditions}
        features = pd.DataFrame([input_data])
        return float(self.model.predict(features)[0])
    
    def save(self, path: Path) -> None:
        metadata = {
            "trained_at": datetime.now().isoformat(),
            "features": self.features
        }
        with open(path / "model.joblib", "wb") as f:
            import joblib
            joblib.dump(self.model, f)
        with open(path / "metadata.json", "w") as f:
            json.dump(metadata, f)

# Usage Example
if __name__ == "__main__":
    predictor = DemandPredictor()
    
    training_data = [
        SalesData(
            item_id=101,
            day_of_week="Mon",
            is_holiday=False,
            temperature=22.5,
            historical_sales=45
        ),
        # Additional 
    ]
    
    predictor.train(training_data)
    print(f"Predicted demand: {predictor.predict(101, day_of_week='Sat', is_holiday=True, temperature=18.0)}")
