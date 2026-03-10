from fastapi import FastAPI, Depends, HTTPException
from app.services.data_collector import get_market_news
from app.services.gemini_analyzer import analyze_market
from app.services.report_generator import generate_markdown
from app.security.auth import verify_api_key
from app.services.gemini_analyzer import analyze_market, client

app = FastAPI(debug=True)


@app.get("/analyze/{sector}")
async def analyze_sector(sector: str, api_key: str = Depends(verify_api_key)):
    try:
       news = get_market_news(sector)

       analysis = analyze_market(sector, news)

       markdown_report = generate_markdown(sector, analysis)

       return {
        "sector": sector,
        "report_markdown": markdown_report
       }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
     
    
