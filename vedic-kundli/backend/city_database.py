"""
Vedic Kundli - Comprehensive Global & Pan-India Cities, Towns & Villages Database.
Contains:
1. All 800+ District Headquarters & Municipalities across all 28 States and 8 Union Territories of India.
2. Major Tehsils, Talukas, Mandals, Historical and Pilgrimage Towns.
3. Top International Metros & Global Hubs.
4. Dynamic OpenStreetMap (Nominatim) Geocoding with Persistent Local Cache for any remote village or hamlet.
"""

import os
import json
import urllib.request
import urllib.parse
from typing import List, Dict, Any

# Path for persistent geocache
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
GEOCACHE_FILE = os.path.join(DATA_DIR, "geocache.json")

# In-memory geocache
_GEOCACHE: Dict[str, List[Dict[str, Any]]] = {}

def _init_geocache():
    global _GEOCACHE
    try:
        if os.path.exists(GEOCACHE_FILE):
            with open(GEOCACHE_FILE, "r", encoding="utf-8") as f:
                _GEOCACHE = json.load(f)
    except Exception:
        _GEOCACHE = {}

def _save_to_geocache(key: str, results: List[Dict[str, Any]]):
    global _GEOCACHE
    _GEOCACHE[key] = results
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(GEOCACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(_GEOCACHE, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

# Initialize cache on module load
_init_geocache()

# --- TOP POPULAR INDIAN CITIES & METROS ---
POPULAR_CITIES: List[Dict[str, Any]] = [
    {"city": "New Delhi", "state": "Delhi", "country": "India", "lat": 28.6139, "lon": 77.2090, "tz": 5.5},
    {"city": "Mumbai", "state": "Maharashtra", "country": "India", "lat": 19.0760, "lon": 72.8777, "tz": 5.5},
    {"city": "Bengaluru", "state": "Karnataka", "country": "India", "lat": 12.9716, "lon": 77.5946, "tz": 5.5},
    {"city": "Kolkata", "state": "West Bengal", "country": "India", "lat": 22.5726, "lon": 88.3639, "tz": 5.5},
    {"city": "Chennai", "state": "Tamil Nadu", "country": "India", "lat": 13.0827, "lon": 80.2707, "tz": 5.5},
    {"city": "Hyderabad", "state": "Telangana", "country": "India", "lat": 17.3850, "lon": 78.4867, "tz": 5.5},
    {"city": "Pune", "state": "Maharashtra", "country": "India", "lat": 18.5204, "lon": 73.8567, "tz": 5.5},
    {"city": "Ahmedabad", "state": "Gujarat", "country": "India", "lat": 23.0225, "lon": 72.5714, "tz": 5.5},
    {"city": "Jaipur", "state": "Rajasthan", "country": "India", "lat": 26.9124, "lon": 75.7873, "tz": 5.5},
    {"city": "Lucknow", "state": "Uttar Pradesh", "country": "India", "lat": 26.8467, "lon": 80.9462, "tz": 5.5},
    {"city": "Varanasi (Kashi / Banaras)", "state": "Uttar Pradesh", "country": "India", "lat": 25.3176, "lon": 82.9739, "tz": 5.5},
    {"city": "Patna", "state": "Bihar", "country": "India", "lat": 25.5941, "lon": 85.1376, "tz": 5.5},
    {"city": "Bhopal", "state": "Madhya Pradesh", "country": "India", "lat": 23.2599, "lon": 77.4126, "tz": 5.5},
    {"city": "Indore", "state": "Madhya Pradesh", "country": "India", "lat": 22.7196, "lon": 75.8577, "tz": 5.5},
    {"city": "Chandigarh", "state": "Chandigarh", "country": "India", "lat": 30.7333, "lon": 76.7794, "tz": 5.5},
    {"city": "Amritsar", "state": "Punjab", "country": "India", "lat": 31.6340, "lon": 74.8723, "tz": 5.5},
    {"city": "Surat", "state": "Gujarat", "country": "India", "lat": 21.1702, "lon": 72.8311, "tz": 5.5},
    {"city": "Nagpur", "state": "Maharashtra", "country": "India", "lat": 21.1458, "lon": 79.0882, "tz": 5.5},
    {"city": "Kanpur", "state": "Uttar Pradesh", "country": "India", "lat": 26.4499, "lon": 80.3319, "tz": 5.5},
    {"city": "Prayagraj (Allahabad)", "state": "Uttar Pradesh", "country": "India", "lat": 25.4358, "lon": 81.8463, "tz": 5.5},
    {"city": "Ayodhya", "state": "Uttar Pradesh", "country": "India", "lat": 26.7922, "lon": 82.1998, "tz": 5.5},
    {"city": "Ujjain", "state": "Madhya Pradesh", "country": "India", "lat": 23.1765, "lon": 75.7885, "tz": 5.5},
    {"city": "Mathura", "state": "Uttar Pradesh", "country": "India", "lat": 27.4924, "lon": 77.6737, "tz": 5.5},
    {"city": "Haridwar", "state": "Uttarakhand", "country": "India", "lat": 29.9457, "lon": 78.1642, "tz": 5.5},
    {"city": "Rishikesh", "state": "Uttarakhand", "country": "India", "lat": 30.0869, "lon": 78.2676, "tz": 5.5},
    {"city": "Tirupati", "state": "Andhra Pradesh", "country": "India", "lat": 13.6288, "lon": 79.4192, "tz": 5.5},
    {"city": "Puri", "state": "Odisha", "country": "India", "lat": 19.8135, "lon": 85.8312, "tz": 5.5},
    {"city": "Kochi (Cochin)", "state": "Kerala", "country": "India", "lat": 9.9312, "lon": 76.2673, "tz": 5.5},
    {"city": "Thiruvananthapuram (Trivandrum)", "state": "Kerala", "country": "India", "lat": 8.5241, "lon": 76.9366, "tz": 5.5},
    {"city": "Guwahati", "state": "Assam", "country": "India", "lat": 26.1445, "lon": 91.7362, "tz": 5.5},
    {"city": "Bhubaneswar", "state": "Odisha", "country": "India", "lat": 20.2961, "lon": 85.8245, "tz": 5.5},
    {"city": "Dehradun", "state": "Uttarakhand", "country": "India", "lat": 30.3165, "lon": 78.0322, "tz": 5.5},
    {"city": "Ranchi", "state": "Jharkhand", "country": "India", "lat": 23.3441, "lon": 85.3096, "tz": 5.5},
    {"city": "Raipur", "state": "Chhattisgarh", "country": "India", "lat": 21.2514, "lon": 81.6296, "tz": 5.5},
    {"city": "Srinagar", "state": "Jammu and Kashmir", "country": "India", "lat": 34.0837, "lon": 74.7973, "tz": 5.5},
    {"city": "Shimla", "state": "Himachal Pradesh", "country": "India", "lat": 31.1048, "lon": 77.1734, "tz": 5.5},
    {"city": "Gaya", "state": "Bihar", "country": "India", "lat": 24.7914, "lon": 85.0002, "tz": 5.5},
    {"city": "Coimbatore", "state": "Tamil Nadu", "country": "India", "lat": 11.0168, "lon": 76.9558, "tz": 5.5},
    {"city": "Madurai", "state": "Tamil Nadu", "country": "India", "lat": 9.9252, "lon": 78.1198, "tz": 5.5},
    {"city": "Mysuru (Mysore)", "state": "Karnataka", "country": "India", "lat": 12.2958, "lon": 76.6394, "tz": 5.5},
    {"city": "Agra", "state": "Uttar Pradesh", "country": "India", "lat": 27.1767, "lon": 78.0081, "tz": 5.5},
    {"city": "Jodhpur", "state": "Rajasthan", "country": "India", "lat": 26.2389, "lon": 73.0243, "tz": 5.5},
    {"city": "Udaipur", "state": "Rajasthan", "country": "India", "lat": 24.5854, "lon": 73.7125, "tz": 5.5},
    {"city": "Shirdi", "state": "Maharashtra", "country": "India", "lat": 19.7667, "lon": 74.4767, "tz": 5.5},
    {"city": "Rameswaram", "state": "Tamil Nadu", "country": "India", "lat": 9.2876, "lon": 79.3129, "tz": 5.5},
    {"city": "Bodh Gaya", "state": "Bihar", "country": "India", "lat": 24.6961, "lon": 84.9869, "tz": 5.5},
    {"city": "Kedarnath", "state": "Uttarakhand", "country": "India", "lat": 30.7352, "lon": 79.0669, "tz": 5.5},
    {"city": "Badrinath", "state": "Uttarakhand", "country": "India", "lat": 30.7433, "lon": 79.4938, "tz": 5.5},
    {"city": "Dwarka", "state": "Gujarat", "country": "India", "lat": 22.2442, "lon": 68.9685, "tz": 5.5},
    {"city": "Somnath", "state": "Gujarat", "country": "India", "lat": 20.8880, "lon": 70.4014, "tz": 5.5},
]

# --- INTERNATIONAL HUBS ---
INTERNATIONAL_CITIES: List[Dict[str, Any]] = [
    {"city": "London", "state": "England", "country": "United Kingdom", "lat": 51.5074, "lon": -0.1278, "tz": 0.0},
    {"city": "New York", "state": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060, "tz": -5.0},
    {"city": "San Francisco", "state": "California", "country": "USA", "lat": 37.7749, "lon": -122.4194, "tz": -8.0},
    {"city": "Chicago", "state": "Illinois", "country": "USA", "lat": 41.8781, "lon": -87.6298, "tz": -6.0},
    {"city": "Dallas", "state": "Texas", "country": "USA", "lat": 32.7767, "lon": -96.7970, "tz": -6.0},
    {"city": "Houston", "state": "Texas", "country": "USA", "lat": 29.7604, "lon": -95.3698, "tz": -6.0},
    {"city": "Seattle", "state": "Washington", "country": "USA", "lat": 47.6062, "lon": -122.3321, "tz": -8.0},
    {"city": "Toronto", "state": "Ontario", "country": "Canada", "lat": 43.6532, "lon": -79.3832, "tz": -5.0},
    {"city": "Vancouver", "state": "British Columbia", "country": "Canada", "lat": 49.2827, "lon": -123.1207, "tz": -8.0},
    {"city": "Dubai", "state": "Dubai", "country": "United Arab Emirates", "lat": 25.2048, "lon": 55.2708, "tz": 4.0},
    {"city": "Abu Dhabi", "state": "Abu Dhabi", "country": "United Arab Emirates", "lat": 24.4539, "lon": 54.3773, "tz": 4.0},
    {"city": "Singapore", "state": "Singapore", "country": "Singapore", "lat": 1.3521, "lon": 103.8198, "tz": 8.0},
    {"city": "Kuala Lumpur", "state": "Federal Territory", "country": "Malaysia", "lat": 3.1390, "lon": 101.6869, "tz": 8.0},
    {"city": "Sydney", "state": "New South Wales", "country": "Australia", "lat": -33.8688, "lon": 151.2093, "tz": 10.0},
    {"city": "Melbourne", "state": "Victoria", "country": "Australia", "lat": -37.8136, "lon": 144.9631, "tz": 10.0},
    {"city": "Auckland", "state": "Auckland", "country": "New Zealand", "lat": -36.8485, "lon": 174.7633, "tz": 12.0},
    {"city": "Kathmandu", "state": "Bagmati", "country": "Nepal", "lat": 27.7172, "lon": 85.3240, "tz": 5.75},
    {"city": "Colombo", "state": "Western", "country": "Sri Lanka", "lat": 6.9271, "lon": 79.8612, "tz": 5.5},
    {"city": "Dhaka", "state": "Dhaka", "country": "Bangladesh", "lat": 23.8103, "lon": 90.4125, "tz": 6.0},
    {"city": "Port Louis", "state": "Black River", "country": "Mauritius", "lat": -20.1609, "lon": 57.5012, "tz": 4.0},
    {"city": "Bangkok", "state": "Bangkok", "country": "Thailand", "lat": 13.7563, "lon": 100.5018, "tz": 7.0},
    {"city": "Tokyo", "state": "Tokyo", "country": "Japan", "lat": 35.6762, "lon": 139.6503, "tz": 9.0},
    {"city": "Berlin", "state": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050, "tz": 1.0},
    {"city": "Paris", "state": "Île-de-France", "country": "France", "lat": 48.8566, "lon": 2.3522, "tz": 1.0},
]

# Import the 871 verified Indian locations from build_cities
try:
    from build_cities import INDIA_PLACES
    ALL_INDIAN_LOCATIONS: List[Dict[str, Any]] = [
        {"city": p[0], "state": f"{p[1]}, {p[2]}", "country": "India", "lat": p[3], "lon": p[4], "tz": 5.5}
        for p in INDIA_PLACES
    ]
except Exception:
    ALL_INDIAN_LOCATIONS = []


def _fetch_nominatim_geocoding(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Live geocoding fallback via OpenStreetMap Nominatim for small villages and remote areas.
    Active when connected to the internet (e.g. deployed on Render).
    """
    q_clean = query.strip()
    if not q_clean or len(q_clean) < 3:
        return []

    # Check cache first
    cache_key = q_clean.lower()
    if cache_key in _GEOCACHE:
        return _GEOCACHE[cache_key][:limit]

    encoded_q = urllib.parse.quote(f"{q_clean}, India")
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_q}&countrycodes=in&format=json&addressdetails=1&limit={limit}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "VedicKundliGeocodingEngine/2.0 (Astrology Portal)"}
    )

    results: List[Dict[str, Any]] = []
    try:
        with urllib.request.urlopen(req, timeout=2.0) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for item in data:
                addr = item.get("address", {})
                name = (
                    addr.get("village")
                    or addr.get("town")
                    or addr.get("city")
                    or addr.get("suburb")
                    or addr.get("hamlet")
                    or item.get("name", q_clean.title())
                )
                district = addr.get("county") or addr.get("state_district") or ""
                state = addr.get("state", "India")
                display_state = f"{district}, {state}" if district else state
                
                lat = round(float(item["lat"]), 4)
                lon = round(float(item["lon"]), 4)

                results.append({
                    "city": name,
                    "state": display_state,
                    "country": "India",
                    "lat": lat,
                    "lon": lon,
                    "tz": 5.5
                })

        if results:
            _save_to_geocache(cache_key, results)
    except Exception:
        # Graceful fallback when offline or sandboxed
        pass

    return results


def search_cities(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Multi-tiered Search:
    1. Popular cities & Metros
    2. Comprehensive Pan-India 870+ Districts & Towns Database
    3. International Hubs
    4. Cached Remote Villages
    5. Real-Time OpenStreetMap Geocoding for any obscure village / hamlet across India
    """
    q = query.strip().lower()
    if not q:
        return POPULAR_CITIES[:limit]

    matches = []
    seen = set()

    def add_match(item, score):
        # Unique identifier by rounded coordinates or name+state
        uid = f"{item['city']}_{item.get('state', '')}_{item.get('country', '')}".lower()
        if uid not in seen:
            seen.add(uid)
            matches.append((score, item))

    # Tier 1: Match against POPULAR_CITIES
    for item in POPULAR_CITIES:
        c_name = item["city"].lower()
        full_name = f"{item['city']} {item.get('state', '')} {item['country']}".lower()
        if c_name.startswith(q):
            add_match(item, 100)
        elif q in c_name:
            add_match(item, 85)
        elif q in full_name:
            add_match(item, 70)

    # Tier 2: Match against ALL_INDIAN_LOCATIONS (870+ districts & towns)
    for item in ALL_INDIAN_LOCATIONS:
        c_name = item["city"].lower()
        full_name = f"{item['city']} {item.get('state', '')} {item['country']}".lower()
        if c_name.startswith(q):
            add_match(item, 95)
        elif q in c_name:
            add_match(item, 80)
        elif q in full_name:
            add_match(item, 65)

    # Tier 3: Match against INTERNATIONAL_CITIES
    for item in INTERNATIONAL_CITIES:
        c_name = item["city"].lower()
        full_name = f"{item['city']} {item.get('state', '')} {item['country']}".lower()
        if c_name.startswith(q):
            add_match(item, 90)
        elif q in c_name:
            add_match(item, 75)
        elif q in full_name:
            add_match(item, 60)

    # Tier 4: Check geocache for previously searched small villages
    for cached_query, cached_list in _GEOCACHE.items():
        if q in cached_query or cached_query.startswith(q):
            for item in cached_list:
                add_match(item, 78)

    # Sort matches by score descending
    matches.sort(key=lambda x: x[0], reverse=True)
    res = [m[1] for m in matches[:limit]]

    # Tier 5: If fewer than limit results found and query has length >= 3,
    # invoke live OpenStreetMap geocoding (works on Render / cloud)
    if len(res) < limit and len(q) >= 3:
        live_results = _fetch_nominatim_geocoding(query, limit=limit - len(res))
        for item in live_results:
            uid = f"{item['city']}_{item.get('state', '')}_{item.get('country', '')}".lower()
            if uid not in seen:
                seen.add(uid)
                res.append(item)

    return res[:limit]
