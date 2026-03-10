from google  import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Make this global so all functions can use it
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_market(sector, news):
    try:
        prompt = f"""
        Analyze the Indian {sector} sector based on the following news:

        {news}

        Generate:
        - Market Trend
        - Top Opportunities
        - Risks
        - Investment Outlook
        """

        # use the global client
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("AI Analysis Error:", e)
        return f"Error generating AI report: {e}"