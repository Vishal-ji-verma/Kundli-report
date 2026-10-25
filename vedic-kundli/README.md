# 🕉️ Vedic Kundli Portal (वैदिक जन्म कुण्डली)

An authentic, high-precision Vedic Astrology (Jyotish) birth chart generator and astrological portal built with **FastAPI**, **PyEphem astronomical engine**, and **interactive vector SVG charts** supporting both **North Indian (Diamond)** and **South Indian (Fixed-Zodiac Box)** traditions.

---

## 🌟 Key Features

1. **Dual Chart Visualizations (Live Toggle)**:
   - **North Indian Diamond Chart**: Fixed houses (H1 to H12) with rotating zodiac signs and planetary placements.
   - **South Indian Box Chart**: Fixed clockwise zodiac signs (Pisces to Aquarius) with Lagna indicator.
   - **D1 (Lagna / Rasi Chart)**: Physical life, personality, general fortune.
   - **D9 (Navamsha Chart)**: Dharma, marital compatibility, inner soul strength.

2. **Astronomical & Vedic Accuracy**:
   - **Chitrapaksha / Lahiri Ayanamsha**: Official standard Indian astronomical ephemeris model.
   - **True Sidereal Ascendant (Lagna)**: Computed from Local Sidereal Time (RAMC) and geographic latitude.
   - **All 9 Vedic Grahas**: Sun (Surya), Moon (Chandra), Mars (Mangal), Mercury (Budha), Jupiter (Guru), Venus (Shukra), Saturn (Shani), Rahu (North Node), Ketu (South Node).
   - **Retrograde Detection (Vakri)**: Real-time velocity and motion tracking.
   - **Dignity Evaluation**: Exalted (Uccha), Debilitated (Neecha), Own Sign (Swakshetra), Neutral.

3. **Vimshottari Dasha 120-Year Timeline**:
   - Calculates the exact starting birth dasha based on Moon's Nakshatra and elapsed degrees.
   - Detailed breakdown of all 9 Mahadashas and sub-periods (Antardashas) with dates.

4. **Complete Vedic Panchang**:
   - **Tithi**: Lunar phase and paksha (Shukla / Krishna).
   - **Vaar**: Weekday and planetary ruler.
   - **Nakshatra**: 27 lunar mansions and Pada (1 to 4).
   - **Yoga**: 27 solar-lunar longitudes sum yogas.
   - **Karana**: Half-tithi intervals (rotating movable and fixed karanas).

5. **Manglik Dosha (Kuja Dosha) Analysis**:
   - Analyzes Mars in houses 1, 2, 4, 7, 8, and 12.
   - Evaluates classical cancellation yogas (own sign, exaltation, Jupiter aspects).
   - Provides severity rating and traditional Vedic remedies.

6. **Instant City Coordinate Autocomplete**:
   - Built-in database of Indian state capitals, pilgrimage centers, and global cities.
   - Automatically sets latitude, longitude, and timezone offsets.

7. **Print / PDF Report Ready**:
   - Optimized print CSS (`@media print`) creates a clean multi-page Vedic horoscope booklet.

---


## 📁 Project Architecture

```
vedic-kundli/
├── backend/
│   ├── astro_engine.py      # Core Jyotish & ephemeris calculations
│   ├── city_database.py     # Curated Indian & world cities database
│   └── main.py              # FastAPI server & static file router
├── frontend/
│   ├── index.html           # Main HTML5 UI structure
│   ├── style.css            # Celestial theme & print formatting
│   └── app.js               # SVG renderers, form logic & tabs
├── requirements.txt         # Python dependencies
├── run.bat                  # One-click Windows launcher
└── README.md                # Project documentation
```
