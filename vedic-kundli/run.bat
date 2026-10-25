@echo off
title Vedic Kundli Portal
echo ===================================================
echo             VEDIC KUNDLI PORTAL
echo   Precision Ephemeris & Jyotish Birth Chart
echo ===================================================
echo Starting FastAPI server at http://127.0.0.1:8000 ...

start "" http://127.0.0.1:8000
py -3.12 -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
pause
