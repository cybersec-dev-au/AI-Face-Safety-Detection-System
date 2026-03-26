<div align="center">

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║    ██████╗ ███████╗████████╗███████╗ ██████╗████████╗    ║
║    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ║
║    ██║  ██║█████╗     ██║   █████╗  ██║        ██║       ║
║    ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║       ║
║    ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║       ║
║    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝       ║
║                                                           ║
║          AI Face Safety Detection System v1.0.0          ║
╚═══════════════════════════════════════════════════════════╝
```

**Real-time sobriety & hazard detection — production-ready.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-Apache_2.0-D22128?style=flat-square&logo=apache&logoColor=white)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production_Ready-22c55e?style=flat-square)](.)

</div>

---

## ◈ Overview

A microservice-based AI classification system that detects sobriety and safety hazards in real time using computer vision. Feed it a webcam stream or a static image — it returns a classified label and a confidence score.

Built for deployment. No fluff.

---

## ◈ Features

| Feature | Description |
|---|---|
| **Live Webcam Inference** | Real-time video stream classification |
| **Image Upload** | Static image analysis endpoint |
| **Confidence Scoring** | Per-prediction reliability metrics |
| **Microservice Architecture** | Decoupled API, model, and frontend layers |
| **Fully Dockerized** | One command to deploy anywhere |

---

## ◈ Tech Stack

```
┌─────────────────────────────────────────────────────────┐
│  LAYER          TECHNOLOGY                               │
├─────────────────────────────────────────────────────────┤
│  Backend        FastAPI (Python)                         │
│  AI Model       TensorFlow / Keras CNN                  │
│  Processing     OpenCV · PIL · NumPy                    │
│  Frontend       Vanilla JS — Glassmorphism UI           │
│  Deployment     Docker                                  │
└─────────────────────────────────────────────────────────┘
```

---

## ◈ Project Structure

```
ai-face-safety-detection/
│
├── app/                    # FastAPI routes & endpoint logic
├── model/                  # Inference class + .h5 model storage
├── frontend/               # HTML / CSS / JS — Glassmorphism UI
├── utils/                  # Preprocessing pipelines & model scripts
├── main.py                 # Application entry point
├── requirements.txt
└── Dockerfile
```

---

## ◈ Quickstart

### 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### 2 — Generate demo model *(skip if you have a trained `.h5`)*
```bash
python utils/generate_dummy_model.py
```

### 3 — Launch
```bash
python main.py
```

> UI available at **`http://localhost:8000`**

---

## ◈ Docker Deployment

```bash
# Build image
docker build -t ai-safety-system .

# Run container
docker run -p 8000:8000 ai-safety-system
```

---

## ◈ API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serve frontend UI |
| `POST` | `/predict/image` | Upload image for classification |
| `GET` | `/predict/stream` | Live webcam inference stream |
| `GET` | `/health` | Service health check |

**Sample response:**
```json
{
  "label": "NORMAL",
  "confidence": 0.9741,
  "inference_time_ms": 38.2
}
```

---

## ◈ License

```
Copyright 2026 Au Amores

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---

<div align="center">

**Built by [Au Amores](https://github.com/ares-coding) · v1.0.0 · Production Ready**

</div>
