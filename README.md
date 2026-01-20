# 🤖 TinyLlama Chat Application

A full-stack web application that provides a chat interface for interacting with the TinyLlama AI language model locally. Built with FastAPI for the backend and vanilla JavaScript for the frontend, this project demonstrates how to deploy and serve a large language model (LLM) without relying on external APIs.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Local AI Processing**: Runs TinyLlama-1.1B language model entirely on your local machine
- **Real-time Chat Interface**: Interactive web UI for natural conversations with the AI
- **FastAPI Backend**: Modern, fast Python web framework with automatic API documentation
- **Apple Silicon Optimized**: Leverages MPS (Metal Performance Shaders) for GPU acceleration on M1/M2/M3 Macs
- **RESTful API**: Clean API endpoints that can be used independently or integrated into other applications
- **Auto-generated Documentation**: Interactive API docs available at `/docs` endpoint

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance web framework for building APIs
- **PyTorch**: Deep learning framework for running the AI model
- **Transformers**: Hugging Face library for loading pre-trained models
- **Uvicorn**: ASGI server for running the FastAPI application

### Frontend
- **HTML5**: Semantic markup for structure
- **CSS3**: Modern styling with gradients and animations
- **JavaScript (ES6+)**: Async/await for API communication

### AI Model
- **TinyLlama-1.1B-Chat**: Compact language model optimized for chat applications

## 📋 Prerequisites

- Python 3.8 or higher
- 8GB RAM minimum (16GB recommended for better performance)
- macOS (for MPS support) or any OS with CPU support

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tinyllama-chat.git
   cd tinyllama-chat
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python3 app.py
   ```

5. **Access the application**
   - Web Interface: Open your browser and navigate to `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`
   - Health Check: `http://localhost:8000/health`

## 📁 Project Structure

```
tinyllama-chat/
│
├── app.py                 # FastAPI backend with AI model integration
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/
│   └── index.html        # HTML structure for the chat interface
│
└── static/
    ├── style.css         # Styling and layout
    └── script.js         # Frontend logic and API calls
```

## 🔧 Configuration

### Model Settings (in `app.py`)

```python
# Change these parameters to adjust AI behavior:
max_length=150           # Maximum total response length
max_new_tokens=100       # Maximum tokens to generate
temperature=0.7          # Creativity (0.1-1.0, higher = more creative)
do_sample=True          # Enable sampling for varied responses
```

### Server Settings

```python
# In app.py, modify uvicorn.run():
host="127.0.0.1"        # Change to "0.0.0.0" to accept external connections
port=8000               # Change port if needed
```

## 📡 API Endpoints

### POST /ask
Send a question to the AI model

**Request Body:**
```json
{
  "question": "What is machine learning?"
}
```

**Response:**
```json
{
  "answer": "Machine learning is a subset of artificial intelligence..."
}
```

### GET /health
Check if the service is running

**Response:**
```json
{
  "status": "healthy",
  "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
}
```

## 💡 Usage Examples

### Using the Web Interface
1. Open `http://localhost:8000` in your browser
2. Type your question in the input field
3. Press Enter or click "Send"
4. View the AI's response in the chat window

### Using the API Programmatically

**Python:**
```python
import requests

response = requests.post(
    "http://localhost:8000/ask",
    json={"question": "Explain Python decorators"}
)
print(response.json()["answer"])
```

**cURL:**
```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is FastAPI?"}'
```

**JavaScript:**
```javascript
fetch('http://localhost:8000/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question: 'Tell me about AI' })
})
.then(res => res.json())
.then(data => console.log(data.answer));
```

## ⚡ Performance Considerations

- **First Run**: The model (~2.2GB) will be downloaded automatically on first run
- **Memory Usage**: Expect ~3-4GB RAM usage when the model is loaded
- **Response Time**: 2-5 seconds per response on M3 Mac (varies by hardware)
- **GPU Acceleration**: Automatically uses MPS on Apple Silicon Macs for faster inference

## 🐛 Troubleshooting

**Issue: "No module named 'transformers'"**
```bash
pip install transformers torch
```

**Issue: Model loading is slow**
- First-time download of ~2.2GB is normal
- Subsequent runs load from cache and are faster

**Issue: Out of memory errors**
- Reduce `max_length` and `max_new_tokens` in `app.py`
- Close other memory-intensive applications

**Issue: Port 8000 already in use**
- Change the port in `app.py`: `uvicorn.run(app, host="127.0.0.1", port=8001)`

## 🔮 Future Enhancements

- [ ] Add conversation history/context retention
- [ ] Implement streaming responses for real-time token generation
- [ ] Add user authentication
- [ ] Support for multiple AI models
- [ ] Docker containerization
- [ ] Add prompt templates for different use cases
- [ ] Implement rate limiting
- [ ] Add message export functionality

## 📝 Requirements.txt

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
transformers==4.35.0
torch==2.1.0
pydantic==2.5.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [TinyLlama](https://github.com/jzhang38/TinyLlama) for the pre-trained model
- [Hugging Face](https://huggingface.co/) for the Transformers library
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework

---

⭐ If you found this project helpful, please give it a star!