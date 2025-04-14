import os
import modal

# Provide your OpenAI key here or via an environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Create a Modal Stub (this groups all Modal functions and deployments)
stub = modal.Stub("my-modal-gpt")

# Define a custom Docker image to include needed Python libraries
# (If you need additional dependencies, just add them in pip_install)
image = modal.Image.debian_slim().pip_install("openai")

@stub.function(image=image)
def ask_gpt(prompt: str) -> str:
    import openai
    
    # Set your OpenAI API key
    openai.api_key = OPENAI_API_KEY
    
    # Call the ChatCompletion API (this is effectively what your original code did)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
