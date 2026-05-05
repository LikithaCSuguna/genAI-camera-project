import os
from google import genai
from google.genai import types
from PIL import Image
import supervision as sv



API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Error: GOOGLE_API_KEY not set.")
    print("Run: export GOOGLE_API_KEY='your_api_key'")
    exit()

# Initialize client
client = genai.Client(api_key=API_KEY)

# Model name
MODEL_NAME = "gemini-1.5-flash"


IMAGE_PATH = "capture_image.png"

# Prompt
PROMPT = "Detect the objects in this image and return a list."

# Load image
try:
    image = Image.open(IMAGE_PATH)
except FileNotFoundError:
    print(f"Error: {IMAGE_PATH} not found.")
    exit()

# Generate response
response = client.models.generate_content(
    model=MODEL_NAME,
    contents=[
        PROMPT,
        image
    ]
)

# Print result
print("\n🔍 Detected Objects:")
print(response.text)
