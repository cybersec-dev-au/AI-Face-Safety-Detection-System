from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from model.inference import Predictor
from utils.preprocessing import preprocess_image
import io
from PIL import Image
import numpy as np

router = APIRouter()
predictor = Predictor()

@router.get("/health")
async def health_check():
    """Health check endpoint to verify API operation."""
    return {"status": "healthy", "model_loaded": predictor.model is not None}

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Prediction endpoint for sober vs intoxicated detection."""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    try:
        # Read and preprocess the image
        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert("RGB")
        processed_img = preprocess_image(img)
        
        # Inference
        label, confidence = predictor.predict(processed_img)
        
        return JSONResponse(content={
            "prediction": label,
            "confidence": float(confidence),
            "status": "success"
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": f"Inference failed: {str(e)}"})
