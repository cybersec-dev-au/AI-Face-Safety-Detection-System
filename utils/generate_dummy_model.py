import tensorflow as tf
from tensorflow.keras import layers, models
import os

def create_model():
    """Create a simple Keras CNN model for demonstration purposes."""
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid') # Binary classification output layer
    ])
    
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    model_dir = os.path.join(os.getcwd(), 'model')
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
        
    model_path = os.path.join(model_dir, 'sober_intoxicated_model.h5')
    model.save(model_path)
    print(f"Dummy model generated successfully at {model_path}")

if __name__ == "__main__":
    create_model()
