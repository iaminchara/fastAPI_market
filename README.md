# Market AI Analysis API

This is a **FastAPI application** that analyzes market data and generates **Markdown reports** with trade opportunities for specific sectors in India. The AI analysis is powered by **Google Gemini API**.

---

## Features
- Market Analysis: AI-powered analysis of Indian market sectors
- Real-time Data: Collects current market news and trends
- Multiple Sectors: Support for 10+ major Indian market sectors
- Security: API key authentication and rate limiting
- Structured Reports: Professional markdown-formatted analysis reports
- Session Tracking: Monitor API usage per client
- Uses AI to analyze market trends, opportunities, risks, and investment outlook
- Generates **Markdown reports** that can be saved as `.md` files
- Fully documented with **Swagger UI**

##Supported Sectors
- Technology (aliases: tech, it, software)
- Pharmaceuticals (aliases: pharma, healthcare, medicine)
- Agriculture (aliases: agri, farming, agro)
- Banking (aliases: banks, finance, financial)
- Automobile (aliases: auto, cars, automotive)
- Energy (aliases: power, oil, gas, renewable)
- Telecom (aliases: telecommunications, communication)
- Retail (aliases: consumer, ecommerce)
- Infrastructure (aliases: construction, real estate)
- Metals (aliases: mining, steel, iron)

  
## Tech Stack
- Backend: FastAPI
- AI Engine: Google Gemini API
- Data Source: DuckDuckGo Search
- Security: API Key Authentication
- Rate Limiting: SlowAPI
- Validation: Pydantic
- Storage: In-memory (no database required)

  
##  Installation
Prerequisites
Python 3.8+
Google Gemini API key (get one from Google AI Studio)

## Setup Steps

1.Clone the repository

git clone <repository-url>
cd Api

2. Create virtual environment

python -m venv venv

#Windows
venv\Scripts\activate

#Linux/Mac
source venv/bin/activate

3.Install dependencies

pip install -r requirements.txt

4. Configure environment variables

#Copy the example environment file
cp .env.example .env

#Edit .env file and add your Gemini API key
#GEMINI_API_KEY=your_actual_gemini_api_key_here

5.Update API key (optional)

Edit .env file to change the default API key from mysecretkey
Or set API_KEY=your_custom_api_key in .env

##  Running the Application

1. Development Mode
   
 python -m uvicorn app.main:app  --host 0.0.0.0 --port $PORT
 
Production Mode
python -m uvicorn main:app  --reload  --port 8001 

The API will be available at http://localhost:8001

## API Documentation
Once the server is running, visit:

Swagger UI: http://localhost:8001/docs

# API Usage

1. Authentication
All API requests require an API key in the header:

X-API-Key: mysecretkey

2. Endpoints
	1. Analyze Sector
	GET /analyze/{sector}

Example Request:

curl -X GET "http://localhost:8000/analyze/technology" \
  -H "X-API-Key: mysecretkey"
Example Response:

{
  "success": true,
  "sector": "technology",
  "report": "# Market Analysis Report\n\n## 📊 Sector Overview\n**Sector:** Technology\n**Analysis Date:** 2024-03-10 15:30:45 IST\n...",
  "session_requests": 1,
  "timestamp": "2024-03-10T10:00:45.123456"
}

2. Get Valid Sectors
GET /sectors

Example Request:

curl -X GET "http://localhost:8000/sectors" \
  -H "X-API-Key: mysecretkey"
  
3. Health Check
GET /

## Sample Analysis Report
The API generates comprehensive markdown reports including:

Market Overview: Current market conditions and size
Key Trends: Major trends shaping the sector
Investment Opportunities: Specific opportunities for investors
Risk Analysis: Key risks and challenges
Trade Opportunities: Actionable trade recommendations
Market Outlook: Short to medium term outlook

## Configuration
Environment Variables:

Variable					Description							Default
GEMINI_API_KEY				Google Gemini API key				Required
API_KEY						API authentication key				mysecretkey
DEFAULT_RATE_LIMIT			Rate limit for analysis endpoint	5/minute
LOG_LEVEL					Logging level						INFO
HOST						Server host							0.0.0.0
PORT						Server port							8001


## Rate Limiting

- Analysis endpoint: 5 requests per minute per IP
- Sectors endpoint: 10 requests per minute per IP

  
## Security Features
- API Key Authentication: All endpoints require valid API key
- Input Validation: Comprehensive validation of all inputs
- Rate Limiting: Prevents API abuse
- Session Tracking: Monitors usage per client
- Error Handling: Secure error responses

## Troubleshooting

# Common Issues:- 

1. "AI analysis failed: API key not configured"

	- Ensure GEMINI_API_KEY is set in .env file
	- Verify your Gemini API key is valid
2. "Invalid API key"

	- Check the X-API-Key header in your request
	- Verify the API key matches your configuration

3. "No recent market data found"

	- Check internet connectivity
	- Try again after a few minutes

 4. Rate limit exceeded

	- Wait before making additional requests
	- Current limit: 5 requests/minute for analysis




## Folder/project Structure
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


## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

















