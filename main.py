from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router
import uvicorn
import os

app = FastAPI(title="AI Face Safety Detection System")

# Allow Cross-Origin Resource Sharing (CORS) for development and frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, this should be restricted to specific URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the main API router
app.include_router(api_router, prefix="/api")

# Static file serving for the frontend UI files
frontend_dir = os.path.join(os.getcwd(), 'frontend')
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
else:
    print(f"Warning: Static files directory {frontend_dir} not found.")

if __name__ == "__main__":
    # Launch the API server using uvicorn locally
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
