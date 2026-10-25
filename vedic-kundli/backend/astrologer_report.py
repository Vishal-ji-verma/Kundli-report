"""
Professional Vedic Astrologer Analysis & Deep Psychological Life Reading.
Provides exhaustive psychological profiling:
- Public Persona (How others see them)
- Hidden Personality & Subconscious Drives (What they keep secret)
- Passions, Hobbies & What recharges their soul
- Dual Analysis: Divine Strengths vs Karmic Blindspots / Shadow Side
- Life Domains (Career, Wealth, Love, Marriage, Health, Spirituality, Current Dasha)
- Personalized Vedic Remedies, Gemstones, and Sacred Mantras.
"""

from datetime import datetime
from typing import Dict, Any, List, Tuple
from astro_engine import ZODIAC_SIGNS

# ==============================================================
# AUSPICIOUS GEMSTONES & VEDIC REMEDIES (GRAHA UPAYA)
# ==============================================================

GRAHA_UPAYA = {
    "Sun": {
        "gemstone": "Ruby (माणिक्य)",
        "metal": "Gold or Copper",
        "finger": "Ring Finger (अनामिका)",
        "day": "Sunday morning during Shukla Paksha",
        "mantra": "ॐ ह्रां ह्रीं ह्रौं सः सूर्याय नमः (Om Hraam Hreem Hroum Sah Suryaya Namah)",
        "daan": "Wheat, copper utensils, jaggery, red flowers, ruby",
        "deity": "Lord Surya / Gayatri Devi"
    },
    "Moon": {
        "gemstone": "Natural Pearl (मोती)",
        "metal": "Silver",
        "finger": "Little Finger (कनिष्ठिका)",
        "day": "Monday evening during Shukla Paksha",
        "mantra": "ॐ श्रां श्रीं श्रौं सः चन्द्राय नमः (Om Shraam Shreem Shroum Sah Chandraya Namah)",
        "daan": "Rice, milk, silver, white sweets, conch shell",
        "deity": "Lord Shiva / Parvati Devi"
    },
    "Mars": {
        "gemstone": "Red Coral (मूंगा)",
        "metal": "Gold or Copper",
        "finger": "Ring Finger (अनामिका)",
        "day": "Tuesday morning during Shukla Paksha",
        "mantra": "ॐ क्रां क्रीं क्रौं सः भौमाय नमः (Om Kraam Kreem Kroum Sah Bhaumaya Namah)",
        "daan": "Red lentils (masoor), copper, jaggery, saffron",
        "deity": "Lord Hanuman / Kartikeya"
    },
    "Mercury": {
        "gemstone": "Emerald (पन्ना)",
        "metal": "Gold or Bronze",
        "finger": "Little Finger (कनिष्ठिका)",
        "day": "Wednesday morning during Shukla Paksha",
        "mantra": "ॐ ब्रां ब्रीं ब्रौं सः बुधाय नमः (Om Braam Breem Broum Sah Budhaya Namah)",
        "daan": "Moong dal (green gram), green clothes, brass, emerald",
        "deity": "Lord Vishnu / Saraswati Devi"
    },
    "Jupiter": {
        "gemstone": "Yellow Sapphire (पुखराज)",
        "metal": "Gold or Brass",
        "finger": "Index Finger (तर्जनी)",
        "day": "Thursday morning during Shukla Paksha",
        "mantra": "ॐ ग्रां ग्रीं ग्रौं सः गुरवे नमः (Om Graam Greem Groum Sah Gurave Namah)",
        "daan": "Chana dal, turmeric, yellow cloth, gold, religious scriptures",
        "deity": "Lord Brihaspati / Dakshinamurthy"
    },
    "Venus": {
        "gemstone": "Diamond (हीरा) or White Zircon",
        "metal": "Silver or Platinum",
        "finger": "Middle or Little Finger",
        "day": "Friday morning during Shukla Paksha",
        "mantra": "ॐ द्रां द्रीं द्रौं सः शुक्राय नमः (Om Draam Dreem Droum Sah Shukraya Namah)",
        "daan": "White silk, curd, camphor, ghee, sugar",
        "deity": "Goddess Mahalakshmi"
    },
    "Saturn": {
        "gemstone": "Blue Sapphire (नीलम) or Amethyst (जमुनिया)",
        "metal": "Iron or Panchdhatu",
        "finger": "Middle Finger (मध्यमा)",
        "day": "Saturday sunset",
        "mantra": "ॐ प्रां प्रीं प्रौं सः शनैश्चराय नमः (Om Praam Preem Proum Sah Shanaishcharaya Namah)",
        "daan": "Mustard oil, black sesame, iron pan, black blanket",
        "deity": "Lord Shani / Lord Shiva"
    },
    "Rahu": {
        "gemstone": "Hessonite Garnet (गोमेद)",
        "metal": "Silver or Ashtadhatu",
        "finger": "Middle Finger",
        "day": "Saturday night",
        "mantra": "ॐ भ्रां भ्रीं भ्रौं सः राहवे नमः (Om Bhraam Bhreem Bhroum Sah Rahave Namah)",
        "daan": "Urad dal, lead, blue cloth, blankets to the needy",
        "deity": "Goddess Durga / Bhairava"
    },
    "Ketu": {
        "gemstone": "Cat's Eye (लहसुनिया)",
        "metal": "Silver or Panchdhatu",
        "finger": "Little Finger",
        "day": "Tuesday midnight",
        "mantra": "ॐ स्रां स्रीं स्रौं सः केतवे नमः (Om Sraam Sreem Sroum Sah Ketave Namah)",
        "daan": "Seven grains (satnaja), grey cloth, sesame seeds",
        "deity": "Lord Ganesha"
    }
}

# ==============================================================
# COMPREHENSIVE ASTROLOGICAL PSYCHOLOGICAL ARCHETYPES (12 SIGNS)
# ==============================================================

DEEP_SIGN_PROFILES = {
    "Aries": {
        "element": "Agni (Fire)",
        "ruler": "Mars (Mangal)",
        "public_persona": "The world sees you as a bold, energetic, commanding trailblazer who fears nobody. You walk with purpose, radiate natural authority, and people instinctively expect you to take charge in an emergency.",
        "hidden_personality": "Behind your fierce armor lies a secret fear of failure and being controlled. You rarely let anyone see how deeply vulnerability or disrespect hurts you. In private, you can feel exhausted from having to be the strong one, and you crave someone you can surrender control to without being judged.",
        "passions_and_loves": [
            "Competitive sports, athletics, martial arts, or high-octane physical challenges",
            "Starting new entrepreneurial ventures and spearheading ambitious projects from scratch",
            "Fast cars, mechanical gear, tech gadgets, or hands-on craftsmanship",
            "Spontaneous road trips, solo adventures, and exploring uncharted paths",
            "Defending the underdog and fighting for justice when you see unfairness"
        ],
        "positive_strengths": [
            "Fearless initiative: You do not hesitate; you act while others are still overthinking.",
            "Radical honesty: What people see is what they get; you despise deceit, pretense, and hidden agendas.",
            "Unstoppable resilience: Even after devastating setbacks, you pick yourself up and rebuild from zero.",
            "Inspiring courage: Your confidence is infectious, giving weaker souls the backbone to face their fears."
        ],
        "shadow_weaknesses": [
            "Explosive impatience: You demand immediate results and can lash out sharply when people move too slowly.",
            "Difficulty finishing what you start: You love the thrill of ignition but get bored during the maintenance phase.",
            "Blunt insensitivity: In your quest for truth, your words can wound sensitive hearts without you realizing it.",
            "Stubborn independence: Refusing to ask for help even when you are drowning in pressure."
        ],
        "karmic_advice": "Practice mindful pauses before reacting. Channel your volcanic fire through regular physical exercise and learn that true strength includes the courage to listen and wait."
    },
    "Taurus": {
        "element": "Prithvi (Earth)",
        "ruler": "Venus (Shukra)",
        "public_persona": "Others perceive you as remarkably calm, dependable, graceful, and unshakeable. People view you as a pillar of sanity—someone with exquisite taste, good manners, and an enviable sense of stability.",
        "hidden_personality": "Beneath your serene composure lies an intense fear of scarcity and unexpected disruptions. You hold on to possessions, memories, and people long after they have expired because change feels like an existential threat. When pushed past your limit, your hidden rage can be an earth-shattering bull-charge that shocks everyone.",
        "passions_and_loves": [
            "Gourmet culinary experiences, fine dining, artisanal cooking, and baking",
            "Collecting aesthetic, durable luxury items, watches, perfumes, and timeless art",
            "Gardening, nature retreats, spending quiet hours among trees and soil",
            "Sensory music, acoustic concerts, soothing interior design, and soft luxury textiles",
            "Financial investment analysis, real estate hunting, and building compounding wealth"
        ],
        "positive_strengths": [
            "Unwavering loyalty: Once you give your word or your heart, you stand by your people through every storm.",
            "Mastery of patience: You possess the rare gift of working methodically toward long-term goals without burning out.",
            "Sensory discernment: You have an innate eye for genuine quality, authentic value, and timeless beauty.",
            "Calming aura: Your grounded presence acts as an emotional anchor for chaotic, anxious individuals."
        ],
        "shadow_weaknesses": [
            "Legendary stubbornness: Once your mind is set, an army of arguments will not move you an inch.",
            "Material possessiveness: Equating emotional self-worth with bank balances and tangible assets.",
            "Comfort-zone paralysis: Staying in dead-end jobs or stale relationships merely because they are familiar.",
            "Passive resistance: When resentful, you shut down into cold, stubborn silence rather than communicating."
        ],
        "karmic_advice": "Embrace change as spiritual evolution, not destruction. Detach your identity from external possessions and practice shedding clutter periodically."
    },
    "Gemini": {
        "element": "Vayu (Air)",
        "ruler": "Mercury (Budha)",
        "public_persona": "The world sees you as a charismatic, witty, conversational genius who knows something about everything. You light up social rooms, effortlessly connect disparate people, and always have the latest insight.",
        "hidden_personality": "Underneath your sparkling humor lies a deep mental restlessness and a profound loneliness. You often feel fractured into multiple personas, wondering who you truly are when the audience leaves. You over-analyze your emotions instead of feeling them, using intellectual banter as a shield against true emotional intimacy.",
        "passions_and_loves": [
            "Reading multiple books simultaneously, podcasts, documentaries, and investigative deep-dives",
            "Creative writing, blogging, public speaking, debating, and expressive storytelling",
            "Social gatherings, trivia nights, networking mixers, and dynamic intellectual banter",
            "Exploring digital media, coding, linguistics, graphic arts, or mastering new instruments",
            "Frequent short travels, city hopping, and discovering quaint cafes and bookshops"
        ],
        "positive_strengths": [
            "Intellectual versatility: You grasp complex theories in minutes and synthesize them for common folk.",
            "Supreme adaptability: You can blend seamlessly into a boardroom, an artist's den, or a street market.",
            "Perennial youthfulness: A childlike curiosity that keeps your mind fresh, vibrant, and innovative forever.",
            "Diplomatic articulation: You know precisely which words to use to defuse tension or persuade opponents."
        ],
        "shadow_weaknesses": [
            "Superficial scatter: Starting ten passions simultaneously and dropping them as soon as hard discipline is required.",
            "Chronic nervous anxiety: An overactive brain that refuses to sleep, leading to mental exhaustion.",
            "Inconsistency: Changing your opinions or loyalties unpredictably based on the latest intellectual stimulus.",
            "Emotional evasion: Joking away serious relational crises rather than confronting deep heartaches."
        ],
        "karmic_advice": "Anchor your mercurial intellect through daily breathwork (Pranayama) and commit to mastering one single craft deeply rather than skimming ten on the surface."
    },
    "Cancer": {
        "element": "Jala (Water)",
        "ruler": "Moon (Chandra)",
        "public_persona": "Others see you as deeply caring, gentle, protective, and profoundly empathetic. Friends and colleagues treat you as their emotional sanctuary, feeling safe to confide their darkest secrets in you.",
        "hidden_personality": "Behind your gentle kindness lies a formidable, impenetrable fortress. You have an eidetic memory for every slight, betrayal, or harsh word ever spoken to you, silently nursing grudges for decades. You have a secret habit of emotionally testing people to see if they will abandon you.",
        "passions_and_loves": [
            "Creating a sacred, cozy home sanctuary adorned with plants, soft lighting, and antiques",
            "Cooking heartfelt meals for loved ones and hosting intimate family gatherings",
            "Collecting family heirlooms, ancestral memories, photo albums, and genealogy research",
            "Water retreats: Oceanside walks, lake visits, long warm baths, and moonlit meditation",
            "Creative expressions: Poetry, music composition, painting, and interior styling"
        ],
        "positive_strengths": [
            "Profound intuition: You sense people's true intentions before they even open their mouths.",
            "Unconditional nurturance: The capacity to love, heal, and restore broken spirits like nobody else.",
            "Fierce protector: Gentle as a lamb with friends, but a roaring lioness if anyone threatens your family.",
            "Enduring tenacity: Like the crab's claws, once you set your heart on a dream, you never let go."
        ],
        "shadow_weaknesses": [
            "Emotional mood swings: Shifting from radiant joy to sullen gloom with the waxing and waning of the Moon.",
            "Passive-aggressive withdrawal: Expecting others to telepathically know why you are upset instead of speaking.",
            "Living in the past: Replaying old heartbreaks and emotional hurts like an endless loop.",
            "Smothering possessiveness: Wanting loved ones so close that you unintentionally stifle their independence."
        ],
        "karmic_advice": "Learn to forgive and release the baggage of the past. Realize that loving someone means giving them wings, not an emotional tether."
    },
    "Leo": {
        "element": "Agni (Fire)",
        "ruler": "Sun (Surya)",
        "public_persona": "The world sees you as a natural monarch—regal, warm-hearted, radiant, and larger than life. You carry yourself with unmissable dignity, magnetic charisma, and an aura of effortless triumph.",
        "hidden_personality": "Beneath your golden crown lies a tender, fragile heart terrified of mediocrity, rejection, or public embarrassment. You secretly crave constant appreciation and can be crushed by simple indifference. You often bear massive burdens in silence because your pride forbids you from showing any weakness.",
        "passions_and_loves": [
            "Performing arts, theater, public speaking, center-stage spotlight, and entertaining",
            "Curating a grand wardrobe, fine jewelry, haute couture, and regal luxury aesthetics",
            "Mentoring youth, championing creative talent, and leading visionary organizations",
            "Throwing lavish celebrations, celebrations of life, and memorable dining events",
            "Creative sovereignty: Directing cinema, writing epic sagas, or building a brand of personal legacy"
        ],
        "positive_strengths": [
            "Magnanimous generosity: You give with both hands and celebrate the victories of others with genuine warmth.",
            "Unyielding loyalty: You are a loyal commander; those who stand by you receive your lifelong protection.",
            "Natural leadership: You inspire bravery in others during crises when everyone else is shrinking back.",
            "Radiant vitality: An innate solar optimism that banishes darkness and despair wherever you go."
        ],
        "shadow_weaknesses": [
            "Ego hypersensitivity: Taking constructive feedback as a personal insult to your dignity.",
            "Entitlement: A subconscious assumption that the universe owes you the throne without ordinary labor.",
            "Craving validation: Allowing your happiness to depend on how many cheers or compliments you receive.",
            "Dramatic overreaction: Turning minor disagreements into operatic battles of honor."
        ],
        "karmic_advice": "True royalty serves without demanding applause. Practice humility and remember that the Sun warms the Earth silently, asking for nothing in return."
    },
    "Virgo": {
        "element": "Prithvi (Earth)",
        "ruler": "Mercury (Budha)",
        "public_persona": "Others see you as the ultimate problem solver—sharp, composed, impeccably organized, and reliable. People trust you with their most complex dilemmas because they know you make zero sloppy mistakes.",
        "hidden_personality": "Inside your mind is a courtroom that never recesses, where you put yourself on trial 24 hours a day. Your secret torment is an agonizing inner critic that whispers that whatever you do is never quite good enough. You carry an immense burden of worry about catastrophes that almost never materialize.",
        "passions_and_loves": [
            "Holistic wellness, herbalism, biohacking, yoga, and organic nutrition research",
            "Organizing systems, spreadsheets, financial budgeting, and optimizing daily routines",
            "Editorial writing, diagnostic research, investigative debugging, and puzzles",
            "Caring for rescued animals, volunteering for community causes, and eco-restoration",
            "Crafts requiring micro-precision: Calligraphy, watchmaking, coding, or pottery"
        ],
        "positive_strengths": [
            "Flawless discernment: You can identify the one broken gear in a million-piece machine in seconds.",
            "Selfless dedication: You find profound dignity in humble, quiet service that holds organizations together.",
            "Diagnostic wisdom: An instinctive talent for natural healing, dietary balance, and mental decluttering.",
            "Unshakable integrity: You despise corruption, shortcuts, and false promises; your work is bulletproof."
        ],
        "shadow_weaknesses": [
            "Chronic perfectionism: Delaying projects indefinitely because they are not 100% flawless.",
            "Hyper-critical demeanor: Picking apart colleagues and partners under the guise of 'just helping'.",
            "Somatic anxiety: Translating mental stress into digestive troubles, insomnia, and nervous exhaustion.",
            "Difficulty receiving: Always giving and fixing for others while feeling deeply guilty if someone helps you."
        ],
        "karmic_advice": "Embrace the Japanese aesthetic of *Wabi-Sabi*—finding beauty in the imperfect. Give yourself the same mercy, grace, and tenderness you offer so generously to others."
    },
    "Libra": {
        "element": "Vayu (Air)",
        "ruler": "Venus (Shukra)",
        "public_persona": "The world sees you as effortlessly charming, elegant, diplomatic, and aesthetically sophisticated. You have a soothing voice, a disarming smile, and people naturally feel attractive and valued around you.",
        "hidden_personality": "Beneath your pleasant diplomacy lies an exhausting battle with indecision and people-pleasing. You secretly suppress your real anger and desires to avoid awkward friction, leading to hidden resentment. You struggle deeply with being alone, often staying in unfulfilling dynamics rather than confronting solitude.",
        "passions_and_loves": [
            "High art galleries, symphony concerts, ballet, and visiting heritage architecture",
            "Fashion styling, personal grooming, perfume collections, and curated interior spaces",
            "Hosting civilized dinner parties, intellectual salon discussions, and relationship mediation",
            "Practicing partner dance, tennis, yoga, or balanced mindfulness disciplines",
            "Advocating for civil liberties, human rights, arbitration, and judicial justice"
        ],
        "positive_strengths": [
            "Master of equilibrium: An extraordinary ability to see every side of an issue without emotional bias.",
            "Social alchemy: Bringing enemies together and creating harmonious partnerships where others see discord.",
            "Refined aesthetic eye: Turning ordinary environments into spaces of grace, harmony, and elegance.",
            "Gentle diplomacy: Achieving through polite sweetness what aggressive bullies fail to accomplish with force."
        ],
        "shadow_weaknesses": [
            "Agonizing indecisiveness: Torturing yourself over trivial choices for fear of choosing wrong.",
            "Conflict avoidance: Swallowing the bitter truth and offering polite lies just to keep the peace.",
            "Codependency: Losing your own identity, goals, and voice inside partnerships.",
            "Passive manipulation: Using charm and covert guilt to get your way without direct confrontation."
        ],
        "karmic_advice": "Real peace is not the absence of conflict; it is the presence of truth. Speak your authentic mind boldly, even if it temporarily upsets the harmony."
    },
    "Scorpio": {
        "element": "Jala (Water)",
        "ruler": "Mars & Ketu",
        "public_persona": "Others see you as mysterious, intense, magnetic, and possessing an x-ray gaze that looks right through them. People either revere your power or feel slightly intimidated by your silent, brooding depth.",
        "hidden_personality": "Behind your fortress of secrecy lies an oceanic emotional sensitivity. You guard your heart with barbed wire because when you love, you love with total soul-fusion, and betrayal feels like literal death to you. You secretly test people's loyalty relentlessly before granting them an inch of trust.",
        "passions_and_loves": [
            "Occult sciences: Vedic astrology, Kundalini yoga, Tantra, psychology, and tarot",
            "Investigative research, uncovering hidden corruption, crime mysteries, and forensics",
            "Intense physical transformations, endurance training, and pushing bodily limits",
            "Solitary nights, deep philosophical conversations under the stars, and shadow work",
            "Managing crises, turnaround investments, and revitalizing bankrupt or ruined projects"
        ],
        "positive_strengths": [
            "Phoenix resilience: You can be destroyed, burned to ashes, and rise again more terrifyingly powerful.",
            "Lie detector: You detect hypocrisy and deceit instantaneously; nobody can con or bamboozle you.",
            "Unmatched depth of devotion: If you love someone, you will walk into the gates of hell to defend them.",
            "Transformative power: An innate capacity to catalyze profound spiritual and psychological rebirth in others."
        ],
        "shadow_weaknesses": [
            "Destructive obsession: Fixating on enemies, past betrayals, or perceived slights with venomous intensity.",
            "Vindictiveness: A refusal to let go until the scales of retribution have been balanced to your liking.",
            "Suffocating secrecy: Demanding absolute transparency from partners while hiding your own cards completely.",
            "Paranoid suspicion: Projecting dark motives onto innocent mistakes and driving away genuine lovers."
        ],
        "karmic_advice": "Surrender the need to control life through suspicion. True power is not in holding a venomous sting; it is in the courage to forgive and let your heart soften."
    },
    "Sagittarius": {
        "element": "Agni (Fire)",
        "ruler": "Jupiter (Guru)",
        "public_persona": "The world sees you as a jovial, philosophical, honest wanderer with a hearty laugh and a contagious thirst for adventure. You are seen as the free spirit who cannot be caged and who always brings good fortune.",
        "hidden_personality": "Behind your booming optimism lies a secret dread of boredom, commitment, and claustrophobia. When reality becomes tedious or routine, your instinct is to run away to the next horizon rather than doing the boring emotional work. You secretly struggle with dogmatism, believing you hold the exclusive patent on truth.",
        "passions_and_loves": [
            "International travel, backpacking through sacred ancient sites, and learning foreign languages",
            "Philosophical debates, comparative religion, publishing, and spiritual scholarship",
            "Outdoor expeditions: Trekking mountain trails, horse riding, camping, and wilderness exploration",
            "Mentoring, higher education, motivational speaking, and inspiring crowds",
            "Archery, martial ethics, comedy, and exploring alternative belief systems"
        ],
        "positive_strengths": [
            "Expansive optimism: A sacred faith in the benevolence of the cosmos that turns dark skies into dawn.",
            "Philosophical breadth: The ability to see the forest when everyone else is lost arguing about individual trees.",
            "Radical truth-telling: Free from petty malice, you speak truth with refreshing, purifying candor.",
            "Cosmic generosity: Sharing wisdom, resources, and joy without counting the cost."
        ],
        "shadow_weaknesses": [
            "Preachy self-righteousness: Lecturing others on how to live while ignoring your own blindspots.",
            "Commitment evasion: Fleeing when relationships or jobs demand slow, patient, unglamorous consistency.",
            "Tactless bluntness: Dropping verbal bombs without caring about the emotional shrapnel left behind.",
            "Gambling on over-optimism: Over-promising and under-delivering because you assume luck will cover the gap."
        ],
        "karmic_advice": "Learn that the greatest pilgrimage is not across continents, but inward into daily stillness. Ground your soaring ideals in patient, disciplined daily reality."
    },
    "Capricorn": {
        "element": "Prithvi (Earth)",
        "ruler": "Saturn (Shani)",
        "public_persona": "Others perceive you as serious, mature, exceptionally capable, and ambitious. You are regarded as an old soul who commands respect without raising your voice—the adult in the room who can shoulder any burden.",
        "hidden_personality": "Inside, you often carry a profound existential melancholy and an intense fear of vulnerability. Because you likely had to grow up too early, you struggle to play, laugh, or trust that anyone will care for you if you are not being 'useful'. You secretly long to lay down your heavy armor and simply be loved for who you are, not what you achieve.",
        "passions_and_loves": [
            "Building long-term legacy projects, architectural engineering, and organizational design",
            "Antiques collection, ancient history research, stone masonry, and geological exploration",
            "Financial structuring, wealth preservation, venture investments, and stock compounding",
            "High-altitude mountain climbing, marathon endurance challenges, and chess",
            "Woodworking, sculpting, vintage mechanics, and restoring classic items"
        ],
        "positive_strengths": [
            "Monumental endurance: While flashier personalities burn out, you keep marching until the summit is won.",
            "Rock-solid dependability: If you say it will be done, the world can set its watch by your delivery.",
            "Strategic mastery: Playing a 20-year chess game while competitors are distracted by tomorrow's trends.",
            "Benevolent stewardship: Creating lasting institutions, businesses, and family legacies that outlive you."
        ],
        "shadow_weaknesses": [
            "Cynical pessimism: Assuming the worst in every situation and killing spontaneous joy with cold realism.",
            "Workaholic martyrdom: Measuring human worth solely by productivity, status, and grueling struggle.",
            "Emotional coldness: Locking away feelings behind an icy wall of pragmatism and professional detachment.",
            "Authoritarian rigidity: Demanding that everyone adhere to your strict rules and timetable."
        ],
        "karmic_advice": "Life is not an endless examination to be endured; it is a sacred lila (play) to be savored. Allow yourself to play, laugh, and celebrate the journey before reaching the peak."
    },
    "Aquarius": {
        "element": "Vayu (Air)",
        "ruler": "Saturn & Rahu",
        "public_persona": "The world sees you as an intellectual visionary, unique, avant-garde, and humanitarian. You stand out from the crowd without trying, famous for your unconventional ideas and egalitarian worldview.",
        "hidden_personality": "Behind your friendly camaraderie lies an emotional alienation. You feel like an alien anthropologist observing humanity from an orbit above. You genuinely love humanity in the abstract, but on an individual intimate level, you can feel terrified of emotional messiness and suffocation, leading you to abruptly vanish into your cold tower.",
        "passions_and_loves": [
            "Cutting-edge science: Artificial intelligence, quantum physics, space exploration, and futuristic tech",
            "Grassroots activism, social reform movements, and human rights causes",
            "Alternative subcultures, indie electronic music, sci-fi literature, and astrology",
            "Building community forums, open-source collaborative networks, and think tanks",
            "Aviation, coding, eccentric inventions, and studying revolutionary history"
        ],
        "positive_strengths": [
            "Visionary foresight: You can see the cultural and technological trends of the next century today.",
            "Zero prejudice: You treat kings and beggars with the exact same dignified, authentic respect.",
            "Intellectual fearlessness: Unafraid to hold unpopular opinions and dismantle decaying orthodoxies.",
            "True altruism: Motivated by the collective evolution and liberation of humanity, not selfish greed."
        ],
        "shadow_weaknesses": [
            "Emotional detachment: Treating deep intimate relationships like academic research projects.",
            "Contrarian rebellion: Rebelling against rules purely for the sake of being different, even when rules are sensible.",
            "Dogmatic intellectual pride: Condescending toward those whose minds operate slower than your lightning brain.",
            "Unpredictable ghosting: Suddenly disconnecting from friends and lovers when emotional demands feel too close."
        ],
        "karmic_advice": "Bridge the gap between your brilliant cosmic mind and your human heart. Remember that the greatest wisdom is not found in cold logic, but in tender, humble human empathy."
    },
    "Pisces": {
        "element": "Jala (Water)",
        "ruler": "Jupiter (Guru)",
        "public_persona": "Others see you as an ethereal, poetic, compassionate dreamer with eyes that gaze into another dimension. People feel an immediate sense of peace, forgiveness, and magic in your presence.",
        "hidden_personality": "Beneath your gentle, sweet exterior lies a dangerous tendency toward escapism and a secret martyrdom complex. Because you absorb the emotional sludge of everyone around you like a psychic sponge, the real world can feel painfully harsh. In secret, you may retreat into fantasies, addictions, or savior-victim dynamics to avoid concrete reality.",
        "passions_and_loves": [
            "Mystical arts: Meditation, lucid dreaming, music composition, and poetry",
            "Cinema, visual arts, theatrical fantasy, photography, and creative fiction",
            "Ocean retreats, swimming, sailing, and spending days in quiet sanctuary near water",
            "Animal rescue, caring for the abandoned, psychic healing, and hospice volunteering",
            "Studying ancient spiritual scriptures, Bhakti yoga, chanting, and sacred temple visits"
        ],
        "positive_strengths": [
            "Divine empathy: An unbounded heart that feels the pain of all sentient beings with christ-like tenderness.",
            "Mystical creativity: Channeling masterpieces from subtle spiritual realms that bring viewers to tears.",
            "Psychic receptivity: Knowing things before they happen through dreams, synchronicities, and gut premonitions.",
            "Forgiving grace: The divine capacity to forgive the unforgivable and see the spark of God in the fallen."
        ],
        "shadow_weaknesses": [
            "Porous boundaries: Allowing users, manipulators, and energetic vampires to drain your vitality dry.",
            "Escapist avoidance: Running away from financial obligations, difficult talks, or deadlines into dreamlands.",
            "Playing the victim: Harboring subconscious bitterness that you sacrifice everything while nobody saves you.",
            "Delusional idealization: Projecting angelic qualities onto toxic partners and ignoring obvious red flags."
        ],
        "karmic_advice": "Compassion without boundaries is self-destruction. Build healthy emotional walls, ground your mystical gifts in practical daily discipline, and be your own savior first."
    }
}


# ==============================================================
# VOCATION & CAREER BLUEPRINTS (12 ZODIAC SIGNS)
# ==============================================================

CAREER_BLUEPRINTS = {
    "Aries": {
        "natural_skills": [
            "Rapid crisis decision-making: Unflinching composure and swift action when others freeze under extreme pressure.",
            "Pioneering initiative: The innate instinct to launch brand-new concepts, ventures, and prototypes from scratch.",
            "Commanding leadership: Natural charisma that rallies teams and motivates them to conquer formidable objectives.",
            "High stamina & tenacity: The energy to outwork competitors and break through bureaucratic roadblocks."
        ],
        "where_to_use": [
            "High-growth startups, venture incubators, and early-stage disruptive technology environments.",
            "Crisis response, emergency management, field operations, and corporate turnaround units.",
            "Competitive arenas such as intellectual litigation, sports management, and high-stakes negotiation.",
            "Autonomous positions where you have full sovereignty over execution without micromanagement."
        ],
        "ideal_careers": [
            "Tech Founder / Serial Entrepreneur",
            "Executive Director / Operations Head",
            "Emergency Surgeon / Critical Care Specialist",
            "Defense, Military & Security Strategist",
            "Civil Infrastructure & Real Estate Developer",
            "Sports Agent / High-Performance Coach",
            "Venture Capital Catalyst"
        ],
        "swadharma_calling": "Vedic wisdom proclaims: *'श्रेयान्स्वधर्मो विगुणः परधर्मात्स्वनुष्ठितात्'* (Better is one's own authentic dharma, however imperfect, than another's path performed flawlessly). You were born to be an initiator and leader, not a passive paper-pusher. If your heart burns to build something independent, do not let cautious, timid voices talk you out of your fire. Do what you truly want to do—your greatest wealth and fulfillment will blossom only when you bet on your own courage.",
        "financial_strategy": "Wealth comes to you through bold initiatives and calculated early moves. Avoid gambling on impulse; pair your aggressive earning power with disciplined, automated investments that lock in your gains."
    },
    "Taurus": {
        "natural_skills": [
            "Asset valuation & financial compounding: An uncanny instinct for real, tangible, lasting worth.",
            "Sensory aesthetic mastery: Supreme taste in design, form, texture, architecture, and quality materials.",
            "Unshakeable patience: The ability to nurture a business or investment methodically across decades.",
            "Operational reliability: Creating stable, frictionless systems that function seamlessly."
        ],
        "where_to_use": [
            "Wealth management firms, private equity, institutional banking, and real estate development.",
            "Luxury lifestyle brands, architecture studios, haute cuisine, and fine art curation.",
            "Sustainable agriculture, organic supply chains, and green infrastructure.",
            "Treasury management and environments demanding rock-solid fiscal conservatism."
        ],
        "ideal_careers": [
            "Investment Banker / Portfolio Wealth Manager",
            "Architectural & Interior Design Director",
            "Luxury Brand Strategist / Art Appraiser",
            "High-End Real Estate Developer",
            "Restaurateur / Gourmet Food Producer",
            "Agricultural Enterprise Founder",
            "Financial Controller / Chief Financial Officer (CFO)"
        ],
        "swadharma_calling": "You cannot thrive in high-stress, chaotic, disposable industries that demand constant frantic pivoting. Follow your authentic desire for beauty, substance, and security. Do what brings you deep sensory pride and peace of mind. Build things designed to outlive you. When you do what you genuinely love with your signature patience, Goddess Lakshmi blesses you with enduring abundance.",
        "financial_strategy": "You are a master accumulator. Your wealth multiplies exponentially through land, prime properties, dividend-yielding equities, and physical assets. Avoid high-risk speculative fads; steady compounding is your royal road."
    },
    "Gemini": {
        "natural_skills": [
            "Rapid information synthesis: Grasping intricate multi-disciplinary concepts in minutes and translating them effortlessly.",
            "Persuasive articulation: Exceptional verbal and written agility that can sell ideas to any demographic.",
            "Dynamic networking: Bridging diverse people, industries, and networks to create unprecedented synergies.",
            "Agile pivoting: Navigating sudden market disruptions with intellectual humor and fresh ideas."
        ],
        "where_to_use": [
            "Media conglomerates, podcasting networks, digital publishing, and content ecosystems.",
            "High-velocity technology firms, software product management, and developer relations.",
            "Public relations, high-stakes trade negotiations, and strategic communications.",
            "Cross-border commerce, consulting firms, and modern educational innovation."
        ],
        "ideal_careers": [
            "Digital Media Mogul / Journalist / Author",
            "Product Strategist in AI & Tech Software",
            "Public Relations & Communications Director",
            "Foreign Trade Negotiator / Diplomatic Liaison",
            "Marketing Strategist / Copywriting Lead",
            "FinTech Consultant / Brokerage Specialist",
            "University Lecturer / Podcaster / Content Creator"
        ],
        "swadharma_calling": "Do not allow conventional society to force you into a single, monotonous, specialized cubicle. Your mind is a kaleidoscope. If you want to run a software business by day, write books by evening, and trade assets on weekends—embrace your multi-hyphenate brilliance! Do what genuinely excites your curiosity. Your true vocation lies wherever knowledge, words, and human connection meet.",
        "financial_strategy": "Multiple streams of income are natural for you. Monetize your ideas, IP rights, royalties, and communication channels. Guard against scattering capital into too many speculative side projects."
    },
    "Cancer": {
        "element": "Jala (Water)",
        "natural_skills": [
            "Profound emotional intelligence: Sensing unseen corporate undercurrents and customer sentiment intuitively.",
            "Nurturing team leadership: Building loyal, family-like organizations where people work with their whole hearts.",
            "Prudent risk assessment: An innate instinct for self-preservation and protecting assets against downturns.",
            "Tenacious memory & storytelling: Connecting historical wisdom with modern community needs."
        ],
        "where_to_use": [
            "Healthcare networks, psychiatric clinics, wellness centers, and specialized hospitals.",
            "Real estate brokerage, residential property development, and home design.",
            "Hospitality empires, luxury resorts, boutique hotels, and culinary institutions.",
            "Human resources leadership, social welfare trusts, and child/family development foundations."
        ],
        "ideal_careers": [
            "Healthcare Executive / Clinical Psychologist",
            "Boutique Hospitality & Hotelier Founder",
            "Residential Real Estate Developer",
            "Chief People Officer / HR Director",
            "Family Office & Wealth Preservation Advisor",
            "Author / Biographer / Screenwriter",
            "Marine & Environmental Conservation Director"
        ],
        "swadharma_calling": "Your greatest career power is not cold calculation—it is your immense heart and intuitive radar. Do what you genuinely care about on a human level. When your work protects, heals, feeds, or shelters people, you become unstoppable. Follow your calling to create sanctuaries of safety in a harsh world; financial prosperity will flow to you naturally as a karmic blessing.",
        "financial_strategy": "You are naturally thrifty and protective. Invest in residential real estate, gold, and tangible assets that provide emotional and financial peace. Avoid emotional over-spending during stressful periods."
    },
    "Leo": {
        "natural_skills": [
            "Magnetic executive presence: Radiating confidence, optimism, and warmth that inspires instant loyalty.",
            "Grand creative vision: The ability to envision majestic, inspiring outcomes and orchestrate talent to manifest them.",
            "Natural showmanship: Thriving in the center-stage spotlight and delivering unforgettable public presentations.",
            "Unyielding dignity: Refusing to compromise on quality, honor, and organizational reputation."
        ],
        "where_to_use": [
            "Executive suites (C-level leadership), boardrooms, and institutional figurehead roles.",
            "Entertainment, theatrical cinema, high fashion, and luxury entertainment.",
            "Political administration, civil governance, and public advocacy.",
            "Brand ambassadorship, motivational keynote speaking, and premium mentorship programs."
        ],
        "ideal_careers": [
            "Chief Executive Officer (CEO) / Founder",
            "Film Director / Creative Producer / Actor",
            "Political Leader / High Government Administrator",
            "Luxury Brand Ambassador / Fashion Director",
            "Keynote Speaker / High-Performance Mentor",
            "Philanthropic Foundation President",
            "Venture Capital Managing Partner"
        ],
        "swadharma_calling": "You were born with the soul of a monarch; you will wither and lose your spirit if you spend your life executing someone else's petty vision. Step onto the stage you were meant to occupy. Do what sets your creative pride ablaze. Pursue the high-visibility, high-impact calling that makes you feel genuinely alive. When you shine your light generously to elevate others, the world will crown your efforts.",
        "financial_strategy": "You love grand spending and generous gestures. Balance your taste for luxury by designating a portion of your revenue to automatic, untouchable wealth-compounding vaults before spending."
    },
    "Virgo": {
        "natural_skills": [
            "Algorithmic precision: An unmatched ability to detect errors, optimize workflows, and refine processes to perfection.",
            "Analytical diagnostics: Dissecting massive mountains of chaotic data into clear, actionable, elegant solutions.",
            "Humble mastery: Total dedication to craftsmanship and delivering flawless, bulletproof deliverables.",
            "Holistic health wisdom: An innate understanding of nutrition, biology, and systems balance."
        ],
        "where_to_use": [
            "High-complexity data science, artificial intelligence validation, and algorithmic development.",
            "Financial auditing, forensic accounting, compliance, and corporate risk management.",
            "Biotechnology, pharmaceutical research, surgical diagnostics, and specialized medicine.",
            "Quality assurance, continuous improvement methodologies (Six Sigma), and systems architecture."
        ],
        "ideal_careers": [
            "Chief Technology Officer (CTO) / Chief Information Officer (CIO)",
            "Data Science & AI Validation Director",
            "Forensic Auditor / Chief Financial Officer (CFO)",
            "Pharmaceutical Research Lead / Medical Specialist",
            "Management Consultant / Lean Operations Architect",
            "Nutrition & Holistic Wellness Entrepreneur",
            "Editor-in-Chief / Investigative Technical Writer"
        ],
        "swadharma_calling": "Silence your inner critic that whispers you are not ready yet. You have mastered details that others overlook entirely. Do not remain perpetually in the background polishing other people's dreams. Launch your own consulting, diagnostic, or tech venture. Pursue what engages your brilliant analytical brain, and trust that your dedication to quality is your golden ticket to wealth.",
        "financial_strategy": "You are naturally prudent with money. Your greatest wealth comes from specialized consulting fees, equity in well-run businesses, and data-driven investments. Avoid over-analyzing investment opportunities to the point of missing market windows."
    },
    "Libra": {
        "natural_skills": [
            "Diplomatic arbitration: Defusing high-tension disputes and finding win-win compromises where others see deadlocks.",
            "Aesthetic symmetry: An intuitive talent for elegance, proportion, beauty, and modern design.",
            "Partnership orchestration: Structuring alliances, joint ventures, and synergistic commercial deals.",
            "Charming persuasion: Achieving through grace, intellect, and etiquette what aggressive personalities fail to achieve by force."
        ],
        "where_to_use": [
            "Corporate legal practices, dispute resolution, international diplomacy, and arbitration.",
            "High-end fashion houses, interior architecture, cosmetic beauty, and contemporary galleries.",
            "Mergers & Acquisitions (M&A), talent agencies, and strategic business development.",
            "Public relations, luxury event curation, and high-stakes media liaison."
        ],
        "ideal_careers": [
            "Corporate Attorney / International Arbitrator",
            "Diplomat / Foreign Affairs Envoy",
            "Creative Director in Haute Couture / Interior Design",
            "Mergers & Acquisitions (M&A) Dealmaker",
            "Talent & Entertainment Agent / Publicist",
            "Art Gallery Director / Luxury Retail Mogul",
            "Executive Relationship & Alliance Manager"
        ],
        "swadharma_calling": "Stop subordinating your professional hunger to please colleagues or maintain a false sense of peace. You possess formidable social and commercial intellect. Follow the vocation that fulfills your passion for justice, beauty, and refined commerce. When you back your gentle charm with bold ambition, you will command both supreme respect and financial prosperity.",
        "financial_strategy": "Joint ventures and strategic partnerships multiply your wealth. Ensure all contracts and financial agreements are formal, legally airtight, and balanced so your generosity is never exploited."
    },
    "Scorpio": {
        "natural_skills": [
            "Penetrative psychological radar: Seeing through corporate deceit, hidden agendas, and masked balance sheets instantly.",
            "Crisis mastery: Thriving in high-stress, life-or-death, or bankrupt situations that paralyze ordinary mortals.",
            "Relentless research: An obsession with getting to the absolute root truth of any complex dilemma.",
            "Phoenix regeneration: Transforming dying companies, broken systems, or distressed assets into gold."
        ],
        "where_to_use": [
            "Cybersecurity, counter-intelligence, forensic investigation, and corporate espionage defense.",
            "Distressed asset investment, turnaround private equity, and bankruptcy restructuring.",
            "Specialized surgery, oncology, psychiatric depth work, and clinical research.",
            "Strategic risk advisory, crisis management, and proprietary trading."
        ],
        "ideal_careers": [
            "Cybersecurity Strategist / Intelligence Officer",
            "Turnaround Venture Capitalist / Distressed Asset Fund Manager",
            "Specialized Surgeon / Neuropsychiatrist",
            "Forensic Investigator / Financial Fraud Detective",
            "Occult Researcher / Vedic Astrologer / Depth Psychologist",
            "Risk Management Director / Commodity Trader",
            "Mergers & Acquisitions Defense Strategist"
        ],
        "swadharma_calling": "You cannot survive in shallow, cheerful, superficial environments where people play corporate games. You require deep intensity, challenge, and transformative power. Do what makes you feel like an investigator solving the ultimate puzzle. Step boldly into the dark, complex, high-risk territories that frighten others—that is precisely where your greatest financial fortune and soul satisfaction await.",
        "financial_strategy": "You excel at identifying undervalued, overlooked, or distressed assets before the herd wakes up. Leverage your research instincts. Protect your wealth through confidential, diversified, and highly secure structures."
    },
    "Sagittarius": {
        "natural_skills": [
            "Macro-philosophical vision: Synthesizing vast global trends and inspiring teams with infectious optimism.",
            "Cross-cultural storytelling: Connecting with people of every nation, faith, and ideology with authentic respect.",
            "Pedagogical wisdom: Mentoring, teaching, and translating profound philosophical insights into life guidance.",
            "Ethical conviction: Championing causes of justice, higher truth, and spiritual liberation."
        ],
        "where_to_use": [
            "International institutions, global travel enterprises, and transnational NGOs.",
            "Universities, academic research institutes, publishing houses, and think tanks.",
            "High courts, jurisprudence bodies, ethical advisory boards, and public policy.",
            "Spiritual academies, wellness publishing, motivational touring, and documentary filmmaking."
        ],
        "ideal_careers": [
            "University Dean / Professor of Higher Thought",
            "International Foreign Correspondent / Travel Author",
            "Supreme Court Jurist / Human Rights Advocate",
            "Global Travel Enterprise / Expedition Founder",
            "Publishing Mogul / Motivational Keynote Orator",
            "Philosophical / Spiritual Mentor & Author",
            "Global ESG & Sustainable Development Director"
        ],
        "swadharma_calling": "You cannot be chained to a desk doing repetitive bookkeeping without your soul slowly suffocating. You need horizontal horizons and vertical wisdom. Follow your urge to teach, travel, publish, and explore. Do what connects you to the wider world. When you follow your quest for authentic truth rather than chasing cheap safety, Jupiter rewards you with abundant fortune.",
        "financial_strategy": "Wealth comes through global ventures, intellectual property, publishing royalties, and international trade. Guard against over-optimistic speculation or reckless expansion; pair your vision with a grounded financial advisor."
    },
    "Capricorn": {
        "natural_skills": [
            "Architect of enduring legacy: The ability to conceptualize a 30-year roadmap and execute it with calm discipline.",
            "Pragmatic realism: Seeing through hype and building on unshakeable foundations of math, law, and reality.",
            "Emotional stoicism: Unruffled by short-term market panic, recessions, or temporary setbacks.",
            "Stewardship of power: Managing massive organizational hierarchies with dignified, fair authority."
        ],
        "where_to_use": [
            "Fortune 500 boardrooms, industrial manufacturing conglomerates, and civil infrastructure.",
            "Government administrative services, policy enforcement, and sovereign wealth stewardship.",
            "Commercial construction, mining, natural resources, and heavy engineering.",
            "Private equity holding companies and multi-generational family office enterprises."
        ],
        "ideal_careers": [
            "Managing Director / Chief Executive Officer (CEO)",
            "Infrastructure & Heavy Engineering Mogul",
            "Sovereign Wealth Fund / Institutional Asset Manager",
            "Senior Government Bureaucrat / Civil Administrator",
            "Real Estate Holding Company Patriarch/Matriarch",
            "Supply Chain & Global Logistics Magnate",
            "Corporate Governance & Ethics Director"
        ],
        "swadharma_calling": "You are built to build empires, but make sure it is an empire YOU actually want to live in. Do not climb a mountain of someone else's choosing simply out of duty. Follow your own authentic ambition to build a monument of excellence. When your grueling discipline is paired with genuine love for your craft, your name will be remembered for generations.",
        "financial_strategy": "You are the ultimate wealth preserver and compounder. Your fortune accumulates like a glacier—slow, unstoppable, and monumental. Invest in blue-chip equities, commercial land, and cash-flow-generating businesses."
    },
    "Aquarius": {
        "natural_skills": [
            "Avant-garde technological foresight: Conceptualizing systems, protocols, and products decades ahead of culture.",
            "Radical humanitarian vision: Solving global challenges through decentralized, egalitarian, collective frameworks.",
            "Unconventional problem solving: Dismantling obsolete orthodoxies with revolutionary logic.",
            "Community mobilization: Bringing eccentric, brilliant minds together into cohesive innovative collectives."
        ],
        "where_to_use": [
            "Artificial intelligence research laboratories, robotics, quantum computing, and aerospace.",
            "Renewable energy, decentralized finance (DeFi), and open-source collaborative technologies.",
            "Social impact enterprises, civil liberty think tanks, and global reform movements.",
            "Alternative energy grids, urban sustainability, and technological innovation hubs."
        ],
        "ideal_careers": [
            "Artificial Intelligence & Quantum Computing Pioneer",
            "Aerospace Engineer / Space Commercialization Director",
            "Decentralized Technology & Blockchain Architect",
            "Renewable Energy & CleanTech Enterprise Founder",
            "Think Tank Director / Future Trend Forecaster",
            "Social Reform & Human Liberation Advocate",
            "Independent Technology Inventor / R&D Scientist"
        ],
        "swadharma_calling": "Do not waste your genius trying to fit into traditional corporate molds that were designed for conformists. You are an emissary from the future. If your chosen passion appears eccentric, strange, or too avant-garde to traditionalists—pursue it with everything you have! Follow the revolutionary ideas that keep you awake at night. The future will pay homage to the path you forge today.",
        "financial_strategy": "Wealth flows to you through patents, groundbreaking technological intellectual property, network effects, and progressive investments. Maintain liquidity so you can pivot into the next technological revolution rapidly."
    },
    "Pisces": {
        "natural_skills": [
            "Boundaryless creative imagination: Channeling transcendent art, cinema, music, and literature from higher realms.",
            "Empathic healing intuition: The ability to understand human suffering and restore mental and spiritual peace.",
            "Subtle pattern recognition: Sensing hidden cultural moods, spiritual currents, and emerging aesthetic waves.",
            "Selfless devotion: A willingness to serve noble causes with unconditional grace and dedication."
        ],
        "where_to_use": [
            "Cinematic film production, music composition, theatrical fantasy, and immersive fine arts.",
            "Holistic wellness sanctuaries, psychiatric healing, spiritual retreats, and hospice care.",
            "International maritime research, ocean conservation, and charitable foundations.",
            "Spiritual academies, creative writing studios, and cross-border humanitarian missions."
        ],
        "ideal_careers": [
            "Cinematographer / Film Director / Creative Producer",
            "Musical Composer / Lyricist / Fine Artist",
            "Psychiatrist / Holistic Healer / Hypnotherapist",
            "Spiritual Mentor / Mystic Author / Meditation Master",
            "International Humanitarian Envoy / NGO Founder",
            "Oceanographic & Marine Conservation Specialist",
            "Luxury Retreat & Spa Hospitality Visionary"
        ],
        "swadharma_calling": "You cannot survive in cold, cutthroat, predatory corporate environments that treat humans like disposable commodities. Do not trade your soul for a sterile paycheck. Follow your authentic creative, healing, or spiritual dream. Do what fills your eyes with wonder and your heart with tears of beauty. When you dedicate your life to art, compassion, and uplifting souls, the divine universe orchestrates abundant financial support for you.",
        "financial_strategy": "You require creative freedom, but money requires grounded boundaries. Work with an honest, pragmatic financial advisor who can protect your earnings, manage contracts, and safeguard your assets while you create."
    }
}

# ==============================================================
# FINANCIAL PROSPERITY STRATEGY & LAKSHMI YOGA BLUEPRINTS
# ==============================================================

FINANCIAL_STRATEGY_BLUEPRINTS = {
    "Aries": {
        "bad_habits_draining_money": [
            "Impulsive Rage-Buying & Spontaneous Splurging: Buying high-ticket items (gadgets, cars, gear) on a sudden emotional whim without sleeping on the decision.",
            "Speculative Gambling & High-Risk 'Get-Rich-Quick' Schemes: Pouring large capital into volatile options, untested cryptos, or unverified angel bets purely for the dopamine rush.",
            "Ego-Driven Competitiveness: Spending heavily just to appear more affluent, successful, or dominant than rivals in social circles.",
            "Impatience with Compounding: Selling quality investments prematurely because they are taking too long to double, chasing the next shiny breakout instead."
        ],
        "mindful_rules": [
            "Enforce a mandatory 72-hour cooling-off rule on any non-essential purchase exceeding ₹25,000 / $300.",
            "Automate wealth accumulation: Automatically transfer 30% of income directly into untouchable index funds and gold before it touches your checking account.",
            "Never invest capital when in an excited, angry, or euphoric state of mind. Consult a dispassionate advisor.",
            "Avoid partnering with yes-men; you need a conservative co-founder or accountant who has the courage to tell you 'NO'."
        ],
        "opportunities_and_support": [
            "First-Mover Wealth: Massive windfalls from being among the first to enter a new market, technology, or real estate corridor.",
            "Sweat-Equity Multipliers: High financial rewards from turning around failing businesses or executing high-stakes emergency projects.",
            "Direct Leadership Compensation: High performance bonuses, founder equity, and uncapped profit-sharing arrangements.",
            "Government, Defense & Land Gains: Lucrative opportunities through commercial infrastructure, real estate acquisition, or government contracts."
        ],
        "what_not_to_expect": [
            "Do NOT expect effortless passive inheritances or handed-down family fortunes without intense strings attached.",
            "Do NOT count on informal loans to friends or colleagues being repaid—any money lent without ironclad legal collateral will likely vanish.",
            "Do NOT expect speculative day-trading to yield sustainable lifetime security; your chart rewards direct creation, not screen gambling."
        ]
    },
    "Taurus": {
        "bad_habits_draining_money": [
            "Luxury Lifestyle Inflation: Insisting on premier brand names, top-shelf wines, five-star hospitality, and designer aesthetics even during lean financial quarters.",
            "Stubborn Denial in Bad Investments: Refusing to cut losses on declining stocks or soured real estate because your pride hates admitting you made a wrong choice.",
            "Physical Asset Hoarding: Tying up an excessive percentage of net worth in illiquid heirlooms, jewelry, and land while suffering from day-to-day cashflow crunches.",
            "Comfort-Zone Inertia: Passing up lucrative expansion opportunities because you dread the initial stress and change required to scale."
        ],
        "mindful_rules": [
            "Set strict pre-defined stop-loss limits on every investment. If an asset drops by 15%, liquidate without emotional attachment.",
            "Maintain at least 12 months of living expenses in ultra-liquid, risk-free emergency debt instruments so you never sell real estate in a panic.",
            "Audit your recurring luxury subscriptions, memberships, and high-end upkeep expenses twice a year.",
            "Distinguish clearly between true appreciating assets and depreciating luxury toys masquerading as investments."
        ],
        "opportunities_and_support": [
            "Multi-Generational Real Estate: Immense financial compounding through prime land, residential rental portfolios, and commercial properties.",
            "Spousal Financial Elevation: Substantial wealth consolidation, joint assets, or family backing arriving post-matrimony.",
            "Consistent Compounding: Steady, unbreakable growth through dividend aristocrats, consumer monopolies, and agricultural commodities.",
            "Patronage of Affluent Clients: High-paying retainers from ultra-wealthy patrons who value your exquisite aesthetic taste and discretion."
        ],
        "what_not_to_expect": [
            "Do NOT expect sudden overnight windfall gains from hyper-volatile, abstract financial innovations.",
            "Do NOT expect financial freedom if you stubbornly remain in a comfortable, low-paying salaried role out of fear of market disruption.",
            "Do NOT rely on speculative partners who promise instant riches; your path to wealth is patient, methodical architecture."
        ]
    },
    "Gemini": {
        "bad_habits_draining_money": [
            "Micro-Expense Bleeding: Unconsciously wasting thousands on scattered digital subscriptions, abandoned courses, gadget accessories, and cafe runs.",
            "Shiny-Object Syndrome: Jumping between five different side-hustles, abandoning them the moment initial momentum slows, thus wasting startup capital.",
            "Over-Reliance on Verbal Agreements: Closing business deals on a friendly handshake and a coffee chat without formal, written legal contracts.",
            "Nervous Trading: Constantly buying and selling stocks on emotional news headlines, eroding your principal balance through transaction fees and taxes."
        ],
        "mindful_rules": [
            "Consolidate your financial accounts: Never have more than two active bank accounts and one clean brokerage account.",
            "Never sign or launch a venture without an objective attorney or accountant vetting the contract.",
            "Commit to a minimum 3-year holding period for any investment; disable trading notifications on your phone to curb restless tinkering.",
            "Focus your intellectual energy on scaling ONE primary business or revenue stream before launching satellite side-projects."
        ],
        "opportunities_and_support": [
            "Intellectual Property & Royalties: Lucrative passive revenue from digital products, books, licensing, software code, and media archives.",
            "Brokerage & Arbitrage Gains: High commissions through connecting affluent buyers with specialized sellers or negotiating major cross-border deals.",
            "Multiple Diverse Income Streams: Earning concurrently through consulting, tech advisory, content licensing, and equity options.",
            "Support from Siblings & Peer Networks: Strategic business collaborations, profitable referrals, and co-founding synergies through close friends."
        ],
        "what_not_to_expect": [
            "Do NOT expect long-term financial security if you continue changing your career focus every 18 months.",
            "Do NOT count on vague promised equity or profit-sharing percentages that are not notarized on stamped legal agreements.",
            "Do NOT expect heavy physical manufacturing or slow capital-intensive industrial plants to suit your cashflow style."
        ]
    },
    "Cancer": {
        "bad_habits_draining_money": [
            "Guilt-Driven Financial Lending: Lending hard-earned savings to troubled family members or manipulative friends who play on your emotional sympathy.",
            "Emotional Retail Therapy: Splurging on comfort shopping, home decor, or expensive gifts for others when feeling lonely, anxious, or undervalued.",
            "Irrational Financial Paranoia: Stashing cash in depreciating zero-interest accounts out of fear of market volatility, allowing inflation to eat your wealth.",
            "Mixing Family with Business: Employing unqualified relatives or forgiving unpaid business debts out of misplaced familial obligation."
        ],
        "mindful_rules": [
            "Adopt an unshakeable personal policy: Never lend money to loved ones that you cannot afford to write off completely as an outright gift.",
            "Automate equity and inflation-beating investments so you are not tempted to leave excessive liquid cash idle.",
            "Establish a firm boundary between family life and commercial enterprises; never give management authority without performance metrics.",
            "Wait 48 hours after an intense emotional argument or heartbreak before making any major financial expenditure or asset liquidation."
        ],
        "opportunities_and_support": [
            "Maternal & Ancestral Blessings: Financial backing, gifted real estate, or heritage property inherited from maternal roots or family trusts.",
            "Hospitality, Food & Care Industries: High recurring profits through businesses that provide shelter, food, wellness, and emotional comfort to communities.",
            "Residential Real Estate Flipping: Exceptional timing in purchasing neglected residential properties, renovating them tastefully, and reselling for massive margins.",
            "Deep Customer Loyalty: Customers who fall in love with your genuine care and become lifetime, non-price-sensitive patrons."
        ],
        "what_not_to_expect": [
            "Do NOT expect money lent to relatives to be returned with gratitude; it will almost always breed resentment instead.",
            "Do NOT expect cold, algorithmic, purely quantitative financial models to satisfy your soul; you need businesses with human heart.",
            "Do NOT expect financial peace if your personal home life is in constant chaos; your financial prosperity is tethered to domestic tranquility."
        ]
    },
    "Leo": {
        "bad_habits_draining_money": [
            "The 'King's Tab' Syndrome: Insisting on paying lavish bills for entire entourages, dinner parties, and luxury outings just to protect your regal reputation.",
            "Prestige Over Profits: Spending excessive operational capital on opulent offices, fancy business cards, and PR campaigns before securing cashflow.",
            "Prideful Refusal to Bargain: Viewing financial negotiation, couponing, or asking for discounts as beneath your dignity.",
            "Flattery Blindness: Investing in ventures proposed by sycophants who stroke your ego and tell you how brilliant you are."
        ],
        "mindful_rules": [
            "Never invest in any deal presented at a social party or lavish dinner; insist on reviewing pitch decks soberly in daylight with an accountant.",
            "Separate personal vanity from corporate budgeting: Measure business success by net profit margins, not gross social prestige.",
            "Let others pick up the check regularly; true nobility does not need to buy social admiration with bank cards.",
            "Maintain an anonymous, discreet wealth reserve that nobody in your social circle knows exists."
        ],
        "opportunities_and_support": [
            "Royal / Government Patronage: Lucrative government tenders, prestigious corporate chairmanships, and institutional state backing.",
            "Executive Leadership Premiums: Commanding top-tier advisory retainers, director fees, and premium equity packages due to your commanding stature.",
            "Luxury Brand Equity: Ability to charge 5x to 10x higher prices because customers perceive your personal brand as the gold standard.",
            "Entertainment & Media Royalties: Immense revenue through creative direction, high-ticket events, cinema, and luxury merchandising."
        ],
        "what_not_to_expect": [
            "Do NOT expect to retain wealth if your social overhead exceeds your operating revenue; vanity is your financial Achilles heel.",
            "Do NOT rely on fair-weather sycophants who applaud your lavish parties; they will vanish during financial winters.",
            "Do NOT expect humble low-margin, high-volume discount businesses to satisfy your temperament; you belong at the premium tier."
        ]
    },
    "Virgo": {
        "bad_habits_draining_money": [
            "Penny-Wise, Pound-Foolish: Agonizing over saving ₹100 on groceries while missing out on ₹10,00,000 growth opportunities due to analysis paralysis.",
            "Under-Pricing Your Genius: Charging modest, humble fees for world-class, meticulous work because you falsely believe 'it was easy for me'.",
            "Burnout Healthcare Expenses: Neglecting physical rest until your body forces you to spend heavily on medical treatments, specialists, and therapies.",
            "Micro-Managing Outsource Costs: Refusing to delegate administrative tasks to assistants, thereby wasting your high-value diagnostic hours on $10/hr chores."
        ],
        "mindful_rules": [
            "Immediately double your professional consulting rates or product prices; your standard of perfection is 3x higher than industry norms.",
            "Delegate all tasks below your hourly earning potential; your time must be fiercely guarded for high-impact diagnostics and strategy.",
            "Set a 2-week deadline for making investment decisions; stop researching the 100th technical indicator and pull the trigger.",
            "Treat health, ergonomic furniture, organic nutrition, and restorative retreats as non-negotiable wealth investments, not optional luxuries."
        ],
        "opportunities_and_support": [
            "Diagnostic & Forensic Consulting: Premium corporate retainers for identifying hidden fraud, system bottlenecks, and compliance vulnerabilities.",
            "Algorithmic & Tech IP: Significant equity and royalties from building efficient software, healthcare algorithms, and workflow architectures.",
            "Healthcare, Wellness & Organic Supply: Steady, recession-proof revenue from essential health products, analytical labs, and diagnostics.",
            "Institutional Performance Bonuses: Outsized financial rewards from employers and clients who cannot function without your operational oversight."
        ],
        "what_not_to_expect": [
            "Do NOT expect to build vast wealth if you remain an underpaid, self-sacrificing employee doing everyone else's work in silence.",
            "Do NOT expect charismatic, fast-talking sales promoters to deliver on their promises; verify every audit trail yourself.",
            "Do NOT expect perfection from market conditions; wealth is made by investing during messy, uncertain phases."
        ]
    },
    "Libra": {
        "bad_habits_draining_money": [
            "Aesthetic Indulgence & Social Image Maintenance: Spending beyond means on designer wardrobes, cosmetic upkeep, and socializing to preserve an elegant persona.",
            "Relational Codependency: Financing the lifestyle, debts, or failed ventures of romantic partners out of fear of abandonment or loneliness.",
            "Indecisive Market Stalling: Watching prime investment opportunities pass by while agonizing between two equally attractive options.",
            "Unwillingness to Enforce Invoices: Delaying chasing late client payments because you feel embarrassed or fear being perceived as rude."
        ],
        "mindful_rules": [
            "Automate invoice collection: Employ a firm accounting manager or automated billing software so you never have to personally ask clients for money.",
            "Keep separate pre-nuptial and distinct commercial bank accounts; never co-mingle your core survival capital with partners.",
            "Make decisions based on cold ROI (Return on Investment) rather than emotional diplomacy or social aesthetics.",
            "Limit dining and entertainment expenses to a fixed percentage of monthly net profit."
        ],
        "opportunities_and_support": [
            "High-Value Joint Ventures: Wealth multiplies exponentially through formal, well-structured business alliances and international partnerships.",
            "Affluent Spousal Elevation: Marriage into a wealthy, cultured family or partnering with a spouse who brings immense commercial luck.",
            "Legal Settlements & Arbitrations: Lucrative payouts through successful mediation, intellectual property licensing, and contract arbitration.",
            "High-End Aesthetic Commerce: Tremendous profits through luxury lifestyle commerce, high fashion, interior design, and fine art curation."
        ],
        "what_not_to_expect": [
            "Do NOT expect financial stability if you surrender control of your checkbook to a charming romantic partner.",
            "Do NOT rely on verbal goodwill in business; if a deal is not written in an ironclad legal contract, assume it does not exist.",
            "Do NOT expect passive indecisiveness to protect your capital; in financial markets, no decision is still a decision that loses money."
        ]
    },
    "Scorpio": {
        "bad_habits_draining_money": [
            "Secret High-Leverage Gambles: Taking massive, undisclosed risks in futures, options, or speculative derivatives to prove your intuitive superiority.",
            "Vindictive Litigation & Grudge Wars: Spending vast sums on legal battles or corporate warfare solely to annihilate a perceived enemy out of revenge.",
            "All-or-Nothing Extremism: Betting your entire portfolio on a single turnaround asset or refusing to diversify because 'you know the truth'.",
            "Suffocating Cash Secrecy: Hoarding wealth in complex, untracked vaults that become chaotic and difficult for loved ones to manage during emergencies."
        ],
        "mindful_rules": [
            "Never allocate more than 5% of your liquid net worth to speculative, high-leverage trades, no matter how certain your intuition feels.",
            "Ask yourself before any legal conflict: 'Will this increase my net worth, or is it merely feeding my ego's thirst for vengeance?' Cut grudges early.",
            "Diversify across at least four uncorrelated asset classes (land, gold, sovereign bonds, enterprise equity).",
            "Maintain a clear, legally sound, encrypted estate plan and will accessible to trusted nominees."
        ],
        "opportunities_and_support": [
            "Unearned & Inherited Wealth: Substantial legacies through ancestral trusts, insurance settlements, wills, or spousal inheritances.",
            "Distressed Asset Revival: Buying bankrupt or undervalued assets at pennies on the dollar and restructuring them for 20x exits.",
            "Crisis Monetization: Making your largest financial windfalls during market crashes and panics when others are desperate to liquidate.",
            "Confidential Advisory Retainers: High-paying, discreet fees for solving high-stakes corporate crises, cybersecurity breaches, and turnaround strategy."
        ],
        "what_not_to_expect": [
            "Do NOT expect emotional vengeance to ever yield a positive financial return on investment.",
            "Do NOT expect financial peace if your business practices involve ethical grey zones; Saturn and Mars will demand severe karmic audits.",
            "Do NOT rely on public institutional hand-holding; your largest wealth is forged through private, independent mastery."
        ]
    },
    "Sagittarius": {
        "bad_habits_draining_money": [
            "Over-Optimistic Speculation: Investing in grandiose ventures based on starry-eyed faith while ignoring boring logistical and cashflow realities.",
            "Careless Generosity & Over-Donating: Giving away large sums to charismatic gurus, overseas foundations, or casual acquaintances without auditing their use.",
            "Restless Travel Expenses: Burning through liquidity on spontaneous international flights, luxury expeditions, and expensive exotic courses.",
            "Neglect of Boring Paperwork: Failing to file taxes on time, track deductibles, or review accounting fine print, leading to hefty penalties."
        ],
        "mindful_rules": [
            "Hire a rigorous, cynical accountant whose entire job is to scrutinize your optimistic ideas and enforce fiscal discipline.",
            "Create a dedicated 'Travel & Adventure Fund'; once that specific bucket is empty, you cannot book the next journey until it refills.",
            "Perform rigorous due diligence on every charity, non-profit, or business partner before transferring philanthropic donations.",
            "Anchor at least 50% of your wealth in conservative, boring, immovable assets (like commercial real estate) that you cannot impulsively liquidate."
        ],
        "opportunities_and_support": [
            "Transnational & Foreign Wealth: Significant revenue generated through foreign currencies, cross-border ventures, export-import, and international clients.",
            "Higher Education & Intellectual Publishing: Massive compounding through educational academies, books, courses, publishing empires, and lecturing.",
            "Divine Synchronicity / Bhagya Luck: Uncanny strokes of good fortune and timely windfalls precisely when you thought all resources were depleted.",
            "Mentorship & Guru Backing: Wealthy mentors and philanthropic investors who believe in your visionary ideals and provide patient seed funding."
        ],
        "what_not_to_expect": [
            "Do NOT expect cosmic luck to bail you out if you consistently neglect basic accounting, tax compliance, and legal diligence.",
            "Do NOT expect casual informal promises made during overseas travels to turn into guaranteed corporate contracts.",
            "Do NOT expect to retain wealth if you treat financial planning as a joke beneath your spiritual intellect."
        ]
    },
    "Capricorn": {
        "bad_habits_draining_money": [
            "Depreciating Cash Hoarding: Keeping excessive capital in low-yield fixed deposits out of cynical pessimism, losing purchasing power to inflation.",
            "Delayed Enjoyment Martyrdom: Working 80 hours a week for decades while refusing to spend a rupee on personal joy, creating bitterness in loved ones.",
            "Squeezing Vendors & Partners: Over-negotiating contracts to the absolute bone, causing talented partners to walk away and costing you more in the long run.",
            "Resistance to High-Tech Scaling: Sticking to outdated manual systems because you distrust new software or modern marketing methods."
        ],
        "mindful_rules": [
            "Allocate a fixed 10% of monthly earnings to a 'Joy & Celebrations Fund' that MUST be spent on yourself and your family without guilt.",
            "Embrace modern technological automation: Invest aggressively in software, AI, and digital infrastructure to scale your operations.",
            "Understand that generosity with valuable employees and key partners builds a fortress of loyalty that protects your wealth.",
            "Deploy cash strategically into high-quality growth equities and infrastructure assets rather than sitting on stagnant fiat currency."
        ],
        "opportunities_and_support": [
            "Institutional & Corporate Dynasties: Massive multi-decade compounding through executive leadership, corporate equity, and board seats.",
            "Heavy Industry & Infrastructure: High recurring revenue through commercial construction, government tenders, warehousing, and supply chains.",
            "Sovereign Real Estate Portfolios: Immense wealth accumulation through acquiring prime industrial corridors and commercial holdings.",
            "Elder & Governmental Support: Significant financial blessings, contracts, and endorsements from senior patriarchs, mentors, and government bodies."
        ],
        "what_not_to_expect": [
            "Do NOT expect quick, exciting viral windfalls; your chart is engineered for the 30-year climb of an unstoppable mountain goat.",
            "Do NOT expect employees to work with your monastic endurance if you do not reward them with generous equity and praise.",
            "Do NOT expect financial net worth to replace genuine emotional warmth in your personal relationships."
        ]
    },
    "Aquarius": {
        "bad_habits_draining_money": [
            "Visionary Idea Hoarding with Zero Monetization: Spending months developing revolutionary humanitarian technologies while neglecting basic cashflow.",
            "Funding Fringe Causes & Eccentric Experiments: Siphoning personal savings into speculative, unproven technological or social experiments.",
            "Contrarian Financial Rebellion: Rejecting traditional wealth-building mechanisms (like index funds or property) simply because 'society does it'.",
            "Abrupt Vanishing from Profitable Projects: Walking away from highly lucrative commercial ventures the moment you get bored or feel bureaucratic constraint."
        ],
        "mindful_rules": [
            "Partner with a grounded, pragmatic business manager (Taurus or Capricorn archetype) who handles monetizing your visionary inventions.",
            "Ensure every innovative venture has a validated cashflow model within its first 90 days before sinking personal capital into it.",
            "Respect traditional wealth anchors: Combine your futuristic crypto/tech bets with traditional real estate and blue-chip equities.",
            "Finish monetizing your current breakthrough before leaping into the next futuristic rabbit hole."
        ],
        "opportunities_and_support": [
            "Disruptive Technology Windfalls: Multi-bagger returns from early investments in artificial intelligence, aerospace, blockchain, and clean energy.",
            "Venture Capital & Angel Syndicates: Substantial funding from visionary tech funds and global family offices looking for transformative IP.",
            "Decentralized Global Networks: Earning across borders in international currencies through open-source communities, platforms, and SaaS products.",
            "Social Enterprise Grants: Significant grants and funding from humanitarian foundations, clean-tech councils, and progressive global institutions."
        ],
        "what_not_to_expect": [
            "Do NOT expect revolutionary ideas to generate revenue automatically without rigorous sales, marketing, and commercialization pipelines.",
            "Do NOT expect financial stability if you constantly abandon projects 80% of the way to completion out of intellectual boredom.",
            "Do NOT rely on speculative crowd-funded promises that have no underlying legal or regulatory substance."
        ]
    },
    "Pisces": {
        "bad_habits_draining_money": [
            "Financial Boundarylessness: Handing over your credit cards, life savings, or signing loan guarantees for unreliable lovers or sob-story acquaintances.",
            "Ostrich Syndrome with Finances: Refusing to open bank statements, review debts, or track accounting books because numbers feel stressful.",
            "Idealistic Business Naivety: Assuming everyone operates with your level of pure spiritual integrity, leading to massive contract exploitation.",
            "Escapist Splurging: Spending recklessly on spiritual seminars, crystals, alternative healing retreats, or luxury escapes when feeling overwhelmed."
        ],
        "mindful_rules": [
            "Never co-sign a loan or become a financial guarantor for ANYONE, under any emotional circumstance.",
            "Appoint a trusted, licensed financial fiduciary who manages your portfolio with strict legal boundaries so you cannot impulsively give it away.",
            "Establish a mandatory financial review session on the 1st of every month to audit your balance sheet and cashflow.",
            "Insist on written, legally binding contracts signed by an attorney before performing any creative, healing, or commercial work."
        ],
        "opportunities_and_support": [
            "Cinematic, Music & Literary Royalties: Immense lifelong passive wealth through copyright ownership of music, films, books, and artwork.",
            "Holistic & Healing Empires: Substantial profits through wellness sanctuaries, specialized clinics, psychological academies, and luxury retreats.",
            "Overseas & Maritime Wealth: Lucrative financial opportunities arriving through foreign lands, international charitable trusts, and coastal enterprises.",
            "Uncanny Intuitive Timing: Making miraculous investment entries and exits by following your deep subconscious dreams and gut premonitions."
        ],
        "what_not_to_expect": [
            "Do NOT expect financial predators to change their nature because you showed them mercy; protect your bank accounts with steel gates.",
            "Do NOT expect spiritual alignment to pay your mortgage if you ignore practical accounting and market realities.",
            "Do NOT expect casual friends who borrowed money to voluntarily pay you back without legal accountability."
        ]
    }
}

# ==============================================================
# VENUSIAN LOVE LANGUAGES & EXPRESSIONS (12 SIGNS OF VENUS)
# ==============================================================

VENUS_LOVE_EXPRESSIONS = {
    "Aries": {
        "love_language": "Spontaneous Passion, Bold Gestures & Playful Vitality",
        "how_they_express": "You express love directly, passionately, and without hesitation. You despise ambiguity, mind games, or prolonged emotional hesitation. When your heart is captured, you pursue your beloved with heroic enthusiasm, plan surprise adventures, protect them fiercely from the world, and express affection through energetic physical touch and spirited banter.",
        "what_melts_heart": "Direct honesty, unhesitating reciprocation of your passion, partners who admire your courage, and playful confidence that challenges you without playing cold games."
    },
    "Taurus": {
        "love_language": "Sensual Devotion, Physical Comfort & Timeless Loyalty",
        "how_they_express": "You express love through unwavering devotion, gentle physical affection, gourmet home-cooked meals, and creating an unshakeable, luxurious sanctuary for your partner. Love for you is not a fleeting spark, but an enduring garden. You show love by investing in the tangible security, physical comfort, and peace of mind of your beloved.",
        "what_melts_heart": "Consistent reliability, gentle physical touch, shared peaceful candlelit dinners, thoughtful timeless gifts, and never being rushed or emotionally destabilized."
    },
    "Gemini": {
        "love_language": "Intellectual Spark, Playful Banter & Shared Curiosity",
        "how_they_express": "You express love through your voice, words, and agile intellect. You shower your beloved with fascinating articles, witty text banter throughout the day, inside jokes, and spontaneous road trips. To you, mental intimacy IS romantic intimacy; conversing until sunrise without running out of ideas is your highest declaration of love.",
        "what_melts_heart": "A quick-witted mind, engaging conversational chemistry, laughing at your humor, and granting you intellectual freedom without suffocating jealousy."
    },
    "Cancer": {
        "love_language": "Emotional Shelter, Maternal/Paternal Warmth & Deep Devotion",
        "how_they_express": "You express love through profound emotional attunement, nurturing meals, sentimental keepsakes, and creating an impenetrable fortress of care around your partner. You remember anniversaries, the exact song playing when you first met, and how they take their tea. You protect your beloved's feelings with tender ferocity.",
        "what_melts_heart": "Emotional vulnerability, deep appreciation for home and family, honoring your sensitivities, and reassuring you that your soft heart is safe with them."
    },
    "Leo": {
        "love_language": "Regal Generosity, Grand Romantic Gestures & Fierce Pride",
        "how_they_express": "You love with the radiant warmth of the midday sun. You shower your beloved with thoughtful, generous gifts, celebrate their achievements publicly, and defend them with ferocious loyalty. When you are in love, the whole world knows it; your affection is noble, theatrical, protective, and wholehearted.",
        "what_melts_heart": "Genuine heartfelt admiration, unwavering loyalty, showing pride in being with you, and reciprocating with warmhearted, undivided attention."
    },
    "Virgo": {
        "love_language": "Acts of Practical Devotion, Attentive Care & Dedicated Service",
        "how_they_express": "You express love not through empty melodramatic poetry, but through quiet, tireless acts of helpful service. You organize their chaotic schedule, brew healing teas when they are unwell, research solutions to their dilemmas, and anticipate their practical needs before they ask. Your love is meticulous and dependable.",
        "what_melts_heart": "Noticing the subtle details you do for them, punctuality, clean aesthetics, and reassuring you that you do not need to be perfect to be cherished."
    },
    "Libra": {
        "love_language": "Harmonious Courtesy, Romantic Aesthetics & Equal Partnership",
        "how_they_express": "You are the quintessential romantic soul. You express love through exquisite aesthetic dates, thoughtful handwritten notes, polite chivalry, and an uncanny ability to understand your partner's viewpoint. You constantly strive for fairness, balance, and peaceful beauty, making your partner feel truly seen, heard, and valued.",
        "what_melts_heart": "Refined manners, thoughtful aesthetic gestures, peaceful communication without screaming or harshness, and carrying equal weight in the partnership."
    },
    "Scorpio": {
        "love_language": "Profound Soul Merging, Fierce Loyalty & Magnetic Intimacy",
        "how_they_express": "You do not know how to love casually or halfway; for you, love is a sacred spiritual fusion. You express affection through unwavering confidentiality, magnetic eye contact, intense emotional vulnerability, and standing by your partner in their darkest, most vulnerable hours where others would flee.",
        "what_melts_heart": "Radical transparency with zero hidden secrets, proving your loyalty under pressure, and meeting your emotional depth without running away in fear."
    },
    "Sagittarius": {
        "love_language": "Inspirational Adventures, Philosophical Laughter & Freedom",
        "how_they_express": "You express love by inviting your partner into your grand journey of discovery. You show affection through shared travel to uncharted lands, laughing through life's absurdities, late-night philosophical debates under the stars, and encouraging them to pursue their wildest dreams. Your love liberates their spirit.",
        "what_melts_heart": "A rich sense of humor, enthusiasm for exploring the world together, giving each other breathing room without clinginess, and shared ethical ideals."
    },
    "Capricorn": {
        "love_language": "Enduring Reliability, Building Legacy & Unshakeable Commitment",
        "how_they_express": "You express love by being the rock that never crumbles. You might not write cheesy sonnets, but you will stand by them in a crisis, help them build an enduring financial plan, and stay committed through recessions and hardships. Your love is built on integrity, respect, and constructing an empire together.",
        "what_melts_heart": "Respecting your ambitions, shared long-term dedication, quiet competence, and standing firmly by your side when times get challenging."
    },
    "Aquarius": {
        "love_language": "Visionary Camaraderie, Quirky Kinship & Freedom of Being",
        "how_they_express": "You express love first and foremost as an extraordinary best friend. You celebrate your partner's unique eccentricities, champion their intellectual independence, collaborate on visionary ideals, and grant them complete space to be their authentic self without suffocating possessiveness.",
        "what_melts_heart": "Intellectual brilliance, sharing humanitarian or visionary dreams, respecting individual freedom, and connecting without outdated dogmas."
    },
    "Pisces": {
        "love_language": "Transcendent Empathy, Poetic Magic & Unconditional Compassion",
        "how_they_express": "You love with the purity of an ancient mystic. You express love through intuitive empathy, romantic poetry, music, healing touch, and seeing the divine light inside your partner even when they feel broken. Your love is a safe harbor of unconditional grace, soft romance, and spiritual devotion.",
        "what_melts_heart": "Gentleness, deep creative or musical connection, spiritual resonance, and partners who treat your delicate, sensitive heart with reverence."
    }
}

# ==============================================================
# 7TH HOUSE (KALATRA BHAVA) FUTURE SPOUSE ARCHETYPES (12 SIGNS)
# ==============================================================

SPOUSE_PROFILES = {
    "Aries": {
        "archetype_title": "The Dynamic Trailblazer & Fearless Companion (मेष - साहसी एवं तेजस्वी जीवनसाथी)",
        "partner_attraction_archetype": "Your soul is karmically drawn to bold, decisive, energetic partners who possess natural leadership and cut through hesitation with courage.",
        "physical_appearance": {
            "stature_and_build": "Athletic, lean, upright posture; carries a vital kinetic energy and decisive stride.",
            "face_and_features": "Well-defined jawline, prominent expressive brows, and a confident, radiant smile that commands attention.",
            "eyes_and_gaze": "Sharp, amber or warm-toned, intensely alert and fearless gaze.",
            "complexion_and_hair": "Vibrant or warm glowing complexion; thick, lustrous hair often worn sportily or cleanly styled.",
            "aesthetic_and_style": "Bold, functional minimalist chic; favors crisp athletic tailoring, vibrant accents (crimson, charcoal, royal black), and fuss-free elegance."
        },
        "personality_traits": [
            "Fearless initiative: Decisive, action-oriented, and refuses to let fear paralyze progress.",
            "Radical honesty: Despises deceit, passive-aggression, and hidden agendas; what you see is what you get.",
            "Protective loyalty: Stands up fiercely for you against any outside opposition or unfair criticism.",
            "Spontaneous enthusiasm: Injects high vitality, playful adventures, and optimism into daily life."
        ],
        "behavioral_characteristics": [
            "Communicates directly and openly; addresses grievances immediately rather than holding simmering grudges.",
            "Pushes you to believe in yourself and take bold leaps in your career and personal aspirations.",
            "Can display a brief flash of temper when frustrated, but cools down rapidly and seeks warm reconciliation.",
            "Thrives on mutual physical fitness, outdoor challenges, and shared competitive fun."
        ]
    },
    "Taurus": {
        "archetype_title": "The Grounded Pillar of Serenity & Aesthetic Grace (वृषभ - सौम्य, स्थिर एवं रूपवान जीवनसाथी)",
        "partner_attraction_archetype": "You are drawn to serene, dependable, sensually grounded partners who bring peace, enduring stability, and exquisite taste to your life.",
        "physical_appearance": {
            "stature_and_build": "Well-proportioned, graceful curves or solid sturdy build; moves with unhurried dignity and poise.",
            "face_and_features": "Soft harmonious facial symmetry, gentle sculpted jaw, graceful neck, and a disarmingly warm smile.",
            "eyes_and_gaze": "Large, soft, velvety, and calm eyes that exude emotional tranquility and trustworthiness.",
            "complexion_and_hair": "Luminous healthy skin with warm undertones; thick, glossy, naturally wavy or rich hair.",
            "aesthetic_and_style": "Timeless luxury; appreciates natural fabrics (silk, cashmere, fine cotton), soothing earthy tones, subtle luxury perfumes, and elegant understated jewelry."
        },
        "personality_traits": [
            "Unshakeable stability: A tranquil emotional anchor that never gets swept up in hysterical panics.",
            "Exquisite aesthetic discernment: An innate eye for quality, timeless comfort, and beautiful domestic spaces.",
            "Steadfast loyalty: Once committed, stands beside you with monumental fidelity through every season.",
            "Pragmatic financial intelligence: Naturally skilled at managing money, conserving assets, and building wealth."
        ],
        "behavioral_characteristics": [
            "Demonstrates devotion through continuous physical affection, comforting hugs, and gourmet meals.",
            "Creates a peaceful, visually stunning home environment where you can recharge without chaos.",
            "Takes time to make major decisions; resists being rushed or pushed into sudden disruptions.",
            "Values consistency, dependable routines, and regular romantic weekend retreats in nature."
        ]
    },
    "Gemini": {
        "archetype_title": "The Witty Wordsmith & Youthful Intellectual (मिथुन - बुद्धिमान, वाकपटु एवं चंचल जीवनसाथी)",
        "partner_attraction_archetype": "Your heart seeks a brilliant conversationalist—someone versatile, curious, and humorous who keeps life intellectually sparkling.",
        "physical_appearance": {
            "stature_and_build": "Slender, agile, youthful demeanor regardless of age; expressive hand gestures and light-footed step.",
            "face_and_features": "Animated, finely chiseled face, quick playful smile with a mischievous twinkle, high expressive forehead.",
            "eyes_and_gaze": "Bright, darting, inquisitive eyes that sparkle with curiosity and observe every subtle nuance.",
            "complexion_and_hair": "Fair or glowing fresh skin; fine, silky, effortlessly modern hair styling.",
            "aesthetic_and_style": "Trendy, versatile smart-casual fashion; loves clever layered outfits, modern smart accessories, and eclectic color palettes."
        },
        "personality_traits": [
            "Brilliant conversationalist: Can talk on art, philosophy, business, or pop culture with effortless wit.",
            "Adaptable versatility: Easily fits into any social setting, family gathering, or professional circle.",
            "Playful youthfulness: Keeps the relationship feeling fresh, spontaneous, and immune to boring domestic rut.",
            "Sharp problem-solver: De-escalates tensions through humor, clever diplomacy, and rational perspective."
        ],
        "behavioral_characteristics": [
            "Loves sharing articles, podcasts, books, and constant witty text updates throughout the day.",
            "Enjoys entertaining friends, hosting intellectual gatherings, and taking spontaneous weekend city-breaks.",
            "Solves marital disagreements through open dialogue and objective logic rather than emotional sulking.",
            "Needs intellectual freedom and diverse social engagements to keep their creative energy high."
        ]
    },
    "Cancer": {
        "archetype_title": "The Nurturing Soul & Tender Protector (कर्क - संवेदनशील, स्नेही एवं गृहप्रिय जीवनसाथी)",
        "partner_attraction_archetype": "You are drawn to deeply nurturing, emotionally sensitive partners who provide a sacred sanctuary of unconditional care and familial warmth.",
        "physical_appearance": {
            "stature_and_build": "Gentle, comforting presence, soft curving posture that instinctively invites closeness and warmth.",
            "face_and_features": "Gentle lunar face with soft cheeks, sweet compassionate smile, and tender expressive lips.",
            "eyes_and_gaze": "Large, watery, luminous, deep eyes that reflect emotional currents like a tranquil sacred lake.",
            "complexion_and_hair": "Pearlescent, radiant smooth complexion; soft, wavy, naturally lustrous hair.",
            "aesthetic_and_style": "Classic, cozy elegance; loves soft knitwear, flowy fabrics, ocean-inspired pastels (pearl white, sea mist, silver), and sentimental heirloom jewelry."
        },
        "personality_traits": [
            "Deep intuitive empathy: Senses your unexpressed anxieties or fatigue before you even utter a word.",
            "Fierce devotion to home & family: Regards the home as a sacred temple of mutual comfort and protection.",
            "Sentimental memory: Cherishes milestones, keepsakes, and family traditions with sacred reverence.",
            "Emotional depth: Possesses immense capacity for unconditional love, patient listening, and tenderness."
        ],
        "behavioral_characteristics": [
            "Cooks soulful, delicious meals and pampers you with attentive care whenever you feel drained.",
            "Builds a loving, harmonious domestic atmosphere filled with comfort, soft lighting, and warmth.",
            "Can occasionally withdraw into their protective shell when feeling emotionally overwhelmed; responds magically to gentle reassurance.",
            "Stands as your most fiercely protective ally whenever outside circumstances threaten family peace."
        ]
    },
    "Leo": {
        "archetype_title": "The Radiant Leader & Noble Heart (सिंह - तेजस्वी, प्रभावशाली एवं उदार जीवनसाथी)",
        "partner_attraction_archetype": "You are attracted to charismatic, radiant, noble partners who walk with dignity, lead with warmth, and inspire pride in your union.",
        "physical_appearance": {
            "stature_and_build": "Commanding upright posture, broad shoulders or graceful regal carriage; turns heads effortlessly upon entering a room.",
            "face_and_features": "Noble, aristocratic bone structure, dazzling warm smile that lights up the room, proud sculpted brow.",
            "eyes_and_gaze": "Bright, magnetic, golden-warm eyes that hold gaze with unwavering self-assurance and charisma.",
            "complexion_and_hair": "Luminous or golden skin; thick, voluminous 'mane-like' hair that commands admiration.",
            "aesthetic_and_style": "Regal, dramatic sophistication; favors statement jewelry, bespoke tailoring, rich royal tones (gold, saffron, deep burgundy), and high-end elegance."
        },
        "personality_traits": [
            "Grand generosity: Loves showering you and family with lavish gifts, warm hospitality, and affection.",
            "Uncompromising integrity: Governed by a strong moral compass of honor, self-respect, and loyalty.",
            "Natural charisma: Radiates uplifting confidence that elevates your social and professional circles.",
            "Fierce protective pride: Champions your talents publicly and celebrates your accomplishments as their own."
        ],
        "behavioral_characteristics": [
            "Treats you with chivalrous, courtly respect and demands that others treat you with equal honor.",
            "Loves romantic grand gestures—surprise luxury celebrations, public declarations of love, and memorable dates.",
            "Values heartfelt appreciation and verbal praise; wounded by public criticism or cold dismissiveness.",
            "Acts as a confident pillar of support, motivating you to pursue your grandest dreams without fear."
        ]
    },
    "Virgo": {
        "archetype_title": "The Refined Analyst & Dedicated Caregiver (कन्या - कुशल, विवेकशील एवं कर्तव्यनिष्ठ जीवनसाथी)",
        "partner_attraction_archetype": "You are drawn to intelligent, methodical, discerning partners who bring clarity, order, and practical devotion to your life.",
        "physical_appearance": {
            "stature_and_build": "Neat, poised, graceful, well-toned; maintains physical fitness and posture with discipline.",
            "face_and_features": "Delicate, chiseled, intellectual features, clean serene forehead, and an observant, subtle smile.",
            "eyes_and_gaze": "Sharp, clear, analytical yet deeply kind eyes that miss nothing in their environment.",
            "complexion_and_hair": "Fresh, porcelain or clean healthy skin; impeccably groomed, polished, and neat hair.",
            "aesthetic_and_style": "Minimalist chic, immaculate tailoring, neutral sophisticated tones (slate grey, navy, forest green, crisp ivory), and functional elegance."
        },
        "personality_traits": [
            "Discerning intellect: Possesses sharp critical thinking and an uncanny knack for organizing chaos into seamless systems.",
            "Devotion through helpfulness: Shows love by solving your practical problems and managing daily responsibilities flawlessly.",
            "Humble integrity: Completely free of vulgar arrogance or empty boastfulness; values substance over superficial hype.",
            "Dedicated health consciousness: Cares deeply about wellness, clean nutrition, and orderly living."
        ],
        "behavioral_characteristics": [
            "Keeps household logistics, schedules, and financial records immaculate and stress-free.",
            "Offers grounded, constructive advice that saves you from costly missteps in career and investments.",
            "Can occasionally fret over minor imperfections; blossoms when you gently remind them of the bigger picture.",
            "Expresses enduring loyalty through constant, reliable presence through all of life's mundane and heroic moments."
        ]
    },
    "Libra": {
        "archetype_title": "The Charming Peacemaker & Cultured Aesthetician (तुला - सौम्य, आकर्षक एवं न्यायप्रिय जीवनसाथी)",
        "partner_attraction_archetype": "Your soul seeks an enchanting, courteous, romantic partner who values equality, peaceful harmony, and refined aesthetics.",
        "physical_appearance": {
            "stature_and_build": "Graceful, balanced, symmetrical proportions; moves with fluid, charming coordination.",
            "face_and_features": "Classic oval facial symmetry, enchanting dimples or warm sweet smile, soft sculpted jawline.",
            "eyes_and_gaze": "Harmonious, luminous, expressive eyes that radiate social warmth and genuine interest in others.",
            "complexion_and_hair": "Clear radiant complexion; effortlessly stylish, artistic, and beautifully conditioned hair.",
            "aesthetic_and_style": "Impeccable fashion sense; masters color harmony, elegant tailoring, tasteful accessories, and sophisticated modern glamour."
        },
        "personality_traits": [
            "Master of diplomacy: De-escalates conflicts with grace, ensuring both sides feel heard and respected.",
            "Romantic idealism: Believes in timeless courtship, mutual courtesy, and sharing life as an equal team.",
            "Cultural appreciation: Loves art, music, fine cuisine, theatre, and culturally enriching social experiences.",
            "Natural fairness: Deeply committed to equity, justice, and maintaining emotional balance in the relationship."
        ],
        "behavioral_characteristics": [
            "Balances your impulsive tendencies with thoughtful perspective and calm rationality.",
            "Plans exquisite date nights, creates harmonious interior spaces, and fosters warm social connections.",
            "Despises vulgar screaming or crude arguments; prefers dignified, calm conversations to resolve differences.",
            "Thrives when decisions are made collaboratively, celebrating joint victories as a unified pair."
        ]
    },
    "Scorpio": {
        "archetype_title": "The Magnetic Mystic & Transformative Guardian (वृश्चिक - गूढ़, निष्ठावान एवं चुंबकीय जीवनसाथी)",
        "partner_attraction_archetype": "You are drawn to intense, deeply intuitive, fiercely loyal partners who possess magnetic charisma and profound emotional depth.",
        "physical_appearance": {
            "stature_and_build": "Mesmerizing, commanding aura; athletic or hypnotic presence that exudes quiet inner power.",
            "face_and_features": "Strong bone structure, intense brows, enigmatic smile, and sharp, memorable facial contours.",
            "eyes_and_gaze": "Penetrating, hypnotic, deep eyes that look straight into your soul with uncanny psychological perception.",
            "complexion_and_hair": "Striking skin contrast; lustrous rich dark hair, radiating an unforgettable smoldering charm.",
            "aesthetic_and_style": "Sleek, enigmatic elegance; favors rich dark shades (obsidian black, deep crimson, midnight blue), leather textures, and minimalist statement jewelry."
        },
        "personality_traits": [
            "Fierce, unbreakable loyalty: Once committed, will walk through fire to defend you and stand by you unconditionally.",
            "Psychological depth: Sees through superficial pretenses and intuitively understands your deepest unspoken feelings.",
            "Transformative resilience: Possesses legendary strength to bounce back from any life adversity stronger than before.",
            "Sacred confidentiality: Keeps your vulnerabilities and private life strictly guarded from the outside world."
        ],
        "behavioral_characteristics": [
            "May take time to fully open their emotional vault, but once trust is earned, loves with monumental intensity.",
            "Forms an impenetrable soul-bond with you, preferring deep private intimacy over shallow public displays.",
            "Requires absolute honesty; hates half-truths or deceit, rewarding transparency with complete devotion.",
            "Serves as your most fearless confidant and protector against life's complex challenges."
        ]
    },
    "Sagittarius": {
        "archetype_title": "The Jovial Explorer & Philosophical Visionary (धनु - आशावादी, विद्वान एवं साहसी जीवनसाथी)",
        "partner_attraction_archetype": "You seek an adventurous, worldly, highly educated, and jovial partner who expands your philosophical horizons and makes life a grand adventure.",
        "physical_appearance": {
            "stature_and_build": "Tall or athletic, open expansive posture, energetic stride, radiating vibrant outdoor vitality.",
            "face_and_features": "Open friendly countenance, infectious broad smile, high noble forehead indicating intellectual wisdom.",
            "eyes_and_gaze": "Optimistic, sparkling, visionary eyes filled with wanderlust, intellectual zest, and good humor.",
            "complexion_and_hair": "Healthy, sun-kissed or vibrant complexion; wavy, breezy, freely flowing hair.",
            "aesthetic_and_style": "Bohemian-chic or international sophistication; travel-ready functional fashion, eclectic textiles, and warm joyful colors (saffron, indigo, olive)."
        },
        "personality_traits": [
            "Infectious optimism: Finds the silver lining in every catastrophe and fills the home with laughter.",
            "Philosophical wisdom: Loves exploring spirituality, higher ethics, global cultures, and big-picture ideas.",
            "Generous honesty: Speaks truth with refreshing candidness, free of pettiness, manipulation, or grudges.",
            "Love of adventure: Eager to explore foreign lands, study new domains, and try spontaneous experiences."
        ],
        "behavioral_characteristics": [
            "Lifts your spirits during gloomy phases by making you laugh and showing you the wider cosmic perspective.",
            "Encourages you to pursue higher education, travel, creative passions, and spiritual growth.",
            "Values mutual freedom and independence within marriage; thrives when both partners have space to grow.",
            "Treats life as an exciting quest, making marriage an inspiring journey rather than a boring routine."
        ]
    },
    "Capricorn": {
        "archetype_title": "The Dignified Achiever & Enduring Foundation (मकर - गंभीर, प्रतिष्ठित एवं कर्तव्यपरायण जीवनसाथी)",
        "partner_attraction_archetype": "You are drawn to mature, ambitious, disciplined partners who command social respect, build lasting legacy, and provide unshakeable security.",
        "physical_appearance": {
            "stature_and_build": "Tall, lean, aristocratic posture; carries themselves with serious, dignified, executive presence.",
            "face_and_features": "Chiseled cheekbones, strong structured jawline, contemplative mature expression, and timeless, elegant aging.",
            "eyes_and_gaze": "Deep-set, steady, serious eyes that convey patience, deep wisdom, and unyielding perseverance.",
            "complexion_and_hair": "Sophisticated cool or olive undertone; neat, classic, immaculate conservative grooming.",
            "aesthetic_and_style": "Executive elegance; favors timeless classics, tailored wool, durable luxury watches, and dark muted tones (charcoal, slate, navy, black)."
        },
        "personality_traits": [
            "Pragmatic maturity: Emotionally calm, responsible, and capable of managing heavy life pressures with composure.",
            "Legacy builder: Highly ambitious with an enduring work ethic, focused on long-term family wealth and social standing.",
            "Steadfast fidelity: Takes marital vows with sacred seriousness; regards commitment as an unbroken lifelong duty.",
            "Quiet emotional depth: Does not make flashy public scenes, but demonstrates love through monumental acts of sacrifice."
        ],
        "behavioral_characteristics": [
            "Establishes a rock-solid financial and domestic foundation, shielding the family from external instability.",
            "Offers pragmatic, wise counsel that helps you navigate complex career decisions and institutional hurdles.",
            "May appear emotionally reserved initially; reveals a dry, witty sense of humor and deep tenderness in private.",
            "Takes immense pride in family lineage, respecting elders and building a durable legacy for future generations."
        ]
    },
    "Aquarius": {
        "archetype_title": "The Avant-Garde Visionary & Intellectual Rebel (कुम्भ - आधुनिक, स्वतंत्र एवं मौलिक जीवनसाथी)",
        "partner_attraction_archetype": "You are drawn to unique, forward-thinking, intellectually independent partners who challenge orthodoxies and champion humanitarian ideals.",
        "physical_appearance": {
            "stature_and_build": "Unique, unconventional posture or build; radiates an electric, distinct, futuristic charisma.",
            "face_and_features": "Angular, striking, memorable facial features, friendly intriguing smile, and an open expressive brow.",
            "eyes_and_gaze": "Visionary, clear, detached yet warmly inclusive gaze that seems to perceive future trends.",
            "complexion_and_hair": "Distinctive styling; modern haircut, creative aesthetics, or effortlessly cool contemporary grooming.",
            "aesthetic_and_style": "Avant-garde, vintage-meets-modern; loves tech-wear, quirky statement pieces, electric blue, silver, and unconventional textures."
        },
        "personality_traits": [
            "Progressive egalitarian: Treats you as an intellectual equal, best friend, and partner in crime.",
            "Original thinker: Completely free of petty social prejudices, gossiping, or narrow-minded conventions.",
            "Humanitarian consciousness: Cares deeply about social impact, environmental causes, and progressive ideals.",
            "Unconditional acceptance: Celebrates your unique quirks and never pressures you to fit a conformist mold."
        ],
        "behavioral_characteristics": [
            "Engages in stimulating discussions on technology, philosophy, sociology, and creative ideas.",
            "Gives you total breathing space to pursue your friendships and interests, expecting the same trust in return.",
            "Replaces stifling possessiveness with deep mutual camaraderie, teamwork, and visionary plans.",
            "Introduces you to fascinating eclectic circles, innovative projects, and progressive worldviews."
        ]
    },
    "Pisces": {
        "archetype_title": "The Soulful Healer & Poetic Romantic (मीन - दयालु, कल्पनाशील एवं दिव्य जीवनसाथी)",
        "partner_attraction_archetype": "Your heart seeks a gentle, artistic, deeply empathetic, and spiritual partner who softens life's harshness with unconditional love and wonder.",
        "physical_appearance": {
            "stature_and_build": "Ethereal, gentle, graceful; moves with fluid, soft, almost musical coordination.",
            "face_and_features": "Soft dreamlike features, tender compassionate smile, youthful and timeless facial expression.",
            "eyes_and_gaze": "Luminous, dreamy, soulful eyes that express boundless empathy and spiritual longing.",
            "complexion_and_hair": "Delicate, luminous skin; soft flowing hair that catches light with natural beauty.",
            "aesthetic_and_style": "Romantic, artistic, flowy fabrics; watercolor palettes (seafoam green, lavender, ivory, aquamarine), and delicate handmade jewelry."
        },
        "personality_traits": [
            "Boundless empathy: Possesses an uncanny ability to absorb and heal your emotional fatigue and sorrow.",
            "Creative imagination: Naturally attuned to music, visual art, cinema, poetry, and transcendent beauty.",
            "Spiritual devotion: Believes in soul connections, destiny, and the divine sacredness of true love.",
            "Forgiving grace: Quickly forgives human flaws, treating you with tenderness even when you feel imperfect."
        ],
        "behavioral_characteristics": [
            "Transforms mundane everyday reality into a poetic, sacred sanctuary filled with soft romance.",
            "Listens without judgment to your deepest fears, providing a peaceful refuge from corporate stress.",
            "Can occasionally be emotionally permeable to external energies; thrives when you provide gentle grounding.",
            "Inspires your spiritual growth, meditation, creative pursuits, and acts of compassionate charity."
        ]
    }
}


def find_active_dasha(dashas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Find the currently active Mahadasha, Antardasha, and the upcoming sub-period."""
    today = datetime.now().strftime("%Y-%m-%d")
    active_m = dashas[0]
    active_ad = active_m.get("antardashas", [{}])[0]
    next_ad = None

    for m_idx, m in enumerate(dashas):
        if m["start_date"] <= today <= m["end_date"]:
            active_m = m
            ads = m.get("antardashas", [])
            for ad_idx, ad in enumerate(ads):
                if ad["start_date"] <= today <= ad["end_date"]:
                    active_ad = ad
                    if ad_idx + 1 < len(ads):
                        next_ad = ads[ad_idx + 1]
                    elif m_idx + 1 < len(dashas):
                        next_m = dashas[m_idx + 1]
                        next_ad = next_m.get("antardashas", [{}])[0]
                    break
            break

    if not next_ad:
        next_ad = {"sub_lord": "Jupiter", "start_date": active_ad.get("end_date", ""), "end_date": ""}

    return {
        "mahadasha_lord": active_m.get("lord", "Jupiter"),
        "mahadasha_start": active_m.get("start_date", ""),
        "mahadasha_end": active_m.get("end_date", ""),
        "antardasha_lord": active_ad.get("sub_lord", active_m.get("lord", "Jupiter")),
        "antardasha_start": active_ad.get("start_date", ""),
        "antardasha_end": active_ad.get("end_date", ""),
        "next_antardasha_lord": next_ad.get("sub_lord", "Saturn"),
        "next_antardasha_start": next_ad.get("start_date", ""),
        "next_antardasha_end": next_ad.get("end_date", "")
    }


# ==============================================================
# 9 PLANETARY DASHA PSYCHOLOGICAL & CIRCUMSTANTIAL PROFILES
# ==============================================================

DASHA_PROFILES = {
    "Sun": {
        "title": "Surya (Sun) — The Cycle of Self-Authority & Purpose",
        "circumstances": "You are navigating a period centered on self-definition, leadership, and public accountability. Career visibility, dealing with government or corporate authorities, and redefining your personal identity are at the forefront.",
        "emotional_state": "You are experiencing a powerful urge to be taken seriously and respected for your worth. You may feel impatient with people who waste your time or undervalue your contributions, alongside a strong inner hunger to step out of the shadows.",
        "karmic_meaning": "The Sun's reign tests your authentic self-worth. It burns away false modesty and dependency, asking you to discover whether your confidence is built on true integrity or mere external validation.",
        "challenges": [
            "Ego clashes with superiors, fathers, or dominant authority figures.",
            "Physical fatigue and heat stress from over-exertion or lack of rest.",
            "Feeling isolated or burdened by having to be the sole decision-maker.",
            "Struggling to balance healthy self-respect with defensive pride."
        ],
        "do": [
            "Wake up early and expose your eyes to the rising morning sunlight.",
            "Take decisive ownership of your career direction and negotiate your worth with calm dignity.",
            "Establish clean, transparent boundaries in professional partnerships.",
            "Channel your authority into uplifting and protecting those who depend on you."
        ],
        "avoid": [
            "Do NOT engage in petty ego battles or power struggles that yield no practical victory.",
            "Do NOT let arrogance alienate loyal friends or dedicated colleagues.",
            "Do NOT ignore cardiovascular health, blood pressure, or eye strain.",
            "Do NOT make decisions solely to impress rivals or prove critics wrong."
        ]
    },
    "Moon": {
        "title": "Chandra (Moon) — The Cycle of Emotional Awakening & Home",
        "circumstances": "This phase highlights domestic affairs, living arrangements, maternal relationships, public reputation, and creative sensitivity. You are undergoing profound emotional recalibration and reassessing where you truly belong.",
        "emotional_state": "Your emotions are heightened and fluid like ocean tides. You feel deeply empathetic, nostalgic about the past, and crave genuine psychological safety, comfort, and unconditional affection.",
        "karmic_meaning": "The Moon's cycle invites you to make peace with your inner child and emotional history. It teaches you that true security is not found in stone walls, but in inner mental tranquility and peace of mind (*Manas Shanti*).",
        "challenges": [
            "Emotional mood swings, anxiety, and sleepless nights spent overthinking.",
            "Absorbing the negative moods and psychological baggage of people around you.",
            "Indecisiveness caused by fluctuating feelings about career or relationships.",
            "Seeking external validation to soothe internal emotional unrest."
        ],
        "do": [
            "Practice grounding daily meditation near water or with a pure silver cup.",
            "Prioritize deep hydration, gut health, and consistent sleep hygiene.",
            "Create a peaceful, clutter-free domestic sanctuary where you can recharge.",
            "Channel intense emotional currents into creative writing, art, or culinary passions."
        ],
        "avoid": [
            "Do NOT make permanent life commitments during extreme emotional highs or lows.",
            "Do NOT indulge in late-night distress spending ('retail therapy') or emotional eating.",
            "Do NOT isolate yourself in melancholic memories of past heartbreaks.",
            "Do NOT allow emotionally manipulative individuals to drain your compassion."
        ]
    },
    "Mars": {
        "title": "Mangal (Mars) — The Cycle of Courage, Action & Conquest",
        "circumstances": "You are in a high-octane, action-packed chapter. Real estate transactions, physical restructuring, entrepreneurial expansion, competitive examinations, and technical challenges dominate your current reality.",
        "emotional_state": "You feel an urgent, kinetic restlessness—a burning desire to execute, conquer backlogged goals, and tolerate zero delays. You feel like a warrior in an arena fighting for your rightful breakthrough.",
        "karmic_meaning": "Mars tests your capacity for disciplined courage. It forces you to discover whether your passion will manifest as reckless destruction or targeted, heroic achievement that clears life's obstacles.",
        "challenges": [
            "Sudden surges of irritation, impatience, and aggressive verbal outbursts.",
            "Physical burnout, inflammation, or minor injuries from rushing tasks.",
            "Contentious friction with brothers, close peers, or competitive rivals.",
            "Acting impulsively before gathering complete facts or legal verification."
        ],
        "do": [
            "Direct intense physical energy through rigorous daily exercise, gym, or martial arts.",
            "Tackle your most intimidating, delayed projects with bold, focused initiative.",
            "Maintain meticulous legal documentation on property and financial deeds.",
            "Practice a mandatory 5-minute pause before responding to infuriating messages."
        ],
        "avoid": [
            "Do NOT engage in aggressive road arguments or hot-headed confrontation.",
            "Do NOT sign financial agreements or settle disputes in an agitated state of mind.",
            "Do NOT neglect hydration, liver cooling foods, or physical safety gear.",
            "Do NOT treat personal relationships as battlegrounds to be conquered."
        ]
    },
    "Rahu": {
        "title": "Rahu (North Node) — The Cycle of Radical Expansion & Disruption",
        "circumstances": "You are navigating an unconventional, fast-evolving phase. Rapid career shifts, international or digital opportunities, sudden unexpected breakthroughs, and breaking away from traditional societal molds define your circumstances.",
        "emotional_state": "You feel ambitious, intellectually stimulated, and hungry for quantum leaps. Simultaneously, you may battle subtle imposter syndrome, fear of missing out (FOMO), and mental overwhelm from too many possibilities.",
        "karmic_meaning": "Rahu's period pulls you out of your ancestral comfort zone to fulfill pending karmic desires in the material world. It teaches you to master the material realm without becoming enslaved by its illusions.",
        "challenges": [
            "Susceptibility to shiny distractions, speculative hype, and 'get-rich-quick' allure.",
            "Phantom anxieties, insomnia, or obsessive overthinking during late night hours.",
            "Feeling alienated from conventional peers who cannot understand your unconventional vision.",
            "Struggling to distinguish genuine opportunities from deceptive mirages."
        ],
        "do": [
            "Leverage cutting-edge technologies, global cross-border networks, and innovative skills.",
            "Anchor yourself with daily unshakeable spiritual grounding (breathwork, walking barefoot on soil).",
            "Consult grounded, conservative mentors before making irreversible career or financial pivots.",
            "Practice strict digital hygiene—shut down screens at least 1 hour before sleep."
        ],
        "avoid": [
            "Do NOT invest capital into unverified crypto schemes, speculative gambles, or shadowy syndicates.",
            "Do NOT compromise your core moral integrity for temporary social prestige.",
            "Do NOT fall into toxic escapism, intoxicants, or erratic sleep schedules.",
            "Do NOT burn existing bridges until your new platform is tested and secure."
        ]
    },
    "Jupiter": {
        "title": "Guru (Jupiter) — The Cycle of Wisdom, Prosperity & Higher Dharma",
        "circumstances": "You are experiencing a period of expanding wisdom, educational elevation, financial compounding, and mentorship. Family blessings, spiritual evolution, and becoming an advisor to others are central themes.",
        "emotional_state": "You feel reflective, benevolent, and intellectually mature. You are thinking in terms of long-term legacy and ethical principles, craving deeper soul meaning beyond mere commercial survival.",
        "karmic_meaning": "Jupiter brings the ripe harvest of past positive karma (*Purva Punya*). It teaches you that true abundance is a state of spiritual grace, ethical integrity, and generosity that flows through you to uplift others.",
        "challenges": [
            "Over-optimism: Agreeing to take on too many projects out of generous enthusiasm.",
            "Complacency or neglecting boring administrative and legal fine print.",
            "Moral fatigue from feeling responsible for solving everyone else's troubles.",
            "Weight gain or metabolic sluggishness from over-indulgence in rich foods."
        ],
        "do": [
            "Invest in higher learning, advanced certifications, and publishing your insights.",
            "Build compounding, ethical wealth through gold, land, and conservative investments.",
            "Engage in regular charitable acts (*Annadaan* - feeding animals, birds, and the needy).",
            "Seek out or serve as a wise spiritual mentor to elevate consciousness."
        ],
        "avoid": [
            "Do NOT become self-righteous, dogmatic, or preachy in personal interactions.",
            "Do NOT guarantee loans or underwrite unviable businesses for loved ones out of guilt.",
            "Do NOT neglect physical cardiovascular health or indulge in excessive sugary foods.",
            "Do NOT ignore practical reality while pursuing grand philosophical ideals."
        ]
    },
    "Saturn": {
        "title": "Shani (Saturn) — The Cycle of Karmic Mastery & Endurance",
        "circumstances": "You are navigating a monumental karmic rebuilding phase. Heavy responsibilities, grueling sustained labor, structural discipline, and shedding superficial illusions characterize your daily life.",
        "emotional_state": "You feel serious, sober, and sometimes emotionally fatigued. You might wonder if your relentless hard work is being recognized, alongside a deep yearning for quiet simplicity, authenticity, and peace.",
        "karmic_meaning": "Saturn is the great cosmic diamond polisher. It tests your endurance by stripping away hollow shortcuts, ensuring that whatever you construct during this phase lasts for decades without collapsing.",
        "challenges": [
            "Frustration with slow timelines, bureaucratic delays, and protracted procedures.",
            "Feelings of loneliness, heavy burdens, or lack of external emotional support.",
            "Stiffness in joints, back pain, or fatigue from carrying prolonged stress.",
            "Falling into cynical pessimism when immediate results do not materialize."
        ],
        "do": [
            "Embrace the beauty of slow compounding: Show up every day with quiet craftsmanship.",
            "Organize your finances, clear overdue debts, and streamline unnecessary overheads.",
            "Practice mindful stretching, yoga, and warm sesame oil massage for joint health.",
            "Serve the underprivileged, laborers, and elderly beings with genuine respect."
        ],
        "avoid": [
            "Do NOT succumb to despair or self-pity; Saturn rewards perseverance with monumental stability.",
            "Do NOT attempt to cut corners on quality, tax compliance, or legal paperwork.",
            "Do NOT hold bitter resentments or nurse grievances from the past.",
            "Do NOT isolate yourself entirely from warmth, laughter, and community."
        ]
    },
    "Mercury": {
        "title": "Budha (Mercury) — The Cycle of Intellect, Commerce & Agility",
        "circumstances": "You are in a bustling, intellectually dynamic chapter. Business negotiations, learning new software or languages, marketing, analytical problem-solving, and diverse networking occupy your reality.",
        "emotional_state": "Your mind is moving at lightning speed. You feel intellectually curious, eager to monetize your skills, and excited by new ideas, but prone to mental restlessness and scattered focus.",
        "karmic_meaning": "Mercury tests your intellectual discernment. It challenges you to convert raw information into actionable wisdom, using your words and business transactions as instruments of truth and value.",
        "challenges": [
            "Nervous exhaustion, mental fatigue, and screen burnout from constant connectivity.",
            "Starting 10 exciting projects simultaneously but struggling to complete them.",
            "Over-analyzing simple emotional situations until you create artificial problems.",
            "Miscommunication or ambiguous contractual clauses causing unnecessary stress."
        ],
        "do": [
            "Focus your intellectual horsepower on your top 2 revenue-generating priorities.",
            "Write down your ideas, maintain immaculate accounting, and audit digital subscriptions.",
            "Have certified legal counsel review contracts before signing commercial deals.",
            "Take scheduled digital detox breaks to walk barefoot in green nature."
        ],
        "avoid": [
            "Do NOT spread your energy thin across multiple half-baked speculative ventures.",
            "Do NOT participate in workplace gossip, cynicism, or sarcastic double-talk.",
            "Do NOT let digital devices hijack your bedtime hours and circadian rhythms.",
            "Do NOT substitute superficial theoretical knowledge for deep experiential mastery."
        ]
    },
    "Ketu": {
        "title": "Ketu (South Node) — The Cycle of Spiritual Awakening & Detachment",
        "circumstances": "You are in an introspective, transitional chapter. You are letting go of outdated career identities, questioning superficial social drama, and seeking deeper spiritual self-realization.",
        "emotional_state": "You feel emotionally detached from hollow status games. You may experience moments of feeling like an observer in your own life, craving solitude, silence, and communion with the transcendent.",
        "karmic_meaning": "Ketu is the cosmic liberator (*Moksha Karaka*). It dissolves obsolete attachments that your soul has outgrown, clearing away false crutches so you can discover your eternal inner light.",
        "challenges": [
            "Feeling aimless, unmotivated by worldly competition, or alienated from peers.",
            "Neglecting practical worldly responsibilities like accounting or health checkups.",
            "Sudden closures or terminations of partnerships that have run their karmic course.",
            "Vulnerability to melancholy, existential dread, or feeling misunderstood."
        ],
        "do": [
            "Commit to serious daily meditation, yogic breathwork (*Pranayama*), and spiritual study.",
            "Declutter your physical home, donate unneeded possessions, and practice minimalism.",
            "Release relationships and projects that end gracefully without clinging or bitterness.",
            "Hire disciplined professionals to handle your routine administrative and tax details."
        ],
        "avoid": [
            "Do NOT escape into numbing substances, apathy, or chronic procrastination.",
            "Do NOT burn bridges abruptly in fits of moodiness or spiritual pride.",
            "Do NOT abandon your worldly duties; practice *Karma Yoga* (duty without selfish attachment).",
            "Do NOT neglect physical health diagnostics or bodily nourishment."
        ]
    },
    "Venus": {
        "title": "Shukra (Venus) — The Cycle of Harmony, Romance & Refined Living",
        "circumstances": "You are navigating a period of relationship focus, aesthetic enhancement, artistic creativity, comfort, and social connection. Upgrading your lifestyle, home, and romantic life are front and center.",
        "emotional_state": "You feel romantic, appreciative of sensory pleasures, and deeply desirous of harmony. You want your surroundings and relationships to feel peaceful, loving, and aesthetically pleasing.",
        "karmic_meaning": "Venus invites you to discover the sacredness of beauty and human connection. It teaches you that true love is an act of honoring the divine spark in another person while preserving your own self-respect.",
        "challenges": [
            "Hedonistic procrastination: Delaying demanding work to chase comfort and leisure.",
            "Disillusionment when human relationships fail to match an idealized fairy tale.",
            "Lifestyle inflation, luxury overspending, and accumulating credit card debts.",
            "Over-compromising your boundaries to avoid temporary domestic conflict."
        ],
        "do": [
            "Channel creative inspiration into visual arts, music, interior design, or branding.",
            "Nurture your primary partnership through thoughtful, consistent romantic dates.",
            "Invest in durable, high-quality aesthetic assets rather than disposable fast fashion.",
            "Practice balanced nutrition and regular physical activity to counteract sensory indulgence."
        ],
        "avoid": [
            "Do NOT take on debts for luxury cars, designer items, or status symbols you cannot afford.",
            "Do NOT stay in toxic, high-maintenance partnerships out of fear of being alone.",
            "Do NOT suppress legitimate grievances simply to maintain a fragile artificial peace.",
            "Do NOT let comfort and pleasure distract you from your higher career discipline."
        ]
    }
}


def analyze_current_life_phase(kundli: Dict[str, Any]) -> Dict[str, Any]:
    """
    Constructs an exhaustive Vedic analysis of the native's Current Life Phase:
    - Active Mahadasha & Antardasha timeline
    - Present circumstances and life theme
    - Emotional state and how they are feeling right now
    - Karmic significance and what this phase means for them
    - Current challenges and friction points
    - Practical guidance: What to DO (Empowered actions) vs What to AVOID (Pitfalls)
    - Near-future preview (grounded outlook)
    - Subtle, reassuring Vedic disclaimer
    """
    dashas = kundli["dashas"]
    dasha_info = find_active_dasha(dashas)

    m_lord = dasha_info["mahadasha_lord"]
    ad_lord = dasha_info["antardasha_lord"]
    next_ad_lord = dasha_info["next_antardasha_lord"]
    next_ad_start = dasha_info["next_antardasha_start"]

    planets = {p["name"]: p for p in kundli["planets"]}
    p_m_lord = planets.get(m_lord, {})
    p_ad_lord = planets.get(ad_lord, {})

    m_profile = DASHA_PROFILES.get(m_lord, DASHA_PROFILES["Jupiter"])
    ad_profile = DASHA_PROFILES.get(ad_lord, DASHA_PROFILES["Mercury"])
    next_profile = DASHA_PROFILES.get(next_ad_lord, DASHA_PROFILES["Saturn"])

    # Synthesis of Mahadasha (macro-environment) + Antardasha (active catalyst)
    present_circumstances = (
        f"You are currently navigating the overarching era of **{m_lord} Mahadasha** (active through {dasha_info['mahadasha_end']}), "
        f"further energized by the immediate catalytic influence of **{ad_lord} Antardasha** (valid through {dasha_info['antardasha_end']}). "
        f"{m_profile['circumstances']} Concurrently, because {ad_lord} is your active sub-period catalyst, "
        f"your day-to-day focus is strongly directed toward {ad_profile['circumstances'].lower()}"
    )

    emotional_state = (
        f"At this specific point in your life journey, your inner world is shaped by the cosmic conversation between {m_lord} and {ad_lord}. "
        f"{m_profile['emotional_state']} In parallel, the immediate {ad_lord} influence introduces a layer of {ad_profile['emotional_state'].lower()}"
    )

    karmic_meaning = (
        f"**The Overarching Karmic Purpose:** {m_profile['karmic_meaning']} "
        f"Under the catalytic sub-cycle of {ad_lord}, the universe is actively pushing you to {ad_profile['karmic_meaning'].lower()} "
        f"This is not a passive waiting period, but a decisive chapter for profound self-realization and course-correction."
    )

    # Combined challenges (2 from Mahadasha, 2 from Antardasha)
    combined_challenges = m_profile["challenges"][:2] + ad_profile["challenges"][:2]

    # Combined DOs (2 from Mahadasha, 2 from Antardasha)
    combined_dos = m_profile["do"][:2] + ad_profile["do"][:2]

    # Combined AVOIDs (2 from Mahadasha, 2 from Antardasha)
    combined_avoids = m_profile["avoid"][:2] + ad_profile["avoid"][:2]

    # Near future outlook
    near_future_preview = (
        f"While your primary cosmic work is to master your present {ad_lord} period, the wheel of time will soon transition into the "
        f"**{next_ad_lord} Antardasha** (beginning around {next_ad_start}). This upcoming transition will gradually shift your energy "
        f"from your current focus toward {next_profile['circumstances'].lower()} "
        f"Grounding yourself in disciplined habits today will ensure that the upcoming {next_ad_lord} chapter unfolds as a period of fruitful expansion rather than stress."
    )

    disclaimer = (
        "🌸 A Gentle Reassuring Note: The insights, circumstances, and guidance presented in this Current Life Phase analysis "
        "are formulated upon the classical principles of Nirayana Vedic Jyotish (Vimshottari Dasha system). "
        "Astrological interpretations are symbolic and reflect cosmic tendencies; their accuracy and real-world effectiveness are not "
        "scientifically established, and planetary cycles may or may not align precisely with your subjective personal experiences. "
        "Please receive these reflections as an empowering compass for mindful living, self-awareness, and conscious personal responsibility."
    )

    return {
        "title": f"Current Life Phase: {m_lord} Mahadasha • {ad_lord} Antardasha (वर्तमान जीवन काल विवेचन)",
        "icon": "⏳",
        "mahadasha_lord": m_lord,
        "mahadasha_start": dasha_info["mahadasha_start"],
        "mahadasha_end": dasha_info["mahadasha_end"],
        "antardasha_lord": ad_lord,
        "antardasha_start": dasha_info["antardasha_start"],
        "antardasha_end": dasha_info["antardasha_end"],
        "next_antardasha_lord": next_ad_lord,
        "next_antardasha_start": next_ad_start,
        "present_circumstances": present_circumstances,
        "emotional_state": emotional_state,
        "karmic_meaning": karmic_meaning,
        "challenges": combined_challenges,
        "what_to_do": combined_dos,
        "what_to_avoid": combined_avoids,
        "near_future_outlook": near_future_preview,
        "disclaimer": disclaimer
    }


SIGN_LORDS = {
    1: "Mars", 2: "Venus", 3: "Mercury", 4: "Moon",
    5: "Sun", 6: "Mercury", 7: "Venus", 8: "Mars",
    9: "Jupiter", 10: "Saturn", 11: "Saturn", 12: "Jupiter"
}


def detect_financial_yogas_and_vyaya(kundli: Dict[str, Any]) -> Tuple[List[Dict[str, str]], Dict[str, Any]]:
    """
    Detects classical Vedic Dhan Yogas (Wealth Combinations) and calculates
    12th House (Vyaya Bhava) Financial Drain and Expenditure Leakages.
    """
    planets = {p["name"]: p for p in kundli["planets"]}
    d1_houses = {h["house"]: h for h in kundli["d1_houses"]}
    lagna = kundli["lagna"]
    lagna_sign_id = lagna["sign_id"]

    moon = planets.get("Moon", {})
    sun = planets.get("Sun", {})
    jupiter = planets.get("Jupiter", {})
    saturn = planets.get("Saturn", {})
    venus = planets.get("Venus", {})
    mars = planets.get("Mars", {})
    mercury = planets.get("Mercury", {})
    rahu = planets.get("Rahu", {})
    ketu = planets.get("Ketu", {})

    dhan_yogas = []

    # 1. Chandra-Mangal Lakshmi Yoga (चन्द्र-मङ्गल महालक्ष्मी योग)
    if moon and mars:
        m_house = moon.get("house", 1)
        ma_house = mars.get("house", 1)
        if m_house == ma_house:
            dhan_yogas.append({
                "name": "Chandra-Mangal Lakshmi Yoga (चन्द्र-मङ्गल महालक्ष्मी योग)",
                "category": "Supreme Commercial Wealth (व्यापारिक एवं अचल सम्पति योग)",
                "description": f"Chandra (Moon) and Mangal (Mars) form a sacred conjunction in House {m_house}. Classical Parashari Jyotish celebrates this as one of the most powerful Lakshmi Yogas, granting relentless earning energy, commercial savvy, real estate acquisition, and multi-source wealth generation."
            })
        elif ((ma_house - m_house) % 12) + 1 == 7:
            dhan_yogas.append({
                "name": "Chandra-Mangal Drishti Lakshmi Yoga (चन्द्र-मङ्गल दृष्टि लक्ष्मी योग)",
                "category": "High Liquid Cashflow (नकद प्रवाह एवं व्यावसायिक सफलता)",
                "description": f"Moon and Mars cast direct mutual aspects on each other across the 1/7 axis (Houses {m_house} and {ma_house}). This fuels unstoppable commercial persistence, rapid recovery from financial shocks, and bold investment compounding."
            })

    # 2. Gajakesari Yoga (गजकेसरी महायोग)
    if moon and jupiter:
        m_house = moon.get("house", 1)
        j_house = jupiter.get("house", 1)
        rel_pos = ((j_house - m_house) % 12) + 1
        if rel_pos in [1, 4, 7, 10]:
            dhan_yogas.append({
                "name": "Gajakesari Samriddhi Yoga (गजकेसरी समृद्धि योग)",
                "category": "Sovereign Institutional Wealth (राजकीय एवं बौद्धिक सम्पति)",
                "description": f"Jupiter resides in a Kendra (House {j_house}) from the Moon (House {m_house}). This provides lasting financial solvency, patronage from wealthy institutions, intellectual asset generation, and divine protection against poverty."
            })

    # 3. Budhaditya Dhana Yoga (बुधादित्य धन योग)
    if sun and mercury:
        if sun.get("house") == mercury.get("house"):
            b_house = sun.get("house", 1)
            dhan_yogas.append({
                "name": "Budhaditya Dhana Yoga (बुधादित्य राजयोग)",
                "category": "Intellectual & Administrative Wealth (बौद्धिक एवं व्यापारिक लाभ)",
                "description": f"Sun (Authority) and Mercury (Commerce & Intellect) unite in House {b_house}. Endows the native with supreme negotiating prowess, lucrative advisory opportunities, government contracts, and profitable financial stewardship."
            })

    # 4. Lords of 2nd (Dhana Sthana) & 11th (Labha Sthana)
    h2_sign = d1_houses.get(2, {}).get("sign_id", 2)
    h11_sign = d1_houses.get(11, {}).get("sign_id", 11)
    lord_2_name = SIGN_LORDS.get(h2_sign, "Venus")
    lord_11_name = SIGN_LORDS.get(h11_sign, "Saturn")
    p_lord_2 = planets.get(lord_2_name)
    p_lord_11 = planets.get(lord_11_name)

    if p_lord_2 and p_lord_11:
        if p_lord_2.get("house") == p_lord_11.get("house"):
            dhan_yogas.append({
                "name": "Maha Parashari Dhana-Labha Yoga (महा धन-लाभ योग)",
                "category": "Direct Income-to-Accumulation Pipeline (अखंड धन संचय)",
                "description": f"The ruler of the 2nd House ({lord_2_name} - Accumulated Wealth) and 11th House ({lord_11_name} - Profit & Liquid Inflow) are conjoined in House {p_lord_2.get('house')}. This directly connects incoming revenue to long-term compounding reserves, minimizing cash leakage."
            })
        elif p_lord_2.get("house") in [1, 2, 5, 9, 11]:
            dhan_yogas.append({
                "name": f"Dhanadhipati Subha Sthana ({lord_2_name} धन भाव शुभ स्थिति)",
                "category": "Asset Fortification (कोष वृद्धि एवं पारिवारिक सम्पति)",
                "description": f"The 2nd house wealth ruler ({lord_2_name}) is strongly positioned in House {p_lord_2.get('house')}, ensuring steady compounding of bank balances, gold holdings, and immovable ancestral assets."
            })
        elif p_lord_11.get("house") in [1, 2, 5, 9, 11]:
            dhan_yogas.append({
                "name": f"Labhadhipati Utkrishta Yoga ({lord_11_name} लाभ भाव वृद्धि)",
                "category": "Continuous Cash Inflow (निरंतर आय एवं व्यावसायिक विस्तार)",
                "description": f"The 11th house ruler of gains ({lord_11_name}) occupies House {p_lord_11.get('house')}, generating recurring high-ticket earnings, multi-channel profit streams, and lucrative institutional networks."
            })

    # 5. Vasumati Yoga (Benefics in Upachayas 3, 6, 10, 11)
    benefics_upachaya = 0
    for b_name in ["Jupiter", "Venus", "Mercury"]:
        bp = planets.get(b_name)
        if bp and bp.get("house") in [3, 6, 10, 11]:
            benefics_upachaya += 1
    if benefics_upachaya >= 2:
        dhan_yogas.append({
            "name": "Vasumati Maha Yoga (वसुमती महालक्ष्मी योग)",
            "category": "Indomitable Financial Independence (अपार समृद्धि एवं स्वावलंबन)",
            "description": "Benefic planets occupy Upachaya houses (3rd, 6th, 10th, or 11th). Sage Varahamihira states that one with Vasumati Yoga never depends on others for sustenance and commands abundant wealth and property throughout life."
        })

    # 6. Shukra Bhogya Samriddhi
    if venus:
        v_house = venus.get("house", 1)
        if venus.get("dignity", "").startswith("Exalted") or v_house in [1, 2, 4, 5, 9, 11]:
            dhan_yogas.append({
                "name": "Shukra Bhogya Samriddhi Yoga (शुक्र भोग्य समृद्धि योग)",
                "category": "Luxury & Aesthetic Wealth (वाहन, आभूषण एवं विलासिता)",
                "description": f"Venus sits auspiciously in House {v_house} in {venus.get('sign_name')}. Bestows natural magnetism for material comfort, luxury vehicles, high-end real estate, and prosperous partnerships."
            })

    # 7. Guru-Mangal Yoga
    if jupiter and mars:
        if jupiter.get("house") == mars.get("house") or ((mars.get("house", 0) - jupiter.get("house", 0)) % 12) + 1 in [1, 4, 7, 10]:
            dhan_yogas.append({
                "name": "Guru-Mangal Parakrama Yoga (गुरु-मङ्गल पराक्रम योग)",
                "category": "Industrial & Real Estate Empire (भूमि, भवन एवं औद्योगिक लाभ)",
                "description": "Jupiter and Mars establish an angular sambandha. Blends moral wisdom with aggressive execution, producing immense fortune in land development, construction, agriculture, and high-capital enterprises."
            })

    if not dhan_yogas:
        dhan_yogas.append({
            "name": "Nisarga Dhana Sthiti (नैसर्गिक धन योग)",
            "category": "Steady Compounding (सतत कर्म एवं नियमित आय)",
            "description": "The fundamental alignment of your wealth houses indicates that systematic discipline, consistent compounding, and avoidance of speculation will steadily build significant financial security."
        })

    # ================= 12th House (Vyaya Bhava) Analysis =================
    h12 = d1_houses.get(12, {})
    h12_sign_id = h12.get("sign_id", 12)
    h12_sign_obj = ZODIAC_SIGNS[h12_sign_id - 1]
    h12_planets_list = [p["name"] for p in kundli["planets"] if p["house"] == 12]

    vyaya_leakage_sources = []
    vyaya_mitigations = []
    vyaya_psychological_triggers = []

    if "Mars" in h12_planets_list:
        vyaya_leakage_sources.append("🚨 Kuja Vyaya Drain: Sudden expenditure through impulsive disputes, traffic fines, aggressive emergency vehicle repairs, surgical bills, or contentious family arguments.")
        vyaya_psychological_triggers.append("Rage spending and impatience: Taking financial actions when aggravated or attempting to solve emotional friction by throwing money at it.")
        vyaya_mitigations.append("Never enter contracts while emotionally heated; institute a 72-hour pause on high-ticket purchases; maintain a dedicated emergency medical and legal buffer fund.")

    if "Rahu" in h12_planets_list:
        vyaya_leakage_sources.append("🚨 Rahu Chhaya Phantom Leak: Money vanishing into speculative digital assets, unverified internet crypto/trading schemes, deceptive foreign travel expenses, or impulsive late-night electronic gadget purchases.")
        vyaya_psychological_triggers.append("Fear of Missing Out (FOMO) and allure of exotic shortcuts: Succumbing to high-yield hype and glossy foreign opportunities without legal vetting.")
        vyaya_mitigations.append("Strictly disable unverified online trading apps; limit daily digital wallet transactions; enforce a mandatory 48-hour cooling-off rule on high-tech splurges.")

    if "Ketu" in h12_planets_list:
        vyaya_leakage_sources.append("⚠️ Ketu Vairagya Carelessness: Forgetting to collect invoices or debts owed to you, losing track of receipts, giving loans without written documentation, and impulsive donations to fraudulent spiritual causes.")
        vyaya_psychological_triggers.append("Spiritual detachment and financial avoidance: Feeling that talking about money is unholy or awkward, leading to severe financial negligence.")
        vyaya_mitigations.append("Hire an uncompromising accountant or use automated invoice-tracking software; never extend loans based on verbal promises or emotional sympathy alone.")

    if "Saturn" in h12_planets_list:
        vyaya_leakage_sources.append("⏳ Shani Vilamba Institutional Drag: Prolonged loan interest accumulations, delayed taxation penalties, chronic recurring maintenance on depreciating legacy equipment, or unexpected bureaucratic fees.")
        vyaya_psychological_triggers.append("Procrastination on debt settlements: Ignoring overdue liabilities until compounding penalties escalate into severe burdens.")
        vyaya_mitigations.append("Prioritize debt amortization above all discretionary spending; keep tax accounting immaculate; avoid taking multi-year unsecured consumer debt.")

    if "Sun" in h12_planets_list:
        vyaya_leakage_sources.append("👑 Surya Tejas Vanity Drain: Overspending to protect social prestige, lavish hosting to appear authoritative, government administrative fines, or underwriting liabilities of dominant authority figures.")
        vyaya_psychological_triggers.append("Ego-driven pride: Inability to say 'I cannot afford this right now' in front of peers, relatives, or social rivals.")
        vyaya_mitigations.append("Separate personal self-worth from material display; keep tax filings strictly audited by qualified professionals; refuse to co-sign sovereign loans.")

    if "Moon" in h12_planets_list:
        vyaya_leakage_sources.append("🌊 Chandra Manas Emotional Drainage: Retail therapy splurges during bouts of sadness, anxiety, or celebration; over-subsidizing emotionally manipulative relatives or friends.")
        vyaya_psychological_triggers.append("Emotional fluctuations: Using credit cards as emotional anesthetics when feeling unloved, overwhelmed, or lonely.")
        vyaya_mitigations.append("Separate emotional healing from financial spending; institute a dual-signature banking system with a grounded partner or fiduciary.")

    if "Venus" in h12_planets_list:
        vyaya_leakage_sources.append("💎 Shukra Vilasa Luxury Splurge: Excessive lifestyle inflation, designer clothing, fine dining, opulent aesthetic remodels, and high-maintenance romantic dates.")
        vyaya_psychological_triggers.append("Aesthetic hedonism: Rationalizing high-ticket luxury purchases as 'essentials' for emotional happiness.")
        vyaya_mitigations.append("Cap discretionary luxury spending strictly at 10% of monthly net income; invest the principal before spending any dividend or bonus.")

    if "Mercury" in h12_planets_list:
        vyaya_leakage_sources.append("📜 Budha Vyaya Intellectual Slip: Careless fine-print contractual mistakes, day-trading algorithm errors, gadget hoarding, or buying subscriptions and online courses that are never completed.")
        vyaya_psychological_triggers.append("Intellectual restlessness: Believing that purchasing information or tools equals having mastered the skill.")
        vyaya_mitigations.append("Have legal contracts reviewed by a certified attorney before signing; cancel recurring unutilized digital subscriptions every quarter.")

    if "Jupiter" in h12_planets_list:
        vyaya_leakage_sources.append("📿 Guru Dharma Moral Over-Commitment: Over-generous donations to temples/institutions exceeding your budget, or financing unviable businesses for loved ones out of moral guilt.")
        vyaya_psychological_triggers.append("Messianic guilt: Feeling spiritually responsible for solving everyone else's financial emergencies.")
        vyaya_mitigations.append("Practice structured tithing (fixed percentage only); remember that your first sacred dharma is ensuring your own family's financial fortress.")

    if not vyaya_leakage_sources:
        h12_element = h12_sign_obj["element"]
        h12_lord = h12_sign_obj["lord"]
        if h12_element == "Fire":
            vyaya_leakage_sources.append(f"🔥 Agni Bhava Drain (Ruled by {h12_lord}): Sudden impulsive expenditures on travel, adventure sports, spontaneous technology upgrades, and quick-trigger purchases.")
            vyaya_psychological_triggers.append("Adrenaline rushes: Purchasing items in the thrill of inspiration without calculating long-term cashflow.")
            vyaya_mitigations.append("Enforce a mandatory 72-hour delay on all non-essential purchases above ₹15,000 / $200.")
        elif h12_element == "Earth":
            vyaya_leakage_sources.append(f"🌍 Prithvi Bhava Drain (Ruled by {h12_lord}): Unexpected domestic repairs, maintenance of vehicles or home appliances, healthcare diagnostics, and bureaucratic fees.")
            vyaya_psychological_triggers.append("Deferred maintenance: Postponing minor structural fixes until they become expensive emergencies.")
            vyaya_mitigations.append("Create a dedicated monthly sinking fund specifically reserved for property, auto, and medical contingencies.")
        elif h12_element == "Air":
            vyaya_leakage_sources.append(f"💨 Vayu Bhava Drain (Ruled by {h12_lord}): Continuous trickle leakages on smart electronics, networking dinners, subscriptions, short commutes, and social travel.")
            vyaya_psychological_triggers.append("Social restlessness: Spending money to maintain active engagement across diverse social and professional circles.")
            vyaya_mitigations.append("Audit all digital bank statements on the 1st of every month and cap monthly networking entertainment budgets.")
        else: # Water
            vyaya_leakage_sources.append(f"🌊 Jala Bhava Drain (Ruled by {h12_lord}): Emotional spending, comforting distressed friends, spiritual journeys, wellness retreats, and impulsive hospitality.")
            vyaya_psychological_triggers.append("Boundless empathy: Carrying the financial burden of loved ones who refuse to practice their own financial discipline.")
            vyaya_mitigations.append("Establish firm emotional and financial boundaries; never give money you cannot afford to write off as a complete gift.")

    vyaya_data = {
        "house_num": 12,
        "sign_name": h12_sign_obj["name"],
        "sign_sanskrit": h12_sign_obj["sanskrit"],
        "lord": h12_sign_obj["lord"],
        "occupants": h12_planets_list if h12_planets_list else [f"Empty (Ruled by {h12_sign_obj['lord']})"],
        "leakage_sources": vyaya_leakage_sources,
        "psychological_triggers": vyaya_psychological_triggers,
        "remedial_mitigations": vyaya_mitigations
    }

    return dhan_yogas, vyaya_data


SIGN_ELEMENTS = {
    1: ("Fire", "Agni (अग्नि)"), 2: ("Earth", "Prithvi (पृथ्वी)"), 3: ("Air", "Vayu (वायु)"), 4: ("Water", "Jala (जल)"),
    5: ("Fire", "Agni (अग्नि)"), 6: ("Earth", "Prithvi (पृथ्वी)"), 7: ("Air", "Vayu (वायु)"), 8: ("Water", "Jala (जल)"),
    9: ("Fire", "Agni (अग्नि)"), 10: ("Earth", "Prithvi (पृथ्वी)"), 11: ("Air", "Vayu (वायु)"), 12: ("Water", "Jala (जल)")
}

NAKSHATRA_AURA = {
    "Ashwini": ("Swift Pioneering Energy", "carries the swift healing vitality of the Ashwini Kumaras, projecting boundless enthusiasm and quick problem-solving initiative"),
    "Bharani": ("Transformative Willpower", "projects an intense, passionate, and magnetic presence ruled by Yama, unafraid of deep responsibility or emotional gravity"),
    "Krittika": ("Penetrating Discernment", "radiates a sharp, radiant, and noble solar flame, commanding respect through uncompromising honesty and intellectual incisiveness"),
    "Rohini": ("Sensory Charm & Grace", "exudes an enchanting, artistic, and soothing aura ruled by Prajapati, naturally drawing people through magnetic warmth and refined grace"),
    "Mrigashira": ("Inquisitive Seeker", "projects a gentle, alert, and perpetually curious aura, constantly scanning horizons for knowledge, beauty, and authentic connection"),
    "Ardra": ("Intellectual Breakthrough", "carries a tempestuous, brilliant, and transformative aura ruled by Rudra, unafraid to dismantle obsolete structures to birth modern clarity"),
    "Punarvasu": ("Benevolent Renewal", "projects an auspicious, comforting, and nurturing presence governed by Aditi, bringing restoration and gentle optimism to troubled waters"),
    "Pushya": ("Sovereign Nourishment", "radiates deep spiritual gravity, grounded ethical wisdom, and quiet paternal authority governed by Brihaspati"),
    "Ashlesha": ("Penetrating Mystical Depth", "projects a hypnotic, intense, and psychologically astute presence ruled by the Nagas, seeing through social masks effortlessly"),
    "Magha": ("Ancestral Royal Dignity", "carries an innate regal carriage, honorable self-respect, and deep veneration for lineage and noble conduct"),
    "Purva Phalguni": ("Charismatic Joy & Warmth", "projects an effortless social magnetism, creative exuberance, and love for celebration and cultural refinement"),
    "Uttara Phalguni": ("Steadfast Honorable Patron", "radiates warm dependability, generous patronage, and a principled commitment to duty and societal welfare"),
    "Hasta": ("Masterful Craftsmanship & Dexterity", "projects an agile, resourceful, and disarmingly witty presence, skilled in turning ideas into tangible practical reality"),
    "Chitra": ("Dazzling Aesthetic Brilliance", "radiates a luminous, sculpted, and highly creative aura governed by Vishwakarma, obsessed with symmetry, elegance, and beauty"),
    "Swati": ("Independent Intellectual Breeze", "projects an adaptable, polite, and fiercely autonomous aura governed by Vayu, navigating diverse social spaces with effortless diplomacy"),
    "Vishakha": ("Triumphant Focused Purpose", "radiates intense determination, goal-oriented momentum, and an unshakeable drive to conquer ambitious summits"),
    "Anuradha": ("Devoted Collaborative Heart", "projects deep emotional loyalty, collaborative spirit, and a soulful ability to unite people across divides"),
    "Jyeshtha": ("Senior Protective Authority", "radiates seasoned dignity, sharp protective instincts, and an aura of an elder statesman who commands respect"),
    "Mula": ("Radical Truth & Root Investigation", "projects a fearless, uncompromising, and deeply introspective aura, seeking the absolute root of every mystery"),
    "Purva Ashadha": ("Invincible Optimism & Grace", "radiates victorious charisma, persuasive eloquence, and an unwavering belief in ultimate triumph"),
    "Uttara Ashadha": ("Enduring Righteousness", "projects quiet universal nobility, deep humility paired with unshakeable resolve, and enduring integrity"),
    "Shravana": ("Scholarly Receptive Wisdom", "radiates deep listening patience, scholarly erudition, and a tranquil aura of traditional wisdom and cultural learning"),
    "Dhanishta": ("Rhythmic Opulence & Drive", "projects a high-spirited, rhythmic, and prosperous confidence, excelling in performance, organizational leadership, and music"),
    "Shatabhisha": ("Enigmatic Healing Vision", "carries a reserved, visionary, and enigmatic aura ruled by Varuna, gifted with deep foresight and unconventional intellect"),
    "Purva Bhadrapada": ("Ascetic Transformative Fire", "projects an intense, philosophically serious, and dual-natured presence, capable of monumental discipline and vision"),
    "Uttara Bhadrapada": ("Contemplative Cosmic Serenity", "radiates serene wisdom, deep ocean-like patience, and a protective, selfless spiritual presence"),
    "Revati": ("Boundless Compassion & Elegance", "projects a gentle, sweet, and transcendent grace governed by Pushan, offering universal nourishment and exquisite aesthetic taste")
}

HOUSE_NAMES = {
    1: "1st House (Lagna Bhava - Self & Vitality)",
    2: "2nd House (Dhana Bhava - Wealth & Family Speech)",
    3: "3rd House (Sahaja Bhava - Courage, Initiative & Siblings)",
    4: "4th House (Sukha Bhava - Home, Heart & Emotional Sanctuary)",
    5: "5th House (Putra & Buddhi Bhava - Intellect, Romance & Creative Genius)",
    6: "6th House (Shatru & Roga Bhava - Service, Overcoming Obstacles & Daily Duty)",
    7: "7th House (Kalatra Bhava - Marriage, Partnerships & Social Mirror)",
    8: "8th House (Ayu & Randhra Bhava - Transformation, Occult & Hidden Depths)",
    9: "9th House (Bhagya & Dharma Bhava - Higher Wisdom, Fortune & Purpose)",
    10: "10th House (Karma Bhava - Profession, Public Stature & Legacy)",
    11: "11th House (Labha Bhava - Gains, Aspirations & Social Networks)",
    12: "12th House (Vyaya & Moksha Bhava - Solitude, Spirituality & Liberation)"
}

SPOUSE_LORD_FEATURES = {
    "Sun": {
        "archetype": "Regal, Authoritative & Honorable Presence",
        "stature_m": "Broad-shouldered, upright, authoritative posture with commanding carriage",
        "stature_f": "Poised, statuesque, elegant posture with noble, proud carriage",
        "face": "Well-chiseled bone structure, high noble forehead, and prominent commanding jawline",
        "eyes": "Bright, warm honey-amber or golden-brown eyes with a direct, penetrating gaze",
        "complexion": "Vibrant, sun-kissed or warm radiant complexion with healthy natural luster",
        "hair": "Thick, slightly coarse or wavy hair, groomed in a clean, sophisticated, stately manner",
        "style": "Regal classicism: crisp tailoring, rich jewel tones (royal blue, crimson, deep gold), and premium statement accessories",
        "personality": [
            "Sovereign self-respect: Possesses an unshakeable inner dignity and despises petty, dishonest, or cowardly behavior.",
            "Natural leadership: Commands respect effortlessly in social and professional arenas without raising their voice.",
            "Generous protector: Fiercely loyal and protective over you, acting as an honorable shield against outside difficulties.",
            "Principled integrity: Values transparency and truth above all else; their word is their unbreakable bond."
        ],
        "behavior": [
            "Treats the marriage as a sacred alliance of equals, taking immense pride in your accomplishments and celebrating your growth.",
            "Can be sensitive to perceived disrespect or public slights; demands heartfelt appreciation and courteous communication.",
            "Steps up fearlessly during family crises to shoulder major responsibilities and provide decisive direction.",
            "Shows devotion through noble gestures, generous patronage, and ensuring the family thrives with high social honor."
        ]
    },
    "Moon": {
        "archetype": "Gentle, Nurturing & Luminous Countenance",
        "stature_m": "Well-proportioned, comfortable build, moves with gentle poise and soothing presence",
        "stature_f": "Gracefully contoured, soft gentle curves, moving with tranquil, feminine elegance",
        "face": "Round or oval contour with soft sculpted features, gentle chin, and an enchanting, disarming smile",
        "eyes": "Large, luminous, limpid eyes that exude tender empathy, emotional transparency, and warmth",
        "complexion": "Fair, glowing, or clear luminous skin that reflects light with natural youthfulness",
        "hair": "Soft, silky, lustrous wavy or flowing hair that frames the face with gentle elegance",
        "style": "Soft romantic elegance: flowing natural fabrics (linen, silk, fine cotton), soothing pastel and pearl-white palettes, and timeless subtle jewelry",
        "personality": [
            "Profound emotional intelligence: Deeply intuitive and perceptive, sensing your feelings before you speak a single word.",
            "Nurturing sanctuary: Naturally creates an oasis of comfort, warmth, and peace where you can completely let your guard down.",
            "Devoted family values: Places home, emotional roots, and domestic happiness at the very heart of their existence.",
            "Gentle peacemaker: Seeks harmony and reconciliation; avoids harsh confrontations and heals tension with tenderness."
        ],
        "behavior": [
            "Expresses love through continuous affectionate care: cooking your favorite meals, soothing physical touch, and listening with patience.",
            "Mood can ebb and flow with emotional tides; thrives when you offer reassuring verbal affirmations of your unconditional love.",
            "Deeply attached to the shared domestic haven; loves spending peaceful evenings together rather than loud social parties.",
            "Becomes your most intuitive emotional anchor, sensing when you are stressed and quietly lifting the burden off your shoulders."
        ]
    },
    "Mars": {
        "archetype": "Athletic, Energetic & Spirited Trailblazer",
        "stature_m": "Toned, athletic, muscular physique; carries an unmistakable kinetic energy and decisive, confident stride",
        "stature_f": "Fit, athletic, supple and toned silhouette; carries dynamic kinetic grace and vibrant stamina",
        "face": "Defined chiseled jaw, strong facial angles, expressive brows, and an energetic, magnetic smile",
        "eyes": "Sharp, piercing, intensely alert amber or dark eyes that hold eye contact fearlessly",
        "complexion": "Warm, healthy, ruddy or vibrant glowing skin with natural athletic vitality",
        "hair": "Dense, strong hair, frequently styled sportily, trimmed sharp, or pulled back cleanly",
        "style": "Sporty chic and crisp minimalism: functional athletic tailoring, clean lines, bold contrast accents (black, scarlet, graphite), and effortless modern flair",
        "personality": [
            "Fearless vitality: Action-oriented, dynamic, and refuses to be paralyzed by indecision or hesitation.",
            "Radical candid honesty: What you see is what you get; they hate passive-aggressive games and speak the direct truth.",
            "Passionate loyalty: Fights fiercely on your side in any dispute, backing you up with complete conviction.",
            "Playful competitive drive: Injects adventurous excitement, spontaneity, and contagious motivation into everyday life."
        ],
        "behavior": [
            "Addresses marital misunderstandings immediately and directly; hates brooding or silent treatments and prefers swift resolution.",
            "Constantly motivates you to conquer fitness goals, career leaps, and personal ambitions without fear.",
            "May have a momentary flash of impatience when plans stall, but cools down rapidly and seeks warm affectionate reconnection.",
            "Thrives on shared active pursuits: outdoor treks, competitive games, travel adventures, and passionate physical intimacy."
        ]
    },
    "Mercury": {
        "archetype": "Evergreen, Witty & Articulate Companion",
        "stature_m": "Slender, youthful, agile build; moves with quick, lively coordination and perpetual youthful energy",
        "stature_f": "Petite or slender, graceful agile build; moves with light-footed, youthful, spirited coordination",
        "face": "Delicate symmetrical features, sparkling expressive eyes, animated brows, and a playful, disarming smile",
        "eyes": "Bright, quick-witted, curious eyes that constantly observe details and twinkle with humor",
        "complexion": "Clear, youthful, fresh complexion with a radiant, well-maintained glow",
        "hair": "Fine, well-groomed, smartly styled hair that always looks polished and contemporary",
        "style": "Smart-casual elegance: versatile contemporary cuts, clever mix-and-match palettes (emerald, mint, crisp white), and modern intellectual accessories",
        "personality": [
            "Brilliant conversationalist: Endless curiosity, sharp wit, and a wonderful sense of humor that turns everyday chores into joyful banter.",
            "Agile problem solver: Pragmatic and adaptable; approaches emotional dilemmas with analytical logic and sensible solutions.",
            "Lifelong learner: Constantly exploring new books, digital trends, podcasts, or business ideas; highly stimulating partner.",
            "Diplomatic bridge-builder: Easily navigates social dynamics and gets along effortlessly with your relatives and friends."
        ],
        "behavior": [
            "Deep bond built on mental camaraderie: loves sending witty texts throughout the day, sharing articles, and having late-night debates.",
            "Diffuses marital tension with gentle humor and logical communication rather than emotional drama.",
            "Manages household logistics, schedules, and daily communications with remarkable efficiency and precision.",
            "Needs intellectual stimulation and variety; thrives when you embark on shared learning projects and cultural adventures together."
        ]
    },
    "Jupiter": {
        "archetype": "Dignified, Scholarly & Noble Soul",
        "stature_m": "Tall, stately, well-proportioned commanding stature; moves with serene poise and natural gravitas",
        "stature_f": "Tall or dignified, gracefully proportioned stature; moves with regal warmth and reassuring presence",
        "face": "Broad, noble countenance, graceful forehead, kind radiant smile, and an aura of profound moral integrity",
        "eyes": "Warm, deep, reassuring eyes that emanate ancient wisdom, benevolence, and non-judgmental acceptance",
        "complexion": "Golden, radiant, clear complexion that exudes good health, vitality, and purity",
        "hair": "Soft, healthy, neatly parted or dignified hair, worn in a classic, timeless style",
        "style": "Noble classical sophistication: traditional handlooms, rich muted golds, cream, saffron, and deep blues; impeccably dignified and respectable",
        "personality": [
            "Moral compass: Governed by deep ethical values, spiritual wisdom, and a generous heart that seeks to uplift everyone around them.",
            "Unshakeable optimism: Brings expansive faith and perspective into your home, reminding you that all challenges pass.",
            "Intellectual depth: Highly educated, philosophical, or deeply rooted in cultural/spiritual heritage; a true mentor and companion.",
            "Magnanimous benevolence: Forgiving, patient, and broad-minded; despises pettiness and treats you with supreme courtesy."
        ],
        "behavior": [
            "Treats you with immense respect and acts as your trusted lifelong counselor, offering calm, balanced guidance in every life decision.",
            "Encourages your spiritual, ethical, and intellectual evolution, celebrating your triumphs without a shred of jealousy.",
            "Maintains harmonious, highly honorable relationships with in-laws and extended family, earning universal admiration.",
            "Creates an auspicious domestic atmosphere filled with books, spiritual reflection, hospitality, and joyful celebrations."
        ]
    },
    "Venus": {
        "archetype": "Harmonious, Artistic & Beautiful Muse",
        "stature_m": "Symmetrically balanced, handsome, athletic yet graceful frame; moves with natural rhythm and magnetic charm",
        "stature_f": "Exquisitely balanced, curvaceous or sculpted silhouette; moves with natural poise and magnetic feminine grace",
        "face": "Exquisite facial symmetry, soft sculpted cheeks, captivating dimpled smile, and beautifully defined lips",
        "eyes": "Captivating, expressive, radiant eyes with long lashes that hold a disarming, hypnotic warmth",
        "complexion": "Luminous, velvety, glowing skin with natural radiance that seems lit from within",
        "hair": "Lustrous, voluminous, beautifully textured hair, carefully conditioned and perfumed",
        "style": "High aesthetic grace: bespoke fashion, luxurious tactile textures (silk, cashmere, velvet), harmonious pastel shades, and exquisite signature fragrance",
        "personality": [
            "Aesthetic genius: An innate eye for visual beauty, music, interior charm, and creating harmonious living environments.",
            "Romantic devotion: Believes in soulful romance, heartfelt courting, mutual pampering, and keeping passion alive through the decades.",
            "Empathetic diplomacy: Exceptionally skilled at resolving conflicts with sweet words, tact, and emotional gentleness.",
            "Generous hospitality: Loves welcoming guests, organizing elegant dinners, and showering loved ones with thoughtful gifts."
        ],
        "behavior": [
            "Showering you with daily affectionate gestures, love notes, sensory pampering, and passionate physical closeness.",
            "Cannot tolerate vulgarity, screaming arguments, or chaos; blossoms when the marital bond is handled with mutual gentleness and courtesy.",
            "Transforms your living space into an aesthetic sanctuary filled with soothing colors, art, soft lighting, and warmth.",
            "Deeply loyal and reciprocal; when they feel cherished, their love compounds into an inexhaustible fountain of devotion."
        ]
    },
    "Saturn": {
        "archetype": "Steadfast, Mature & Enduring Anchor",
        "stature_m": "Tall, lean, structured bone framework; moves with deliberate, unhurried, grounded dignity and an ageless presence",
        "stature_f": "Tall or lean, structured elegant silhouette; carries an ageless, quiet, refined poise",
        "face": "Strong defined jawline, contemplative cheekbones, deep thoughtful expression, and an earnest, trustworthy smile",
        "eyes": "Deep-set, steady, introspective dark eyes that look through illusions into the core reality",
        "complexion": "Earthy, distinguished, healthy matte complexion that matures with incredible grace over time",
        "hair": "Straight or structured hair, groomed conservatively, neatly maintained, and timelessly styled",
        "style": "Understated luxury & timeless minimalism: structured coats, dark neutral tones (slate gray, charcoal, navy, earth brown), and durable high-quality craft",
        "personality": [
            "Monumental loyalty: Once their commitment is given, it is written in stone; they will stand beside you through poverty or wealth, storm or sunshine.",
            "Emotional maturity: A quiet rock who never gets swept away by hysterical panic; supremely grounded in practical reality.",
            "Pragmatic financial stewardship: Brilliant at long-term planning, building generational security, and avoiding wasteful impulses.",
            "Patient perseverance: Works tirelessly for the family's welfare without boasting, letting their steady actions speak for them."
        ],
        "behavior": [
            "Demonstrates love through quiet, steadfast acts of dedicated service and lifelong emotional safety rather than theatrical flattery.",
            "May take time to open up emotionally, but their inner devotion is profoundly deep, dependable, and rock-solid.",
            "Helps you structure your life, organize finances, and stay anchored during external storms.",
            "Values privacy and quiet evenings at home; a true anchor who grows increasingly romantic and affectionate as the years mature."
        ]
    }
}


def generate_personalized_psychological_profile(kundli: Dict[str, Any]) -> Dict[str, Any]:
    lagna = kundli["lagna"]
    planets = {p["name"]: p for p in kundli["planets"]}
    d1_houses = {h["house"]: h for h in kundli["d1_houses"]}

    lagna_id = lagna["sign_id"]
    lagna_name = lagna["sign_name"]
    lagna_sanskrit = lagna["sign_sanskrit"]
    lagna_nak = lagna["nakshatra"]
    lagna_pada = lagna["pada"]
    lagna_elem_eng, lagna_elem_san = SIGN_ELEMENTS.get(lagna_id, ("Fire", "Agni"))
    lagna_lord_name = SIGN_LORDS.get(lagna_id, "Mars")
    p_lagna_lord = planets.get(lagna_lord_name, {})
    ll_house = p_lagna_lord.get("house", 1)
    ll_sign = p_lagna_lord.get("sign_name", lagna_name)
    ll_dignity = p_lagna_lord.get("dignity", "Neutral")

    h1_occupants = [p["name"] for p in kundli["planets"] if p["house"] == 1]

    moon = planets.get("Moon", {})
    moon_sign_id = moon.get("sign_id", lagna_id)
    moon_sign = moon.get("sign_name", "Taurus")
    moon_sanskrit = moon.get("sign_sanskrit", "Vrishabha")
    moon_house = moon.get("house", 1)
    moon_nak = moon.get("nakshatra", "Rohini")
    moon_dignity = moon.get("dignity", "Neutral")
    moon_conjuncts = [p["name"] for p in kundli["planets"] if p["house"] == moon_house and p["name"] != "Moon"]

    h5 = d1_houses.get(5, {})
    h5_sign_id = h5.get("sign_id", ((lagna_id + 3) % 12) + 1)
    h5_sign_name = ZODIAC_SIGNS[h5_sign_id - 1]["name"]
    h5_lord_name = SIGN_LORDS.get(h5_sign_id, "Sun")
    h5_occupants = [p["name"] for p in kundli["planets"] if p["house"] == 5]

    venus = planets.get("Venus", {})
    mercury = planets.get("Mercury", {})
    mars = planets.get("Mars", {})

    nak_title, nak_desc = NAKSHATRA_AURA.get(lagna_nak, ("Dynamic Radiance", "radiates distinct vitality and purpose"))

    elem_traits = {
        "Fire": "You enter any space with an unmistakable kinetic charge, high-voltage enthusiasm, and an instinctual readiness to lead. Others instinctively look to you when decisive action and bold courage are required.",
        "Earth": "You project an aura of monumental composure, grounded reliability, and unflappable practical intelligence. People perceive you as an unshakeable pillar of sanity who commands respect through quiet competence.",
        "Air": "You project an intellectually luminous, socially nimble, and captivating aura. People perceive you as an agile communicator, endlessly curious, diplomatic, and capable of synthesizing complex concepts effortlessly.",
        "Water": "You project an empathetic, intuitive, and enigmatic presence with deep emotional resonance. Others sense your psychological perceptiveness and instinctively feel understood in your presence."
    }
    elem_text = elem_traits.get(lagna_elem_eng, elem_traits["Fire"])

    ll_house_expr = {
        1: f"Because your Lagna Lord ({lagna_lord_name}) resides directly in the 1st House ({ll_dignity}), you project supreme self-direction, unborrowed authority, and commanding personal charisma. You are an epicenter wherever you stand.",
        2: f"With your Lagna Lord ({lagna_lord_name}) stationed in the 2nd House ({ll_sign}), you are perceived as an eloquent, dignified custodian of family values, financial prudence, and cultured wisdom.",
        3: f"With your Lagna Lord ({lagna_lord_name}) energized in the 3rd House of initiative, people view you as a fearless, hands-on go-getter, possessed of restless enterprise, sharp communicative wit, and dynamic stamina.",
        4: f"Because your Lagna Lord ({lagna_lord_name}) anchors your 4th House, you radiate a deeply comforting, protective, and paternal/maternal aura that makes people feel instantly safe and grounded in your presence.",
        5: f"With your Lagna Lord ({lagna_lord_name}) situated in creative brilliance in the 5th House, people perceive you as an intellectual mentor, a visionary strategist, and an inspiring soul radiant with joyful charm.",
        6: f"With your Lagna Lord ({lagna_lord_name}) situated in the 6th House of service, you are perceived as an indomitable problem-solver and relentless warrior who thrives under pressure and resolves impossible bottlenecks.",
        7: f"Because your Lagna Lord ({lagna_lord_name}) sits in the 7th House of partnership, you project a socially radiant, charming, and highly diplomatic persona that commands respect through reciprocal grace and rapport.",
        8: f"With your Lagna Lord ({lagna_lord_name}) submerged in the 8th House, you project an enigmatic, deeply perceptive poker face. Others instinctively sense your profound psychological depth and resilience against crises.",
        9: f"Because your Lagna Lord ({lagna_lord_name}) graces the 9th House of Dharma, you radiate a noble, principled, and philosophical aura. People perceive you as someone naturally favored by good fortune and moral authority.",
        10: f"With your Lagna Lord ({lagna_lord_name}) occupying the 10th House (forming an auspicious Kuladipaka / Karma Yoga), you project commanding leadership, executive competence, and an unmistakable aura of public authority.",
        11: f"With your Lagna Lord ({lagna_lord_name}) placed in the 11th House of gains, people perceive you as a visionary catalyst, exceptionally well-connected, community-minded, and blessed with expansive social influence.",
        12: f"Because your Lagna Lord ({lagna_lord_name}) resides in the 12th House, you project a serene, contemplative, and otherworldly dignity. People sense that you operate on a higher, private plane, unattached to petty drama."
    }
    ll_text = ll_house_expr.get(ll_house, f"Your Lagna Lord {lagna_lord_name} in House {ll_house} ({ll_sign}) channels your outward vitality into disciplined achievement.")

    if h1_occupants:
        occ_desc = []
        for o in h1_occupants:
            if o == "Sun": occ_desc.append("the regal brilliance of the Sun (commanding bone structure, authoritative gaze, and noble pride)")
            elif o == "Moon": occ_desc.append("the luminous gentleness of the Moon (soft facial aura, receptive warmth, and disarming charm)")
            elif o == "Mars": occ_desc.append("the dynamic kinetic fire of Mars (athletic posture, fearless eye contact, and decisive momentum)")
            elif o == "Mercury": occ_desc.append("the youthful agility of Mercury (expressive eyes, quick wit, and eloquent conversational charm)")
            elif o == "Jupiter": occ_desc.append("the sovereign benevolence of Jupiter (commanding forehead, scholarly dignity, and an aura that inspires immediate trust)")
            elif o == "Venus": occ_desc.append("the magnetic beauty of Venus (symmetrical elegance, refined aesthetic grooming, and captivating social grace)")
            elif o == "Saturn": occ_desc.append("the mature gravitas of Saturn (chiseled composure, serious contemplative gaze, and an ageless, disciplined presence)")
            elif o == "Rahu": occ_desc.append("the mesmerizing magnetism of Rahu (unconventional avant-garde style, striking gaze, and an aura that defies ordinary boxes)")
            elif o == "Ketu": occ_desc.append("the enigmatic detachment of Ketu (piercing introspective eyes, minimalist demeanor, and deep spiritual independence)")
        h1_text = f"Your outward aura is profoundly amplified by the direct presence of **{', '.join(h1_occupants)}** in your 1st House, infusing your public presence with {' and '.join(occ_desc)}."
    else:
        h1_text = f"With your 1st House pristine and governed smoothly by {lagna_lord_name} without conflicting occupant friction, your outward persona is a pure, unadulterated expression of classical {lagna_name} energy."

    public_persona_text = (
        f"You meet the world through the lens of a **{lagna_name} ({lagna_sanskrit})** Ascendant, "
        f"radiating the prime frequencies of the **{lagna_elem_eng} ({lagna_elem_san})** element. {elem_text}\n\n"
        f"Your rising degree is specifically anchored in the sacred Nakshatra of **{lagna_nak} (Pada {lagna_pada})**, "
        f"governed by {lagna.get('nakshatra_lord', 'the cosmos')}. This endows you with **{nak_title}**: your physical aura {nak_desc}.\n\n"
        f"{ll_text}\n\n"
        f"{h1_text} In professional and social gatherings, people instinctively take you seriously—sensing both your sharp inner backbone and your refusal to engage in shallow pretense."
    )

    moon_elem_eng, moon_elem_san = SIGN_ELEMENTS.get(moon_sign_id, ("Water", "Jala"))

    moon_house_psych = {
        1: "experiencing feelings directly through the body; you have a sensitive emotional radar and require authentic personal validation, feeling deeply stung by perceived indifference.",
        2: "tangible financial self-reliance, family peace, and emotional security; instability or financial unpredictability triggers profound subconscious anxiety, whereas comfort and beauty restore your soul.",
        3: "mental restlessness and intellectual processing; your subconscious constantly analyzes feelings through writing, communication, or physical movement, hating mental stagnation.",
        4: "a sacred domestic sanctuary and maternal emotional connection; behind closed doors, you need an impenetrable private haven where you can fully drop your guard and replenish your spirit.",
        5: "romantic idealism, creative playfulness, and intellectual celebration; you possess a vibrant inner theater that feels most alive when creating, mentoring, or indulging in heartfelt joy.",
        6: "hyper-vigilant duty, perfectionism, and problem-solving; your subconscious tends to internalize tension into worrying over details or health, carrying an innate urge to fix and serve.",
        7: "relational equilibrium and partnership mirror; your inner mood fluctuates intensely based on the emotional temperature of your closest relationships, craving deep reciprocal loyalty.",
        8: "psychological intensity, ocean-deep intuition, and guarded secrets; you experience periodic subconscious 'deaths and rebirths', sensing hidden motives effortlessly while shielding your own vulnerability.",
        9: "higher cosmic truth, philosophical expansion, and divine faith; you cannot stand petty mundane gossip, finding true emotional peace only when aligned with a grander moral purpose.",
        10: "public competence, honorable legacy, and achievement; subconscious fear of irrelevance or failure drives your relentless work ethic, finding emotional solace in tangible accomplishments.",
        11: "community vision, intellectual camaraderie, and long-range aspirations; you find emotional safety in diverse intellectual circles and working toward collective, progressive ideals.",
        12: "profound psychic sensitivity, vivid dream states, and mystic detachment; you absorb the unspoken emotional baggage of everyone around you and desperately require regular periods of total solitude."
    }
    m_house_text = moon_house_psych.get(moon_house, "seeking deep emotional balance and sanctuary.")

    moon_conj_notes = []
    if "Saturn" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Saturn (Vish / Shani-Chandra influence) installs a stoic emotional fortress: you rarely cry in front of others, prefer to bear burdens alone, and carry a profound sense of duty, yet secretly yearn for someone to hold space for your tired heart.")
    if "Mars" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Mars (Chandra-Mangala Yoga) ignites a fiery emotional bloodstream: your feelings are intense, passionate, and swift to ignite; you possess incredible emotional courage but must guard against internalizing stress into acidic burnout.")
    if "Jupiter" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Jupiter (Gajakesari Yoga) bestows an expansive emotional optimism: even in your darkest hours, an indestructible moral compass and faith in divine grace whisper that dawn is approaching.")
    if "Mercury" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Mercury creates an emotionally agile, poetic mind: you intellectualize your feelings, dissecting emotions with sharp wit and logic before allowing yourself to feel their raw sting.")
    if "Venus" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Venus infuses your subconscious with exquisite aesthetic sensitivity: harsh voices, vulgarity, or chaotic spaces physically drain you, while music, soft scents, and tender intimacy instantly heal your nervous system.")
    if "Rahu" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Rahu induces sudden tidal waves of intense emotional longing, uncanny psychic dreams, and a restless feeling of being an outsider in conventional social systems.")
    if "Ketu" in moon_conjuncts:
        moon_conj_notes.append("Moon conjunct Ketu gives an innate ascetic detachment: a part of your soul always remains an observer, quietly disconnected from worldly drama and deeply attuned to meditative stillness.")

    if moon_conj_notes:
        conj_text = " ".join(moon_conj_notes)
    else:
        conj_text = f"With the Moon sitting unblemished in {moon_sign} ({moon_dignity}), your subconscious emotional processing operates with classical clarity and focus."

    hidden_personality_text = (
        f"While your **{lagna_name} Ascendant** presents a {lagna_elem_eng.lower()} facade of strength to the public, "
        f"your true subconscious feeling world is governed by your Janma Rashi, **{moon_sign} ({moon_sanskrit})**—a realm of **{moon_elem_eng} ({moon_elem_san})** energy.\n\n"
        f"Situated in your **{HOUSE_NAMES.get(moon_house, f'House {moon_house}')}**, your inner psychological frequency is anchored in {m_house_text}\n\n"
        f"Under your Janma Nakshatra **{moon_nak}**, your soul carries deep emotional sensitivity that only your innermost circle ever witnesses. {conj_text}\n\n"
        f"In private, away from worldly cameras and expectations, you are far more tender, introspective, and spiritually contemplative than people realize. "
        f"You carry a sacred need to be loved for your vulnerable, unpolished self—not merely applauded for your outer achievements."
    )

    passions = []
    h5_sign_passions = {
        "Aries": f"Pioneering creative ventures, high-octane physical challenges, and starting ambitious creative projects from scratch (5th House in Aries / Mars)",
        "Taurus": f"Artisanal culinary arts, collecting timeless aesthetic treasures, luxury interior crafting, and gardening in natural soil (5th House in Taurus / Venus)",
        "Gemini": f"Creative writing, witty podcasting, reading multifaceted genres, coding, and engaging in rapid intellectual strategy games (5th House in Gemini / Mercury)",
        "Cancer": f"Nurturing culinary recipes, creating a cozy home sanctuary, artistic photography, and capturing soulful family memories (5th House in Cancer / Moon)",
        "Leo": f"Theatrical storytelling, performing arts, high-visibility creative leadership, and curating celebratory social experiences (5th House in Leo / Sun)",
        "Virgo": f"Mastering intricate crafts, data analytics, precision design, holistic wellness regimens, and optimizing systems (5th House in Virgo / Mercury)",
        "Libra": f"Aesthetic interior design, fine art appreciation, attending acoustic concerts, and curating balanced fashion harmony (5th House in Libra / Venus)",
        "Scorpio": f"Investigating psychological mysteries, occult research, deep investigative reading, and transformative fitness (5th House in Scorpio / Mars)",
        "Sagittarius": f"Philosophical exploration, spontaneous travel to sacred heritage sites, archery/outdoor adventures, and studying higher wisdom (5th House in Sagittarius / Jupiter)",
        "Capricorn": f"Building long-term enterprise systems, woodworking/architecture, vintage collection, and strategic chess or financial compounding (5th House in Capricorn / Saturn)",
        "Aquarius": f"Exploring cutting-edge technologies, futuristic innovation, astronomy, and spearheading progressive humanitarian movements (5th House in Aquarius / Saturn)",
        "Pisces": f"Immersive musical meditation, poetry, cinema that touches the soul, watercolor painting, and solitary retreats near water (5th House in Pisces / Jupiter)"
    }
    passions.append(h5_sign_passions.get(h5_sign_name, "Engaging in creative ventures and artistic self-expression"))

    if h5_occupants:
        for occ in h5_occupants:
            if occ == "Moon":
                passions.append(f"Soul-nourishing creative daydreaming, writing poetic reflections, and culinary experimentation (amplified by Moon in 5th House)")
            elif occ == "Sun":
                passions.append(f"Directing creative projects, performing on stage, or organizing grand gatherings where your creative vision shines (Sun in 5th House)")
            elif occ == "Mercury":
                passions.append(f"Strategy board games, cryptography, witty satirical writing, and learning new technical or linguistic skills (Mercury in 5th House)")
            elif occ == "Venus":
                passions.append(f"Fine arts, luxury styling, attending theatrical concerts, and indulging in romantic sensory adventures (Venus in 5th House)")
            elif occ == "Mars":
                passions.append(f"Competitive sports, high-intensity workouts, speculative trading, and fast-paced hands-on mechanics (Mars in 5th House)")
            elif occ == "Jupiter":
                passions.append(f"Mentoring eager minds, reading deep spiritual treatises, philosophy discussions, and philanthropic giving (Jupiter in 5th House)")
            elif occ == "Saturn":
                passions.append(f"Mastering patient classical disciplines, studying ancient history, antique restoration, and deep meditative focus (Saturn in 5th House)")
            elif occ == "Rahu":
                passions.append(f"Unconventional digital media, avant-garde art, cinema, and exploring boundary-pushing subcultures (Rahu in 5th House)")
            elif occ == "Ketu":
                passions.append(f"Esoteric astrology, silent meditation, sacred geometry, and solitary walks in pristine wilderness (Ketu in 5th House)")

    v_sign = venus.get("sign_name", "Taurus")
    v_house = venus.get("house", 1)
    v_passions = {
        "Aries": f"Passionate adventures, spontaneous weekend road trips, and vibrant fitness fashion (Venus in Aries, House {v_house})",
        "Taurus": f"Savoring gourmet gastronomy, collecting fine perfumes, and soaking in peaceful acoustic music (Venus in Taurus, House {v_house})",
        "Gemini": f"Lively intellectual banter, visiting modern art galleries, and curating eclectic music playlists (Venus in Gemini, House {v_house})",
        "Cancer": f"Cooking heartfelt comfort food for loved ones, soulful domestic nesting, and visiting seaside retreats (Venus in Cancer, House {v_house})",
        "Leo": f"Attending glamorous cultural galas, dressing with bold regal elegance, and celebrating life with grand generosity (Venus in Leo, House {v_house})",
        "Virgo": f"Curating minimalist capsule wardrobes, artisanal craft hobbies, and herbal/botanical gardening (Venus in Virgo, House {v_house})",
        "Libra": f"Immersing in classical art, cultural museum exhibits, elegant dinner parties, and aesthetic harmony (Venus in Libra, House {v_house})",
        "Scorpio": f"Exploring intense psychological cinema, hypnotic ambient music, and exploring sacred esoteric shrines (Venus in Scorpio, House {v_house})",
        "Sagittarius": f"Backpacking across foreign cultures, horse-riding/outdoor treks, and studying international art forms (Venus in Sagittarius, House {v_house})",
        "Capricorn": f"Collecting architectural photography, visiting timeless historic monuments, and classic jazz or symphony (Venus in Capricorn, House {v_house})",
        "Aquarius": f"Exploring indie music festivals, digital media creation, and brainstorming utopian social concepts (Venus in Aquarius, House {v_house})",
        "Pisces": f"Spiritual meditation, writing transcendent poetry, beachside contemplation, and mystical sound baths (Venus in Pisces, House {v_house})"
    }
    passions.append(v_passions.get(v_sign, f"Aesthetic and sensory enjoyment (Venus in {v_sign})"))

    m_sign = mercury.get("sign_name", "Gemini")
    m_house = mercury.get("house", 1)
    passions.append(f"Deep-dive research into complex subjects, analytical strategy, and lively debate on modern ideas (Mercury in {m_sign}, House {m_house})")

    ma_sign = mars.get("sign_name", "Aries")
    ma_house = mars.get("house", 1)
    passions.append(f"Physical conditioning, pushing endurance limits, dynamic outdoor excursions, and taking calculated personal risks (Mars in {ma_sign}, House {ma_house})")

    strengths = []
    for p_name in ["Jupiter", "Venus", "Mars", "Saturn", "Sun", "Mercury", "Moon"]:
        p_obj = planets.get(p_name)
        if p_obj:
            dig = p_obj.get("dignity", "")
            h_num = p_obj.get("house", 1)
            sign_n = p_obj.get("sign_name", "")
            if dig.startswith("Exalted") or dig.startswith("Own Sign"):
                strengths.append(f"**{p_name} in {sign_n} ({dig}) in House {h_num}:** Bestows extraordinary cosmic potency in its domain, giving you formidable resilience, moral spine, and an unshakeable foundation during times of trial.")
            elif h_num in [1, 4, 7, 10] and p_name in ["Jupiter", "Venus", "Mercury"]:
                strengths.append(f"**Benefic {p_name} in Kendra (House {h_num}):** Acts as a divine protective shield, granting intellectual lucidity, honorable social reputation, and timely rescues when difficulties loom.")

    strengths.append(f"**{lagna_name} Ascendant Tenacity:** An instinctual ability to adapt your {lagna_elem_eng.lower()} constitution to overcome heavy odds without conceding your personal integrity.")
    strengths.append(f"**Janma Rashi {moon_sign} Empathy:** Profound emotional depth that enables you to read between the lines, sense hidden motives, and provide steadfast counsel to those you cherish.")

    shadows = []
    rahu = planets.get("Rahu", {})
    ketu = planets.get("Ketu", {})
    if rahu:
        shadows.append(f"**Rahu's Restless Hunger in House {rahu.get('house')}:** Creates occasional bouts of insatiable ambition or fear of missing out, driving you to over-extend yourself before solidifying existing victories.")
    if ketu:
        shadows.append(f"**Ketu's Sudden Detachment in House {ketu.get('house')}:** Triggers sudden phases of apathy or withdrawal where you feel like abandoning worldly projects when minor disillusionment strikes.")

    for p_name, p_obj in planets.items():
        if p_obj.get("dignity", "").startswith("Debilitated"):
            shadows.append(f"**Neecha {p_name} in House {p_obj.get('house')}:** Can manifest as recurring self-doubt, second-guessing your instinct, or settling for less than your true worth in partnerships or negotiations.")

    if not shadows or len(shadows) < 3:
        shadows.append(f"**{lagna_name} Blindspot:** Tendency to keep emotional burdens strictly compartmentalized, risking sudden physical fatigue when your nervous system demands quiet replenishment.")
        shadows.append(f"**Over-Intellectualizing Grief:** Processing emotional wounds with the mind rather than allowing your heart to feel and release them naturally.")

    karmic_remedy = (
        f"**The Vedic Alignment Practice:** Because your chart harmonizes the {lagna_elem_eng} energy of your {lagna_name} Ascendant "
        f"with the {moon_elem_eng} frequency of your {moon_sign} Moon, make a sacred daily practice of grounding yourself. "
        f"Spend 10 minutes in morning stillness before checking screens, hydrate with clean water, and observe a conscious pause "
        f"before making reactive life decisions. True strength lies not in never bending, but in bending gracefully without breaking."
    )

    return {
        "public_persona": {
            "title": "How Others See You (सामाजिक छवि एवं बाह्य प्रभाव)",
            "icon": "🎭",
            "text": public_persona_text
        },
        "hidden_personality": {
            "title": "Your Hidden Subconscious Self (गुप्त स्वभाव एवं अंतर्मन)",
            "icon": "🗝️",
            "text": hidden_personality_text
        },
        "passions_and_loves": {
            "title": "What You Truly Love Doing (रुचियां, शौक एवं मनोविनोद)",
            "icon": "🎨",
            "items": passions
        },
        "positive_strengths": {
            "title": "Your Divine Strengths & Gifts (सकारात्मक शक्तियां एवं दैवीय गुण)",
            "icon": "✨",
            "items": strengths[:4]
        },
        "shadow_weaknesses": {
            "title": "Shadow Blindspots & Traps to Avoid (कमजोरियां, छाया पक्ष एवं सावधानियां)",
            "icon": "⚠️",
            "items": shadows[:4],
            "karmic_remedy": karmic_remedy
        }
    }


def generate_personalized_marriage_blueprint(kundli: Dict[str, Any]) -> Dict[str, Any]:
    planets = {p["name"]: p for p in kundli["planets"]}
    d1_houses = {h["house"]: h for h in kundli["d1_houses"]}
    lagna = kundli["lagna"]
    manglik = kundli.get("manglik", {})
    meta = kundli.get("metadata", {})
    gender = meta.get("gender", "Male").strip().capitalize()

    h7 = d1_houses.get(7, {})
    h7_sign_id = h7.get("sign_id", 7)
    h7_sign = ZODIAC_SIGNS[h7_sign_id - 1]
    h7_sign_name = h7_sign["name"]
    h7_sign_san = h7_sign["sanskrit"]
    h7_elem_eng, h7_elem_san = SIGN_ELEMENTS.get(h7_sign_id, ("Air", "Vayu"))
    h7_lord_name = SIGN_LORDS.get(h7_sign_id, "Venus")
    p_h7_lord = planets.get(h7_lord_name, {})
    h7_lord_house = p_h7_lord.get("house", 7)
    h7_lord_sign = p_h7_lord.get("sign_name", h7_sign_name)
    h7_lord_dig = p_h7_lord.get("dignity", "Neutral")
    h7_occupants = [p["name"] for p in kundli["planets"] if p["house"] == 7]

    h5 = d1_houses.get(5, {})
    h5_sign_id = h5.get("sign_id", 5)
    h5_sign = ZODIAC_SIGNS[h5_sign_id - 1]
    h5_lord_name = SIGN_LORDS.get(h5_sign_id, "Sun")
    p_h5_lord = planets.get(h5_lord_name, {})
    h5_occupants = [p["name"] for p in kundli["planets"] if p["house"] == 5]

    venus = planets.get("Venus", {})
    mars = planets.get("Mars", {})
    jupiter = planets.get("Jupiter", {})
    rahu = planets.get("Rahu", {})
    saturn = planets.get("Saturn", {})

    v_sign_name = venus.get("sign_name", "Taurus")
    v_sign_san = venus.get("sign_sanskrit", "Vrishabha")
    v_house = venus.get("house", 1)
    v_dignity = venus.get("dignity", "Neutral")
    v_conjuncts = [p["name"] for p in kundli["planets"] if p["house"] == v_house and p["name"] != "Venus"]

    love_languages = {
        "Aries": "Fervent Passion, Bold Initiative & Magnetic Playfulness",
        "Taurus": "Sensual Loyalty, Dedicated Acts of Service & Timeless Comfort",
        "Gemini": "Witty Intellectual Camaraderie, Playful Banter & Deep Conversation",
        "Cancer": "Soulful Devotion, Nurturing Sanctuary & Emotional Attunement",
        "Leo": "Regal Generosity, Theatrical Romance & Proud Adoration",
        "Virgo": "Meticulous Practical Care, Quiet Devotion & Everyday Helpfulness",
        "Libra": "Aesthetic Harmony, Courteous Courtship & Reciprocal Romance",
        "Scorpio": "All-or-Nothing Intensity, Soulful Intimacy & Fierce Protection",
        "Sagittarius": "Philosophical Companionship, Freedom & Shared Adventures",
        "Capricorn": "Steadfast Fidelity, Generational Building & Enduring Loyalty",
        "Aquarius": "Intellectual Kinship, Humanitarian Ideals & Unconventional Devotion",
        "Pisces": "Transcendent Empathy, Sacred Romance & Unconditional Selflessness"
    }
    love_lang = love_languages.get(v_sign_name, "Deep Romantic Devotion & Loyalty")
    if v_conjuncts:
        love_lang += f" (Energized by {' & '.join(v_conjuncts)})"

    v_house_meaning = {
        1: "directly wears your heart on your sleeve. Romance and personal warmth are inseparable from your identity, and your presence naturally disarms and attracts admirers.",
        2: "expresses love through heartfelt spoken words, generous gifts, gourmet dinners, and offering rock-solid financial safety and domestic comfort.",
        3: "expresses love through lively daily communication, witty text exchanges, playful road trips, and engaging in collaborative hands-on projects together.",
        4: "expresses love by creating a cozy, sacred domestic haven. For you, true love is baking a warm meal, wrapping your partner in comfort, and protecting the emotional peace of the home.",
        5: "is a born romantic courtier. You love dramatic romantic surprises, writing heartfelt poetry or love letters, and showering your partner with celebratory dates.",
        6: "demonstrates love not through hollow theatrical words, but through practical problem-solving: taking care of your partner when they are sick, handling logistics, and smoothing out daily friction.",
        7: "is entirely relationship-centric. You place your partner on an equal pedestal, thriving on mutual consultation, exquisite courtesy, and deep reciprocal devotion.",
        8: "craves profound psychological and physical union. For you, love is a sacred, all-or-nothing emotional bond; casual dating feels empty, and once committed, your loyalty is fiercely protective.",
        9: "approaches love as a sacred spiritual journey. You express affection through shared philosophical exploration, visiting heritage and pilgrimage sites, and inspiring each other's moral growth.",
        10: "expresses pride in your partner's career and aspirations. You love being a power couple, celebrating their victories in public, and building an honorable generational empire together.",
        11: "believes that true lovers must be best friends first. You express affection through shared intellectual interests, welcoming them into your vibrant social circle, and supporting their highest life dreams.",
        12: "loves with boundless, selfless, and soulful devotion. You crave private romantic getaways, spiritual emotional bonding away from crowd noise, and quiet telepathic intimacy."
    }
    how_express = (
        f"With your Venus positioned in **{v_sign_name} ({v_sign_san})** in the **{HOUSE_NAMES.get(v_house, f'House {v_house}')}** ({v_dignity}), "
        f"you {v_house_meaning.get(v_house, 'approach intimate relationships with deep devotion.')} "
    )
    if "Mars" in v_conjuncts:
        how_express += " The conjunction of Venus and Mars ignites an irresistible physical chemistry, playful teasing, and a passionate, tactile romantic drive."
    if "Jupiter" in v_conjuncts:
        how_express += " The conjunction of Venus and Jupiter bestows magnanimous nobility, high ethical values, and a habit of pampering your partner like royalty."
    if "Saturn" in v_conjuncts:
        how_express += " The influence of Saturn with Venus makes you deliberate and cautious in early courtship, but once your trust is won, you offer an unbreakable, lifelong fidelity."
    if "Mercury" in v_conjuncts:
        how_express += " The union of Venus and Mercury infuses your courtship with sparkling wit, intellectual camaraderie, clever love notes, and endless conversational charm."

    heart_melts = {
        "Aries": "Spontaneous brave declarations of love, a partner who cheers your boldest ambitions, and passionate unexpected adventures.",
        "Taurus": "Unwavering loyalty, peaceful domestic consistency, gentle sensory massages, and being treated to exquisite gourmet meals.",
        "Gemini": "Witty late-night banters that stimulate your mind, unexpected thoughtful voice notes, and a lover who laughs genuinely at your jokes.",
        "Cancer": "Tender emotional check-ins, a partner who makes you feel completely safe to cry, and a warm, loving home environment.",
        "Leo": "Sincere public praise, celebrating your achievements with sparkling eyes, and generous romantic gestures that make you feel truly special.",
        "Virgo": "Noticing the small ways you help, bringing order to chaos, honest and calm communication, and being appreciated for your thoughtful efforts.",
        "Libra": "Aesthetic refinement, polite and courteous communication, romantic candlelit dinners, and a partner who values mutual harmony above all.",
        "Scorpio": "Absolute raw honesty, unshakeable emotional loyalty during your darkest moods, and eye-to-eye vulnerability without any masks.",
        "Sagittarius": "Spontaneous road trips, intellectual freedom to debate philosophy, and a partner who explores foreign cultures and hikes trails with you.",
        "Capricorn": "Steadfast reliability, someone who keeps their promises without fail, respects your work ethic, and builds a legacy beside you.",
        "Aquarius": "Treating you as an intellectual equal, honoring your independence, and sharing your passionate dreams for a better world.",
        "Pisces": "Soulful empathy, listening to ambient music by the water together, and gentle, unconditional acceptance of your tender spirit."
    }
    what_melts = heart_melts.get(v_sign_name, "Genuine emotional loyalty, reciprocal kindness, and shared laughter.")

    h7_lord_desc = {
        1: f"Your 7th Lord ({h7_lord_name}) sits directly in your 1st House ({h7_lord_sign}). Your partner is magnetically drawn to your authentic personality, self-direction, and natural charisma. They seek a life partner who acts as an inspiring captain of their shared journey.",
        2: f"Your 7th Lord ({h7_lord_name}) resides in your 2nd House ({h7_lord_sign}). Your partner is drawn to your articulate speech, family values, and financial prudence. They seek someone who provides emotional peace, cultured dignity, and lasting generational wealth.",
        3: f"Your 7th Lord ({h7_lord_name}) sits in your 3rd House ({h7_lord_sign}). Your partner is drawn to your energetic courage, sharp communicative wit, and adventurous spirit. They seek an active co-pilot for life's travels and creative projects.",
        4: f"Your 7th Lord ({h7_lord_name}) anchors your 4th House ({h7_lord_sign}). Your partner is karmically magnetized to your nurturing heart, domestic emotional stability, and protective presence. They seek a peaceful emotional sanctuary in you.",
        5: f"Your 7th Lord ({h7_lord_name}) occupies your 5th House of romance ({h7_lord_sign}). Your partner is drawn to your creative intellect, romantic charisma, and playful joy. They fell in love with your mind and artistic spirit before anything else.",
        6: f"Your 7th Lord ({h7_lord_name}) sits in your 6th House ({h7_lord_sign}). Your partner is deeply drawn to your dedicated service, problem-solving intelligence, and steadfast work ethic. They admire someone who stands resilient against all adversity.",
        7: f"Your 7th Lord ({h7_lord_name}) resides proudly in its own 7th House ({h7_sign_name}). This forms an exceptionally potent Malavya / Swa-Bhava Yoga: your partner is drawn to your innate relational fairness, diplomatic grace, and magnetic interpersonal beauty.",
        8: f"Your 7th Lord ({h7_lord_name}) sits in your 8th House ({h7_lord_sign}). Your partner is drawn to your hypnotic psychological depth, mysterious aura, and transformative resilience. They sense that your love is deeply transformative.",
        9: f"Your 7th Lord ({h7_lord_name}) resides in your 9th House of Dharma ({h7_lord_sign}). Your partner is drawn to your noble moral character, philosophical wisdom, and spiritual principles. They see you as an auspicious blessing and guiding light in their destiny.",
        10: f"Your 7th Lord ({h7_lord_name}) sits in your 10th House of Career ({h7_lord_sign}). Your partner is drawn to your professional ambition, leadership standing, and high social respect. They take deep pride in your accomplishments and public honor.",
        11: f"Your 7th Lord ({h7_lord_name}) occupies your 11th House of gains ({h7_lord_sign}). Your partner is drawn to your expansive social vision, intellectual networks, and progressive ideals. They seek a best friend with whom they can manifest ambitious dreams.",
        12: f"Your 7th Lord ({h7_lord_name}) resides in your 12th House ({h7_lord_sign}). Your partner is drawn to your serene spiritual detachment, selfless empathy, and private contemplative grace. They crave deep soul-level sanctuary with you."
    }
    attraction_text = (
        f"Your 7th House (Kalatra Bhava) is governed by **{h7_sign_name} ({h7_sign_san})**, carrying the balancing frequencies of the **{h7_elem_eng} ({h7_elem_san})** element. "
        f"In Vedic Jyotish, the 7th House represents the complementary energy your soul requires to achieve cosmic equilibrium.\n\n"
        f"{h7_lord_desc.get(h7_lord_house, f'Your 7th Lord {h7_lord_name} in House {h7_lord_house} creates an enduring karmic magnetism.')}\n\n"
        f"Rather than being swayed by shallow flattery, your life partner is karmically destined to recognize the true depth of your character, "
        f"seeking a lifelong union anchored in mutual honor, intellectual respect, and complementary strengths."
    )

    score = 42
    reasons = []

    if p_h5_lord and p_h7_lord:
        if p_h5_lord.get("house") == p_h7_lord.get("house"):
            score += 34
            reasons.append(f"The 5th Lord of romance ({h5_lord_name}) and 7th Lord of marriage ({h7_lord_name}) sit conjoined in House {p_h5_lord.get('house')}. Classical texts (*Jataka Parijata*) celebrate this Sambandha as the supreme indicator of a heartfelt love marriage.")
        elif p_h5_lord.get("house") == 7:
            score += 30
            reasons.append(f"The 5th Lord of romance ({h5_lord_name}) resides directly in the 7th House of matrimony, turning romantic courtship into lifelong matrimonial commitment.")
        elif p_h7_lord.get("house") == 5:
            score += 30
            reasons.append(f"The 7th Lord of marriage ({h7_lord_name}) occupies the 5th House of romance, indicating that your spouse enters your life first as a romantic darling before family formalization.")
        elif ((p_h7_lord.get("house", 0) - p_h5_lord.get("house", 0)) % 12) + 1 == 7:
            score += 24
            reasons.append(f"The 5th Lord ({h5_lord_name}) and 7th Lord ({h7_lord_name}) cast direct mutual aspects on each other across the 1/7 axis, bridging heartfelt affection with formal marriage.")

    if rahu:
        if rahu.get("house") in [5, 7]:
            score += 22
            reasons.append(f"Rahu occupies House {rahu.get('house')}, breaking conventional cultural boundaries and favoring an unconventional, modern, or self-chosen romantic union.")
        elif rahu.get("house") == 1:
            score += 15
            reasons.append("Rahu in the 1st House aspects the 7th House across the relationship axis, bestowing independent choice and modern self-determination in partner selection.")

    if venus and mars:
        if venus.get("house") == mars.get("house"):
            score += 20
            reasons.append(f"Venus (Love) and Mars (Passion) unite in House {venus.get('house')}, generating magnetic physical attraction and self-initiated romantic bonding.")
        elif ((mars.get("house", 0) - venus.get("house", 0)) % 12) + 1 == 7:
            score += 16
            reasons.append("Venus and Mars establish a direct mutual 7th aspect across opposite houses, sparking intense romantic chemistry and self-chosen partner selection.")

    if jupiter:
        if jupiter.get("house") == 7:
            score -= 22
            reasons.append("Benefic Jupiter resides in the 7th House, bestowing strong traditional family approval, noble lineage matching, and elder-supported matrimonial harmony.")
        elif p_h7_lord and p_h7_lord.get("house") in [2, 9] and score < 60:
            score -= 15
            reasons.append(f"The 7th Lord ({h7_lord_name}) connects to the family/dharma axis (House {p_h7_lord.get('house')}), favoring an alliance backed by family elders and shared cultural values.")

    if saturn and saturn.get("house") == 7 and score < 60:
        score -= 14
        reasons.append("Saturn in the 7th House promotes mature deliberation, structured family vetting, and patience over hasty romantic infatuation.")

    score = max(18, min(88, score))

    if score >= 62:
        m_type = "Love Marriage (प्रेम विवाह)"
        m_badge = f"{score}% Love Marriage • {100 - score}% Traditional Alliance"
        m_verdict = (
            f"Your birth chart exhibits a high astrological probability of a **Self-Chosen / Love Marriage (प्रेम विवाह)**. "
            f"The interplay of your {h5_lord_name} (5th Lord of affection) and {h7_lord_name} (7th Lord of union) indicates that personal romantic chemistry, "
            f"intellectual resonance, and heartfelt personal choice will be the primary catalysts bringing you together with your life partner."
        )
    elif score <= 40:
        m_type = "Arranged Marriage (पारंपरिक / पारिवारिक विवाह)"
        m_badge = f"{100 - score}% Arranged • {score}% Self-Chosen"
        m_verdict = (
            f"Your birth chart strongly aligns with an auspicious **Traditional / Family-Arranged Marriage (पारंपरिक विवाह)**. "
            f"Family blessings, cultural compatibility, and shared ethical foundations will play a decisive, harmonious role in introducing "
            f"and uniting you with your life partner, ensuring solid generational stability."
        )
    else:
        m_type = "Love-Cum-Arranged (प्रेम विवाह सह पारिवारिक सहमति)"
        m_badge = f"{score}% Love-cum-Arranged • {100 - score}% Traditional Alliance"
        m_verdict = (
            f"Your birth chart indicates an auspicious **Love-Cum-Arranged Marriage (प्रेम विवाह सह पारिवारिक सहमति)**. "
            f"You are destined to meet your partner independently through education, career, or mutual social networks, "
            f"and once your personal connection blossoms, it will naturally and enthusiastically receive the full blessing and celebration of both families."
        )

    if not reasons:
        reasons.append(f"The balanced placement of Venus in {v_sign_name} and your 7th Lord {h7_lord_name} ensures that personal romantic attraction and family harmony blend seamlessly in your marital destiny.")

    features = SPOUSE_LORD_FEATURES.get(h7_lord_name, SPOUSE_LORD_FEATURES["Venus"])
    spouse_label = "Bride / Wife" if gender == "Male" else ("Groom / Husband" if gender == "Female" else "Spouse / Life Partner")

    # Dynamic archetype title
    sign_base_title = {
        "Aries": "Dynamic Trailblazer & Fearless Companion",
        "Taurus": "Steadfast Pillar of Serenity & Aesthetic Grace",
        "Gemini": "Brilliant Conversationalist & Youthful Muse",
        "Cancer": "Nurturing Guardian & Soulful Emotional Anchor",
        "Leo": "Regal Luminary of Warmth & Noble Dignity",
        "Virgo": "Meticulous Intellectual & Devoted Problem-Solver",
        "Libra": "Harmonious Diplomat of Refinement & Beauty",
        "Scorpio": "Enigmatic Soulmate of Passion & Transformative Loyalty",
        "Sagittarius": "Philosophical Visionary of Truth & High Adventure",
        "Capricorn": "Resolute Architect of Generational Security & Honor",
        "Aquarius": "Visionary Humanitarian of Intellectual Freedom",
        "Pisces": "Transcendent Mystic of Compassion & Artistic Grace"
    }
    lord_blessing = f"Ruled by {h7_lord_name} in House {h7_lord_house}"
    if h7_occupants:
        lord_blessing += f" • Influenced by {', '.join(h7_occupants)}"
    archetype_title = f"{sign_base_title.get(h7_sign_name, 'Devoted Companion')} ({h7_sign_san} • {lord_blessing})"

    # Physical Appearance Breakdown with gender and occupants
    base_stature = features["stature_f"] if gender == "Male" else features["stature_m"]
    occ_str = f" (further shaped by {', '.join(h7_occupants)} in 7th House)" if h7_occupants else ""
    stature = f"{base_stature}{occ_str}."
    face = f"{features['face']}, reflecting a distinctive {h7_sign_name} facial contour."
    eyes = f"{features['eyes']} that reflect genuine warmth and sincere affection."
    complexion = f"{features['complexion']}, endowed with natural vitality."
    style = f"{features['style']}."

    personality_traits = list(features["personality"])
    if h7_occupants:
        for occ in h7_occupants:
            if occ == "Jupiter": personality_traits.append("Scholarly nobility: Blessed by Jupiter's grace in the 7th house, embodying moral wisdom, kindness, and spiritual poise.")
            elif occ == "Venus": personality_traits.append("Artistic elegance: Possesses an enchanting eye for fine aesthetics, music, luxury, and harmonious domestic beauty.")
            elif occ == "Mercury": personality_traits.append("Playful wit: Brings evergreen conversational humor, agile business acumen, and intellectual camaraderie.")
            elif occ == "Mars": personality_traits.append("Fierce protective drive: High energy, athletic passion, decisive boldness, and unyielding loyalty.")
            elif occ == "Saturn": personality_traits.append("Rock-solid maturity: Enduring patience, deep emotional reliability, and generational financial discipline.")
            elif occ == "Sun": personality_traits.append("Regal honor: Radiant self-respect, leadership charisma, and an honorable family lineage.")
            elif occ == "Moon": personality_traits.append("Gentle lunar compassion: Deep emotional empathy, maternal/paternal warmth, and a comforting presence.")
            elif occ == "Rahu": personality_traits.append("Charismatic individuality: An unconventional, avant-garde magnetism that stands out in any crowd.")
            elif occ == "Ketu": personality_traits.append("Spiritual contemplation: Deep meditative depth, humility, and detachment from petty vanity.")

    behavioral_traits = list(features["behavior"])

    # Incorporate 7th Lord House into behavioral dynamic with native
    h7_lord_behavior_modifier = {
        1: f"Because your 7th Lord ({h7_lord_name}) sits in your 1st House, your {spouse_label.lower()} acts as your closest confidant and co-captain, naturally prioritizing your presence, seeking your counsel in every endeavor, and thriving when doing things together.",
        2: f"With your 7th Lord in the 2nd House, your {spouse_label.lower()} takes deep pride in nurturing family traditions, managing household prosperity prudently, and speaking with encouraging words that soothe your tension.",
        3: f"With your 7th Lord in the 3rd House, your {spouse_label.lower()} treats you as an active comrade-in-arms, inspiring you to take brave career leaps, join them in frequent road trips, and engage in stimulating daily banter.",
        4: f"Because your 7th Lord anchors the 4th House, your {spouse_label.lower()} transforms your home into a tranquil emotional sanctuary, ensuring you return from the outside world into warmth, peace, and domestic comfort.",
        5: f"With your 7th Lord in the 5th House, your {spouse_label.lower()} keeps romantic courtship alive through years of marriage with playful dates, intellectual discussions, and celebrating your creative talents.",
        6: f"With your 7th Lord in the 6th House, your {spouse_label.lower()} displays monumental devotion through practical problem-solving, tirelessly organizing routines, and nursing you back to strength during stressful periods.",
        7: f"Because your 7th Lord sits in its own 7th House, your {spouse_label.lower()} treats marital harmony as sacred, practicing transparent communication and resolving differences with calm diplomatic grace.",
        8: f"With your 7th Lord in the 8th House, your {spouse_label.lower()} shares a deeply bonded, intense, and transformative intimacy with you, guarding your secrets with monumental loyalty.",
        9: f"Because your 7th Lord resides in the 9th House, your {spouse_label.lower()} inspires your higher moral purpose, loves undertaking spiritual journeys together, and acts as an auspicious beacon of good fortune in your life.",
        10: f"With your 7th Lord in the 10th House, your {spouse_label.lower()} acts as an ambitious partner who takes immense pride in your career achievements, helping you strategize professional milestones and maintain high social honor.",
        11: f"With your 7th Lord in the 11th House, your {spouse_label.lower()} is your truest best friend, seamlessly integrating into your friend circle, championing your grandest dreams, and celebrating shared financial abundance.",
        12: f"Because your 7th Lord occupies the 12th House, your {spouse_label.lower()} values sacred domestic privacy, enjoying solitary quiet moments and romantic retreats away from external social noise."
    }
    if h7_lord_house in h7_lord_behavior_modifier:
        behavioral_traits.insert(0, h7_lord_behavior_modifier[h7_lord_house])

    planetary_modifiers = []
    for occ in h7_occupants:
        planetary_modifiers.append(f"🌟 **{occ} in 7th House:** Deeply colors your {spouse_label.lower()}'s nature with {occ}'s signature cosmic frequency, elevating mutual harmony and shared growth.")

    friction_points = []
    harmony_rules = []

    if manglik.get("is_manglik", False):
        friction_points.append(f"Kuja (Mars) Influence / Manglik Sensitivity: {manglik.get('description', 'Fiery energy on the marital axis')}. Can spark sudden flashes of temper or battles of ego if communication breaks down.")
        harmony_rules.append("Institute a mandatory 15-minute cooling-off rule during heated arguments; channel excess fiery energy into shared workouts, sports, or travel rather than verbal debate.")
    else:
        harmony_rules.append("Mars sits peacefully in relation to your 7th house, allowing misunderstandings to be resolved through patient, affectionate conversation.")

    if h7_sign_name in ["Aries", "Scorpio"]:
        friction_points.append("Willpower Clashes: Both partners carry strong convictions and hate conceding ground during disagreements.")
        harmony_rules.append("Remember that marriage is a collaborative partnership, not a contest; treat mutual compromise as a mark of supreme maturity and love.")
    elif h7_sign_name in ["Taurus", "Capricorn"]:
        friction_points.append("Stubborn Entrenchment & Emotional Silence: A tendency to withdraw into silent treatments or rigid routines during emotional tension.")
        harmony_rules.append("Make it a sacred rule never to let silent treatments linger past 2 hours; break tension with a reassuring hug and shared comfort.")
    elif h7_sign_name in ["Gemini", "Virgo"]:
        friction_points.append("Over-Analytical Critique & Verbal Nitpicking: Focusing excessively on minor flaws, household schedules, or careless wordings.")
        harmony_rules.append("Prioritize heartfelt emotional warmth over intellectual perfection; replace critiques with sincere daily appreciation.")
    elif h7_sign_name in ["Cancer", "Pisces"]:
        friction_points.append("Emotional Permeability & Unspoken Expectations: Expecting the partner to read minds without clear verbal communication, leading to hurt feelings.")
        harmony_rules.append("Practice transparent, compassionate communication; express vulnerabilities directly rather than waiting for them to be guessed.")
    elif h7_sign_name in ["Leo", "Aquarius"]:
        friction_points.append("Balancing Independence with Dedicated Intimacy: Ensuring outside career, social circles, or humanitarian missions do not crowd out private romance.")
        harmony_rules.append("Protect weekly uninterrupted date nights and celebrate each other's individual achievements with proud enthusiasm.")
    else: # Libra, Sagittarius
        friction_points.append("Idealistic Expectations vs Everyday Realities: Expecting cinematic romance 24/7 and growing restless during routine domestic phases.")
        harmony_rules.append("Find deep sacred romance in everyday mundane moments—cooking together, morning tea, and quiet shared evenings.")

    harmony_rules.append("Maintain sacred privacy around your marital matters; never air intimate domestic disagreements before friends, social media, or outside parties.")
    harmony_rules.append("Chant the sacred Shukra-Lakshmi Beej Mantra on Friday evenings together to invite lasting harmony and abundance into your home.")

    disclaimer = (
        "🌸 A Gentle Astrological Note on Life’s Beautiful Mysteries: "
        "While Vedic astrology illuminates the planetary energies, cosmic archetypes, and aesthetic geometry surrounding your 7th House (Kalatra Bhava), "
        "the universe weaves human destiny with infinite creativity and personal free will. These descriptions of physical appearance, overall looks, and behavioral characteristics "
        "are intuitive astrological archetypes—celestial guiding signatures rather than rigid physical molds. The soul you eventually marry may embody these cosmic vibrations "
        "in unexpected, delightful ways, or bring their own unique grace. Keep your heart open to genuine love, authentic communication, and the wondrous surprises of destiny!"
    )

    return {
        "title": "Marriage, Love & Partner Dynamics (दाम्पत्य, प्रेम एवं जीवनसाथी)",
        "icon": "❤️",
        "seventh_house_sign": h7_sign_name,
        "seventh_house_sanskrit": h7_sign_san,
        "seventh_house_lord": h7_lord_name,
        "seventh_house_occupants": h7_occupants if h7_occupants else [f"Empty (Ruled by {h7_lord_name})"],
        "partner_attraction_archetype": attraction_text,
        "love_expression": {
            "venus_sign": v_sign_name,
            "love_language": love_lang,
            "how_they_express": how_express,
            "what_melts_their_heart": what_melts
        },
        "marriage_type_analysis": {
            "marriage_type": m_type,
            "probability_badge": m_badge,
            "marriage_verdict": m_verdict,
            "astrological_reasons": reasons
        },
        "spouse_profile": {
            "archetype_title": archetype_title,
            "physical_appearance": {
                "stature_and_build": stature,
                "face_and_features": face,
                "eyes_and_gaze": eyes,
                "complexion_and_hair": complexion,
                "aesthetic_and_style": style
            },
            "personality_traits": personality_traits[:4],
            "behavioral_characteristics": behavioral_traits[:4],
            "planetary_modifiers": planetary_modifiers
        },
        "marital_dynamics": {
            "friction_points": friction_points,
            "harmony_rules": harmony_rules
        },
        "gentle_disclaimer": disclaimer
    }


def generate_personalized_career_blueprint(kundli: Dict[str, Any]) -> Dict[str, Any]:
    planets = {p["name"]: p for p in kundli["planets"]}
    d1_houses = {h["house"]: h for h in kundli["d1_houses"]}

    h10 = d1_houses.get(10, {})
    h10_sign_id = h10.get("sign_id", 10)
    h10_sign = ZODIAC_SIGNS[h10_sign_id - 1]
    h10_sign_name = h10_sign["name"]
    h10_sign_san = h10_sign["sanskrit"]
    h10_lord_name = SIGN_LORDS.get(h10_sign_id, "Saturn")
    p_h10_lord = planets.get(h10_lord_name, {})
    h10_lord_house = p_h10_lord.get("house", 10)
    h10_lord_sign = p_h10_lord.get("sign_name", h10_sign_name)
    h10_occupants = [p["name"] for p in kundli["planets"] if p["house"] == 10]

    mercury = planets.get("Mercury", {})

    skills = [
        f"Strategic execution aligned with {h10_sign_name} (Ruled by {h10_lord_name}): Natural ability to structure complex goals into milestone-driven successes.",
        f"Leadership presence: Your 10th Lord ({h10_lord_name}) situated in House {h10_lord_house} ({h10_lord_sign}) directs your professional authority toward tangible public impact."
    ]
    if h10_occupants:
        skills.append(f"Direct vocational catalyst: **{', '.join(h10_occupants)}** in your 10th House supercharges your career visibility and executive competence.")
    else:
        skills.append(f"Unblemished Karma Bhava: Smooth professional progression through steady merit and ethical discipline.")

    if mercury:
        skills.append(f"Intellectual and analytical acumen (Mercury in {mercury.get('sign_name', 'Virgo')}, House {mercury.get('house', 1)}): Swift decision-making and articulate communication.")

    ideal_careers = {
        "Aries": ["Executive Leadership & Defense", "Entrepreneurial Tech Startups", "High-Stakes Surgery & Engineering", "Competitive Athletics & Sports Management"],
        "Taurus": ["Wealth Asset Management & Private Banking", "Luxury Real Estate & Architecture", "Fine Gastronomy & Hospitality", "High-End Aesthetics & Design"],
        "Gemini": ["Media Broadcasting & Journalism", "Software Engineering & Data Architecture", "Public Relations & International Trade", "Publishing & Digital Media"],
        "Cancer": ["Healthcare Administration & Pediatrics", "Human Resources & Talent Development", "Interior Design & Real Estate", "Culinary Enterprises & Education"],
        "Leo": ["Government Administration & Civil Services", "Corporate Executive & Board Leadership", "Entertainment & Theatrical Direction", "Luxury Brand Management"],
        "Virgo": ["Data Science & Algorithmic Strategy", "Healthcare Analytics & Pharmaceuticals", "Financial Auditing & Management Consulting", "Precision Engineering & Logistics"],
        "Libra": ["Corporate Law & International Diplomacy", "Art Direction & Fashion Enterprise", "High-Stakes Commercial Negotiation", "Public Relations & Luxury Goods"],
        "Scorpio": ["Cybersecurity & Intelligence Strategy", "Biomedical & Pharmaceutical Research", "Private Equity & Crisis Turnarounds", "Occult & Forensic Investigation"],
        "Sagittarius": ["Higher Education & University Deans", "International Law & Foreign Affairs", "Spiritual Mentorship & Publishing", "Global Philanthropy & Tourism"],
        "Capricorn": ["Heavy Industry & Infrastructure", "Chief Executive & Corporate Governance", "Government Policy & Public Infrastructure", "Mining, Geology & Long-Term Compounding"],
        "Aquarius": ["Artificial Intelligence & Advanced Robotics", "Aviation, Aerospace & Telecommunications", "Humanitarian NGOs & Social Enterprise", "Futuristic Research & Innovation"],
        "Pisces": ["Creative Arts, Film Direction & Music", "Global Marine Commerce & Import-Export", "Psychological Counseling & Healing Sanctuaries", "Spiritual Teaching & Philanthropy"]
    }

    careers = ideal_careers.get(h10_sign_name, ["Executive Leadership", "Strategic Consulting", "Technological Innovation"])

    swadharma = (
        f"Your true Swadharma (highest vocation) is governed by **{h10_sign_name} ({h10_sign_san})** and its ruler **{h10_lord_name}** in House {h10_lord_house}. "
        f"You are not meant for mundane, repetitive labor without purpose; your soul thrives when you build enduring systems that outlast you, "
        f"combining intellectual rigor with ethical leadership. You achieve peak professional momentum when you hold yourself to the highest standards of integrity."
    )

    fin_strat = (
        f"Compound wealth steadily by linking your vocation to the strengths of {h10_lord_name}. Avoid speculative shortcuts; "
        f"your chart favors systematic investments in productive assets, strategic career pivots during favorable Dashas, and building generational equity."
    )

    return {
        "title": "Career, Vocation & Financial Prosperity (कर्म, आजीविका एवं धन)",
        "icon": "💼",
        "natural_skills": skills,
        "where_to_use": [
            f"High-impact organizational environments governed by {h10_sign_name} principles",
            f"Enterprises requiring structured problem-solving and ethical governance",
            f"Strategic roles where your {h10_lord_name} placement (House {h10_lord_house}) grants clear autonomy",
            f"Collaborative, forward-thinking teams that respect long-term compounding"
        ],
        "ideal_careers": careers,
        "swadharma_calling": swadharma,
        "financial_strategy": fin_strat
    }


def generate_personalized_financial_strategy(kundli: Dict[str, Any], dhan_yogas: List[Dict[str, str]], vyaya_data: Dict[str, Any]) -> Dict[str, Any]:
    d1_houses = {h["house"]: h for h in kundli["d1_houses"]}

    h2 = d1_houses.get(2, {})
    h2_sign_id = h2.get("sign_id", 2)
    h2_sign_name = ZODIAC_SIGNS[h2_sign_id - 1]["name"]
    h2_lord_name = SIGN_LORDS.get(h2_sign_id, "Venus")

    h11 = d1_houses.get(11, {})
    h11_sign_id = h11.get("sign_id", 11)
    h11_sign_name = ZODIAC_SIGNS[h11_sign_id - 1]["name"]
    h11_lord_name = SIGN_LORDS.get(h11_sign_id, "Saturn")

    h12 = d1_houses.get(12, {})
    h12_sign_id = h12.get("sign_id", 12)
    h12_sign_name = ZODIAC_SIGNS[h12_sign_id - 1]["name"]
    h12_lord_name = SIGN_LORDS.get(h12_sign_id, "Jupiter")

    bad_habits = [
        f"Emotional or impulsive purchases triggered by stress (12th House in {h12_sign_name} / Ruled by {h12_lord_name}).",
        f"Under-monetizing your specialized skills; charging less than your true market value in negotiations.",
        f"Lending money to casual acquaintances without clear written terms, risking capital erosion.",
        f"Impatience with compounding; chasing volatile speculative fads instead of disciplined asset growth."
    ]

    mindful_rules = [
        f"Institute a mandatory 48-hour pause before making discretionary purchases above a threshold.",
        f"Channel your {h2_sign_name} Dhana Bhava energy: allocate at least 25% of all incoming revenue into untouchable compounding assets.",
        f"Honor your 11th Lord ({h11_lord_name}): build diverse, uncorrelated income streams rather than relying on a single employer.",
        f"Perform regular acts of Gupt Daan (anonymous charity) on your lucky planetary day to purify your 12th House Vyaya karma."
    ]

    opps = [
        f"Strategic wealth accumulation through {h2_sign_name} domains: tangible assets, real estate, and fixed-income compounding.",
        f"Cashflow scalability through {h11_sign_name} networks: digital platforms, royalties, partnerships, and high-value consulting.",
        f"Capitalizing on auspicious Dhan Yogas identified in your birth chart during major planetary Antardashas."
    ]

    not_expect = [
        "Instant overnight windfalls without disciplined effort and patient compounding.",
        "Smooth financial cooperation with individuals who lack ethical transparency.",
        "Permanent wealth retention if living expenses outpace savings rate during peak earning years."
    ]

    return {
        "title": "Financial Prosperity Strategy & Lakshmi Yoga (धन सम्पति एवं लक्ष्मी योग)",
        "icon": "💰",
        "bad_habits_draining_money": bad_habits,
        "mindful_rules": mindful_rules,
        "financial_yogas": dhan_yogas,
        "vyaya_analysis": vyaya_data,
        "opportunities_and_support": opps,
        "what_not_to_expect": not_expect,
        "wealth_mantra": "ॐ श्रीं ह्रीं क्लीं त्रिभुवन महालक्ष्म्यै अस्मांक दारिद्र्य नाशय प्रचुर धन देहि देहि क्लीं ह्रीं श्रीं ॐ ॥",
        "wealth_mantra_instructions": "Chant this sacred Mahalakshmi Beej Stotra 108 times on Friday mornings or evenings facing North-East with a pure cow-ghee lamp (दीप) to dissolve financial scarcity and activate permanent Dhan Akarshana (wealth magnetism)."
    }


def analyze_marriage_and_spouse_dynamics(kundli: Dict[str, Any]) -> Dict[str, Any]:
    """Alias for generate_personalized_marriage_blueprint for backwards compatibility."""
    return generate_personalized_marriage_blueprint(kundli)



def compute_life_milestones_timeline(kundli: Dict[str, Any]) -> Dict[str, Any]:
    """
    Computes a comprehensive, multi-decade astrological timeline highlighting key milestones
    across different life arenas:
    1. Expected Marriage Year Window (शुभ विवाह मुहूर्त काल)
    2. Career Breakthrough & Professional Pinnacle (कर्मोदय एवं पदोन्नति वर्ष)
    3. Financial Breakthrough & Wealth Compounding Era (महालक्ष्मी योग एवं धन संचय काल)
    4. Property, Real Estate & Conveyance Acquisition (भूमि, भवन एवं वाहन लाभ)
    5. Spiritual Realization & Higher Dharma Milestone (ज्ञानोदय एवं आत्मिक जागरण)
    6. Complete Chronological Life Trail from Youth to Maturity
    """
    meta = kundli.get("metadata", {})

    # 1. Precise Birth Date & Year Extraction with multiple robust fallbacks
    birth_year = meta.get("year")
    birth_month = meta.get("month", 1)
    birth_day = meta.get("day", 1)

    if not birth_year and meta.get("birth_date"):
        try:
            b_parts = [int(x) for x in str(meta["birth_date"]).split("-")]
            birth_year, birth_month, birth_day = b_parts[0], b_parts[1], b_parts[2]
        except Exception:
            pass

    if not birth_year and kundli.get("dashas"):
        try:
            b_str = kundli["dashas"][0].get("start_date", "")
            if b_str:
                b_parts = [int(x) for x in b_str.split("-")]
                birth_year, birth_month, birth_day = b_parts[0], b_parts[1], b_parts[2]
        except Exception:
            pass

    if not birth_year and meta.get("birth_time_local"):
        import re
        m_yr = re.search(r'\b(19\d\d|20\d\d)\b', meta.get("birth_time_local", ""))
        if m_yr:
            birth_year = int(m_yr.group(1))

    if not birth_year:
        birth_year = 1995

    now = datetime.now()
    current_year = now.year

    # Accurate birthday-aware current age calculation
    current_age = current_year - birth_year
    if (now.month, now.day) < (birth_month, birth_day):
        current_age -= 1
    current_age = max(0, current_age)

    def get_age_on_date(target_date_str: str) -> int:
        try:
            parts = [int(x) for x in str(target_date_str).split("-")[:3]]
            t_yr, t_mo, t_dy = parts[0], parts[1], parts[2]
            age = t_yr - birth_year
            if (t_mo, t_dy) < (birth_month, birth_day):
                age -= 1
            return max(0, age)
        except Exception:
            return max(0, int(str(target_date_str).split("-")[0]) - birth_year)

    lagna = kundli.get("lagna", {})
    lagna_num = lagna.get("sign_id") or lagna.get("sign_number", 1)

    def get_lord(h_num: int) -> str:
        s_num = ((lagna_num - 1 + (h_num - 1)) % 12) + 1
        return SIGN_LORDS.get(s_num, "Jupiter")

    h1_lord = get_lord(1)
    h2_lord = get_lord(2)
    h3_lord = get_lord(3)
    h4_lord = get_lord(4)
    h5_lord = get_lord(5)
    h6_lord = get_lord(6)
    h7_lord = get_lord(7)
    h8_lord = get_lord(8)
    h9_lord = get_lord(9)
    h10_lord = get_lord(10)
    h11_lord = get_lord(11)
    h12_lord = get_lord(12)

    planets_list = kundli.get("planets", [])
    h1_occupants = [p["name"] for p in planets_list if p.get("house") == 1]
    h2_occupants = [p["name"] for p in planets_list if p.get("house") == 2]
    h4_occupants = [p["name"] for p in planets_list if p.get("house") == 4]
    h7_occupants = [p["name"] for p in planets_list if p.get("house") == 7]
    h10_occupants = [p["name"] for p in planets_list if p.get("house") == 10]
    h11_occupants = [p["name"] for p in planets_list if p.get("house") == 11]

    def get_aspecting_planets(target_house: int) -> list:
        aspecting = []
        for p in planets_list:
            h = p.get("house", 1)
            name = p.get("name")
            dist = ((target_house - h) % 12) + 1
            if dist == 7 and name not in aspecting:
                aspecting.append(name)
            if name == "Mars" and dist in [4, 8] and name not in aspecting:
                aspecting.append(name)
            if name == "Jupiter" and dist in [5, 9] and name not in aspecting:
                aspecting.append(name)
            if name == "Saturn" and dist in [3, 10] and name not in aspecting:
                aspecting.append(name)
        return aspecting

    h4_aspects = get_aspecting_planets(4)
    h7_aspects = get_aspecting_planets(7)
    h10_aspects = get_aspecting_planets(10)

    # Navamsha (D9) Key Lords
    d9_houses = kundli.get("d9_houses", [])
    d9_h1_lord = "Mercury"
    d9_h7_lord = "Jupiter"
    d9_h10_lord = "Mercury"
    for dh in d9_houses:
        h = dh.get("house")
        sid = dh.get("sign_id", 1)
        if h == 1:
            d9_h1_lord = SIGN_LORDS.get(sid, "Mercury")
        elif h == 7:
            d9_h7_lord = SIGN_LORDS.get(sid, "Jupiter")
        elif h == 10:
            d9_h10_lord = SIGN_LORDS.get(sid, "Mercury")

    rahu_ketu_vivaha = [p["name"] for p in planets_list if p.get("name") in ["Rahu", "Ketu"] and p.get("house") in [1, 5, 7, 9, 11]]

    today_str = now.strftime("%Y-%m-%d")

    # Extract all Antardashas chronologically with exact age calculation
    all_ads = []
    active_ad_idx = -1
    for m in kundli.get("dashas", []):
        m_lord = m.get("lord", "Jupiter")
        for ad in m.get("antardashas", []):
            ad_lord = ad.get("sub_lord", m_lord)
            s_date = ad.get("start_date", "")
            e_date = ad.get("end_date", "")
            if s_date and e_date:
                try:
                    s_yr = int(s_date.split("-")[0])
                    e_yr = int(e_date.split("-")[0])
                    s_age = get_age_on_date(s_date)
                    e_age = get_age_on_date(e_date)
                    is_active = (s_date <= today_str <= e_date)
                    idx = len(all_ads)
                    if is_active:
                        active_ad_idx = idx
                    all_ads.append({
                        "m_lord": m_lord,
                        "ad_lord": ad_lord,
                        "start_date": s_date,
                        "end_date": e_date,
                        "start_year": s_yr,
                        "end_year": e_yr,
                        "start_age": s_age,
                        "end_age": e_age,
                        "is_active": is_active
                    })
                except Exception:
                    pass

    # Helper to find optimal period based on planetary targets and timing priorities
    def find_best_period(target_roles: List[str], min_eligible_age: int, max_age: int, prefer_current: bool = True) -> Tuple[Dict[str, Any], str]:
        # Scenario 1: Native is CURRENTLY within this life domain's eligible age window
        if prefer_current and (min_eligible_age <= current_age <= max_age) and active_ad_idx >= 0:
            curr_ad = all_ads[active_ad_idx]
            if curr_ad["ad_lord"] in target_roles or curr_ad["m_lord"] in target_roles:
                return curr_ad, "ACTIVE"
            if active_ad_idx + 1 < len(all_ads):
                next_ad = all_ads[active_ad_idx + 1]
                if next_ad["start_year"] <= current_year + 1:
                    if next_ad["ad_lord"] in target_roles or next_ad["m_lord"] in target_roles:
                        return next_ad, "UPCOMING"

        # Scenario 2: Native has already crossed max_age (e.g. 50+ looking at first marriage) -> Historical Past
        if current_age > max_age:
            candidates = []
            for ad in all_ads:
                if min_eligible_age <= ad["start_age"] <= max_age:
                    score = 0
                    if ad["ad_lord"] in target_roles:
                        idx = target_roles.index(ad["ad_lord"])
                        score += 50 + max(0, (len(target_roles) - idx) * 3)
                    if ad["m_lord"] in target_roles:
                        score += 35
                    candidates.append((score, ad))
            if candidates:
                candidates.sort(key=lambda x: x[0], reverse=True)
                return candidates[0][1], "PAST"

        # Scenario 3: Future upcoming periods (for young native or upcoming window)
        candidates = []
        for ad in all_ads:
            if ad["end_year"] >= current_year and ad["start_age"] >= min_eligible_age and ad["start_age"] <= max_age:
                score = 0
                if ad["ad_lord"] in target_roles:
                    idx = target_roles.index(ad["ad_lord"])
                    score += 50 + max(0, (len(target_roles) - idx) * 3)
                if ad["m_lord"] in target_roles:
                    score += 35

                diff = max(0, ad["start_year"] - current_year)
                if diff <= 1:
                    score += 40
                elif diff <= 3:
                    score += 25
                elif diff <= 6:
                    score += 15

                candidates.append((score, ad))

        if candidates:
            candidates.sort(key=lambda x: x[0], reverse=True)
            chosen = candidates[0][1]
            st = "UPCOMING" if chosen["start_year"] <= current_year + 3 else "FUTURE"
            return chosen, st

        future_ads = [ad for ad in all_ads if ad["end_year"] >= current_year]
        if future_ads:
            return future_ads[0], "FUTURE"
        return all_ads[-1] if all_ads else {
            "m_lord": "Jupiter", "ad_lord": "Venus", "start_year": current_year,
            "end_year": current_year + 1, "start_age": current_age, "end_age": current_age + 1,
            "is_active": True
        }, "ACTIVE"

    # 1. Expected Marriage Window
    marr_targets = list(dict.fromkeys(
        [h7_lord] + h7_occupants + h7_aspects + ["Venus", "Jupiter", d9_h7_lord, h5_lord, h2_lord, h11_lord, h1_lord] + rahu_ketu_vivaha
    ))
    marr_ad, marr_tag = find_best_period(marr_targets, min_eligible_age=20, max_age=38, prefer_current=True)

    if marr_tag == "ACTIVE" or (marr_ad["start_year"] <= current_year <= marr_ad["end_year"] and current_age <= 38):
        marr_s_yr = current_year
        marr_e_yr = max(marr_ad["end_year"], current_year + 1)
        marr_s_age = current_age
        marr_e_age = max(marr_ad["end_age"], current_age + 1)
        marr_status = "ACTIVE / PRESENT HORIZON"
        marr_catalyst = (
            f"Activation of the 7th House (Kalatra Bhava) lord **{h7_lord}** and Vivaha catalyst **{marr_ad['ad_lord']}** under your active **{marr_ad['m_lord']}–{marr_ad['ad_lord']}** period. "
            f"Your cosmic marriage portal is OPEN RIGHT NOW ({marr_s_yr} – {marr_e_yr}). Celestial energies are directly aligned for spouse meeting, matrimonial engagement, and joyful wedding ceremonies."
        )
        marr_guidance = "Your matrimonial window is actively open right now. Finalize marriage arrangements, engage trusted elders in wedding preparations, and maintain warm emotional understanding."
    elif marr_tag == "PAST":
        marr_s_yr = marr_ad["start_year"]
        marr_e_yr = max(marr_ad["end_year"], marr_s_yr + 1)
        marr_s_age = marr_ad["start_age"]
        marr_e_age = max(marr_ad["end_age"], marr_s_age + 1)
        marr_status = "PAST / CONSOLIDATED FOUNDATION"
        marr_catalyst = (
            f"Classical Vivaha era materialized under the **{marr_ad['m_lord']}–{marr_ad['ad_lord']}** period, "
            f"establishing your core partnership, domestic foundation, and family lineage."
        )
        marr_guidance = "Nurture spousal companionship and mutual dharmic support; honor shared milestones and family traditions."
    elif marr_ad["start_year"] <= current_year + 3:
        marr_s_yr = marr_ad["start_year"]
        marr_e_yr = max(marr_ad["end_year"], marr_s_yr + 1)
        marr_s_age = marr_ad["start_age"]
        marr_e_age = max(marr_ad["end_age"], marr_s_age + 1)
        marr_status = "UPCOMING GOLDEN WINDOW"
        marr_catalyst = (
            f"Upcoming activation of the 7th House lord **{h7_lord}** and benefic graha **{marr_ad['ad_lord']}**. "
            f"This upcoming celestial era creates fertile cosmic conditions for soul-partner entry, matchmaking success, and spousal harmony."
        )
        marr_guidance = "Prepare your lifestyle for partnership; maintain clear emotional clarity; cultivate shared values and openness to matrimonial connections."
    else:
        marr_s_yr = marr_ad["start_year"]
        marr_e_yr = max(marr_ad["end_year"], marr_s_yr + 1)
        marr_s_age = marr_ad["start_age"]
        marr_e_age = max(marr_ad["end_age"], marr_s_age + 1)
        marr_status = "FUTURE CELESTIAL HORIZON"
        marr_catalyst = (
            f"Long-range marital harmonization under **{marr_ad['m_lord']}–{marr_ad['ad_lord']}** dasha period, "
            f"activating the 7th house and spousal karakas in your birth chart."
        )
        marr_guidance = "Focus on personal dharmic grounding and financial independence; matrimonial energies mature in due cosmic season."

    marr_window = f"{marr_s_yr} – {marr_e_yr}"
    marr_age_str = f"Age {marr_s_age} – {marr_e_age}" if marr_s_age != marr_e_age else f"Age {marr_s_age}"

    # 2. Career Breakthrough Window
    career_targets = list(dict.fromkeys(
        [h10_lord] + h10_occupants + h10_aspects + ["Sun", "Mars", "Saturn", "Mercury", h1_lord, h9_lord, d9_h10_lord, h6_lord]
    ))
    career_ad, career_tag = find_best_period(career_targets, min_eligible_age=22, max_age=52, prefer_current=True)

    if career_tag == "ACTIVE" or (career_ad["start_year"] <= current_year <= career_ad["end_year"] and current_age <= 52):
        car_s_yr = current_year
        car_e_yr = max(career_ad["end_year"], current_year + 1)
        car_s_age = current_age
        car_e_age = max(career_ad["end_age"], current_age + 1)
        car_status = "ACTIVE / PRESENT HORIZON"
        car_catalyst = (
            f"Empowerment of the 10th House (Karma Bhava) lord **{h10_lord}** synthesized with **{career_ad['ad_lord']}**'s executive drive. "
            f"Active right now ({car_s_yr} – {car_e_yr}), this astrological alignment dissolves past professional stagnation, granting heightened public recognition, executive mandate, and career authority."
        )
        car_guidance = "Do not hesitate to assume executive responsibilities; turn workplace tests into public demonstrations of mastery; your karma is in active ascension."
    elif career_tag == "PAST":
        car_s_yr = career_ad["start_year"]
        car_e_yr = max(career_ad["end_year"], car_s_yr + 1)
        car_s_age = career_ad["start_age"]
        car_e_age = max(career_ad["end_age"], car_s_age + 1)
        car_status = "PAST / CONSOLIDATED FOUNDATION"
        car_catalyst = f"Foundational career zenith achieved under **{career_ad['m_lord']}–{career_ad['ad_lord']}** period."
        car_guidance = "Transition into mentorship; leverage your wealth of professional experience to guide the next generation."
    elif career_ad["start_year"] <= current_year + 3:
        car_s_yr = career_ad["start_year"]
        car_e_yr = max(career_ad["end_year"], car_s_yr + 1)
        car_s_age = career_ad["start_age"]
        car_e_age = max(career_ad["end_age"], car_s_age + 1)
        car_status = "UPCOMING GOLDEN HORIZON"
        car_catalyst = (
            f"Impending mobilization of the 10th House lord **{h10_lord}** under **{career_ad['ad_lord']}**. "
            f"Opens high-visibility leadership avenues, promotions, or successful commercial expansion."
        )
        car_guidance = "Hone technical skills and strategic networking today; the upcoming period will test and reward your professional readiness."
    else:
        car_s_yr = career_ad["start_year"]
        car_e_yr = max(career_ad["end_year"], car_s_yr + 1)
        car_s_age = career_ad["start_age"]
        car_e_age = max(career_ad["end_age"], car_s_age + 1)
        car_status = "FUTURE CAREER PINNACLE"
        car_catalyst = f"Major institutional elevation under **{career_ad['m_lord']}–{career_ad['ad_lord']}** period."
        car_guidance = "Build steady professional reputation; enduring career achievements accumulate through perseverance."

    car_window = f"{car_s_yr} – {car_e_yr}"
    car_age_str = f"Age {car_s_age} – {car_e_age}" if car_s_age != car_e_age else f"Age {car_s_age}"

    # 3. Financial Breakthrough Window
    wealth_targets = list(dict.fromkeys(
        [h11_lord, h2_lord, "Jupiter", "Mercury", "Venus", h9_lord, h5_lord, h1_lord]
    ))
    wealth_ad, wealth_tag = find_best_period(wealth_targets, min_eligible_age=23, max_age=55, prefer_current=True)

    if wealth_tag == "ACTIVE" or (wealth_ad["start_year"] <= current_year <= wealth_ad["end_year"] and current_age <= 55):
        fin_s_yr = current_year
        fin_e_yr = max(wealth_ad["end_year"], current_year + 1)
        fin_s_age = current_age
        fin_e_age = max(wealth_ad["end_age"], current_age + 1)
        fin_status = "ACTIVE / PRESENT HORIZON"
        fin_catalyst = (
            f"Confluence of the 2nd House (Dhana Bhava) lord **{h2_lord}** and 11th House (Labha Bhava) lord **{h11_lord}** catalyzed by **{wealth_ad['ad_lord']}**. "
            f"Ripening of latent Dhana Yogas in your chart right now ({fin_s_yr} – {fin_e_yr}), unlocking notable compensation jumps, successful investments, and capital compounding."
        )
        fin_guidance = "Channel surplus revenue into compounding assets; avoid impulsive speculation; practice regular charitable giving (Daan) to sustain Lakshmi's grace."
    elif wealth_tag == "PAST":
        fin_s_yr = wealth_ad["start_year"]
        fin_e_yr = max(wealth_ad["end_year"], fin_s_yr + 1)
        fin_s_age = wealth_ad["start_age"]
        fin_e_age = max(wealth_ad["end_age"], fin_s_age + 1)
        fin_status = "PAST / CONSOLIDATED FOUNDATION"
        fin_catalyst = f"Major wealth accumulation era consolidated under **{wealth_ad['m_lord']}–{wealth_ad['ad_lord']}** period."
        fin_guidance = "Preserve accumulated capital; manage estate planning and family wealth protection."
    elif wealth_ad["start_year"] <= current_year + 3:
        fin_s_yr = wealth_ad["start_year"]
        fin_e_yr = max(wealth_ad["end_year"], fin_s_yr + 1)
        fin_s_age = wealth_ad["start_age"]
        fin_e_age = max(wealth_ad["end_age"], fin_s_age + 1)
        fin_status = "UPCOMING WEALTH ERA"
        fin_catalyst = (
            f"Cosmic activation of Dhana Karakas Jupiter and Mercury under **{wealth_ad['ad_lord']}**. "
            f"Paves the way for debt retirement, salary breakthroughs, and commercial profitability."
        )
        fin_guidance = "Eliminate high-interest liabilities; build emergency reserves; prepare capital for high-ROI opportunities."
    else:
        fin_s_yr = wealth_ad["start_year"]
        fin_e_yr = max(wealth_ad["end_year"], fin_s_yr + 1)
        fin_s_age = wealth_ad["start_age"]
        fin_e_age = max(wealth_ad["end_age"], fin_s_age + 1)
        fin_status = "FUTURE PROSPERITY PINNACLE"
        fin_catalyst = f"Major financial consolidation under **{wealth_ad['m_lord']}–{wealth_ad['ad_lord']}** period."
        fin_guidance = "Maintain disciplined saving habits; compound growth takes time to reach scale."

    fin_window = f"{fin_s_yr} – {fin_e_yr}"
    fin_age_str = f"Age {fin_s_age} – {fin_e_age}" if fin_s_age != fin_e_age else f"Age {fin_s_age}"

    # 4. Property & Fixed Asset Window
    property_targets = list(dict.fromkeys(
        [h4_lord] + h4_occupants + h4_aspects + ["Mars", "Venus", "Moon", h1_lord]
    ))
    property_ad, property_tag = find_best_period(property_targets, min_eligible_age=24, max_age=55, prefer_current=True)

    if property_tag == "ACTIVE" or (property_ad["start_year"] <= current_year <= property_ad["end_year"] and current_age <= 55):
        prop_s_yr = current_year
        prop_e_yr = max(property_ad["end_year"], current_year + 1)
        prop_s_age = current_age
        prop_e_age = max(property_ad["end_age"], current_age + 1)
        prop_status = "ACTIVE / PRESENT HORIZON"
        prop_catalyst = (
            f"Harmonization of the 4th House (Sukha, Bhumi & Vahana Bhava) lord **{h4_lord}** under the grounding influence of **{property_ad['ad_lord']}**. "
            f"Cosmic energies favor acquiring residential property, purchasing family conveyances, or renovating your domestic sanctuary."
        )
        prop_guidance = "Thoroughly inspect all property documentation; ensure clean legal title; create a peaceful, Vastu-harmonized living environment."
    elif property_tag == "PAST":
        prop_s_yr = property_ad["start_year"]
        prop_e_yr = max(property_ad["end_year"], prop_s_yr + 1)
        prop_s_age = property_ad["start_age"]
        prop_e_age = max(property_ad["end_age"], prop_s_age + 1)
        prop_status = "PAST / CONSOLIDATED FOUNDATION"
        prop_catalyst = f"Real estate and property foundation acquired under **{property_ad['m_lord']}–{property_ad['ad_lord']}** period."
        prop_guidance = "Maintain living sanctuary harmony and positive Vastu vibrations."
    elif property_ad["start_year"] <= current_year + 3:
        prop_s_yr = property_ad["start_year"]
        prop_e_yr = max(property_ad["end_year"], prop_s_yr + 1)
        prop_s_age = property_ad["start_age"]
        prop_e_age = max(property_ad["end_age"], prop_s_age + 1)
        prop_status = "UPCOMING ASSET WINDOW"
        prop_catalyst = (
            f"Energizing of the 4th House lord **{h4_lord}** and Bhumi Karaka Mars. "
            f"Signals favorable cosmic timing for real estate investments or vehicle acquisition."
        )
        prop_guidance = "Consolidate savings for down payment; research prime locations; avoid hurried emotional property commitments."
    else:
        prop_s_yr = property_ad["start_year"]
        prop_e_yr = max(property_ad["end_year"], prop_s_yr + 1)
        prop_s_age = property_ad["start_age"]
        prop_e_age = max(property_ad["end_age"], prop_s_age + 1)
        prop_status = "FUTURE SANCTUARY PINNACLE"
        prop_catalyst = f"Long-term property acquisition window under **{property_ad['m_lord']}–{property_ad['ad_lord']}** period."
        prop_guidance = "Maintain good creditworthiness and steady savings for future asset building."

    prop_window = f"{prop_s_yr} – {prop_e_yr}"
    prop_age_str = f"Age {prop_s_age} – {prop_e_age}" if prop_s_age != prop_e_age else f"Age {prop_s_age}"

    # 5. Spiritual Awakening Window
    spiritual_targets = list(dict.fromkeys([h9_lord, h12_lord, "Ketu", "Jupiter", "Sun"]))
    spiritual_ad, spiritual_tag = find_best_period(spiritual_targets, min_eligible_age=36, max_age=65, prefer_current=True)

    # Compile the Top 4 Highlight Milestones
    highlights = {
        "marriage": {
            "title": "Expected Marriage Window (शुभ विवाह मुहूर्त काल)",
            "year_window": marr_window,
            "age_window": marr_age_str,
            "icon": "💍",
            "active_dasha": f"{marr_ad['m_lord']} Mahadasha • {marr_ad['ad_lord']} Antardasha",
            "astrological_catalyst": marr_catalyst,
            "nature_of_event": "Sacred marital alliance, lifelong emotional anchoring, and family expansion.",
            "status": marr_status,
            "guidance": marr_guidance
        },
        "career_breakthrough": {
            "title": "Career Breakthrough Year (कर्मोदय एवं पदोन्नति वर्ष)",
            "year_window": car_window,
            "age_window": car_age_str,
            "icon": "🚀",
            "active_dasha": f"{career_ad['m_lord']} Mahadasha • {career_ad['ad_lord']} Antardasha",
            "astrological_catalyst": car_catalyst,
            "nature_of_event": "Executive title ascension, breakthrough entrepreneurship scale, or prominent institutional mandate.",
            "status": car_status,
            "guidance": car_guidance
        },
        "financial_breakthrough": {
            "title": "Financial Breakthrough & Wealth Era (महालक्ष्मी योग एवं धन संचय काल)",
            "year_window": fin_window,
            "age_window": fin_age_str,
            "icon": "💰",
            "active_dasha": f"{wealth_ad['m_lord']} Mahadasha • {wealth_ad['ad_lord']} Antardasha",
            "astrological_catalyst": fin_catalyst,
            "nature_of_event": "Surge in liquid assets, debt elimination, portfolio compounding, and durable financial safety.",
            "status": fin_status,
            "guidance": fin_guidance
        },
        "property_acquisition": {
            "title": "Property Acquisition Window (भूमि, भवन एवं वाहन लाभ)",
            "year_window": prop_window,
            "age_window": prop_age_str,
            "icon": "🏡",
            "active_dasha": f"{property_ad['m_lord']} Mahadasha • {property_ad['ad_lord']} Antardasha",
            "astrological_catalyst": prop_catalyst,
            "nature_of_event": "Real estate registration, home sanctification (Griha Pravesha), or acquisition of long-coveted vehicles.",
            "status": prop_status,
            "guidance": prop_guidance
        }
    }

    def get_dasha_for_year(target_yr: int, default_str: str) -> str:
        for ad in all_ads:
            if ad["start_year"] <= target_yr <= ad["end_year"]:
                return f"{ad['m_lord']} Mahadasha • {ad['ad_lord']} Antardasha"
        return default_str

    # Assemble 8 Chronological Eras with accurate age mapping
    chronological_raw = [
        {
            "id": "m1_foundation",
            "title": "Academic Foundation & Core Competency (विद्यार्जन एवं प्रतिभा निर्माण)",
            "category": "Education & Core Identity",
            "category_icon": "🌱",
            "start_year": birth_year + 17,
            "end_year": birth_year + 22,
            "start_age": 17,
            "end_age": 22,
            "dasha": get_dasha_for_year(birth_year + 19, f"{h1_lord} Period"),
            "astrological_rationale": (
                f"Formative intellectual period governed by the Ascendant ({lagna.get('sign_name', 'Rising Sign')}) and Mercury/Jupiter influence. "
                f"Focus centers on academic specialization, developing foundational discipline, and establishing your moral compass."
            ),
            "actionable_guidance": "Cultivate deep intellectual rigor, seek seasoned academic mentors, and avoid scattered, unfocused pursuits."
        },
        {
            "id": "m2_career_launch",
            "title": "Professional Launch & First Major Leap (कर्मारम्भ एवं स्वावलंबन)",
            "category": "Career & Identity",
            "category_icon": "⚡",
            "start_year": birth_year + 23,
            "end_year": birth_year + 27,
            "start_age": 23,
            "end_age": 27,
            "dasha": get_dasha_for_year(birth_year + 25, f"{h10_lord} Period"),
            "astrological_rationale": (
                f"The initial testing ground of the 10th House (Karma Bhava) and Sun/Mars vitality. "
                f"Marks the transition into economic independence, navigating competitive workplace dynamics, and discovering your authentic vocational strengths."
            ),
            "actionable_guidance": "Embrace steep learning curves without fear; demonstrate unwavering reliability and build an unassailable professional reputation."
        },
        {
            "id": "m3_vivaha",
            "title": "Sacred Vivaha: Marriage & Karmic Partner Union (शुभ विवाह एवं दाम्पत्य प्रवेश)",
            "category": "Marriage & Family",
            "category_icon": "💍",
            "start_year": marr_s_yr,
            "end_year": marr_e_yr,
            "start_age": marr_s_age,
            "end_age": marr_e_age,
            "dasha": f"{marr_ad['m_lord']} Mahadasha • {marr_ad['ad_lord']} Antardasha",
            "astrological_rationale": (
                f"Auspicious celestial confluence activating the 7th House (Kalatra Bhava) lord **{h7_lord}** and Venusian harmony. "
                f"Your birth chart indicates the entrance of a life partner whose complementary temperament fosters emotional stability and shared dharmic growth."
            ),
            "actionable_guidance": "Approach partnership with open emotional transparency; respect each other's individuality while cultivating shared family traditions."
        },
        {
            "id": "m4_property",
            "title": "Property, Land & Conveyance Acquisition (भूमि, भवन एवं वाहन सुख)",
            "category": "Property & Real Estate",
            "category_icon": "🏡",
            "start_year": prop_s_yr,
            "end_year": prop_e_yr,
            "start_age": prop_s_age,
            "end_age": prop_e_age,
            "dasha": f"{property_ad['m_lord']} Mahadasha • {property_ad['ad_lord']} Antardasha",
            "astrological_rationale": (
                f"Energizing of the 4th House (Sukha Bhava) lord **{h4_lord}** and planetary karakas Mars and Venus. "
                f"Cosmic energies favor the acquisition of real estate assets, home transformation, and securing comfortable family shelter."
            ),
            "actionable_guidance": "Perform thorough title verification on all real estate purchases; prioritize structural longevity and serene surroundings over ostentation."
        },
        {
            "id": "m5_career_zenith",
            "title": "Career Zenith & Executive Leadership (पदोन्नति, कीर्ति एवं अधिकार लाभ)",
            "category": "Career & Power",
            "category_icon": "👑",
            "start_year": car_s_yr,
            "end_year": car_e_yr,
            "start_age": car_s_age,
            "end_age": car_e_age,
            "dasha": f"{career_ad['m_lord']} Mahadasha • {career_ad['ad_lord']} Antardasha",
            "astrological_rationale": (
                f"Solar and Martian elevation over the 10th House (Karma Sthana) catalyzed by **{career_ad['ad_lord']}**. "
                f"Brings your highest professional autonomy, public leadership responsibilities, and significant industry acclaim."
            ),
            "actionable_guidance": "Exercise leadership with fairness and humility; empower subordinates; build institutional systems that endure."
        },
        {
            "id": "m6_financial_breakthrough",
            "title": "Major Financial Breakthrough & Wealth Compounding (अखंड धन लाभ एवं संचय)",
            "category": "Wealth & Lakshmi Yoga",
            "category_icon": "💰",
            "start_year": fin_s_yr,
            "end_year": fin_e_yr,
            "start_age": fin_s_age,
            "end_age": fin_e_age,
            "dasha": f"{wealth_ad['m_lord']} Mahadasha • {wealth_ad['ad_lord']} Antardasha",
            "astrological_rationale": (
                f"Ripening of wealth houses: 2nd House (Dhana Sthana) and 11th House (Labha Sthana) catalyzed by classical Dhana Yogas in your horoscope. "
                f"Multiple capital investments and commercial endeavors yield abundant, long-lasting returns, freeing you from financial anxiety."
            ),
            "actionable_guidance": "Anchor surplus liquidity into productive, tangible assets; avoid speculative greed; practice regular charity (Daan) to sustain Lakshmi's grace."
        },
        {
            "id": "m7_legacy",
            "title": "Legacy Building, Mentorship & Family Prosperity (वैभव संचय एवं परिवार कल्याण)",
            "category": "Legacy & Status",
            "category_icon": "🏛️",
            "start_year": birth_year + 48,
            "end_year": birth_year + 55,
            "start_age": 48,
            "end_age": 55,
            "dasha": get_dasha_for_year(birth_year + 50, f"{h9_lord} / Jupiter Period"),
            "astrological_rationale": (
                f"Maturation of life's material efforts and elevation of family standing under the benign gaze of Jupiter and the 9th House (Dharma). "
                f"Attention shifts toward family legacy, nurturing children's aspirations, establishing family trusts, and enjoying community respect."
            ),
            "actionable_guidance": "Transition gracefully from competitive striving to paternal/maternal mentorship; pass down ethical values and generational wisdom."
        },
        {
            "id": "m8_spirituality",
            "title": "Spiritual Illumination & Higher Dharma Realization (ज्ञानोदय, तीर्थाटन एवं आत्मिक शांति)",
            "category": "Spirituality & Moksha",
            "category_icon": "🕉️",
            "start_year": max(birth_year + 56, spiritual_ad["start_year"]),
            "end_year": max(birth_year + 66, spiritual_ad["end_year"]),
            "start_age": max(56, spiritual_ad["start_age"]),
            "end_age": max(66, spiritual_ad["end_age"]),
            "dasha": f"{spiritual_ad['m_lord']} Mahadasha • {spiritual_ad['ad_lord']} Antardasha",
            "astrological_rationale": (
                f"Spiritual culmination guided by Ketu (Mokshakaraka), Jupiter (Devaguru), and the 12th House (Moksha Sthana). "
                f"Material desires recede into deep inner fulfillment, sacred pilgrimages, meditation, and direct contemplation of the Supreme Self."
            ),
            "actionable_guidance": "Immerse in daily contemplative meditation, study timeless sacred scriptures, and dedicate time to selfless community service (Nishkama Seva)."
        }
    ]

    # Sort chronological milestones by start year
    chronological_raw.sort(key=lambda x: (x["start_year"], x["end_year"]))

    # Enrich each milestone with calculated age range and status tags
    chronological_journey = []
    for item in chronological_raw:
        s_yr = item["start_year"]
        e_yr = item["end_year"]
        s_age = item["start_age"]
        e_age = item["end_age"]

        if e_yr < current_year:
            st = "PAST / CONSOLIDATED FOUNDATION"
            st_cls = "past"
        elif s_yr <= current_year <= e_yr:
            st = "ACTIVE / PRESENT HORIZON"
            st_cls = "active"
        elif s_yr > current_year and s_yr <= current_year + 4:
            st = "UPCOMING GOLDEN WINDOW"
            st_cls = "upcoming"
        else:
            st = "FUTURE CELESTIAL PINNACLE"
            st_cls = "future"

        chronological_journey.append({
            "id": item["id"],
            "title": item["title"],
            "category": item["category"],
            "category_icon": item["category_icon"],
            "year_range": f"{s_yr} – {e_yr}",
            "age_range": f"Age {s_age} – {e_age}" if s_age != e_age else f"Age {s_age}",
            "dasha_catalyst": item["dasha"],
            "status": st,
            "status_class": st_cls,
            "astrological_rationale": item["astrological_rationale"],
            "actionable_guidance": item["actionable_guidance"]
        })

    return {
        "title": "Sacred Life Timeline & Key Karmic Milestones (जीवन कालक्रम एवं प्रमुख भाग्य चक्र)",
        "subtitle": "Vedic Vimshottari Dasha Chronology: Auspicious Windows for Vivaha, Career Zenith, Dhana Yoga & Life Milestones",
        "native_current_age": current_age,
        "native_birth_year": birth_year,
        "highlight_milestones": highlights,
        "chronological_journey": chronological_journey,
        "timing_guidance_disclaimer": (
            "🌸 Astrological Timing Note: Planetary periods (Dashas) indicate fertile cosmic seasons when circumstances organically favor specific life developments. "
            "These predicted windows are celestial catalysts; personal conscious intention (Purushartha), righteous moral conduct, and proactive effort are the divine bridge that materializes these potentials into reality."
        )
    }


def generate_professional_astrologer_report(kundli: Dict[str, Any]) -> Dict[str, Any]:
    """
    Constructs an exhaustive, profoundly detailed astrological life reading.
    Written in the classical yet psychologically penetrating voice of a revered
    Vedic Astrologer (ज्योतिषाचार्य), covering public persona, hidden subconscious drives,
    passions/hobbies, positive virtues, shadow weaknesses, and full life domains.
    """
    meta = kundli["metadata"]
    lagna = kundli["lagna"]
    planets = {p["name"]: p for p in kundli["planets"]}
    d1_houses = {h["house"]: h for h in kundli["d1_houses"]}
    dashas = kundli["dashas"]
    manglik = kundli["manglik"]

    lagna_name = lagna["sign_name"]
    lagna_sanskrit = lagna["sign_sanskrit"]
    # profile dynamically generated below

    moon = planets.get("Moon", {})
    sun = planets.get("Sun", {})
    jupiter = planets.get("Jupiter", {})
    saturn = planets.get("Saturn", {})
    venus = planets.get("Venus", {})
    mars = planets.get("Mars", {})

    active_dasha = find_active_dasha(dashas)
    m_lord = active_dasha["mahadasha_lord"]
    ad_lord = active_dasha["antardasha_lord"]

    # Auspicious Planetary Yogas
    detected_yogas = []
    if moon and jupiter:
        m_house = moon.get("house", 1)
        j_house = jupiter.get("house", 1)
        rel_pos = ((j_house - m_house) % 12) + 1
        if rel_pos in [1, 4, 7, 10]:
            detected_yogas.append({
                "name": "Gajakesari Yoga (गजकेसरी महायोग)",
                "description": "Jupiter occupies a Kendra (1st, 4th, 7th, or 10th house) from the Moon. This is one of the highest royal yogas in Vedic Jyotish, ensuring lasting intellectual reputation, honorable social standing, prosperity, and divine protection during times of adversity."
            })

    if sun and planets.get("Mercury"):
        if sun.get("house") == planets["Mercury"].get("house"):
            detected_yogas.append({
                "name": "Budhaditya Yoga (बुधादित्य राजयोग)",
                "description": "The conjunction of the radiant Sun (Soul & Authority) and Mercury (Intellect & Speech) in the same Bhava creates brilliant analytical acumen, eloquence in speech, administrative competence, and high esteem from governance and peers."
            })

    for p_name in ["Jupiter", "Saturn", "Mars", "Venus"]:
        p_obj = planets.get(p_name)
        if p_obj and p_obj.get("dignity", "").startswith("Exalted"):
            detected_yogas.append({
                "name": f"Uccha {p_name} Yoga ({p_obj.get('hindi', p_name)} उच्च प्रभाव)",
                "description": f"{p_name} is situated in its sign of maximum exaltation, elevating the significations of its houses and bestowing monumental karmic rewards during its operational periods."
            })

    if not detected_yogas:
        detected_yogas.append({
            "name": "Subha Graha Drishti Yoga (शुभ ग्रह दृष्टि प्रभाव)",
            "description": "Benefic planetary placements in key angular houses provide resilience against adversity, steady financial compounding, and dignified recognition."
        })

    # Deep Domain Dynamic Analyses
    dhan_yogas, vyaya_data = detect_financial_yogas_and_vyaya(kundli)
    psycho_profile = generate_personalized_psychological_profile(kundli)
    marriage_bp = generate_personalized_marriage_blueprint(kundli)
    career_bp = generate_personalized_career_blueprint(kundli)
    fin_bp = generate_personalized_financial_strategy(kundli, dhan_yogas, vyaya_data)
    current_phase_data = analyze_current_life_phase(kundli)
    milestones_timeline = compute_life_milestones_timeline(kundli)

    # Gemstone & Remedies Configuration
    lucky_graha = GRAHA_UPAYA.get(m_lord, GRAHA_UPAYA["Jupiter"])
    lagna_graha = GRAHA_UPAYA.get(lagna["nakshatra_lord"], GRAHA_UPAYA["Sun"])

    remedies_summary = {
        "bhagya_gemstone": lucky_graha["gemstone"],
        "wearing_rules": f"Wear in {lucky_graha['metal']} on the {lucky_graha['finger']} on {lucky_graha['day']}.",
        "lucky_metal": lucky_graha["metal"],
        "sacred_mantra": lucky_graha["mantra"],
        "auspicious_deity": lucky_graha["deity"],
        "charity_items": lucky_graha["daan"],
        "daily_guidance": [
            "Offer clean water (Arghya) to the rising Sun every morning in a copper vessel with a pinch of red kumkum and flowers.",
            f"Chant the sacred Mahadasha Beej Mantra: '{lucky_graha['mantra']}' 108 times daily facing East.",
            "Observe regular acts of Annadaan (feeding hungry beings, cows, or birds) on your planetary day to dissolve karmic blockages."
        ]
    }

    return {
        "invocation": "॥ श्री गणेशाय नमः • ॐ गुरुभ्यो नमः • ॐ नमः शिवाय ॥",
        "astrologer_title": "Detailed Astrological Life Reading & Psychological Profile",
        "preamble": (
            f"This profound astrological reading is formulated for **{meta['name']}**, "
            f"born on {meta['birth_time_local']} at {meta['city']} (Latitude: {meta['latitude']}°, Longitude: {meta['longitude']}°). "
            f"Calculated using the authentic Nirayana Chitrapaksha (Lahiri) Ayanamsha ({meta['ayanamsha']}), "
            f"this assessment uncovers not merely outer planetary geometry, but your hidden psychological matrix, "
            f"authentic passions, public persona versus private reality, and karmic strengths and blindspots."
        ),
        # 1. Psychological Pillars (Dynamic Multi-Factor Chart Synthesis)
        "psychological_profile": psycho_profile,
        # 2. Planetary Yogas
        "yogas": detected_yogas,
        # 3. Dedicated Career, Vocation & Swadharma Blueprint
        "career_blueprint": career_bp,
        # 4. Dedicated Financial Prosperity Strategy & Lakshmi Yoga (Section 2)
        "financial_strategy": fin_bp,
        # 4. Dedicated Current Life Phase & Astrological Timing (Current Dasha)
        "current_life_phase": current_phase_data,
        # 5. Dedicated Sacred Life Timeline & Key Karmic Milestones
        "life_milestones_timeline": milestones_timeline,
        # 3. Dedicated Marriage, Love & Partner Dynamics
        "marriage_blueprint": marriage_bp,
        # 7. Remaining Life Domains
        "domains": [
            {
                "id": "health",
                "title": "1. Physical Energy, Health & Ayurveda Balance (आरोग्य एवं जीवन शक्ति)",
                "icon": "🌿",
                "content": (
                    f"Your physical constitution is governed by the **{lagna['sign_name']} ({lagna.get('sign_sanskrit', '')})** Ascendant ({SIGN_ELEMENTS.get(lagna['sign_id'], ('Fire', ''))[0]} element). "
                    f"When aligned, your vitality is vibrant and resilient. However, chronic stress and mental over-exertion can manifest as sensitivity in bodily heat, digestion, or spinal posture. "
                    f"Incorporate daily grounding rituals: morning sunlight exposure, hydration with copper-infused water, and avoiding erratic eating schedules."
                )
            },
            {
                "id": "spirituality",
                "title": "2. Spiritual Path, Dharma & Higher Wisdom (धर्म, ज्ञान एवं मोक्ष)",
                "icon": "🕉️",
                "content": (
                    f"The 9th House (Dharma) and 12th House (Moksha) indicate a soul that cannot be satisfied by mere materialistic trivialities. "
                    f"You have carried forward deep philosophical impressions (Poorva Samskaras) from past incarnations. "
                    f"Your consciousness expands exponentially through regular meditation, solitude near sacred bodies of water, and selfless service (Nishkama Karma)."
                )
            }
        ],
        "remedies": remedies_summary,
        "signature": {
            "name": "Jyotishacharya Assessment Board",
            "date": datetime.now().strftime("%d %B %Y"),
            "blessing": "॥ ॐ शुभमस्तु • सर्वजन हिताय • सर्वजन सुखाय ॥"
        },
        "legal_disclaimer": (
            "Disclaimer: This report is based purely on astrological interpretations and is intended for informational and guidance purposes only. "
            "Any decisions you make based on this report are entirely your own responsibility. We shall not be held legally liable for any loss, damage, "
            "or consequences arising from decisions made in reliance on the information provided in this report, to the extent permitted by applicable law."
        )
    }
