/**
 * Vedic Kundli Portal - Frontend Logic
 * Theme: Hindu Vedic Blend & 3-Step Guided Wizard
 */

// Global Application State
let currentKundli = null;
let currentStep = 1;
let activeChartType = 'd1';    // 'd1' or 'd9'
let activeChartStyle = 'north'; // 'north' or 'south'

// Sacred Graha Colors & Sanskrit Config
const PLANET_CONFIG = {
    'Sun': { symbol: '☉', short: 'Su', color: '#b45309', sanskrit: 'Surya', hindi: 'सूर्य' },
    'Moon': { symbol: '☽', short: 'Mo', color: '#0284c7', sanskrit: 'Chandra', hindi: 'चन्द्र' },
    'Mars': { symbol: '♂', short: 'Ma', color: '#dc2626', sanskrit: 'Mangal', hindi: 'मंगल' },
    'Mercury': { symbol: '☿', short: 'Me', color: '#059669', sanskrit: 'Budha', hindi: 'बुध' },
    'Jupiter': { symbol: '♃', short: 'Ju', color: '#d97706', sanskrit: 'Guru', hindi: 'गुरु' },
    'Venus': { symbol: '♀', short: 'Ve', color: '#db2777', sanskrit: 'Shukra', hindi: 'शुक्र' },
    'Saturn': { symbol: '♄', short: 'Sa', color: '#4f46e5', sanskrit: 'Shani', hindi: 'शनि' },
    'Rahu': { symbol: '☊', short: 'Ra', color: '#7c3aed', sanskrit: 'Rahu', hindi: 'राहु' },
    'Ketu': { symbol: '☋', short: 'Ke', color: '#57534e', sanskrit: 'Ketu', hindi: 'केतु' }
};

const ZODIAC_NAMES = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
];

const ZODIAC_SANSKRIT = [
    'Mesha', 'Vrishabha', 'Mithuna', 'Karka', 'Simha', 'Kanya',
    'Tula', 'Vrishchika', 'Dhanu', 'Makara', 'Kumbha', 'Meena'
];

const BHAVA_KARAKAS = [
    'Tanu (तनु • Self, Vitality, Physical Appearance, Temperament)',
    'Dhana (धन • Wealth, Family, Speech, Assets, Eyesight)',
    'Sahaja (सहज • Siblings, Courage, Valor, Communication)',
    'Sukha (सुख • Mother, Domestic Happiness, Fixed Assets, Vehicles)',
    'Putra (पुत्र • Children, Intellect, Creativity, Poorva Punya)',
    'Ari (अरि • Enemies, Debts, Diseases, Service, Daily Work)',
    'Yuvati (युवति • Spouse, Marriage, Partnerships, Foreign Travels)',
    'Randhra (रन्ध्र • Longevity, Sudden Events, Occult, Transformation)',
    'Dharma (धर्म • Fortune, Higher Wisdom, Spirituality, Father, Guru)',
    'Karma (कर्म • Career, Profession, Social Status, Authority)',
    'Labha (लाभ • Gains, Desires Fulfilled, Elder Siblings, Networks)',
    'Vyaya (व्यय • Losses, Liberation / Moksha, Foreign Lands, Expenses)'
];

// Document Ready Initialization
document.addEventListener('DOMContentLoaded', () => {
    initCityAutocomplete();
    initEventListeners();
    // Pre-calculate sample so step 2 & 3 are instantly available if user navigates
    triggerCalculation(false);
});

// ----------------- Guided Wizard Step Navigation -----------------
function goToStep(step) {
    if ((step === 2 || step === 3) && !currentKundli) {
        triggerCalculation(true);
        return;
    }

    currentStep = step;

    // Panes
    document.querySelectorAll('.wizard-step-pane').forEach((pane, idx) => {
        pane.classList.toggle('active', (idx + 1) === step);
    });

    // Stepper indicators
    for (let i = 1; i <= 3; i++) {
        const item = document.getElementById(`stepIndicator${i}`);
        if (!item) continue;

        item.classList.remove('active', 'completed');
        if (i < step) {
            item.classList.add('completed');
        } else if (i === step) {
            item.classList.add('active');
        }
    }

    // Step connecting lines
    const line1 = document.getElementById('stepLine1');
    const line2 = document.getElementById('stepLine2');
    if (line1) line1.classList.toggle('completed', step > 1);
    if (line2) line2.classList.toggle('completed', step > 2);

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ----------------- Trigger PDF / Print -----------------
function triggerPrint() {
    if (currentKundli && currentKundli.metadata) {
        document.title = `${currentKundli.metadata.name} - Vedic Kundli Astrological Report`;
    }
    window.print();
}

function initEventListeners() {
    // Form Submission
    const form = document.getElementById('kundliForm');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        triggerCalculation(true);
    });

    // Quick Sample Button
    document.getElementById('quickSampleBtn').addEventListener('click', () => {
        document.getElementById('name').value = 'Arjun Sharma';
        document.getElementById('gender').value = 'Male';
        document.getElementById('birthDate').value = '1995-10-24';
        document.getElementById('birthTime').value = '10:30:00';
        document.getElementById('citySearch').value = 'New Delhi, Delhi, India';
        document.getElementById('latitude').value = '28.6139';
        document.getElementById('longitude').value = '77.2090';
        document.getElementById('timezone').value = '5.5';
        triggerCalculation(true);
    });

    // Print / Download PDF
    document.getElementById('printReportBtn').addEventListener('click', triggerPrint);

    // Chart Type (D1 vs D9)
    document.querySelectorAll('[data-chart]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('[data-chart]').forEach(b => b.classList.remove('active'));
            e.currentTarget.classList.add('active');
            activeChartType = e.currentTarget.getAttribute('data-chart');
            updateChartDisplay();
        });
    });

    // Chart Style (North vs South)
    document.querySelectorAll('[data-style]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('[data-style]').forEach(b => b.classList.remove('active'));
            e.currentTarget.classList.add('active');
            activeChartStyle = e.currentTarget.getAttribute('data-style');
            updateChartDisplay();
        });
    });

    // In-depth Tabs in Step 3
    document.querySelectorAll('.vedic-tab').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.vedic-tab').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.vedic-tab-panel').forEach(c => c.classList.remove('active'));

            const targetTab = e.currentTarget.getAttribute('data-tab');
            e.currentTarget.classList.add('active');
            const panel = document.getElementById(targetTab);
            if (panel) panel.classList.add('active');
        });
    });
}

// ----------------- City Autocomplete -----------------
function initCityAutocomplete() {
    const input = document.getElementById('citySearch');
    const dropdown = document.getElementById('cityDropdown');
    let debounceTimer;

    input.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        const query = input.value.trim();
        if (query.length < 2) {
            dropdown.style.display = 'none';
            return;
        }

        debounceTimer = setTimeout(async () => {
            try {
                const res = await fetch(`/api/cities?q=${encodeURIComponent(query)}&limit=12`);
                const data = await res.json();
                renderCityDropdown(data.cities || []);
            } catch (err) {
                console.warn('City lookup error:', err);
            }
        }, 150);
    });

    document.addEventListener('click', (e) => {
        if (!input.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });
}

function renderCityDropdown(cities) {
    const dropdown = document.getElementById('cityDropdown');
    dropdown.innerHTML = '';

    if (cities.length === 0) {
        dropdown.style.display = 'none';
        return;
    }

    cities.forEach(item => {
        const div = document.createElement('div');
        div.className = 'dropdown-item';
        const stateStr = item.state ? item.state + ', ' : '';
        div.innerHTML = `
            <span class="city-name">${item.city}, <small style="color:var(--gold, #d4af37); font-size:0.85em;">${stateStr}${item.country}</small></span>
            <span class="city-tz">UTC${item.tz >= 0 ? '+' : ''}${item.tz}</span>
        `;
        div.addEventListener('click', () => {
            document.getElementById('citySearch').value = `${item.city}, ${stateStr}${item.country}`;
            document.getElementById('latitude').value = item.lat;
            document.getElementById('longitude').value = item.lon;
            document.getElementById('timezone').value = item.tz;
            dropdown.style.display = 'none';
        });
        dropdown.appendChild(div);
    });

    dropdown.style.display = 'block';
}

// ----------------- Calculation & Data Population -----------------
async function triggerCalculation(advanceToStep2 = true) {
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    const loadingBox = document.getElementById('loadingBox');

    submitBtn.disabled = true;
    if (btnText) btnText.style.display = 'none';
    if (btnSpinner) btnSpinner.style.display = 'inline-block';
    if (advanceToStep2) loadingBox.style.display = 'block';

    let latVal = parseFloat(document.getElementById('latitude').value);
    let lonVal = parseFloat(document.getElementById('longitude').value);
    let tzVal = parseFloat(document.getElementById('timezone').value);
    const cityNameInput = document.getElementById('citySearch').value.trim();

    // Auto-resolve city/village coordinates if not selected from dropdown or default coordinates remained
    if (cityNameInput && cityNameInput.length >= 2 && (!latVal || (Math.abs(latVal - 28.6139) < 0.001 && !cityNameInput.toLowerCase().includes('delhi')))) {
        try {
            const checkRes = await fetch(`/api/cities?q=${encodeURIComponent(cityNameInput)}&limit=1`);
            const checkData = await checkRes.json();
            if (checkData.cities && checkData.cities.length > 0) {
                const bestCity = checkData.cities[0];
                latVal = bestCity.lat;
                lonVal = bestCity.lon;
                tzVal = bestCity.tz;
                document.getElementById('latitude').value = latVal;
                document.getElementById('longitude').value = lonVal;
                document.getElementById('timezone').value = tzVal;
            }
        } catch (e) {
            console.warn("Auto-resolution of city coords skipped:", e);
        }
    }

    const bDate = document.getElementById('birthDate').value.split('-');
    const bTime = document.getElementById('birthTime').value.split(':');

    const payload = {
        name: document.getElementById('name').value.trim() || 'Seeker',
        gender: document.getElementById('gender').value,
        year: parseInt(bDate[0], 10),
        month: parseInt(bDate[1], 10),
        day: parseInt(bDate[2], 10),
        hour: parseInt(bTime[0], 10),
        minute: parseInt(bTime[1], 10),
        second: bTime[2] ? parseInt(bTime[2], 10) : 0,
        latitude: latVal,
        longitude: lonVal,
        timezone_offset: tzVal,
        city_name: cityNameInput || 'Custom Place'
    };

    try {
        const res = await fetch('/api/kundli', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || 'Calculation failed');
        }

        const data = await res.json();
        currentKundli = data;
        populateKundliData(data);

        document.getElementById('printReportBtn').style.display = 'inline-flex';

        if (advanceToStep2) {
            goToStep(2);
        }
    } catch (err) {
        alert('Astrological calculation error: ' + err.message);
    } finally {
        submitBtn.disabled = false;
        if (btnText) btnText.style.display = 'inline';
        if (btnSpinner) btnSpinner.style.display = 'none';
        loadingBox.style.display = 'none';
    }
}

function populateKundliData(data) {
    const meta = data.metadata;
    document.getElementById('resName').textContent = meta.name;
    document.getElementById('resMeta').textContent = `${meta.birth_time_local} • ${meta.city} (${meta.timezone})`;

    // Lagna Pillar
    document.getElementById('resLagnaSign').textContent = `${data.lagna.sign_name} (${data.lagna.sign_sanskrit})`;
    document.getElementById('resLagnaDeg').textContent = `${data.lagna.degrees} • ${data.lagna.nakshatra}`;

    // Moon & Sun
    const moon = data.planets.find(p => p.name === 'Moon');
    const sun = data.planets.find(p => p.name === 'Sun');

    if (moon) {
        document.getElementById('resMoonSign').textContent = `${moon.sign_name} (${moon.sign_sanskrit})`;
        document.getElementById('resMoonNak').textContent = `${moon.nakshatra} • Pada ${moon.pada}`;
    }

    if (sun) {
        document.getElementById('resSunSign').textContent = `${sun.sign_name} (${sun.sign_sanskrit})`;
        document.getElementById('resSunDeg').textContent = `${sun.deg_str} • ${sun.nakshatra}`;
    }

    // Manglik
    const m = data.manglik;
    const mb = document.getElementById('resManglikBadge');
    mb.textContent = m.status;
    document.getElementById('resManglikSub').textContent = `Mars placed in House ${m.mars_house}`;

    // Ephemeris Footers
    document.getElementById('metaAyanamshaBadge').textContent = meta.ayanamsha;
    document.getElementById('metaAyanamsha').textContent = meta.ayanamsha;
    document.getElementById('metaJd').textContent = meta.julian_day;

    // Render active SVG chart
    updateChartDisplay();

    // Populate Step 3 Tables & Reports
    renderAstrologerReport(data.astrologer_report);
    renderPlanetsTable(data.planets);
    renderHousesTable(data.d1_houses, data.lagna);
    renderDashas(data.dashas);
    renderPanchang(data.panchang);
    renderManglikDetails(data.manglik);
}

function updateChartDisplay() {
    if (!currentKundli) return;

    const isD1 = activeChartType === 'd1';
    const isNorth = activeChartStyle === 'north';

    const titleEl = document.getElementById('currentChartTitle');
    const subEl = document.getElementById('currentChartSubtitle');
    const wrapper = document.getElementById('chartSvgWrapper');

    titleEl.textContent = isD1 ? 'D1 • Lagna / Rasi Kundli (लग्न जन्म चक्र)' : 'D9 • Navamsha Kundli (नवांश चक्र)';
    subEl.textContent = isNorth
        ? 'North Indian Diamond Format • Houses Fixed (1-12), Signs Rotate Based on Lagna'
        : 'South Indian Box Format • Signs Fixed Clockwise (Pisces to Aquarius), Lagna Marked';

    const housesData = isD1 ? currentKundli.d1_houses : currentKundli.d9_houses;
    const lagnaSignId = isD1 ? currentKundli.lagna.sign_id : currentKundli.lagna.navamsha_sign_id;

    if (isNorth) {
        wrapper.innerHTML = generateNorthIndianSvg(housesData, lagnaSignId);
    } else {
        wrapper.innerHTML = generateSouthIndianSvg(currentKundli.planets, lagnaSignId, isD1);
    }
}

// ----------------- Hindu Vedic North Indian Diamond SVG -----------------
function generateNorthIndianSvg(houses, lagnaSignId) {
    const W = 600;
    const H = 600;

    // Fixed House centers & planet anchor coordinates
    const houseCenters = {
        1: { signX: 300, signY: 220, pX: 300, pY: 130 },
        2: { signX: 235, signY: 75,  pX: 195, pY: 90 },
        3: { signX: 75,  signY: 235, pX: 90,  pY: 190 },
        4: { signX: 220, signY: 300, pX: 130, pY: 300 },
        5: { signX: 75,  signY: 365, pX: 90,  pY: 410 },
        6: { signX: 235, signY: 525, pX: 195, pY: 510 },
        7: { signX: 300, signY: 380, pX: 300, pY: 470 },
        8: { signX: 365, signY: 525, pX: 405, pY: 510 },
        9: { signX: 525, signY: 365, pX: 510, pY: 410 },
        10:{ signX: 380, signY: 300, pX: 470, pY: 300 },
        11:{ signX: 525, signY: 235, pX: 510, pY: 190 },
        12:{ signX: 365, signY: 75,  pX: 405, pY: 90 }
    };

    let planetsSvg = '';
    houses.forEach(h => {
        const hc = houseCenters[h.house];
        const signNum = h.sign_id;

        // Zodiac Sign Number in Rich Crimson
        planetsSvg += `<text x="${hc.signX}" y="${hc.signY}" fill="#881337" font-size="19" font-weight="800" font-family="'Cinzel', serif" text-anchor="middle" dominant-baseline="central">${signNum}</text>`;

        // House Identifier Sub-hint
        const houseLabelX = (hc.signX + hc.pX) / 2;
        const houseLabelY = (hc.signY + hc.pY) / 2;
        planetsSvg += `<text x="${houseLabelX}" y="${houseLabelY}" fill="#b45309" font-size="11" font-weight="600" opacity="0.6" text-anchor="middle" dominant-baseline="central">H${h.house}</text>`;

        // Grahas in this House
        if (h.planets && h.planets.length > 0) {
            const count = h.planets.length;
            const startY = hc.pY - ((count - 1) * 11);

            h.planets.forEach((p, idx) => {
                const cfg = PLANET_CONFIG[p.name] || { color: '#1c1917', short: p.name.substring(0,2) };
                const py = startY + (idx * 22);
                const retroTag = p.is_retrograde && p.name !== 'Rahu' && p.name !== 'Ketu' ? ' <tspan fill="#dc2626" font-weight="900">(R)</tspan>' : '';

                planetsSvg += `
                    <text x="${hc.pX}" y="${py}" text-anchor="middle" dominant-baseline="central" fill="${cfg.color}" font-size="14" font-weight="700" font-family="'Inter', sans-serif">
                        ${cfg.short} ${Math.floor(p.deg_num || 0)}°${retroTag}
                    </text>
                `;
            });
        }
    });

    return `
    <svg viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg" class="vedic-kundli-svg">
        <defs>
            <linearGradient id="vedicParchment" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fffefb"/>
                <stop offset="100%" stop-color="#fdf6e9"/>
            </linearGradient>
        </defs>

        <!-- Parchment Base -->
        <rect x="0" y="0" width="${W}" height="${H}" fill="url(#vedicParchment)" stroke="#881337" stroke-width="4" rx="8"/>

        <!-- Sacred Double Inner Borders -->
        <rect x="12" y="12" width="${W-24}" height="${H-24}" fill="none" stroke="#d4a373" stroke-width="1.5"/>
        <rect x="18" y="18" width="${W-36}" height="${H-36}" fill="none" stroke="#881337" stroke-width="2"/>

        <!-- Main Diagonals -->
        <line x1="18" y1="18" x2="${W-18}" y2="${H-18}" stroke="#881337" stroke-width="2.2"/>
        <line x1="${W-18}" y1="18" x2="18" y2="${H-18}" stroke="#881337" stroke-width="2.2"/>

        <!-- Central Diamond (Rhombus) -->
        <polygon points="${W/2},18 ${W-18},${H/2} ${W/2},${H-18} 18,${H/2}" fill="none" stroke="#881337" stroke-width="2.5"/>

        <!-- Subtle Internal Cross Guide -->
        <line x1="18" y1="${H/2}" x2="${W-18}" y2="${H/2}" stroke="#d4a373" stroke-width="1" stroke-dasharray="3,3"/>
        <line x1="${W/2}" y1="18" x2="${W/2}" y2="${H-18}" stroke="#d4a373" stroke-width="1" stroke-dasharray="3,3"/>

        <!-- Sacred Central Om Medallion -->
        <circle cx="${W/2}" cy="${H/2}" r="15" fill="#fdf5e8" stroke="#881337" stroke-width="2"/>
        <text x="${W/2}" y="${H/2}" text-anchor="middle" dominant-baseline="central" fill="#b45309" font-size="15" font-family="'Tiro Devanagari Sanskrit', serif">ॐ</text>

        <!-- Injected Planets & Labels -->
        ${planetsSvg}
    </svg>
    `;
}

// ----------------- Hindu Vedic South Indian Box SVG -----------------
function generateSouthIndianSvg(planets, lagnaSignId, isD1) {
    const W = 600;
    const H = 600;
    const boxSize = 150;

    const signCoordinates = {
        12: { col: 0, row: 0 },
        1:  { col: 1, row: 0 },
        2:  { col: 2, row: 0 },
        3:  { col: 3, row: 0 },
        4:  { col: 3, row: 1 },
        5:  { col: 3, row: 2 },
        6:  { col: 3, row: 3 },
        7:  { col: 2, row: 3 },
        8:  { col: 1, row: 3 },
        9:  { col: 0, row: 3 },
        10: { col: 0, row: 2 },
        11: { col: 0, row: 1 }
    };

    const signPlanets = {};
    for (let s = 1; s <= 12; s++) signPlanets[s] = [];

    planets.forEach(p => {
        const sign = isD1 ? p.sign_id : p.navamsha_sign_id;
        signPlanets[sign].push(p);
    });

    let boxesSvg = '';

    for (let s = 1; s <= 12; s++) {
        const coord = signCoordinates[s];
        const bx = coord.col * boxSize;
        const by = coord.row * boxSize;
        const isLagna = (s === lagnaSignId);

        // Cell Box
        boxesSvg += `
            <rect x="${bx}" y="${by}" width="${boxSize}" height="${boxSize}" fill="${isLagna ? '#fef3e7' : '#fffdfa'}" stroke="#881337" stroke-width="1.8"/>
        `;

        // Sign Name Header
        const signName = ZODIAC_SANSKRIT[s - 1];
        boxesSvg += `
            <text x="${bx + 8}" y="${by + 16}" fill="#78716c" font-size="11" font-weight="700">${s}. ${signName}</text>
        `;

        // Auspicious Lagna Indicator Banner
        if (isLagna) {
            boxesSvg += `
                <polygon points="${bx + boxSize - 45},${by} ${bx + boxSize},${by} ${bx + boxSize},${by + 45}" fill="#ea580c"/>
                <text x="${bx + boxSize - 15}" y="${by + 18}" fill="#fff" font-size="10" font-weight="900" text-anchor="middle">लग्न</text>
            `;
        }

        // Planets inside this Zodiac box
        const pList = signPlanets[s] || [];
        pList.forEach((p, idx) => {
            const cfg = PLANET_CONFIG[p.name] || { color: '#1c1917', short: p.name.substring(0,2) };
            const py = by + 42 + (idx * 21);
            const retroTag = p.is_retrograde && p.name !== 'Rahu' && p.name !== 'Ketu' ? ' <tspan fill="#dc2626" font-weight="900">(R)</tspan>' : '';

            boxesSvg += `
                <text x="${bx + 12}" y="${py}" fill="${cfg.color}" font-size="13" font-weight="700">
                    ${cfg.short} ${Math.floor(p.deg_num || 0)}°${retroTag}
                </text>
            `;
        });
    }

    // Auspicious Center 2x2 Cell
    const cx = boxSize;
    const cy = boxSize;
    const cw = boxSize * 2;
    const ch = boxSize * 2;

    const centerSvg = `
        <rect x="${cx}" y="${cy}" width="${cw}" height="${ch}" fill="#fdf7ed" stroke="#881337" stroke-width="2.5"/>
        <rect x="${cx+8}" y="${cy+8}" width="${cw-16}" height="${ch-16}" fill="none" stroke="#d4a373" stroke-width="1.5" stroke-dasharray="4,4"/>

        <text x="${cx + cw/2}" y="${cy + 55}" text-anchor="middle" fill="#881337" font-size="20" font-family="'Cinzel', serif" font-weight="bold">
            ${isD1 ? 'D1 • RASI KUNDLI' : 'D9 • NAVAMSHA'}
        </text>
        <text x="${cx + cw/2}" y="${cy + 85}" text-anchor="middle" fill="#b45309" font-size="14" font-weight="bold">
            लग्न: ${ZODIAC_SANSKRIT[lagnaSignId - 1]} (${ZODIAC_NAMES[lagnaSignId - 1]})
        </text>
        <text x="${cx + cw/2}" y="${cy + 115}" text-anchor="middle" fill="#57534e" font-size="12" font-weight="600">
            ${currentKundli.metadata.name} • ${currentKundli.metadata.city}
        </text>
        <text x="${cx + cw/2}" y="${cy + 140}" text-anchor="middle" fill="#78716c" font-size="11">
            Lahiri Ayanamsha • South Indian Format
        </text>
        <text x="${cx + cw/2}" y="${cy + 210}" text-anchor="middle" fill="#ea580c" font-size="34" font-family="'Tiro Devanagari Sanskrit', serif">॥ शुभ लाभ ॥</text>
    `;

    return `
    <svg viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg" class="vedic-kundli-svg">
        <rect x="0" y="0" width="${W}" height="${H}" fill="#fffefb" stroke="#881337" stroke-width="4" rx="8"/>
        ${boxesSvg}
        ${centerSvg}
    </svg>
    `;
}

// ----------------- Tab 1: Planetary Positions -----------------
function renderPlanetsTable(planets) {
    const tbody = document.getElementById('planetsTableBody');
    tbody.innerHTML = '';

    planets.forEach(p => {
        const cfg = PLANET_CONFIG[p.name] || { color: '#1c1917', symbol: '' };
        const tr = document.createElement('tr');

        let digClass = 'dignity-sam';
        if (p.dignity.includes('Exalted')) digClass = 'dignity-uccha';
        else if (p.dignity.includes('Own')) digClass = 'dignity-swakshetra';
        else if (p.dignity.includes('Debilitated')) digClass = 'dignity-neecha';

        tr.innerHTML = `
            <td>
                <span class="graha-pill">
                    <span style="color: ${cfg.color}; font-size: 1.15rem;">${cfg.symbol}</span>
                    <strong>${p.name}</strong> (${p.sanskrit})
                </span>
            </td>
            <td><strong>${p.sign_name}</strong> (${p.sign_sanskrit})</td>
            <td>${p.deg_str}</td>
            <td><strong>House ${p.house}</strong></td>
            <td>${p.nakshatra} <span style="color: var(--text-muted);">(Pada ${p.pada})</span></td>
            <td>${p.navamsha_sign_name}</td>
            <td><span class="dignity-badge ${digClass}">${p.dignity}</span></td>
            <td>${p.is_retrograde && p.name !== 'Rahu' && p.name !== 'Ketu' ? '<span class="retro-badge-legend">Vakri (R)</span>' : '<span style="color: #059669; font-weight: 600;">Marga (Direct)</span>'}</td>
        `;
        tbody.appendChild(tr);
    });
}

// ----------------- Tab 2: Houses Table -----------------
function renderHousesTable(houses, lagna) {
    const tbody = document.getElementById('housesTableBody');
    tbody.innerHTML = '';

    houses.forEach(h => {
        const signName = ZODIAC_NAMES[h.sign_id - 1];
        const signSanskrit = ZODIAC_SANSKRIT[h.sign_id - 1];
        const karaka = BHAVA_KARAKAS[h.house - 1] || '';

        const planetsInHouse = (h.planets || []).map(p => {
            const cfg = PLANET_CONFIG[p.name] || { color: '#1c1917' };
            const rTag = p.is_retrograde && p.name !== 'Rahu' && p.name !== 'Ketu' ? '(R)' : '';
            return `<span style="color: ${cfg.color}; font-weight: 700; margin-right: 8px;">${p.name}${rTag}</span>`;
        }).join('') || '<span style="color: var(--text-muted);">Empty</span>';

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><strong>House ${h.house}</strong> ${h.house === 1 ? '<span style="color: var(--saffron-sacred); font-weight: 700;">(Lagna)</span>' : ''}</td>
            <td>${signName} (${signSanskrit})</td>
            <td><strong>Sign ${h.sign_id} Ruler</strong></td>
            <td><span style="font-size: 0.85rem; color: var(--text-secondary);">${karaka}</span></td>
            <td>${planetsInHouse}</td>
        `;
        tbody.appendChild(tr);
    });
}

// ----------------- Tab 3: Vimshottari Dashas -----------------
function renderDashas(dashas) {
    const container = document.getElementById('dashaTimelineContainer');
    container.innerHTML = '';

    const msContainer = document.getElementById('dashaMilestonesContainer');
    let activeMahadashaLord = '';

    if (currentKundli && currentKundli.astrologer_report) {
        const rep = currentKundli.astrologer_report;
        const clp = rep.current_life_phase;
        const lmt = rep.life_milestones_timeline;

        if (clp) {
            activeMahadashaLord = clp.mahadasha_lord || '';
        }

        if (msContainer && (clp || lmt)) {
            let bannerHtml = '';

            // 1. Current Active Dasha Banner
            if (clp) {
                bannerHtml += `
                    <div class="active-dasha-hero-banner">
                        <div class="hero-dasha-left">
                            <span class="hero-dasha-icon">⏳</span>
                            <div>
                                <div class="hero-dasha-badge">॥ वर्तमान सक्रिय महादशा एवं अंतर्दशा काल ॥</div>
                                <h4 class="hero-dasha-title">Current Active Dasha: <strong>${clp.mahadasha_lord}</strong> Mahadasha • <strong>${clp.antardasha_lord}</strong> Antardasha</h4>
                                <p class="hero-dasha-dates">Mahadasha ends: <strong>${clp.mahadasha_end}</strong> • Active Antardasha ends: <strong>${clp.antardasha_end}</strong> (Upcoming next: <em>${clp.next_antardasha_lord}</em>)</p>
                            </div>
                        </div>
                    </div>
                `;
            }

            // 2. Key Milestones Timeline directly in Tab 3 as well
            if (lmt && lmt.highlight_milestones) {
                const hm = lmt.highlight_milestones;
                const marr = hm.marriage || {};
                const car = hm.career_breakthrough || {};
                const fin = hm.financial_breakthrough || {};
                const prop = hm.property_acquisition || {};

                bannerHtml += `
                    <div class="dasha-milestones-highlight-box">
                        <div class="dm-header">
                            <span class="dm-header-icon">🌟</span>
                            <div>
                                <h5 class="dm-title">Key Life Milestones & Expected Breakthrough Years (प्रमुख जीवन कालक्रम)</h5>
                                <p class="dm-subtitle">Astrological Timing Derived from Active & Upcoming Vimshottari Planetary Cycles</p>
                            </div>
                        </div>
                        <div class="milestones-highlight-grid" style="margin-bottom: 1.5rem;">
                            <!-- 1. Expected Marriage Year -->
                            <div class="milestone-highlight-card marriage-highlight">
                                <div class="m-card-top">
                                    <span class="m-card-icon">💍</span>
                                    <span class="m-status-pill ${marr.status && marr.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${marr.status || 'Golden Window'}</span>
                                </div>
                                <h5 class="m-card-title">${marr.title || 'Expected Marriage Window'}</h5>
                                <div class="m-year-display">
                                    <span class="m-year-number">${marr.year_window || '2026 – 2028'}</span>
                                    <span class="m-age-badge">${marr.age_window || 'Age 31 – 33'}</span>
                                </div>
                                <div class="m-dasha-pill">
                                    <span class="m-dasha-label">Astrological Catalyst:</span>
                                    <strong>${marr.active_dasha || '7th Lord'}</strong>
                                </div>
                                <p class="m-card-desc">${(marr.astrological_catalyst || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</p>
                                <div class="m-guidance-box">
                                    <strong>🕊️ Astrologer's Counsel:</strong> ${(marr.guidance || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}
                                </div>
                            </div>

                            <!-- 2. Career Breakthrough Year -->
                            <div class="milestone-highlight-card career-highlight">
                                <div class="m-card-top">
                                    <span class="m-card-icon">🚀</span>
                                    <span class="m-status-pill ${car.status && car.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${car.status || 'Breakthrough Horizon'}</span>
                                </div>
                                <h5 class="m-card-title">${car.title || 'Career Breakthrough Year'}</h5>
                                <div class="m-year-display">
                                    <span class="m-year-number">${car.year_window || '2027 – 2029'}</span>
                                    <span class="m-age-badge">${car.age_window || 'Age 32 – 34'}</span>
                                </div>
                                <div class="m-dasha-pill">
                                    <span class="m-dasha-label">Astrological Catalyst:</span>
                                    <strong>${car.active_dasha || '10th Lord'}</strong>
                                </div>
                                <p class="m-card-desc">${(car.astrological_catalyst || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</p>
                                <div class="m-guidance-box">
                                    <strong>⚡ Astrologer's Counsel:</strong> ${(car.guidance || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}
                                </div>
                            </div>

                            <!-- 3. Financial Breakthrough Year -->
                            <div class="milestone-highlight-card wealth-highlight">
                                <div class="m-card-top">
                                    <span class="m-card-icon">💰</span>
                                    <span class="m-status-pill ${fin.status && fin.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${fin.status || 'Wealth Horizon'}</span>
                                </div>
                                <h5 class="m-card-title">${fin.title || 'Financial Breakthrough Window'}</h5>
                                <div class="m-year-display">
                                    <span class="m-year-number">${fin.year_window || '2029 – 2031'}</span>
                                    <span class="m-age-badge">${fin.age_window || 'Age 34 – 36'}</span>
                                </div>
                                <div class="m-dasha-pill">
                                    <span class="m-dasha-label">Astrological Catalyst:</span>
                                    <strong>${fin.active_dasha || '2nd & 11th Lord'}</strong>
                                </div>
                                <p class="m-card-desc">${(fin.astrological_catalyst || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</p>
                                <div class="m-guidance-box">
                                    <strong>🪔 Astrologer's Counsel:</strong> ${(fin.guidance || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}
                                </div>
                            </div>

                            <!-- 4. Property & Asset Acquisition -->
                            <div class="milestone-highlight-card property-highlight">
                                <div class="m-card-top">
                                    <span class="m-card-icon">🏡</span>
                                    <span class="m-status-pill ${prop.status && prop.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${prop.status || 'Asset Horizon'}</span>
                                </div>
                                <h5 class="m-card-title">${prop.title || 'Property Acquisition Window'}</h5>
                                <div class="m-year-display">
                                    <span class="m-year-number">${prop.year_window || '2028 – 2030'}</span>
                                    <span class="m-age-badge">${prop.age_window || 'Age 33 – 35'}</span>
                                </div>
                                <div class="m-dasha-pill">
                                    <span class="m-dasha-label">Astrological Catalyst:</span>
                                    <strong>${prop.active_dasha || '4th Lord'}</strong>
                                </div>
                                <p class="m-card-desc">${(prop.astrological_catalyst || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</p>
                                <div class="m-guidance-box">
                                    <strong>🌿 Astrologer's Counsel:</strong> ${(prop.guidance || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }

            msContainer.innerHTML = bannerHtml;
        }
    }

    dashas.forEach((d, idx) => {
        const card = document.createElement('div');
        const isCurrentActive = (d.lord === activeMahadashaLord);
        card.className = `dasha-box ${isCurrentActive ? 'current-active-dasha-box' : ''}`;

        const birthBadge = d.is_birth_dasha ? '<span class="dasha-period-badge">Birth Mahadasha</span>' : '';
        const currentActiveBadge = isCurrentActive ? '<span class="dasha-current-badge">⚡ Current Active Dasha</span>' : '';

        let adHtml = '';
        (d.antardashas || []).forEach(ad => {
            adHtml += `
                <div class="antardasha-card">
                    <div class="ad-title">${d.lord} - ${ad.sub_lord}</div>
                    <div class="ad-period">${ad.start_date} to ${ad.end_date}</div>
                </div>
            `;
        });

        card.innerHTML = `
            <div class="dasha-box-header">
                <div>
                    <span class="dasha-title">${d.lord} Mahadasha</span>
                    ${currentActiveBadge}
                    ${birthBadge}
                    <span style="color: var(--text-muted); font-size: 0.85rem; margin-left: 6px;">(${d.actual_years} yrs)</span>
                </div>
                <div class="dasha-dates-text">
                    ${d.start_date} ➔ ${d.end_date}
                    <span style="margin-left: 8px; color: var(--gold-temple);">▼ Sub-periods</span>
                </div>
            </div>
            <div class="antardasha-drawer">
                <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 0.5rem; font-weight: 600;">Antardasha (Sub-Period) Dates:</p>
                <div class="antardasha-grid">${adHtml}</div>
            </div>
        `;

        const header = card.querySelector('.dasha-box-header');
        const drawer = card.querySelector('.antardasha-drawer');
        header.addEventListener('click', () => {
            const isOpen = drawer.style.display === 'block';
            drawer.style.display = isOpen ? 'none' : 'block';
        });

        if (isCurrentActive || (idx === 0 && !activeMahadashaLord)) {
            drawer.style.display = 'block';
        }

        container.appendChild(card);
    });
}

// ----------------- Tab 4: Vedic Panchang -----------------
function renderPanchang(p) {
    const grid = document.getElementById('panchangGrid');
    grid.innerHTML = `
        <div class="panchang-card">
            <span class="panchang-kpi-label">Tithi (तिथि)</span>
            <span class="panchang-kpi-val">${p.tithi}</span>
            <span class="panchang-kpi-desc">${p.paksha}</span>
        </div>
        <div class="panchang-card">
            <span class="panchang-kpi-label">Vaar (वार / Day)</span>
            <span class="panchang-kpi-val">${p.vara}</span>
            <span class="panchang-kpi-desc">Weekday Ruler</span>
        </div>
        <div class="panchang-card">
            <span class="panchang-kpi-label">Nakshatra (नक्षत्र)</span>
            <span class="panchang-kpi-val">${p.nakshatra}</span>
            <span class="panchang-kpi-desc">Lord: ${p.nakshatra_lord}</span>
        </div>
        <div class="panchang-card">
            <span class="panchang-kpi-label">Yoga (योग)</span>
            <span class="panchang-kpi-val">${p.yoga}</span>
            <span class="panchang-kpi-desc">Solar-Lunar Longitude</span>
        </div>
        <div class="panchang-card">
            <span class="panchang-kpi-label">Karana (करण)</span>
            <span class="panchang-kpi-val">${p.karana}</span>
            <span class="panchang-kpi-desc">Half Tithi</span>
        </div>
    `;
}

// ----------------- Tab 5: Manglik Analysis -----------------
function renderManglikDetails(m) {
    const box = document.getElementById('manglikBox');

    let cancelHtml = '';
    if (m.cancellations && m.cancellations.length > 0) {
        cancelHtml = `
            <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 1.25rem;">
                <h4 style="color: #166534; margin-bottom: 0.5rem; font-family: var(--font-sanskrit); font-size: 1.1rem;">॥ दोष निवारक योग (Mitigating Factors & Cancellations) ॥</h4>
                <ul style="padding-left: 1.25rem; color: #166534; font-size: 0.9rem; line-height: 1.6;">
                    ${m.cancellations.map(c => `<li>${c}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    const remediesHtml = `
        <div>
            <h4 style="color: var(--maroon-deep); margin-bottom: 0.5rem; font-family: var(--font-sanskrit); font-size: 1.15rem;">॥ पारम्परिक वैदिक उपाय (Traditional Remedies) ॥</h4>
            <ul class="vedic-remedies-list">
                ${m.remedies.map(r => `<li>🕉️ ${r}</li>`).join('')}
            </ul>
        </div>
    `;

    const icon = m.severity === 'None' ? '🛡️' : (m.severity === 'Mild' ? '⚖️' : '🔥');

    box.innerHTML = `
        <div class="manglik-banner-alert ${m.severity === 'High' ? 'high-severity' : (m.severity === 'Mild' ? 'mild-severity' : '')}">
            <div class="manglik-big-icon">${icon}</div>
            <div>
                <h3 style="font-size: 1.35rem; color: var(--maroon-deep);">${m.status} (Severity: ${m.severity})</h3>
                <p style="color: var(--text-secondary); margin-top: 0.35rem;">${m.description}</p>
            </div>
        </div>
        ${cancelHtml}
        ${remediesHtml}
    `;
}

// ----------------- Professional Astrologer Report Renderer -----------------
function renderAstrologerReport(rep) {
    if (!rep) return;
    const container = document.getElementById('astrologerReportContainer');
    if (!container) return;

    // Helper to format bold markdown
    const mdToHtml = (txt) => {
        return (txt || '').replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    };

    // 1. Invocations & Preamble
    const preambleHtml = `
        <div class="report-preamble-card">
            <div class="report-invocation">${rep.invocation}</div>
            <h3 class="report-astrologer-heading">${rep.astrologer_title}</h3>
            <p class="report-preamble-text">${mdToHtml(rep.preamble)}</p>
        </div>
    `;

    // 2. Psychological Deep Profile (Public, Hidden, Passions, Strengths & Shadow)
    let psychoHtml = '';
    const psycho = rep.psychological_profile;
    if (psycho) {
        // Dual Persona: Public Persona vs Hidden Subconscious Self
        psychoHtml += `
            <div class="psycho-dual-grid">
                <div class="persona-card">
                    <div class="persona-header">
                        <span class="persona-icon">${psycho.public_persona.icon}</span>
                        <h4 class="persona-title">${psycho.public_persona.title}</h4>
                    </div>
                    <p class="persona-body">${mdToHtml(psycho.public_persona.text)}</p>
                </div>
                <div class="persona-card hidden-self">
                    <div class="persona-header">
                        <span class="persona-icon">${psycho.hidden_personality.icon}</span>
                        <h4 class="persona-title">${psycho.hidden_personality.title}</h4>
                    </div>
                    <p class="persona-body">${mdToHtml(psycho.hidden_personality.text)}</p>
                </div>
            </div>
        `;

        // Passions & What They Truly Love Doing
        if (psycho.passions_and_loves && psycho.passions_and_loves.items) {
            psychoHtml += `
                <div class="passions-card">
                    <h4 class="passions-title">
                        <span>${psycho.passions_and_loves.icon}</span>
                        ${psycho.passions_and_loves.title}
                    </h4>
                    <ul class="passions-list">
                        ${psycho.passions_and_loves.items.map(item => `
                            <li><span>⭐</span> <div>${mdToHtml(item)}</div></li>
                        `).join('')}
                    </ul>
                </div>
            `;
        }

        // Dual Spectrum: Strengths vs Shadow Weaknesses
        const pos = psycho.positive_strengths;
        const shadow = psycho.shadow_weaknesses;
        if (pos && shadow) {
            psychoHtml += `
                <div class="strengths-weaknesses-grid">
                    <div class="traits-column positive">
                        <div class="traits-header">
                            <span style="font-size: 1.5rem;">${pos.icon}</span>
                            <h4 class="traits-title pos-title">${pos.title}</h4>
                        </div>
                        <ul class="traits-list">
                            ${pos.items.map(item => `
                                <li><span class="trait-bullet-pos">✔</span> <div>${mdToHtml(item)}</div></li>
                            `).join('')}
                        </ul>
                    </div>
                    <div class="traits-column shadow">
                        <div class="traits-header">
                            <span style="font-size: 1.5rem;">${shadow.icon}</span>
                            <h4 class="traits-title neg-title">${shadow.title}</h4>
                        </div>
                        <ul class="traits-list">
                            ${shadow.items.map(item => `
                                <li><span class="trait-bullet-neg">⚠</span> <div>${mdToHtml(item)}</div></li>
                            `).join('')}
                        </ul>
                        ${shadow.karmic_remedy ? `
                            <div class="karmic-mastery-banner">
                                <div class="karmic-mastery-title">Karmic Mastery Guidance (आत्म-सुधार उपाय)</div>
                                <div class="karmic-mastery-text">${mdToHtml(shadow.karmic_remedy)}</div>
                            </div>
                        ` : ''}
                    </div>
                </div>
            `;
        }
    }

    // 3. Dedicated Career, Vocation & Swadharma Blueprint
    let careerHtml = '';
    const cbp = rep.career_blueprint;
    if (cbp) {
        careerHtml = `
            <div class="career-blueprint-card">
                <div class="career-blueprint-header">
                    <span class="career-icon">💼</span>
                    <div>
                        <h4 class="career-title">${cbp.title}</h4>
                        <p class="career-subtitle">Innate Talents, Strategic Applications, Ideal Careers & The Swadharma Calling</p>
                    </div>
                </div>

                <!-- 2-Col Grid: What you are good at vs Where to use it -->
                <div class="career-skills-grid">
                    <div class="career-skill-box">
                        <h5 class="skill-box-title"><span>🎯</span> What You Are Naturally Good At (जन्मजात कौशल व प्रतिभा)</h5>
                        <ul class="career-bullet-list">
                            ${cbp.natural_skills.map(s => `<li><span class="bullet-star">⭐</span> <div>${mdToHtml(s)}</div></li>`).join('')}
                        </ul>
                    </div>
                    <div class="career-skill-box">
                        <h5 class="skill-box-title"><span>🚀</span> Where To Apply Your Skills (व्यावहारिक उपयोग के सर्वोत्तम क्षेत्र)</h5>
                        <ul class="career-bullet-list">
                            ${cbp.where_to_use.map(w => `<li><span class="bullet-check">✔</span> <div>${mdToHtml(w)}</div></li>`).join('')}
                        </ul>
                    </div>
                </div>

                <!-- Recommended Careers Chips -->
                <div class="career-vocations-section">
                    <h5 class="vocation-title"><span>🏆</span> Highly Recommended Careers & Industries (सर्वोत्तम आजीविका एवं व्यवसाय):</h5>
                    <div class="career-chips-grid">
                        ${cbp.ideal_careers.map(c => `<span class="career-chip">${c}</span>`).join('')}
                    </div>
                </div>

                <!-- The Swadharma Calling: Do What You Truly Want To Do -->
                <div class="swadharma-calling-banner">
                    <div class="swadharma-badge">॥ स्वधर्म: वही करें जो आपका मन चाहे ॥</div>
                    <h5 class="swadharma-heading">Empowering Guidance: Follow Your Heart's Calling</h5>
                    <p class="swadharma-quote">${mdToHtml(cbp.swadharma_calling)}</p>
                </div>

                <!-- Financial Strategy -->
                <div class="financial-strategy-box">
                    <strong>💰 Wealth & Vocation Alignment:</strong>
                    <span>${mdToHtml(cbp.financial_strategy)} <em>(Detailed Financial Prosperity Strategy & Lakshmi Yoga analysis presented below)</em></span>
                </div>
            </div>
        `;
    }

    // 4. Dedicated Financial Prosperity Strategy & Lakshmi Yoga (धन सम्पति एवं लक्ष्मी योग)
    let finStrategyHtml = '';
    const fsp = rep.financial_strategy;
    if (fsp) {
        finStrategyHtml = `
            <div class="financial-strategy-card">
                <!-- Royal Lakshmi Header -->
                <div class="fin-strategy-header">
                    <div class="fin-lotus-icon">🪷</div>
                    <div class="fin-header-text">
                        <div class="fin-badge">॥ श्री महालक्ष्मी प्रसन्न • धन वैभव विवेचन ॥</div>
                        <h4 class="fin-card-title">${fsp.title}</h4>
                        <p class="fin-card-subtitle">Comprehensive Astrological Wealth Architecture: Personality Leakages, Classical Dhan Yogas, 12th House Drain, Support Avenues & Realism Filters</p>
                    </div>
                </div>

                <!-- SECTION 1: Behavioral Financial Matrix (Bad Habits vs Mindful Rules) -->
                <div class="fin-dual-grid">
                    <!-- Left: How you lose money -->
                    <div class="fin-matrix-box habits-box">
                        <div class="fin-box-header habit-header">
                            <span class="fin-header-icon">🚨</span>
                            <div>
                                <h5 class="fin-box-title habit-title">How You Could Lose Money Due to Bad Habits</h5>
                                <div class="fin-box-subtitle">(धन हानि के अवचेतन कारण एवं हानिकारक वित्तीय आदतें)</div>
                            </div>
                        </div>
                        <p class="fin-box-intro">Based on your horoscope and planetary nature, these behavioral blindspots represent your most hazardous cash drains:</p>
                        <ul class="fin-list habit-list">
                            ${(fsp.bad_habits_draining_money || []).map(h => `
                                <li>
                                    <span class="fin-bullet habit-bullet">⚠️</span>
                                    <div class="fin-item-text">${mdToHtml(h)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>

                    <!-- Right: Mindfulness Rules -->
                    <div class="fin-matrix-box rules-box">
                        <div class="fin-box-header rule-header">
                            <span class="fin-header-icon">🛡️</span>
                            <div>
                                <h5 class="fin-box-title rule-title">Astrological Mindfulness & Wealth Discipline</h5>
                                <div class="fin-box-subtitle">(वित्तीय अनुशासन, आत्म-संयम एवं संरक्षण के अचूक नियम)</div>
                            </div>
                        </div>
                        <p class="fin-box-intro">Vedic guidelines and non-negotiable boundaries formulated specifically to seal financial leaks and preserve compounding:</p>
                        <ul class="fin-list rule-list">
                            ${(fsp.mindful_rules || []).map(r => `
                                <li>
                                    <span class="fin-bullet rule-bullet">✔</span>
                                    <div class="fin-item-text">${mdToHtml(r)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>

                <!-- SECTION 2: Kundli Financial Yogas & 12th House (Vyaya) Drain -->
                <div class="fin-kundli-dual-section">
                    <!-- Active Classical Dhan Yogas in Chart -->
                    <div class="fin-yogas-card">
                        <div class="fin-subcard-header">
                            <span class="fin-subcard-icon">🌟</span>
                            <div>
                                <h5 class="fin-subcard-title">Classical Dhan & Lakshmi Yogas in Your Kundli</h5>
                                <div class="fin-subcard-sub">(आपकी जन्मपत्रिका में सक्रिय धन, लाभ एवं लक्ष्मी योग)</div>
                            </div>
                        </div>
                        <div class="fin-yogas-grid">
                            ${(fsp.financial_yogas || []).map(y => `
                                <div class="fin-yoga-item">
                                    <div class="fin-yoga-top">
                                        <div class="fin-yoga-name">${y.name}</div>
                                        <span class="fin-yoga-badge">${y.category || 'Dhana Yoga'}</span>
                                    </div>
                                    <div class="fin-yoga-desc">${mdToHtml(y.description)}</div>
                                </div>
                            `).join('')}
                        </div>
                    </div>

                    <!-- 12th House (Vyaya Bhava) Financial Drain Warning -->
                    ${fsp.vyaya_analysis ? `
                        <div class="fin-vyaya-card">
                            <div class="fin-subcard-header vyaya-header">
                                <span class="fin-subcard-icon">⚡</span>
                                <div>
                                    <h5 class="fin-subcard-title vyaya-title">12th House (व्यय भाव - Vyaya Bhava) Financial Leakage Analysis</h5>
                                    <div class="fin-subcard-sub">Cosmic Analysis of Planetary Inflow vs Inescapable Expenditure Outflow</div>
                                </div>
                            </div>
                            <div class="fin-vyaya-body">
                                <div class="vyaya-meta-row">
                                    <span class="vyaya-meta-pill"><strong>12th Bhava Sign:</strong> ${fsp.vyaya_analysis.sign_name} (${fsp.vyaya_analysis.sign_sanskrit})</span>
                                    <span class="vyaya-meta-pill"><strong>House Ruler:</strong> ${fsp.vyaya_analysis.lord}</span>
                                    <span class="vyaya-meta-pill"><strong>Occupants / Influences:</strong> ${fsp.vyaya_analysis.occupants.join(', ')}</span>
                                </div>
                                <div class="vyaya-content-grid">
                                    <div class="vyaya-block">
                                        <div class="vyaya-block-title">📉 Primary Financial Leakage Channel:</div>
                                        <div class="vyaya-block-text">${fsp.vyaya_analysis.leakage_sources.map(s => mdToHtml(s)).join('<br>')}</div>
                                    </div>
                                    <div class="vyaya-block">
                                        <div class="vyaya-block-title">🧠 Subconscious Psychological Trigger:</div>
                                        <div class="vyaya-block-text">${fsp.vyaya_analysis.psychological_triggers.map(t => mdToHtml(t)).join('<br>')}</div>
                                    </div>
                                    <div class="vyaya-block remedy-block">
                                        <div class="vyaya-block-title">🪔 Astrological & Practical Mitigation (व्यय रोकथाम उपाय):</div>
                                        <div class="vyaya-block-text">${fsp.vyaya_analysis.remedial_mitigations.map(m => mdToHtml(m)).join('<br>')}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    ` : ''}
                </div>

                <!-- SECTION 3: Opportunity Support vs What NOT to Expect -->
                <div class="fin-dual-grid">
                    <!-- Left: Opportunities You WILL Receive -->
                    <div class="fin-matrix-box support-box">
                        <div class="fin-box-header support-header">
                            <span class="fin-header-icon">🌱</span>
                            <div>
                                <h5 class="fin-box-title support-title">Opportunities & Financial Support You WILL Receive</h5>
                                <div class="fin-box-subtitle">(दैवीय कृपा, अनुकूल सहयोग एवं सुनिश्चित धनोपार्जन के स्रोत)</div>
                            </div>
                        </div>
                        <p class="fin-box-intro">Your astrological matrix naturally attracts backing, patronage, and wealth breakthroughs through these channels:</p>
                        <ul class="fin-list support-list">
                            ${(fsp.opportunities_and_support || []).map(o => `
                                <li>
                                    <span class="fin-bullet support-bullet">✨</span>
                                    <div class="fin-item-text">${mdToHtml(o)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>

                    <!-- Right: What You Will NOT Receive -->
                    <div class="fin-matrix-box false-hopes-box">
                        <div class="fin-box-header no-support-header">
                            <span class="fin-header-icon">⛔</span>
                            <div>
                                <h5 class="fin-box-title no-support-title">What You Will NOT Receive — False Hopes to Avoid</h5>
                                <div class="fin-box-subtitle">(मिथ्या आशाएं, अवास्तविक अपेक्षाएं एवं निषेध क्षेत्र)</div>
                            </div>
                        </div>
                        <p class="fin-box-intro">Astrological realism: Do NOT waste time, emotional energy, or capital chasing these unreliable illusions:</p>
                        <ul class="fin-list no-support-list">
                            ${(fsp.what_not_to_expect || []).map(w => `
                                <li>
                                    <span class="fin-bullet no-support-bullet">🚫</span>
                                    <div class="fin-item-text">${mdToHtml(w)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>

                <!-- SECTION 4: Sacred Mahalakshmi Wealth Stotra Banner -->
                <div class="fin-lakshmi-mantra-banner">
                    <div class="lakshmi-mantra-badge">॥ दारिद्र्य दहन महालक्ष्मी बीज साधना ॥</div>
                    <h5 class="lakshmi-mantra-heading">Sacred Mahalakshmi Wealth Manifestation Mantra</h5>
                    <div class="lakshmi-mantra-shloka">${fsp.wealth_mantra}</div>
                    <p class="lakshmi-mantra-guide"><strong>विधी एवं साधना निर्देश:</strong> ${fsp.wealth_mantra_instructions}</p>
                </div>
            </div>
        `;
    }

    // 5. Dedicated Marriage, Love & Partner Dynamics (दाम्पत्य, प्रेम एवं जीवनसाथी - Section 3)
    let marriageHtml = '';
    const mbp = rep.marriage_blueprint;
    if (mbp) {
        const loveExp = mbp.love_expression || {};
        const mType = mbp.marriage_type_analysis || {};
        const sp = mbp.spouse_profile || {};
        const app = sp.physical_appearance || {};
        const dyn = mbp.marital_dynamics || {};

        marriageHtml = `
            <div class="marriage-blueprint-card">
                <!-- Sacred Vivaha Header -->
                <div class="marriage-header">
                    <div class="marriage-icon">💍</div>
                    <div class="marriage-header-text">
                        <div class="marriage-badge">॥ दाम्पत्य सुखं भवतु • शुभ विवाह एवं जीवनसाथी योग ॥</div>
                        <h4 class="marriage-card-title">${mbp.title}</h4>
                        <p class="marriage-card-subtitle">Vedic Kalatra Bhava Insights: How You Express Love, Love vs Arranged Marriage Indicator, Future Spouse Physical & Behavioral Profile, Challenges & Harmony Rules</p>
                    </div>
                </div>

                <!-- SECTION 1: Love Expression & Partner Attraction Matrix (2-Col Grid) -->
                <div class="marriage-dual-grid">
                    <!-- Left: How You Express Love -->
                    <div class="marriage-matrix-box love-box">
                        <div class="marriage-box-header love-header">
                            <span class="marriage-header-icon">💖</span>
                            <div>
                                <h5 class="marriage-box-title love-title">How You Express Love & Affection</h5>
                                <div class="marriage-box-subtitle">(प्रेम एवं अनुराग की अभिव्यक्ति • Venus in ${loveExp.venus_sign || 'Venus'})</div>
                            </div>
                        </div>
                        <div class="love-language-pill">
                            <strong>Love Language:</strong> ${loveExp.love_language || ''}
                        </div>
                        <p class="marriage-body-text">${mdToHtml(loveExp.how_they_express || '')}</p>
                        <div class="heart-melt-box">
                            <strong>✨ What Melts Your Heart:</strong> ${mdToHtml(loveExp.what_melts_their_heart || '')}
                        </div>
                    </div>

                    <!-- Right: Karmic Partner Attraction -->
                    <div class="marriage-matrix-box attraction-box">
                        <div class="marriage-box-header attraction-header">
                            <span class="marriage-header-icon">🧲</span>
                            <div>
                                <h5 class="marriage-box-title attraction-title">Partner You Are Karmically Drawn To</h5>
                                <div class="marriage-box-subtitle">(आकर्षित होने वाला साथी • 7th House in ${mbp.seventh_house_sign} / ${mbp.seventh_house_sanskrit})</div>
                            </div>
                        </div>
                        <div class="attraction-pill">
                            <strong>7th House Lord:</strong> ${mbp.seventh_house_lord} • <strong>Influences:</strong> ${mbp.seventh_house_occupants.join(', ')}
                        </div>
                        <p class="marriage-body-text">${mdToHtml(mbp.partner_attraction_archetype || '')}</p>
                        <div class="karmic-mirror-box">
                            <strong>🪞 The Cosmic Mirror:</strong> Your 7th House represents the complementary energy your soul craves to achieve wholeness and lifelong equilibrium.
                        </div>
                    </div>
                </div>

                <!-- SECTION 2: Love vs Arranged Marriage Indicator -->
                <div class="marriage-type-card">
                    <div class="mtype-header">
                        <div class="mtype-left">
                            <span class="mtype-icon">⚖️</span>
                            <div>
                                <h5 class="mtype-heading">Love vs Arranged Marriage Indicator (विवाह का स्वरूप)</h5>
                                <div class="mtype-sub">Calculated via 5th-7th House Nexus, Rahu/Venus Placements & Jupiterian Dharma Alliances</div>
                            </div>
                        </div>
                        <div class="mtype-badge">${mType.probability_badge || 'Love-Cum-Arranged'}</div>
                    </div>
                    <div class="mtype-verdict-banner">
                        <div class="mtype-verdict-title">${mType.marriage_type || 'Marriage Prediction'}</div>
                        <p class="mtype-verdict-text">${mdToHtml(mType.marriage_verdict || '')}</p>
                    </div>
                    <div class="mtype-reasons-box">
                        <div class="mtype-reasons-title">Astrological Combinations in Your Kundli:</div>
                        <ul class="mtype-reasons-list">
                            ${(mType.astrological_reasons || []).map(r => `<li><span class="mtype-bullet">📜</span> <div>${mdToHtml(r)}</div></li>`).join('')}
                        </ul>
                    </div>
                </div>

                <!-- SECTION 3: Future Spouse Profile (Appearance, Personality & Behavior) -->
                <div class="spouse-profile-card">
                    <div class="spouse-profile-header">
                        <span class="spouse-icon">👰🤵</span>
                        <div>
                            <div class="spouse-badge">॥ भावी जीवनसाथी स्वरूप विवेचन ॥</div>
                            <h5 class="spouse-heading">${sp.archetype_title || 'Future Spouse Profile'}</h5>
                        </div>
                    </div>

                    <!-- 3-Column Detailed Spouse Breakdown -->
                    <div class="spouse-breakdown-grid">
                        <!-- Col 1: Physical Appearance & Style -->
                        <div class="spouse-feature-col appearance-col">
                            <div class="col-title"><span class="col-icon">✨</span> Physical Appearance & Style (शारीरिक रूप-रंग)</div>
                            <ul class="feature-spec-list">
                                <li>
                                    <strong>Stature & Build:</strong>
                                    <span>${app.stature_and_build || 'Graceful and well-proportioned.'}</span>
                                </li>
                                <li>
                                    <strong>Face & Features:</strong>
                                    <span>${app.face_and_features || 'Pleasing, symmetrical features with an attractive smile.'}</span>
                                </li>
                                <li>
                                    <strong>Eyes & Gaze:</strong>
                                    <span>${app.eyes_and_gaze || 'Expressive, warm, and communicative eyes.'}</span>
                                </li>
                                <li>
                                    <strong>Complexion & Hair:</strong>
                                    <span>${app.complexion_and_hair || 'Luminous healthy skin and lustrous hair.'}</span>
                                </li>
                                <li>
                                    <strong>Aesthetic & Style:</strong>
                                    <span>${app.aesthetic_and_style || 'Tasteful, elegant dressing with attention to color harmony.'}</span>
                                </li>
                            </ul>
                        </div>

                        <!-- Col 2: Personality Traits & Mindset -->
                        <div class="spouse-feature-col personality-col">
                            <div class="col-title"><span class="col-icon">🧠</span> Core Personality & Mindset (स्वभाव व गुण)</div>
                            <ul class="feature-bullets-list">
                                ${(sp.personality_traits || []).map(t => `<li><span class="feature-bullet">⭐</span> <div>${mdToHtml(t)}</div></li>`).join('')}
                            </ul>
                        </div>

                        <!-- Col 3: Behavioral Characteristics & Habits -->
                        <div class="spouse-feature-col behavior-col">
                            <div class="col-title"><span class="col-icon">🤝</span> Behavioral Dynamics with You (व्यवहार व आचरण)</div>
                            <ul class="feature-bullets-list">
                                ${(sp.behavioral_characteristics || []).map(b => `<li><span class="feature-bullet-check">✔</span> <div>${mdToHtml(b)}</div></li>`).join('')}
                            </ul>
                        </div>
                    </div>

                    <!-- Planetary Modifiers if 7th house has occupants -->
                    ${(sp.planetary_modifiers && sp.planetary_modifiers.length > 0) ? `
                        <div class="spouse-planetary-modifiers">
                            <div class="modifiers-title">Planetary Influences on Your Spouse (7th House Graha Prabhav):</div>
                            <ul class="modifiers-list">
                                ${sp.planetary_modifiers.map(m => `<li>${mdToHtml(m)}</li>`).join('')}
                            </ul>
                        </div>
                    ` : ''}
                </div>

                <!-- SECTION 4: Challenges & Harmony Solutions (2-Col Grid) -->
                <div class="marriage-dual-grid">
                    <!-- Left: Potential Challenges -->
                    <div class="marriage-matrix-box challenge-box">
                        <div class="marriage-box-header challenge-header">
                            <span class="marriage-header-icon">⚠️</span>
                            <div>
                                <h5 class="marriage-box-title challenge-title">Potential Challenges & Friction Points</h5>
                                <div class="marriage-box-subtitle">(वैवाहिक जीवन की संभावित चुनौतियां एवं सावधानियां)</div>
                            </div>
                        </div>
                        <ul class="marriage-bullet-list challenge-list">
                            ${(dyn.friction_points || []).map(f => `
                                <li><span class="challenge-bullet">⚡</span> <div>${mdToHtml(f)}</div></li>
                            `).join('')}
                        </ul>
                    </div>

                    <!-- Right: Golden Rules for Harmony -->
                    <div class="marriage-matrix-box harmony-box">
                        <div class="marriage-box-header harmony-header">
                            <span class="marriage-header-icon">🪔</span>
                            <div>
                                <h5 class="marriage-box-title harmony-title">Golden Rules for Lasting Marital Bliss</h5>
                                <div class="marriage-box-subtitle">(दाम्पत्य सुख, प्रेम संवर्धन एवं अखंड सौभाग्य के सूत्र)</div>
                            </div>
                        </div>
                        <ul class="marriage-bullet-list harmony-list">
                            ${(dyn.harmony_rules || []).map(r => `
                                <li><span class="harmony-bullet">🕊️</span> <div>${mdToHtml(r)}</div></li>
                            `).join('')}
                        </ul>
                    </div>
                </div>

                <!-- SECTION 5: Gentle Reassuring Astrological Disclaimer -->
                <div class="spouse-disclaimer-card">
                    <div class="disclaimer-header">
                        <span class="disclaimer-lotus">🌸</span>
                        <span class="disclaimer-title">A Gentle Astrological Note on Life’s Beautiful Mysteries</span>
                    </div>
                    <p class="disclaimer-body">${mbp.gentle_disclaimer}</p>
                </div>
            </div>
        `;
    }

    // 6. Dedicated Current Life Phase & Astrological Timing (वर्तमान जीवन काल विवेचन - Section 4)
    let lifePhaseHtml = '';
    const clp = rep.current_life_phase;
    if (clp) {
        lifePhaseHtml = `
            <div class="life-phase-card">
                <!-- Header with Hourglass / Kaal Chakra -->
                <div class="phase-header">
                    <div class="phase-icon">⏳</div>
                    <div class="phase-header-text">
                        <div class="phase-badge">॥ कालचक्र विवेचन • दशा एवं गोचर प्रभाव ॥</div>
                        <h4 class="phase-card-title">${clp.title}</h4>
                        <p class="phase-card-subtitle">Vedic Dasha Chronology: Present Reality, Emotional Currents, Karmic Blueprint, Prescribed Actions & Near-Future Horizon</p>
                    </div>
                    <div class="phase-timeline-badges">
                        <div class="dasha-pill mahadasha">
                            <span class="dasha-pill-label">Mahadasha:</span>
                            <strong>${clp.mahadasha_lord}</strong>
                            <span class="dasha-pill-date">thru ${clp.mahadasha_end}</span>
                        </div>
                        <div class="dasha-pill antardasha">
                            <span class="dasha-pill-label">Active Antardasha:</span>
                            <strong>${clp.antardasha_lord}</strong>
                            <span class="dasha-pill-date">thru ${clp.antardasha_end}</span>
                        </div>
                    </div>
                </div>

                <!-- SECTION 1: Present Circumstances vs Inner Emotional State (2-Col Grid) -->
                <div class="phase-dual-grid">
                    <!-- Left: Present Circumstances -->
                    <div class="phase-box circumstances-box">
                        <div class="phase-box-header circ-header">
                            <span class="phase-header-icon">🌍</span>
                            <div>
                                <h5 class="phase-box-title circ-title">Present Circumstances & Life Theme</h5>
                                <div class="phase-box-subtitle">(वर्तमान परिस्थितियां एवं सांसारिक परिवेश)</div>
                            </div>
                        </div>
                        <div class="phase-body-text">${mdToHtml(clp.present_circumstances)}</div>
                    </div>

                    <!-- Right: Emotional State -->
                    <div class="phase-box emotional-box">
                        <div class="phase-box-header emo-header">
                            <span class="phase-header-icon">🧠</span>
                            <div>
                                <h5 class="phase-box-title emo-title">Inner Emotional State & What You Are Feeling</h5>
                                <div class="phase-box-subtitle">(आंतरिक मनोदशा, भावनाएं एवं मानसिक स्थिति)</div>
                            </div>
                        </div>
                        <div class="phase-body-text">${mdToHtml(clp.emotional_state)}</div>
                    </div>
                </div>

                <!-- SECTION 2: Karmic Meaning & Current Challenges -->
                <div class="phase-karmic-grid">
                    <!-- Karmic Significance Card -->
                    <div class="phase-meaning-card">
                        <div class="phase-subcard-header meaning-header">
                            <span class="phase-subcard-icon">🕉️</span>
                            <div>
                                <h5 class="phase-subcard-title">Karmic Significance: What This Phase Means For You</h5>
                                <div class="phase-subcard-sub">(इस कालखंड का गूढ़ आध्यात्मिक एवं व्यावहारिक प्रयोजन)</div>
                            </div>
                        </div>
                        <div class="phase-body-text">${mdToHtml(clp.karmic_meaning)}</div>
                    </div>

                    <!-- Challenges Experienced Card -->
                    <div class="phase-challenges-card">
                        <div class="phase-subcard-header challenges-header">
                            <span class="phase-subcard-icon">⚡</span>
                            <div>
                                <h5 class="phase-subcard-title challenges-title">Current Challenges & Friction Points</h5>
                                <div class="phase-subcard-sub">(वर्तमान संघर्ष, दबाव एवं परीक्षा के क्षेत्र)</div>
                            </div>
                        </div>
                        <ul class="phase-challenges-list">
                            ${(clp.challenges || []).map(c => `
                                <li>
                                    <span class="challenge-sparkle">⚠️</span>
                                    <div class="challenge-item-text">${mdToHtml(c)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>

                <!-- SECTION 3: Practical Guidance Matrix (What to DO vs What to AVOID) -->
                <div class="phase-actions-grid">
                    <!-- Left: What to DO -->
                    <div class="phase-action-box do-box">
                        <div class="action-box-header do-header">
                            <span class="action-header-icon">🌱</span>
                            <div>
                                <h5 class="action-box-title do-title">What You SHOULD DO (शुभ एवं अनुशंसित कार्य)</h5>
                                <div class="action-box-sub">Empowered Actions, Strategic Habits & Productive Focus</div>
                            </div>
                        </div>
                        <ul class="action-list do-list">
                            ${(clp.what_to_do || []).map(item => `
                                <li>
                                    <span class="action-bullet do-bullet">✔</span>
                                    <div class="action-item-text">${mdToHtml(item)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>

                    <!-- Right: What to AVOID -->
                    <div class="phase-action-box avoid-box">
                        <div class="action-box-header avoid-header">
                            <span class="action-header-icon">⛔</span>
                            <div>
                                <h5 class="action-box-title avoid-title">What You SHOULD AVOID (सावधानियां एवं निषेध)</h5>
                                <div class="action-box-sub">Pitfalls, Impulsive Mistakes & Destructive Habits</div>
                            </div>
                        </div>
                        <ul class="action-list avoid-list">
                            ${(clp.what_to_avoid || []).map(item => `
                                <li>
                                    <span class="action-bullet avoid-bullet">🚫</span>
                                    <div class="action-item-text">${mdToHtml(item)}</div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>

                <!-- SECTION 4: Near Future Horizon -->
                <div class="phase-future-card">
                    <div class="future-header">
                        <span class="future-icon">🌅</span>
                        <div>
                            <div class="future-badge">॥ आगामी समय की संक्षिप्त रूपरेखा ॥</div>
                            <h5 class="future-heading">The Horizon Ahead: What the Near Future Holds</h5>
                        </div>
                    </div>
                    <p class="future-body-text">${mdToHtml(clp.near_future_outlook)}</p>
                </div>

                <!-- SECTION 5: Subtle Reassuring Disclaimer -->
                <div class="phase-disclaimer-card">
                    <div class="disclaimer-header">
                        <span class="disclaimer-lotus">🌸</span>
                        <span class="disclaimer-title">A Gentle Note on Astrological Timing & Free Will</span>
                    </div>
                    <p class="disclaimer-body">${clp.disclaimer}</p>
                </div>
            </div>
        `;
    }

    // 7. Dedicated Sacred Life Timeline & Key Karmic Milestones (जीवन कालक्रम एवं प्रमुख भाग्य चक्र - Section 5)
    let timelineHtml = '';
    const lmt = rep.life_milestones_timeline;
    if (lmt) {
        const hm = lmt.highlight_milestones || {};
        const marr = hm.marriage || {};
        const car = hm.career_breakthrough || {};
        const fin = hm.financial_breakthrough || {};
        const prop = hm.property_acquisition || {};
        const journey = lmt.chronological_journey || [];

        timelineHtml = `
            <div class="life-milestones-card" id="lifeMilestonesSection">
                <!-- Royal Timeline Header -->
                <div class="timeline-header">
                    <div class="timeline-header-icon">🛤️</div>
                    <div class="timeline-header-text">
                        <div class="timeline-badge">॥ जीवन कालक्रम • प्रमुख भाग्य चक्र एवं शुभ मुहूर्त ॥</div>
                        <h4 class="timeline-card-title">${lmt.title || 'Sacred Life Timeline & Key Karmic Milestones'}</h4>
                        <p class="timeline-card-subtitle">${lmt.subtitle || 'Vedic Vimshottari Dasha Chronology: Auspicious Windows for Vivaha, Career Zenith, Dhana Yoga & Life Milestones'}</p>
                    </div>
                </div>

                <!-- 4 Highlight Milestone Cards (Grid of 4) -->
                <div class="milestones-highlight-grid">
                    <!-- 1. Expected Marriage Year -->
                    <div class="milestone-highlight-card marriage-highlight">
                        <div class="m-card-top">
                            <span class="m-card-icon">💍</span>
                            <span class="m-status-pill ${marr.status && marr.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${marr.status || 'Golden Window'}</span>
                        </div>
                        <h5 class="m-card-title">${marr.title || 'Expected Marriage Window'}</h5>
                        <div class="m-year-display">
                            <span class="m-year-number">${marr.year_window || '2026 – 2028'}</span>
                            <span class="m-age-badge">${marr.age_window || 'Age 31 – 33'}</span>
                        </div>
                        <div class="m-dasha-pill">
                            <span class="m-dasha-label">Astrological Catalyst:</span>
                            <strong>${marr.active_dasha || '7th House Lord Dasha'}</strong>
                        </div>
                        <p class="m-card-desc">${mdToHtml(marr.astrological_catalyst || '')}</p>
                        <div class="m-guidance-box">
                            <strong>🕊️ Astrologer's Counsel:</strong> ${mdToHtml(marr.guidance || '')}
                        </div>
                    </div>

                    <!-- 2. Career Breakthrough Year -->
                    <div class="milestone-highlight-card career-highlight">
                        <div class="m-card-top">
                            <span class="m-card-icon">🚀</span>
                            <span class="m-status-pill ${car.status && car.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${car.status || 'Breakthrough Horizon'}</span>
                        </div>
                        <h5 class="m-card-title">${car.title || 'Career Breakthrough Year'}</h5>
                        <div class="m-year-display">
                            <span class="m-year-number">${car.year_window || '2027 – 2029'}</span>
                            <span class="m-age-badge">${car.age_window || 'Age 32 – 34'}</span>
                        </div>
                        <div class="m-dasha-pill">
                            <span class="m-dasha-label">Astrological Catalyst:</span>
                            <strong>${car.active_dasha || '10th House Lord Dasha'}</strong>
                        </div>
                        <p class="m-card-desc">${mdToHtml(car.astrological_catalyst || '')}</p>
                        <div class="m-guidance-box">
                            <strong>⚡ Astrologer's Counsel:</strong> ${mdToHtml(car.guidance || '')}
                        </div>
                    </div>

                    <!-- 3. Financial Breakthrough Year -->
                    <div class="milestone-highlight-card wealth-highlight">
                        <div class="m-card-top">
                            <span class="m-card-icon">💰</span>
                            <span class="m-status-pill ${fin.status && fin.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${fin.status || 'Wealth Horizon'}</span>
                        </div>
                        <h5 class="m-card-title">${fin.title || 'Financial Breakthrough Window'}</h5>
                        <div class="m-year-display">
                            <span class="m-year-number">${fin.year_window || '2029 – 2031'}</span>
                            <span class="m-age-badge">${fin.age_window || 'Age 34 – 36'}</span>
                        </div>
                        <div class="m-dasha-pill">
                            <span class="m-dasha-label">Astrological Catalyst:</span>
                            <strong>${fin.active_dasha || '2nd & 11th Lord Dasha'}</strong>
                        </div>
                        <p class="m-card-desc">${mdToHtml(fin.astrological_catalyst || '')}</p>
                        <div class="m-guidance-box">
                            <strong>🪔 Astrologer's Counsel:</strong> ${mdToHtml(fin.guidance || '')}
                        </div>
                    </div>

                    <!-- 4. Property & Asset Acquisition -->
                    <div class="milestone-highlight-card property-highlight">
                        <div class="m-card-top">
                            <span class="m-card-icon">🏡</span>
                            <span class="m-status-pill ${prop.status && prop.status.includes('ACTIVE') ? 'status-active' : 'status-upcoming'}">${prop.status || 'Asset Horizon'}</span>
                        </div>
                        <h5 class="m-card-title">${prop.title || 'Property Acquisition Window'}</h5>
                        <div class="m-year-display">
                            <span class="m-year-number">${prop.year_window || '2028 – 2030'}</span>
                            <span class="m-age-badge">${prop.age_window || 'Age 33 – 35'}</span>
                        </div>
                        <div class="m-dasha-pill">
                            <span class="m-dasha-label">Astrological Catalyst:</span>
                            <strong>${prop.active_dasha || '4th House Lord Dasha'}</strong>
                        </div>
                        <p class="m-card-desc">${mdToHtml(prop.astrological_catalyst || '')}</p>
                        <div class="m-guidance-box">
                            <strong>🌿 Astrologer's Counsel:</strong> ${mdToHtml(prop.guidance || '')}
                        </div>
                    </div>
                </div>

                <!-- Complete Chronological Journey Roadmap -->
                <div class="chronological-roadmap-box">
                    <div class="roadmap-header">
                        <span class="roadmap-icon">🧭</span>
                        <div>
                            <h5 class="roadmap-title">The Complete Chronological Life Trail (जीवन यात्रा कालक्रम)</h5>
                            <div class="roadmap-subtitle">Sequential Vimshottari Milestones from Foundation to Dharma Realization</div>
                        </div>
                    </div>

                    <div class="roadmap-timeline">
                        ${journey.map((item, idx) => `
                            <div class="timeline-step-card ${item.status_class || 'upcoming'}">
                                <div class="timeline-node-marker">
                                    <span class="node-bullet">${idx + 1}</span>
                                    <span class="node-icon">${item.category_icon || '⭐'}</span>
                                </div>
                                <div class="timeline-card-content">
                                    <div class="step-card-header">
                                        <div class="step-left">
                                            <span class="step-years">${item.year_range}</span>
                                            <span class="step-age">${item.age_range}</span>
                                        </div>
                                        <span class="step-status-tag ${item.status_class || 'upcoming'}">${item.status}</span>
                                    </div>
                                    <h6 class="step-heading">${item.title}</h6>
                                    <div class="step-dasha-tag">
                                        <span>⏳ Cosmic Catalyst:</span> <strong>${item.dasha_catalyst}</strong>
                                    </div>
                                    <p class="step-desc">${mdToHtml(item.astrological_rationale)}</p>
                                    <div class="step-guidance-note">
                                        <strong>🎯 Prescribed Focus:</strong> ${mdToHtml(item.actionable_guidance)}
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <!-- Timing Guidance & Reassuring Disclaimer -->
                <div class="timeline-disclaimer-card">
                    <div class="disclaimer-header">
                        <span class="disclaimer-lotus">🌸</span>
                        <span class="disclaimer-title">Astrological Timing & Personal Agency (काल एवं पुरुषार्थ)</span>
                    </div>
                    <p class="disclaimer-body">${lmt.timing_guidance_disclaimer || ''}</p>
                </div>
            </div>
        `;
    }

    // 6. Auspicious Yogas
    let yogasHtml = '';
    if (rep.yogas && rep.yogas.length > 0) {
        yogasHtml = `
            <div class="yoga-showcase-box">
                <h4 class="yoga-box-title"><span>🌟</span> विशेष ग्रह योग (Prominent Planetary Yogas)</h4>
                <div class="yogas-grid">
                    ${rep.yogas.map(y => `
                        <div class="yoga-item-card">
                            <div class="yoga-item-name">${y.name}</div>
                            <div class="yoga-item-desc">${y.description}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // 7. Remaining Life Domains
    let domainsHtml = '<div class="domains-stack">';
    (rep.domains || []).forEach(d => {
        if (cbp && d.id === 'career') return; // Handled by rich career_blueprint above
        if (mbp && d.id === 'marriage') return; // Handled by rich marriage_blueprint above
        domainsHtml += `
            <div class="domain-reading-card">
                <div class="domain-header">
                    <span class="domain-icon">${d.icon}</span>
                    <h4 class="domain-title">${d.title}</h4>
                </div>
                <div class="domain-body">${mdToHtml(d.content)}</div>
            </div>
        `;
    });
    domainsHtml += '</div>';

    // 4. Remedies Hero
    const rem = rep.remedies || {};
    const remediesHtml = `
        <div class="remedies-hero-card">
            <h4 class="remedies-heading">॥ व्यक्तिगत वैदिक उपाय एवं भाग्य संवर्धन (Personalized Vedic Remedies) ॥</h4>
            
            <div class="remedies-grid">
                <div class="remedy-box">
                    <span class="remedy-label">Auspicious Gemstone (भाग्य रत्न)</span>
                    <span class="remedy-val" style="color: var(--gold-temple);">${rem.bhagya_gemstone || 'Yellow Sapphire'}</span>
                    <span class="remedy-sub">${rem.wearing_rules || ''}</span>
                </div>
                <div class="remedy-box">
                    <span class="remedy-label">Auspicious Metal & Day</span>
                    <span class="remedy-val">${rem.lucky_metal || 'Gold'}</span>
                    <span class="remedy-sub">Wear during Shukla Paksha on recommended weekday.</span>
                </div>
                <div class="remedy-box">
                    <span class="remedy-label">Ishta Devata & Worship</span>
                    <span class="remedy-val">${rem.auspicious_deity || 'Lord Vishnu'}</span>
                    <span class="remedy-sub">Daily prayers foster peace, divine protection and prosperity.</span>
                </div>
                <div class="remedy-box">
                    <span class="remedy-label">Charity (दान परामर्श)</span>
                    <span class="remedy-val" style="font-size: 1.05rem;">${rem.charity_items || 'Yellow grains, food'}</span>
                    <span class="remedy-sub">Offer on auspicious days to appease planetary lords.</span>
                </div>
            </div>

            <div class="mantra-banner">
                <div class="mantra-title">Sacred Mahadasha Beej Mantra (महादशा बीज मन्त्र)</div>
                <div class="mantra-text">${rem.sacred_mantra || ''}</div>
                <p style="font-size: 0.82rem; color: #9a3412; margin-top: 0.4rem;">Chant 108 times daily using a Rudraksha or Tulsi mala facing East during morning hours.</p>
            </div>

            <div style="margin-top: 1rem;">
                <h5 style="color: var(--maroon-deep); margin-bottom: 0.5rem; font-weight: 700; font-size: 1rem;">Daily Astrological Guidance:</h5>
                <ul class="vedic-remedies-list">
                    ${(rem.daily_guidance || []).map(g => `<li>🪔 ${mdToHtml(g)}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;

    // 5. Astrologer Signature Seal
    const sig = rep.signature || {};
    const sealHtml = `
        <div class="astrologer-seal-box">
            <div class="seal-left">
                <div class="seal-stamp">
                    <span>ज्योतिष</span>
                    <span>प्रमाणित</span>
                </div>
                <div>
                    <div class="seal-title">${sig.name || 'Jyotishacharya Assessment Board'}</div>
                    <div style="font-size: 0.85rem; color: var(--text-secondary);">Date of Assessment: ${sig.date || ''}</div>
                </div>
            </div>
            <div class="seal-blessing">${sig.blessing || '॥ शुभमस्तु ॥'}</div>
        </div>
    `;

    // 6. Mandatory Legal & Astrological Disclaimer (At the end of the report)
    const defaultDisclaimer = "Disclaimer: This report is based purely on astrological interpretations and is intended for informational and guidance purposes only. Any decisions you make based on this report are entirely your own responsibility. We shall not be held legally liable for any loss, damage, or consequences arising from decisions made in reliance on the information provided in this report, to the extent permitted by applicable law.";
    const disclaimerRaw = rep.legal_disclaimer || defaultDisclaimer;
    const disclaimerBody = disclaimerRaw.replace(/^Disclaimer:\s*/i, '');

    const legalDisclaimerHtml = `
        <div class="report-legal-disclaimer-card" id="reportLegalDisclaimer">
            <div class="legal-disclaimer-header">
                <span class="legal-disclaimer-icon">⚠️</span>
                <span class="legal-disclaimer-badge">STATUTORY ASTROLOGICAL DISCLAIMER</span>
            </div>
            <div class="legal-disclaimer-body">
                <p class="legal-disclaimer-text">
                    <strong>Disclaimer:</strong> ${disclaimerBody}
                </p>
            </div>
        </div>
    `;

    container.innerHTML = preambleHtml + psychoHtml + careerHtml + finStrategyHtml + marriageHtml + lifePhaseHtml + timelineHtml + yogasHtml + domainsHtml + remediesHtml + sealHtml + legalDisclaimerHtml;
}
