import os
import tensorflow as tf
import numpy as np
from pathlib import Path

class Predictor:
    """Predictor class responsible for model loading and inference logic."""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Predictor, cls).__new__(cls)
            cls._instance.model = None
            cls._instance.load_model()
        return cls._instance

    def load_model(self):
        """Load the pre-trained Keras model from the specified file path."""
        try:
            model_path = Path(__file__).parent / "sober_intoxicated_model.h5"
            if model_path.exists():
                self.model = tf.keras.models.load_model(str(model_path))
                print(f"Model loaded successfully from {model_path}")
            else:
                print(f"Warning: Model file not found at {model_path}. Please place a valid model file.")
                self.model = None
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            self.model = None

    def predict(self, processed_img: np.ndarray):
        """Perform predictions on the processed image array."""
        if self.model is None:
            # Placeholder/Mock logic for the demo if model fails to load
            print("Running in mock inference mode...")
            prediction_score = float(np.random.uniform(0.1, 0.95))
            label = "Intoxicated" if prediction_score > 0.5 else "Sober"
            return label, prediction_score
            
        prediction = self.model.predict(processed_img, verbose=0)
        
        # Binary classification logic: > 0.5 is Intoxicated, <= 0.5 is Sober
        # Adjust based on how your specific model was trained
        score = float(prediction[0][0])
        label = "Intoxicated" if score > 0.5 else "Sober"
        confidence = score if score > 0.5 else (1.0 - score)
        
        return label, confidence
