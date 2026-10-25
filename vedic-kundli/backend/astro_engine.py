"""
Vedic Astrology (Jyotish) Calculation Engine.
Calculates high-precision Nirayana (Sidereal) planetary longitudes, Lahiri Ayanamsha,
Ascendant (Lagna), Bhavas, D1 Rasi, D9 Navamsha, Vimshottari Dashas, Panchang, and Manglik Dosha.
"""

import math
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import ephem

# ----------------- Astronomical & Vedic Constants -----------------

ZODIAC_SIGNS = [
    {"id": 1, "name": "Aries", "sanskrit": "Mesha", "hindi": "मेष", "lord": "Mars", "element": "Fire"},
    {"id": 2, "name": "Taurus", "sanskrit": "Vrishabha", "hindi": "वृषभ", "lord": "Venus", "element": "Earth"},
    {"id": 3, "name": "Gemini", "sanskrit": "Mithuna", "hindi": "मिथुन", "lord": "Mercury", "element": "Air"},
    {"id": 4, "name": "Cancer", "sanskrit": "Karka", "hindi": "कर्क", "lord": "Moon", "element": "Water"},
    {"id": 5, "name": "Leo", "sanskrit": "Simha", "hindi": "सिंह", "lord": "Sun", "element": "Fire"},
    {"id": 6, "name": "Virgo", "sanskrit": "Kanya", "hindi": "कन्या", "lord": "Mercury", "element": "Earth"},
    {"id": 7, "name": "Libra", "sanskrit": "Tula", "hindi": "तुला", "lord": "Venus", "element": "Air"},
    {"id": 8, "name": "Scorpio", "sanskrit": "Vrishchika", "hindi": "वृश्चिक", "lord": "Mars", "element": "Water"},
    {"id": 9, "name": "Sagittarius", "sanskrit": "Dhanu", "hindi": "धनु", "lord": "Jupiter", "element": "Fire"},
    {"id": 10, "name": "Capricorn", "sanskrit": "Makara", "hindi": "मकर", "lord": "Saturn", "element": "Earth"},
    {"id": 11, "name": "Aquarius", "sanskrit": "Kumbha", "hindi": "कुम्भ", "lord": "Saturn", "element": "Air"},
    {"id": 12, "name": "Pisces", "sanskrit": "Meena", "hindi": "मीन", "lord": "Jupiter", "element": "Water"}
]

NAKSHATRAS = [
    {"id": 1, "name": "Ashwini", "lord": "Ketu"},
    {"id": 2, "name": "Bharani", "lord": "Venus"},
    {"id": 3, "name": "Krittika", "lord": "Sun"},
    {"id": 4, "name": "Rohini", "lord": "Moon"},
    {"id": 5, "name": "Mrigashira", "lord": "Mars"},
    {"id": 6, "name": "Ardra", "lord": "Rahu"},
    {"id": 7, "name": "Punarvasu", "lord": "Jupiter"},
    {"id": 8, "name": "Pushya", "lord": "Saturn"},
    {"id": 9, "name": "Ashlesha", "lord": "Mercury"},
    {"id": 10, "name": "Magha", "lord": "Ketu"},
    {"id": 11, "name": "Purva Phalguni", "lord": "Venus"},
    {"id": 12, "name": "Uttara Phalguni", "lord": "Sun"},
    {"id": 13, "name": "Hasta", "lord": "Moon"},
    {"id": 14, "name": "Chitra", "lord": "Mars"},
    {"id": 15, "name": "Swati", "lord": "Rahu"},
    {"id": 16, "name": "Vishakha", "lord": "Jupiter"},
    {"id": 17, "name": "Anuradha", "lord": "Saturn"},
    {"id": 18, "name": "Jyeshtha", "lord": "Mercury"},
    {"id": 19, "name": "Mula", "lord": "Ketu"},
    {"id": 20, "name": "Purva Ashadha", "lord": "Venus"},
    {"id": 21, "name": "Uttara Ashadha", "lord": "Sun"},
    {"id": 22, "name": "Shravana", "lord": "Moon"},
    {"id": 23, "name": "Dhanishta", "lord": "Mars"},
    {"id": 24, "name": "Shatabhisha", "lord": "Rahu"},
    {"id": 25, "name": "Purva Bhadrapada", "lord": "Jupiter"},
    {"id": 26, "name": "Uttara Bhadrapada", "lord": "Saturn"},
    {"id": 27, "name": "Revati", "lord": "Mercury"}
]

VIMSHOTTARI_LORDS = [
    ("Ketu", 7),
    ("Venus", 20),
    ("Sun", 6),
    ("Moon", 10),
    ("Mars", 7),
    ("Rahu", 18),
    ("Jupiter", 16),
    ("Saturn", 19),
    ("Mercury", 17)
]

YOGAS = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda", "Sukarma",
    "Dhriti", "Shoola", "Ganda", "Vriddhi", "Dhruva", "Vyaghata", "Harshana",
    "Vajra", "Siddhi", "Vyatipata", "Variyan", "Parigha", "Shiva", "Siddha",
    "Sadhya", "Shubha", "Shukla", "Brahma", "Indra", "Vaidhriti"
]

KARANAS = [
    "Bava", "Balava", "Kaulava", "Taitila", "Gara", "Vanija", "Vishti (Bhadra)",
    "Shakuni", "Chatushpada", "Naga", "Kintughna"
]

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shasthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shasthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
]

PLANET_EXALTATION_DEBILITATION = {
    "Sun": {"exalted_sign": 1, "exalted_deg": 10, "debilitated_sign": 7, "own_signs": [5]},
    "Moon": {"exalted_sign": 2, "exalted_deg": 3, "debilitated_sign": 8, "own_signs": [4]},
    "Mars": {"exalted_sign": 10, "exalted_deg": 28, "debilitated_sign": 4, "own_signs": [1, 8]},
    "Mercury": {"exalted_sign": 6, "exalted_deg": 15, "debilitated_sign": 12, "own_signs": [3, 6]},
    "Jupiter": {"exalted_sign": 4, "exalted_deg": 5, "debilitated_sign": 10, "own_signs": [9, 12]},
    "Venus": {"exalted_sign": 12, "exalted_deg": 27, "debilitated_sign": 6, "own_signs": [2, 7]},
    "Saturn": {"exalted_sign": 7, "exalted_deg": 20, "debilitated_sign": 1, "own_signs": [10, 11]},
    "Rahu": {"exalted_sign": 2, "exalted_deg": 15, "debilitated_sign": 8, "own_signs": [11]},
    "Ketu": {"exalted_sign": 8, "exalted_deg": 15, "debilitated_sign": 2, "own_signs": [8]}
}


def compute_lahiri_ayanamsha(jd: float) -> float:
    """Compute official Chitrapaksha / Lahiri Ayanamsha for Julian Day."""
    t = (jd - 2451545.0) / 36525.0
    # Standard IAU/Lahiri polynomial: 23°51'25.53" at J2000.0 + 50.2796" per year
    ayanamsha = 23.8570928 + 1.3960416 * t + 0.000308 * (t ** 2)
    return ayanamsha


def compute_ascendant(obs: ephem.Observer, ayanamsha: float) -> float:
    """
    Calculate high-precision Sidereal Ascendant (Lagna) using observer's
    Local Sidereal Time (RAMC) and true geographic latitude.
    """
    theta = float(obs.sidereal_time())  # radians
    phi = float(obs.lat)  # radians
    jd = ephem.julian_date(obs.date)
    t = (jd - 2451545.0) / 36525.0
    eps = math.radians(23.4392911 - (46.8150 * t) / 3600.0)

    y = -math.cos(theta)
    x = math.sin(theta) * math.cos(eps) + math.tan(phi) * math.sin(eps)

    root1 = math.degrees(math.atan2(y, x)) % 360
    root2 = (root1 + 180) % 360

    # Determine which intersection point is rising (Ascendant) by testing altitude rate
    obs_test1 = ephem.Observer()
    obs_test1.lat, obs_test1.lon, obs_test1.date = obs.lat, obs.lon, obs.date

    obs_test2 = ephem.Observer()
    obs_test2.lat, obs_test2.lon = obs.lat, obs.lon
    obs_test2.date = ephem.Date(obs.date + (ephem.minute * 2))

    rising_root = root1
    for r in [root1, root2]:
        sin_dec = math.sin(eps) * math.sin(math.radians(r))
        dec = math.asin(max(-1.0, min(1.0, sin_dec)))
        ra = math.atan2(math.cos(eps) * math.sin(math.radians(r)), math.cos(math.radians(r))) % (2 * math.pi)

        b = ephem.FixedBody()
        b._ra = ra
        b._dec = dec
        b.compute(obs_test1)
        alt1 = float(b.alt)
        b.compute(obs_test2)
        alt2 = float(b.alt)

        if alt2 > alt1:
            rising_root = r
            break

    sidereal_lagna = (rising_root - ayanamsha) % 360
    return sidereal_lagna


def dms(deg_val: float) -> Tuple[int, int, int]:
    """Convert floating degrees into (Degrees, Minutes, Seconds)."""
    deg = int(deg_val)
    rem = (deg_val - deg) * 60.0
    minutes = int(rem)
    seconds = int((rem - minutes) * 60.0)
    return deg, minutes, seconds


def get_nakshatra_info(longitude: float) -> Dict[str, Any]:
    """Calculate Nakshatra, Pada, and ruler for a given sidereal longitude."""
    nak_span = 360.0 / 27.0  # 13°20' = 13.33333333°
    pada_span = nak_span / 4.0  # 3°20' = 3.33333333°

    idx = int(longitude // nak_span)
    nak = NAKSHATRAS[idx % 27]

    rem_in_nak = longitude % nak_span
    pada = int(rem_in_nak // pada_span) + 1

    return {
        "nakshatra_id": nak["id"],
        "nakshatra_name": nak["name"],
        "nakshatra_lord": nak["lord"],
        "pada": pada,
        "elapsed_deg": rem_in_nak,
        "remaining_deg": nak_span - rem_in_nak
    }


def get_navamsha_sign(longitude: float) -> int:
    """Calculate D9 Navamsha sign (1-12) for a given sidereal longitude."""
    # Each navamsha is 3°20' (3.333333°).
    # 12 signs * 9 padas = 108 navamshas across the 360° zodiac.
    pada_span = 360.0 / 108.0
    navamsha_idx = int(longitude // pada_span)
    return (navamsha_idx % 12) + 1


def determine_dignity(planet: str, sign_id: int) -> str:
    """Determine planetary dignity: Exalted, Debilitated, Own Sign, or Neutral."""
    rules = PLANET_EXALTATION_DEBILITATION.get(planet)
    if not rules:
        return "Neutral"
    if sign_id == rules["exalted_sign"]:
        return "Exalted (Uccha)"
    if sign_id == rules["debilitated_sign"]:
        return "Debilitated (Neecha)"
    if sign_id in rules["own_signs"]:
        return "Own Sign (Swakshetra)"
    return "Neutral"


def calculate_vimshottari_dasha(moon_sid: float, birth_dt: datetime) -> List[Dict[str, Any]]:
    """
    Compute Vimshottari Mahadasha timeline starting from birth date.
    Calculates exact start and end dates for each Mahadasha cycle.
    """
    nak_info = get_nakshatra_info(moon_sid)
    birth_lord = nak_info["nakshatra_lord"]

    # Locate starting lord index
    start_idx = 0
    for i, (lord, _) in enumerate(VIMSHOTTARI_LORDS):
        if lord == birth_lord:
            start_idx = i
            break

    # Calculate remaining balance of the first Mahadasha
    total_lord_years = VIMSHOTTARI_LORDS[start_idx][1]
    fraction_remaining = nak_info["remaining_deg"] / (360.0 / 27.0)
    first_dasha_remaining_years = fraction_remaining * total_lord_years

    timeline = []
    current_date = birth_dt

    for step in range(len(VIMSHOTTARI_LORDS)):
        curr_idx = (start_idx + step) % len(VIMSHOTTARI_LORDS)
        lord, full_years = VIMSHOTTARI_LORDS[curr_idx]

        duration_years = first_dasha_remaining_years if step == 0 else full_years
        end_date = current_date + timedelta(days=duration_years * 365.2425)

        # Generate sub-periods (Antardashas)
        antardashas = []
        ad_current_date = current_date
        for ad_step in range(len(VIMSHOTTARI_LORDS)):
            ad_idx = (curr_idx + ad_step) % len(VIMSHOTTARI_LORDS)
            ad_lord, ad_full_years = VIMSHOTTARI_LORDS[ad_idx]
            ad_years = (full_years * ad_full_years) / 120.0
            ad_end_date = ad_current_date + timedelta(days=ad_years * 365.2425)

            antardashas.append({
                "sub_lord": ad_lord,
                "start_date": ad_current_date.strftime("%Y-%m-%d"),
                "end_date": ad_end_date.strftime("%Y-%m-%d"),
                "duration_months": round(ad_years * 12, 1)
            })
            ad_current_date = ad_end_date

        timeline.append({
            "lord": lord,
            "full_years": full_years,
            "actual_years": round(duration_years, 2),
            "start_date": current_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "is_birth_dasha": (step == 0),
            "antardashas": antardashas
        })

        current_date = end_date

    return timeline


def calculate_panchang(sun_sid: float, moon_sid: float, birth_dt: datetime) -> Dict[str, Any]:
    """Calculate Vedic Panchang: Tithi, Nakshatra, Yoga, Karana, and Vara."""
    # 1. Tithi
    diff = (moon_sid - sun_sid) % 360.0
    tithi_num = int(diff // 12.0) + 1
    tithi_name = TITHI_NAMES[tithi_num - 1]
    paksha = "Shukla Paksha" if tithi_num <= 15 else "Krishna Paksha"

    # 2. Vara (Weekday)
    weekdays_sanskrit = [
        "Somavara (Monday)", "Mangalavara (Tuesday)", "Budhavara (Wednesday)",
        "Guruvara (Thursday)", "Shukravara (Friday)", "Shanivara (Saturday)", "Ravivara (Sunday)"
    ]
    vara = weekdays_sanskrit[birth_dt.weekday()]

    # 3. Nakshatra
    nak_info = get_nakshatra_info(moon_sid)

    # 4. Yoga
    yoga_sum = (sun_sid + moon_sid) % 360.0
    yoga_idx = int(yoga_sum // (360.0 / 27.0))
    yoga_name = YOGAS[yoga_idx % 27]

    # 5. Karana
    karana_idx = int(diff // 6.0)
    if karana_idx == 0:
        karana_name = "Kintughna"
    elif 1 <= karana_idx <= 56:
        karana_name = KARANAS[(karana_idx - 1) % 7]
    elif karana_idx == 57:
        karana_name = "Shakuni"
    elif karana_idx == 58:
        karana_name = "Chatushpada"
    else:
        karana_name = "Naga"

    return {
        "tithi": f"{tithi_name} ({paksha})",
        "tithi_number": tithi_num,
        "paksha": paksha,
        "vara": vara,
        "nakshatra": f"{nak_info['nakshatra_name']} (Pada {nak_info['pada']})",
        "nakshatra_lord": nak_info["nakshatra_lord"],
        "yoga": yoga_name,
        "karana": karana_name
    }


def check_manglik_dosha(mars_house: int, mars_sign: int, jupiter_house: int) -> Dict[str, Any]:
    """
    Detailed Manglik (Kuja) Dosha analysis.
    Mars in 1st, 2nd, 4th, 7th, 8th, or 12th house forms Manglik Dosha.
    Also evaluates classical cancellation rules.
    """
    manglik_houses = [1, 2, 4, 7, 8, 12]
    is_in_manglik_house = mars_house in manglik_houses

    cancellations = []
    # Classical exceptions
    if mars_sign in [1, 8]:  # Aries or Scorpio (Own signs)
        cancellations.append("Mars is situated in its own sign (Swakshetra).")
    if mars_sign == 10:  # Capricorn (Exalted)
        cancellations.append("Mars is exalted in Capricorn (Uccha).")
    if mars_house == 1 and mars_sign == 1:
        cancellations.append("Mars in 1st house in Aries negates Kuja Dosha.")
    if mars_house == 4 and mars_sign == 8:
        cancellations.append("Mars in 4th house in Scorpio cancels Dosha.")
    if mars_house == 7 and mars_sign in [10, 4]:
        cancellations.append("Mars in 7th house in Capricorn or Cancer softens Dosha.")
    if mars_house == 8 and mars_sign in [9, 12]:
        cancellations.append("Mars in 8th house in Jupiter's sign cancels Dosha.")

    # Jupiter conjunction or aspect
    # Jupiter aspects 5th, 7th, 9th houses from its placement
    jup_aspects = [(jupiter_house - 1 + asp) % 12 + 1 for asp in [0, 4, 6, 8]]
    if mars_house in jup_aspects:
        cancellations.append("Benefic Jupiter conjuncts or casts aspect on Mars.")

    if not is_in_manglik_house:
        status = "Non-Manglik"
        severity = "None"
        description = f"Mars is favorably located in House {mars_house}, which does not form Manglik Dosha."
    elif len(cancellations) > 0:
        status = "Manglik (Cancelled / Very Mild)"
        severity = "Mild"
        description = f"Mars is in House {mars_house}, but classical astrological cancellations neutralize its negative effects."
    else:
        status = "Manglik"
        severity = "High" if mars_house in [7, 8] else "Moderate"
        description = f"Mars is located in House {mars_house}, forming {severity} Manglik Dosha."

    remedies = [
        "Worship Lord Hanuman and chant the Hanuman Chalisa on Tuesdays.",
        "Perform Kumbh Vivah or Vishnu Vivah prior to marriage if indicated.",
        "Recite the Mangal Gayatri Mantra: 'Om Angarkaya Vidmahe Bhoomipalaya Dheemahi Tanno Kujah Prachodayat'.",
        "Donate red lentils (masoor dal), jaggery, or copper on Tuesdays."
    ]

    return {
        "status": status,
        "is_manglik": is_in_manglik_house and len(cancellations) == 0,
        "severity": severity,
        "mars_house": mars_house,
        "description": description,
        "cancellations": cancellations,
        "remedies": remedies
    }


def compute_full_kundli(
    name: str,
    gender: str,
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    second: int,
    lat: float,
    lon: float,
    tz_offset: float,
    city_name: str
) -> Dict[str, Any]:
    """
    Main entry point: Generates complete Vedic Kundli chart and astrological analysis.
    """
    # 1. Prepare Local & UTC datetimes
    local_dt = datetime(year, month, day, hour, minute, second)
    utc_dt = local_dt - timedelta(hours=tz_offset)

    # 2. PyEphem Observer
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.date = ephem.Date(utc_dt)

    jd = ephem.julian_date(obs.date)
    t = (jd - 2451545.0) / 36525.0
    ayanamsha = compute_lahiri_ayanamsha(jd)

    # 3. Ascendant (Lagna)
    lagna_sid = compute_ascendant(obs, ayanamsha)
    lagna_sign_id = int(lagna_sid // 30.0) + 1
    lagna_nak = get_nakshatra_info(lagna_sid)
    lagna_navamsha_sign = get_navamsha_sign(lagna_sid)

    deg, m, s = dms(lagna_sid % 30.0)
    lagna_info = {
        "longitude": lagna_sid,
        "sign_id": lagna_sign_id,
        "sign_name": ZODIAC_SIGNS[lagna_sign_id - 1]["name"],
        "sign_sanskrit": ZODIAC_SIGNS[lagna_sign_id - 1]["sanskrit"],
        "degrees": f"{deg}° {m:02d}' {s:02d}\"",
        "deg_num": round(lagna_sid % 30.0, 2),
        "nakshatra": lagna_nak["nakshatra_name"],
        "nakshatra_lord": lagna_nak["nakshatra_lord"],
        "pada": lagna_nak["pada"],
        "navamsha_sign_id": lagna_navamsha_sign,
        "navamsha_sign_name": ZODIAC_SIGNS[lagna_navamsha_sign - 1]["name"]
    }

    # 4. Calculate Seven Physical Planets
    ephem_planets = {
        "Sun": (ephem.Sun(), "Surya", "सूर्य"),
        "Moon": (ephem.Moon(), "Chandra", "चंद्र"),
        "Mars": (ephem.Mars(), "Mangal", "मंगल"),
        "Mercury": (ephem.Mercury(), "Budha", "बुध"),
        "Jupiter": (ephem.Jupiter(), "Guru", "बृहस्पति"),
        "Venus": (ephem.Venus(), "Shukra", "शुक्र"),
        "Saturn": (ephem.Saturn(), "Shani", "शनि"),
    }

    planets_data = []
    moon_sid = 0.0
    sun_sid = 0.0
    mars_house = 1
    mars_sign = 1
    jupiter_house = 1

    for name_en, (body, sanskrit, hindi) in ephem_planets.items():
        body.compute(obs)
        ecl = ephem.Ecliptic(body)
        trop_lon = math.degrees(ecl.lon) % 360.0
        sid_lon = (trop_lon - ayanamsha) % 360.0

        if name_en == "Sun":
            sun_sid = sid_lon
        elif name_en == "Moon":
            moon_sid = sid_lon

        # Check retrograde status by sampling 1 hour ahead
        obs_ahead = ephem.Observer()
        obs_ahead.lat, obs_ahead.lon = obs.lat, obs.lon
        obs_ahead.date = ephem.Date(obs.date + ephem.hour)
        body.compute(obs_ahead)
        ecl_ahead = ephem.Ecliptic(body)
        motion_diff = (math.degrees(ecl_ahead.lon) - trop_lon + 180.0) % 360.0 - 180.0
        is_retrograde = motion_diff < 0.0 if name_en not in ["Sun", "Moon"] else False

        sign_id = int(sid_lon // 30.0) + 1
        sign_deg = sid_lon % 30.0
        deg, m, s = dms(sign_deg)
        house = ((sign_id - lagna_sign_id) % 12) + 1
        nak = get_nakshatra_info(sid_lon)
        navamsha_sign = get_navamsha_sign(sid_lon)
        dignity = determine_dignity(name_en, sign_id)

        if name_en == "Mars":
            mars_house = house
            mars_sign = sign_id
        elif name_en == "Jupiter":
            jupiter_house = house

        planets_data.append({
            "name": name_en,
            "sanskrit": sanskrit,
            "hindi": hindi,
            "longitude": sid_lon,
            "sign_id": sign_id,
            "sign_name": ZODIAC_SIGNS[sign_id - 1]["name"],
            "sign_sanskrit": ZODIAC_SIGNS[sign_id - 1]["sanskrit"],
            "house": house,
            "deg_str": f"{deg}° {m:02d}' {s:02d}\"",
            "deg_num": round(sign_deg, 2),
            "is_retrograde": is_retrograde,
            "nakshatra": nak["nakshatra_name"],
            "nakshatra_lord": nak["nakshatra_lord"],
            "pada": nak["pada"],
            "navamsha_sign_id": navamsha_sign,
            "navamsha_sign_name": ZODIAC_SIGNS[navamsha_sign - 1]["name"],
            "dignity": dignity
        })

    # 5. Nodes: Rahu (North Node) and Ketu (South Node)
    rahu_trop = (125.04452 - 1934.136261 * t + 0.0020708 * (t ** 2)) % 360.0
    rahu_sid = (rahu_trop - ayanamsha) % 360.0
    ketu_sid = (rahu_sid + 180.0) % 360.0

    for node_name, sid_lon, sanskrit, hindi in [
        ("Rahu", rahu_sid, "Rahu", "राहु"),
        ("Ketu", ketu_sid, "Ketu", "केतु")
    ]:
        sign_id = int(sid_lon // 30.0) + 1
        sign_deg = sid_lon % 30.0
        deg, m, s = dms(sign_deg)
        house = ((sign_id - lagna_sign_id) % 12) + 1
        nak = get_nakshatra_info(sid_lon)
        navamsha_sign = get_navamsha_sign(sid_lon)
        dignity = determine_dignity(node_name, sign_id)

        planets_data.append({
            "name": node_name,
            "sanskrit": sanskrit,
            "hindi": hindi,
            "longitude": sid_lon,
            "sign_id": sign_id,
            "sign_name": ZODIAC_SIGNS[sign_id - 1]["name"],
            "sign_sanskrit": ZODIAC_SIGNS[sign_id - 1]["sanskrit"],
            "house": house,
            "deg_str": f"{deg}° {m:02d}' {s:02d}\"",
            "deg_num": round(sign_deg, 2),
            "is_retrograde": True,  # Nodes are always retrograde in mean motion
            "nakshatra": nak["nakshatra_name"],
            "nakshatra_lord": nak["nakshatra_lord"],
            "pada": nak["pada"],
            "navamsha_sign_id": navamsha_sign,
            "navamsha_sign_name": ZODIAC_SIGNS[navamsha_sign - 1]["name"],
            "dignity": dignity
        })

    # 6. Houses (Bhavas) Mapping for D1 (Rasi) & D9 (Navamsha)
    d1_houses = {h: {"house": h, "sign_id": ((lagna_sign_id - 1 + h - 1) % 12) + 1, "planets": []} for h in range(1, 13)}
    for p in planets_data:
        d1_houses[p["house"]]["planets"].append(p)

    d9_houses = {h: {"house": h, "sign_id": ((lagna_navamsha_sign - 1 + h - 1) % 12) + 1, "planets": []} for h in range(1, 13)}
    for p in planets_data:
        p_nav_house = ((p["navamsha_sign_id"] - lagna_navamsha_sign) % 12) + 1
        p_copy = dict(p)
        p_copy["d9_house"] = p_nav_house
        d9_houses[p_nav_house]["planets"].append(p_copy)

    # 7. Vimshottari Dashas
    dashas = calculate_vimshottari_dasha(moon_sid, local_dt)

    # 8. Panchang
    panchang = calculate_panchang(sun_sid, moon_sid, local_dt)

    # 9. Manglik Dosha Analysis
    manglik = check_manglik_dosha(mars_house, mars_sign, jupiter_house)

    return {
        "metadata": {
            "name": name,
            "gender": gender,
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": second,
            "birth_date": f"{year:04d}-{month:02d}-{day:02d}",
            "birth_time_local": local_dt.strftime("%d %b %Y, %I:%M:%S %p"),
            "city": city_name,
            "latitude": lat,
            "longitude": lon,
            "timezone": f"UTC+{tz_offset}" if tz_offset >= 0 else f"UTC{tz_offset}",
            "julian_day": round(jd, 4),
            "ayanamsha": f"{dms(ayanamsha)[0]}° {dms(ayanamsha)[1]:02d}' {dms(ayanamsha)[2]:02d}\" (Lahiri / Chitrapaksha)"
        },
        "lagna": lagna_info,
        "planets": planets_data,
        "d1_houses": list(d1_houses.values()),
        "d9_houses": list(d9_houses.values()),
        "dashas": dashas,
        "panchang": panchang,
        "manglik": manglik
    }
