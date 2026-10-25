"""
FastAPI Server for Vedic Kundli Web Application.
Serves REST API endpoints and static frontend assets.
"""

import os
import sys

# Ensure backend directory is in sys.path for direct imports
BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from city_database import search_cities, POPULAR_CITIES
from astro_engine import compute_full_kundli
from astrologer_report import generate_professional_astrologer_report

app = FastAPI(
    title="Vedic Kundli Portal API",
    description="High-precision Vedic Astrology & Kundli Generation Engine",
    version="1.0.0"
)

# Enable CORS for local development and embedding
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class KundliRequest(BaseModel):
    name: str = Field(default="Seeker", description="Name of the person")
    gender: str = Field(default="Male", description="Gender (Male/Female/Other)")
    year: int = Field(..., ge=1800, le=2200, description="Birth year")
    month: int = Field(..., ge=1, le=12, description="Birth month")
    day: int = Field(..., ge=1, le=31, description="Birth day")
    hour: int = Field(..., ge=0, le=23, description="Birth hour (0-23)")
    minute: int = Field(..., ge=0, le=59, description="Birth minute (0-59)")
    second: int = Field(default=0, ge=0, le=59, description="Birth second (0-59)")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Birth place latitude")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Birth place longitude")
    timezone_offset: float = Field(default=5.5, ge=-12.0, le=14.0, description="UTC offset in hours")
    city_name: str = Field(default="Custom Location", description="City / Place name")


@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "Vedic Kundli API", "version": "1.0.0"}


@app.get("/api/cities")
def get_cities(q: Optional[str] = None, limit: int = 12):
    """Search autocomplete for cities with coordinates and timezones."""
    results = search_cities(q or "", limit=limit)
    return {"cities": results}


@app.post("/api/kundli")
def generate_kundli(req: KundliRequest):
    """Generate complete Vedic Kundli chart, planetary details, dashas, and panchang."""
    try:
        chart_data = compute_full_kundli(
            name=req.name,
            gender=req.gender,
            year=req.year,
            month=req.month,
            day=req.day,
            hour=req.hour,
            minute=req.minute,
            second=req.second,
            lat=req.latitude,
            lon=req.longitude,
            tz_offset=req.timezone_offset,
            city_name=req.city_name
        )
        # Attach comprehensive professional astrologer analysis report
        chart_data["astrologer_report"] = generate_professional_astrologer_report(chart_data)
        return chart_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Astrological calculation error: {str(e)}")


# Mount frontend directory for web access
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

if os.path.exists(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/")
    def serve_home():
        index_path = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_path):
            return FileResponse(
                index_path,
                headers={
                    "Cache-Control": "no-cache, no-store, must-revalidate",
                    "Pragma": "no-cache",
                    "Expires": "0"
                }
            )
        return {"message": "Vedic Kundli frontend index.html not found"}


if __name__ == "__main__":
    import uvicorn
    # Support dynamic PORT environment variable provided by cloud hosts like Render, Railway, etc.
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

