import gradio as gr
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, MllamaProcessor
from huggingface_hub import login
import argparse

# Function to log into Hugging Face
def login_huggingface(token: str):
    """Logs into Hugging Face using the provided token."""
    login(token=token)

# Function to load the model and processor
def load_model_and_processor(model_id: str):
    """Loads the specified model and processor from Hugging Face."""
    model = MllamaForConditionalGeneration.from_pretrained(
        model_id,
        device_map="auto", 
        torch_dtype=torch.bfloat16
    )
    processor = MllamaProcessor.from_pretrained(model_id)
    return model, processor

# Function to process the input for the Gradio interface
def process_input(image: Image.Image, text_input: str) -> str:
    """
    Processes the input image and text prompt to generate a response from the LLAMA 3.2 Vision model.
    
    Args:
    image (PIL.Image): The input image.
    text_input (str): The text prompt to accompany the image.
    
    Returns:
    str: The generated text from the model.
    """
    
    # Combine image and text input into the final prompt
    prompt = f"<|image|><|begin_of_text|>{text_input}"
    
    # Preprocess inputs for the model
    inputs = processor(image, prompt, return_tensors="pt").to(model.device)
    
    # Generate the model's output based on the inputs
    output = model.generate(**inputs, max_new_tokens=30)
    
    # Decode the generated output into readable text
    generated_text = processor.decode(output[0], skip_special_tokens=True)
    
    return generated_text

# Main execution
if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Run LLAMA 3.2 Vision model with Gradio.")
    parser.add_argument('--token', type=str, required=True, help='Hugging Face token for authentication.')
    args = parser.parse_args()

    # Log into Hugging Face
    login_huggingface(args.token)

    # Load model and processor
    model_id = "meta-llama/Llama-3.2-11B-Vision"
    model, processor = load_model_and_processor(model_id)

    # Define and set up the Gradio interface
    demo = gr.Interface(
        fn=process_input,  # Function that handles the inputs
        inputs=[
            gr.Image(type="pil", label="Input Image"),  # Image input
            gr.Textbox(label="Text Prompt")              # Text input box for prompt
        ], 
        outputs=gr.Textbox(label="Generated Output"),    # Output box for generated text
        title="LLAMA 3.2 Vision: Image & Text Understanding",  # Title for UI
        description="Upload an image and provide a text prompt. The LLAMA 3.2 Vision model will generate a response based on the combined inputs."
    )

    # Launch the interface
    demo.launch(share=False)
