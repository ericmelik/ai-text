from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Model ID
huggingface_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load the model and tokenizer (downloads automatically)
model = AutoModelForCausalLM.from_pretrained(huggingface_model)
tokenizer = AutoTokenizer.from_pretrained(huggingface_model)

# Create a text generation pipeline
text_generator_pipeline = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer,
    max_length=100,
)

# Example usage
response = text_generator_pipeline("Hello, tell me a joke, please.")
print(response)



# from huggingface_hub import hf_hub_download
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# # Set huggingface API token
# HUGGING_FACE_API_TOKEN = "your_huggingface_api_token_here"

# # Model ID for llambda-3.2-1b model on Hugging Face
# huggingface_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0" # Replace with actual model ID if different

# # List of requierd files for the model
# required_files = [
#      "special_tokens_map.json",
#      "generation_config.json",
#      "tokenizer_config.json",
#      "model.safetensors",
#      "eval_results.json",
#      "tokenizer.model",
#      "tokenizer.json",
#      "config.json"
# ]

# # Download required files from Hugging Face Hub
# for file_name in required_files:
#     download_location = hf_hub_download(
#         repo_id=huggingface_model,
#         filename=file_name,
#         token=HUGGING_FACE_API_TOKEN
#     ) 
#     print(f"Downloaded {file_name} to {download_location}")

# # Load the model and tokenizer
# model = AutoModelForCausalLM.from_pretrained(huggingface_model) # Enable trust_remote_code for safetensors if needed
# tokenizer = AutoTokenizer.from_pretrained(huggingface_model)

# # Create a text generation pipeline
# text_generator_pipeline = pipeline(
#      "text-generation", 
#      model=model, 
#      tokenizer=tokenizer,
#      max_length=100,
# ) 

# # Example usage of the text generation pipeline
# response = text_generator_pipeline("Hello, how are you?")
# print(response)