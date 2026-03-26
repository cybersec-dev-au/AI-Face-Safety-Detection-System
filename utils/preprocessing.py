from PIL import Image
import numpy as np

def preprocess_image(image: Image.Image, target_size=(224, 224)):
    """Preprocess an input image for model inference."""
    # Resize image to model expected input size
    image = image.resize(target_size)
    
    # Convert image to numpy array and normalize pixel values
    img_array = np.array(image).astype('float32') / 255.0
    
    # Add batch dimension (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array
