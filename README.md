# AI Face Safety Detection System

A production-ready AI classification system built with **FastAPI**, **TensorFlow**, and **OpenCV** to detect sobriety and safety hazards in real-time.

---

### Core Features
- **Real-time Webcam Inference**: Stream video from your device for live safety checks.
- **Image Upload Support**: Upload static images for analysis.
- **Confidence Scoring**: High-precision reliability metrics for every prediction.
- **Microservice Architecture**: Clean separation between API, AI model, and Frontend layers.
- **Dockerized**: Fully containerized for seamless cloud deployment.

### Tech Stack
- **Backend**: FastAPI (Python)
- **AI Model**: TensorFlow/Keras CNN
- **Processing**: OpenCV, PIL, NumPy
- **Frontend**: Vanilla JS (Modern Glassmorphism Design)
- **Deployment**: Docker

### Project Structure
- `/app`: FastAPI routes and endpoint logic.
- `/model`: Inference class and pre-trained `.h5` model storage.
- `/frontend`: High-end UI (HTML/CSS/JS).
- `/utils`: Preprocessing pipelines and model generation scripts.
- `main.py`: Entry point for the entire application.

### Installation & Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Demo Model** (if you don't have one):
   ```bash
   python utils/generate_dummy_model.py
   ```

3. **Launch Application**:
   ```bash
   python main.py
   ```
   Access the UI at: `http://localhost:8000`

### Docker Deployment
To build and run the container:
```bash
docker build -t ai-safety-system .
docker run -p 8000:8000 ai-safety-system
```

---
**Developer**: Au Amores  
**Version**: 1.0.0 (Production Ready)
