# Import FastAPI - the main framework for building our web API
from fastapi import FastAPI, HTTPException
# Import HTMLResponse - allows us to return HTML content to the browser
from fastapi.responses import HTMLResponse
# Import StaticFiles - for serving static files like CSS and JavaScript
from fastapi.staticfiles import StaticFiles
# Import BaseModel from Pydantic - used for data validation and defining request/response models
from pydantic import BaseModel
# Import transformers library components - these handle loading and using the AI model
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# Import torch - PyTorch deep learning framework (needed for the model to run)
import torch
# Import uvicorn - ASGI server that runs our FastAPI application
import uvicorn

# Create an instance of FastAPI application with a custom title
# This title will appear in the auto-generated API documentation
app = FastAPI(title="TinyLlama Chat API")

# Mount the static files directory so FastAPI can serve CSS and JS files
# Any file in the "static" folder will be accessible at the "/static" URL path
# name="static" is just an internal identifier for this mount
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a Pydantic model for the request body
# This ensures that POST requests to /ask must include a "question" field with string data
class Question(BaseModel):
    question: str  # The user's question as a string

# Print a message to console indicating the model loading process has started
print("Loading model...")

# Define which model we want to use from Hugging Face's model hub
# TinyLlama is a small (1.1B parameters) language model optimized for chat
huggingface_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load the pre-trained model from Hugging Face
# AutoModelForCausalLM automatically selects the right model architecture
# from_pretrained downloads the model files if not already cached locally
model = AutoModelForCausalLM.from_pretrained(huggingface_model)

# Load the tokenizer for this model
# Tokenizer converts text into numbers (tokens) that the model can understand
# It also converts the model's output numbers back into readable text
tokenizer = AutoTokenizer.from_pretrained(huggingface_model)

# Move model to MPS device if available for GPU acceleration
if torch.backends.mps.is_available():
    device = torch.device("mps")
    model = model.to(device)
    print("Device set to use mps")
else:
    device = torch.device("cpu")
    print("Device set to use cpu")

# Create a text generation pipeline - this simplifies using the model
# Pipeline handles tokenization, model inference, and decoding automatically
text_generator = pipeline(
    "text-generation",  # Specifies we want to generate text (not classify, translate, etc.)
    model=model,  # Pass in our loaded model
    tokenizer=tokenizer,  # Pass in our loaded tokenizer
    device=device  # Explicitly pass the device
)

# Print confirmation that the model loaded successfully
print("Model loaded successfully!")

# Define a route for the root URL ("/") that returns HTML
# The @app.get decorator means this function handles GET requests to "/"
# response_class=HTMLResponse tells FastAPI we're returning HTML, not JSON
@app.get("/", response_class=HTMLResponse)
async def home():
    # Open and read the HTML file from the templates folder
    # "r" means read mode
    with open("templates/index.html", "r") as f:
        # Read the entire file content and return it
        # This HTML will be rendered in the user's browser
        return f.read()

# Define a route for "/ask" that accepts POST requests
# This is where users send their questions to get AI responses
@app.post("/ask")
async def ask(question_data: Question):
    # Check if the question field is empty or just whitespace
    if not question_data.question:
        # If empty, raise an HTTP 400 Bad Request error with a message
        raise HTTPException(status_code=400, detail="No question provided")
    
    # Use try-except to catch any errors during text generation
    try:
        # Generate a response using our text generation pipeline
        response = text_generator(
            question_data.question,  # The user's input question
            max_new_tokens=50,  # Generate up to 50 new tokens (reduced for speed)
            do_sample=True,  # Use sampling instead of greedy decoding for more varied responses
            temperature=0.2,  # Controls randomness: 0.7 is balanced (lower=more focused, higher=more creative)
            pad_token_id=tokenizer.eos_token_id  # Prevent warnings about padding
        )
        
        # Extract the generated text from the response
        # response is a list, we take the first item [0]
        # Then get the 'generated_text' field which contains the complete output
        answer = response[0]['generated_text']
        
        # Return the answer as a JSON object
        # FastAPI automatically converts this Python dict to JSON
        return {"answer": answer}
    
    # If anything goes wrong during generation, catch the exception
    except Exception as e:
        # Raise an HTTP 500 Internal Server Error with details about what went wrong
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

# Define a health check endpoint - useful for monitoring if the service is running
# GET request to "/health" returns the service status
@app.get("/health")
async def health():
    # Return a simple JSON response indicating the service is healthy
    # Also includes which model is loaded
    return {"status": "healthy", "model": huggingface_model}

# This block only runs if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the uvicorn server to run our FastAPI app
    # app is our FastAPI instance
    # host="127.0.0.1" means only accept connections from this computer (localhost)
    # port=8000 means the server listens on port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)