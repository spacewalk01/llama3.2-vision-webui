---

# Gradio WebUI for Llama-3.2-Vision Model 

<p align="center">
  <img src="./data/image1.png" alt="Llama 3.2 Vision Model" />
</p>

This project uses the Llama-3.2-Vision model to generate text responses from images and text prompts, with a user-friendly interface built using Gradio.

## Requirements

Make sure you have the following dependencies installed:

- `gradio`
- `torch`
- `Pillow`
- `transformers`
- `huggingface_hub`

You can install these dependencies using pip:

```bash
pip install gradio torch Pillow transformers huggingface_hub
```

## Getting Started

### Hugging Face Token

To use the model, you'll need a Hugging Face account and a token. Follow these steps:

1. Sign up for a Hugging Face account [here](https://huggingface.co/join).
2. Obtain your access token from [your settings](https://huggingface.co/settings/tokens).

### Setting Up the Project

1. Clone this repository:

    ```bash
    git clone https://github.com/spacewalk01/llama3.2-vision-webui.git
    cd llama3.2-vision-webui
    ```

### Running the Application

To run the Gradio interface, execute the following command, replacing `"Your_Hugging_Face_Token"` with your actual Hugging Face token:

```bash
python main.py --token Your_Hugging_Face_Token
```

When the application starts, it shows a local URL for the demo. This opens a web interface where you can upload an image and add a text prompt, and the Llama 3.2 Vision model will generate a response.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
