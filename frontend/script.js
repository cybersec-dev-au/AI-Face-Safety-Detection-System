const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas-overlay');
const imagePreview = document.getElementById('image-preview');
const imageUpload = document.getElementById('image-upload');
const startWebcamBtn = document.getElementById('start-webcam');
const captureBtn = document.getElementById('capture-frame');
const spinner = document.getElementById('spinner');
const predictionLabel = document.getElementById('prediction-label');
const predictionMsg = document.getElementById('prediction-msg');
const confidenceBar = document.getElementById('confidence-bar');
const confidencePercentage = document.getElementById('confidence-percentage');
const analyzeBtn = document.getElementById('analyze-upload');

let stream = null;
let currentFile = null;

// Function to initialize webcam
async function startWebcam() {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' } });
        webcamElement.srcObject = stream;
        webcamElement.classList.add('active');
        imagePreview.style.display = 'none';
        
        startWebcamBtn.style.display = 'none';
        captureBtn.style.display = 'block';
        analyzeBtn.style.display = 'none';
        
        // Start real-time analysis loop
        setInterval(analyzeFrame, 2000); // Analyze every 2 seconds
    } catch (err) {
        console.error('Error accessing webcam:', err);
        alert('Could not access webcam. Please check permissions.');
    }
}

// Function to analyze current webcam frame
async function analyzeFrame() {
    if (!stream) return;
    
    // Create canvas capture
    const canvas = document.createElement('canvas');
    canvas.width = webcamElement.videoWidth;
    canvas.height = webcamElement.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(webcamElement, 0, 0, canvas.width, canvas.height);
    
    canvas.toBlob(async (blob) => {
        const formData = new FormData();
        formData.append('file', blob, 'capture.jpg');
        await performPrediction(formData);
    }, 'image/jpeg');
}

// Function to handle file uploads
imageUpload.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (file) {
        // Show preview
        const reader = new FileReader();
        reader.onload = (event) => {
            imagePreview.src = event.target.result;
            imagePreview.style.display = 'block';
            webcamElement.classList.remove('active');
            
            // Show analyze button
            analyzeBtn.style.display = 'block';
            
            // Stop webcam if it was running
            if (stream) {
                stream.getTracks().forEach(track => track.stop());
                stream = null;
                startWebcamBtn.style.display = 'block';
                captureBtn.style.display = 'none';
            }
        };
        reader.readAsDataURL(file);
        
        // Store current file for analysis
        currentFile = file;
    }
});

// Event listener for manual analysis button
analyzeBtn.addEventListener('click', async () => {
    if (currentFile) {
        const formData = new FormData();
        formData.append('file', currentFile);
        await performPrediction(formData);
    }
});

// Primary function to communicate with the FastAPI backend
async function performPrediction(formData) {
    spinner.style.display = 'block';
    
    const oriText = analyzeBtn.innerHTML;
    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            updateUI(result.prediction, result.confidence);
        } else {
            console.error('Prediction failed:', result.message);
            alert('Prediction error: ' + (result.message || 'Unknown error'));
        }
    } catch (err) {
        console.error('API Error:', err);
        alert('Network error: Could not reach the detection API. Check if server is running.');
    } finally {
        spinner.style.display = 'none';
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = oriText;
    }
}

// Update the UI with prediction results
function updateUI(prediction, confidence) {
    predictionLabel.textContent = prediction;
    predictionLabel.className = 'prediction-value ' + (prediction === 'Sober' ? 'state-sober' : 'state-intoxicated');
    
    const confScore = (confidence * 100).toFixed(1);
    confidencePercentage.textContent = confScore + '%';
    confidenceBar.style.width = confScore + '%';
    
    // Update message based on status
    if (prediction === 'Sober') {
        predictionMsg.textContent = 'Safe to operate equipment/vehicles. Sobriety confirmed.';
    } else {
        predictionMsg.textContent = 'Alert! Potential safety hazard detected. Take immediate action.';
    }
}

startWebcamBtn.addEventListener('click', startWebcam);
captureBtn.addEventListener('click', analyzeFrame);
