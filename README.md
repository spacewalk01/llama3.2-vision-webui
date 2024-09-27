---

# Gradio WebUI for Llama-3.2-Vision Model 

<p align="center">
  <img src="./data/image1.png" alt="Llama 3.2 Vision Model" />
</p>

This project uses the Llama-3.2-Vision model to generate text responses from images and text prompts, with a user-friendly web ui interface built using Gradio.

## Requirements

- `gradio`
- `torch`
- `Pillow`
- `transformers`
- `huggingface_hub`

## Getting Started

1. **Get a Hugging Face Token**  
   - Sign up for an account [here](https://huggingface.co/join).
   - Get your token from [your settings](https://huggingface.co/settings/tokens).

2. **Project Setup**  
   - Clone the repository:  
     ```bash
     git clone https://github.com/spacewalk01/llama3.2-vision-webui.git
     cd llama3.2-vision-webui
     ```
   - Install the required dependencies:  
     ```bash
     pip install gradio torch Pillow transformers huggingface_hub
     ```

3. **Run the Application**  
   - Start the Gradio interface by running:  
     ```bash
     python main.py --token Your_Hugging_Face_Token
     ```  
   - Access the local URL to upload images and prompts, and view the Llama 3.2 Vision model's responses.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
