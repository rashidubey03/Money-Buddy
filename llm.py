import os
from google import genai

# Initialize Gemini client
def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ Missing GEMINI_API_KEY. Please set it as an environment variable.")
    return genai.Client(api_key=api_key)

# Function to punch up roast text using Gemini
def punch_up_roast_gemini(roast_text: str) -> str:
    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Rewrite this roast in a short, funny Gen-Z savage style:\n\n{roast_text}"
        )
        if response and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        return roast_text  # fallback if Gemini doesn’t return
    except Exception as e:
        return f"[Gemini Error] {str(e)}"
