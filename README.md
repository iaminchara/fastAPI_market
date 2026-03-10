# Market AI Analysis API

This is a **FastAPI application** that analyzes market data and generates **Markdown reports** with trade opportunities for specific sectors in India. The AI analysis is powered by **Google Gemini API**.

---

## Features

- Fetches current news for a sector (e.g., technology, pharmaceuticals, agriculture)
- Uses AI to analyze market trends, opportunities, risks, and investment outlook
- Generates **Markdown reports** that can be saved as `.md` files
- API Key-based authentication for security
- Rate limiting to prevent abuse
- Fully documented with **Swagger UI**

---

## Folder Structure

```text
market_ai_api/
│
├── app/
│   ├── main.py                # FastAPI app
│   ├── routes.py              # Endpoint definitions
│   ├── services/
│   │      ├── data_collector.py      # Fetch news
│   │      ├── gemini_analyzer.py     # AI analysis
│   │      ├── report_generator.py    # Markdown generation
│   ├── security/
│   │      ├── auth.py                # API Key verification
│   │      ├── rate_limiter.py        # Limit requests per user/session
│   └── utils/
│          └── logger.py
│
├── requirements.txt
├── README.md
└── .env          # API keys (do not push to Git)




Setup Instructions
1.Clone the repository:

git clone <your-repo-url>
cd market_ai_api

2.Create and activate virtual environment:

 # macOS/Linux
 python -m venv venv
 source venv/bin/activate


3.Install dependencies:

 pip install -r requirements.txt

4.Create a .env file in the project root with your API keys:

 GEMINI_API_KEY=<your-gemini-api-key>

5.Run the FastAPI server:

 uvicorn app.main:app --reload --port 8001


⸻

API Usage

Endpoint

GET /analyze/{sector}

	•	Path Parameter: sector (example: technology, pharmaceuticals, agriculture)
	•	Header: x-api-key (your API key)

Example Request with Python

import requests

sector = "technology"
url = f"http://127.0.0.1:8001/analyze/{sector}"
headers = {"x-api-key": "mysecurekey"}

response = requests.get(url, headers=headers)

# Save Markdown report
with open(f"{sector}_report.md", "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved {sector}_report.md successfully!")


⸻

Response

The endpoint returns a Markdown report, example:

# Market Analysis Report

**Sector:** technology

**Date:** 2026-03-10 01:07:33

---

## AI Market Insights

- Market Trend: Indian technology sector shows moderate growth with increased AI adoption.
- Top Opportunities: Cloud computing startups, AI-enabled SaaS platforms, semiconductor investments.
- Risks: Global chip shortage, regulatory changes, cybersecurity threats.
- Investment Outlook: Positive long-term outlook with short-term volatility.

---

## Conclusion

This report was generated automatically using AI market analysis.



Security
	•	API Key authentication required via x-api-key header
	•	Rate limiting implemented per user/session to prevent abuse

⸻

API Documentation
	•	FastAPI provides built-in Swagger UI at:

http://127.0.0.1:8001/docs

	•	You can test endpoints, view parameters, and see response examples.



Notes
	•	Free-tier Gemini API may have quota limits (429 errors).
	•	For testing without quota, you can use a fake AI response.
	•	Ensure .env is not pushed to GitHub for security.

⸻

Optional Enhancements
	•	Append multiple reports into README.md automatically with timestamps
	•	Add PDF export for reports
	•	Schedule automatic daily updates using a cron job or task scheduler


