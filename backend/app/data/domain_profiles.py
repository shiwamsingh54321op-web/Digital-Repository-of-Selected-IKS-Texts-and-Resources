"""
Verified encyclopedic metadata and educational profiles for all 52 Knowledge Domains
(12 primary disciplines and 40 specialized subcategories) in the IKS Digital Repository.

All historical dates, authors, texts, and institutional references are grounded in
established scholarship (INSA, IGNCA, NDLI, BORI, and Ministry of Education IKS Division).
"""

from typing import Dict, Any, List

# Verified institutional reference links reused across domains
REF_MOE_IKS = {"label": "IKS Division, Ministry of Education (Govt. of India)", "url": "https://iksindia.org/"}
REF_NDLI = {"label": "National Digital Library of India (IIT Kharagpur)", "url": "https://ndl.iitkgp.ac.in/"}
REF_IGNCA = {"label": "Indira Gandhi National Centre for the Arts (IGNCA)", "url": "https://ignca.gov.in/"}
REF_INSA = {"label": "Indian National Science Academy (INSA) – History of Science", "url": "https://insaindia.res.in/"}
REF_BORI = {"label": "Bhandarkar Oriental Research Institute (BORI, Pune)", "url": "https://bori.ac.in/"}
REF_ARCHIVE = {"label": "Internet Archive – Digital Manuscript & Indology Collections", "url": "https://archive.org/"}
REF_AAHF = {"label": "Asian Agri-History Foundation (AAHF)", "url": "https://www.asianagrihistory.org/"}
REF_VEDIC_HERITAGE = {"label": "Vedic Heritage Portal (IGNCA)", "url": "https://vedicheritage.gov.in/"}

DOMAIN_PROFILES: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # 1. INDIAN MATHEMATICS (1 + 4 subcategories = 5)
    # =========================================================================
    "indian-mathematics": {
        "sanskrit_name": "Gaṇita (गणित)",
        "introduction": "Indian Mathematics (Gaṇita) encompasses over three millennia of mathematical inquiry, from Vedic altar geometry and the decimal place-value system with zero to medieval algebra, trigonometry, and infinite series.",
        "detailed_explanation": "Unlike purely axiomatic Greek geometry, classical Indian mathematics emphasized constructive algorithms (Kriyā), numerical computation, algebraic problem-solving (Bījagaṇita), and astronomical applications. Treatises were composed in concise Sanskrit verse (Sūtras and Āryā meter) accompanied by detailed prose commentaries (Bhāṣyas) containing worked examples and proofs (Upapatti).",
        "historical_background": "Historical evidence traces geometric constructions to the Śulba Sūtras (c. 800–500 BCE), combinatorics to Piṅgala's Chandaḥśāstra (c. 3rd–2nd century BCE), and positional decimal notation with zero (Śūnya) in epigraphic and textual records by the early centuries CE (Bakhshali manuscript, Āryabhaṭīya 499 CE, Brahmasphuṭasiddhānta 628 CE). Later highlights include Bhāskara II's Līlāvatī (1150 CE) and the Kerala School's power-series expansions (14th–16th century CE).",
        "important_concepts": [
            {"term": "Śūnya (शून्य)", "meaning": "Zero, conceptualized both as a placeholder digit and an independent number with arithmetic rules."},
            {"term": "Daśaguṇottara Saṁjñā", "meaning": "Decimal place-value system based on powers of ten."},
            {"term": "Kuṭṭaka (कुट्टक)", "meaning": "The 'pulverizer' algorithm for solving linear Diophantine equations (ax + c = by)."},
            {"term": "Upapatti (उपपत्ति)", "meaning": "Logical demonstration or proof used in Sanskrit commentaries to validate algorithms."}
        ],
        "major_contributors": [
            {"name": "Baudhāyana & Āpastamba", "era": "c. 800–500 BCE", "contribution": "Geometric altar constructions and rational approximations of √2 in the Śulba Sūtras."},
            {"name": "Āryabhaṭa I", "era": "476–550 CE", "contribution": "Author of Āryabhaṭīya; sine tables (Jya), π ≈ 3.1416, and Kuṭṭaka."},
            {"name": "Brahmagupta", "era": "598–668 CE", "contribution": "Formalized arithmetic rules for zero and negative numbers; cyclic quadrilateral area."},
            {"name": "Bhāskarācārya (Bhāskara II)", "era": "1114–1185 CE", "contribution": "Author of Līlāvatī and Bījagaṇita; early concepts of instantaneous velocity (Tatkalika-gati)."}
        ],
        "important_texts": [
            {"title": "Āryabhaṭīya", "author": "Āryabhaṭa", "period": "499 CE"},
            {"title": "Brahmasphuṭasiddhānta", "author": "Brahmagupta", "period": "628 CE"},
            {"title": "Līlāvatī & Bījagaṇita", "author": "Bhāskara II", "period": "1150 CE"},
            {"title": "Baudhāyana Śulba Sūtra", "author": "Baudhāyana", "period": "c. 800 BCE"}
        ],
        "practical_applications": [
            "Modern computing and base-10 positional arithmetic",
            "Modular arithmetic and cryptography (descended from Kuṭṭaka)",
            "Trigonometric tables for navigation, surveying, and astronomy"
        ],
        "references": [REF_INSA, REF_NDLI, REF_MOE_IKS],
        "linked_resource_ids": [1, 2, 3, 31, 32]
    },
    "number-systems-arithmetic": {
        "sanskrit_name": "Pāṭīgaṇita (पाटीगणित)",
        "introduction": "Pāṭīgaṇita (literally 'board arithmetic', from writing calculations on a dust-covered board) covers the decimal place-value system, zero, fractions, proportions, and commercial computation.",
        "detailed_explanation": "Indian mathematicians developed the nine numerals plus zero (Śūnya) in a base-10 positional system, enabling compact representation of arbitrarily large numbers and efficient written algorithms for addition, subtraction, multiplication, division, square roots, and cube roots.",
        "historical_background": "Decimal number names up to 10^12 appear in Vedic texts like the Yajurveda. By the 5th–7th centuries CE, Āryabhaṭa, Bhāskara I, and Brahmagupta used place-value arithmetic routinely; Śrīdhara's Pāṭīgaṇita (c. 8th–9th century CE) and Bhāskara II's Līlāvatī (1150 CE) standardized algorithmic pedagogy.",
        "important_concepts": [
            {"term": "Sthāna-māna (स्थानमान)", "meaning": "Positional place-value where a digit's value depends on its position."},
            {"term": "Trairāśika (त्रैराशिक)", "meaning": "The 'Rule of Three' for solving proportions."},
            {"term": "Bhinna (भिन्न)", "meaning": "Fractions and rules for simplifying mixed and compound fractions."}
        ],
        "major_contributors": [
            {"name": "Āryabhaṭa", "era": "499 CE", "contribution": "Root extraction algorithms and alphabetical number notation."},
            {"name": "Śrīdharācārya", "era": "c. 750–900 CE", "contribution": "Author of Pāṭīgaṇita and Triśatikā on systematic arithmetic."},
            {"name": "Bhāskara II", "era": "1150 CE", "contribution": "Līlāvatī, the most widely studied Sanskrit arithmetic manual."}
        ],
        "important_texts": [
            {"title": "Līlāvatī", "author": "Bhāskara II", "period": "1150 CE"},
            {"title": "Āryabhaṭīya (Gaṇitapāda)", "author": "Āryabhaṭa", "period": "499 CE"}
        ],
        "practical_applications": [
            "Global Hindu-Arabic numeral system",
            "Interest, partnership, and commercial accounting calculations",
            "Algorithmic mental and written computation methods"
        ],
        "references": [REF_INSA, REF_NDLI],
        "linked_resource_ids": [1, 2, 31]
    },
    "algebra-bijaganita": {
        "sanskrit_name": "Bījagaṇita (बीजगणित)",
        "introduction": "Bījagaṇita ('seed-computation' or symbolic algebra) deals with unknown quantities (Avyakta), linear and quadratic equations, negative numbers, surds, and indeterminate equations.",
        "detailed_explanation": "Indian algebra introduced symbolic abbreviations for unknowns (such as yāvat-tāvat for 'as much as', shortened to yā) and systematic operations on positive (Dhana) and negative (Ṛṇa) numbers as well as irrational square roots (Karaṇī).",
        "historical_background": "Brahmagupta's Brahmasphuṭasiddhānta (628 CE) gave the first general solution to the quadratic equation and linear indeterminate equations, later refined into the Cakravāla ('cyclic') method for Pell-type equations (Nx² + 1 = y²) by Jayadeva (11th century) and Bhāskara II (1150 CE).",
        "important_concepts": [
            {"term": "Avyakta (अव्यक्त)", "meaning": "An unknown variable represented symbolically."},
            {"term": "Dhana & Ṛṇa", "meaning": "Positive (asset) and negative (debt) quantities."},
            {"term": "Cakravāla (चक्रवाल)", "meaning": "Cyclic algorithm for solving quadratic indeterminate equations Nx² + 1 = y²."}
        ],
        "major_contributors": [
            {"name": "Brahmagupta", "era": "628 CE", "contribution": "Algebraic rules for zero, negatives, and Bhāvanā composition law."},
            {"name": "Bhāskara II", "era": "1150 CE", "contribution": "Systematized Bījagaṇita and demonstrated the Cakravāla method."}
        ],
        "important_texts": [
            {"title": "Līlāvatī & Bījagaṇita", "author": "Bhāskara II", "period": "1150 CE"},
            {"title": "Āryabhaṭīya", "author": "Āryabhaṭa", "period": "499 CE"}
        ],
        "practical_applications": [
            "Solving systems of equations and Diophantine problems",
            "Astronomical conjunction and cycle calculations",
            "Foundations of modern symbolic algebra"
        ],
        "references": [REF_INSA, REF_NDLI],
        "linked_resource_ids": [1, 2, 31]
    },
    "geometry-sulba-sutras": {
        "sanskrit_name": "Śulba-śāstra (शुल्वशास्त्र)",
        "introduction": "The Śulba Sūtras ('Rules of the Cord') are the earliest surviving Indian geometric manuals, composed to construct precise geometric fire altars (Vedi and Citi) using measuring cords and pegs.",
        "detailed_explanation": "Attached to the Kalpa Sūtras of the Vedas, these texts present geometric constructions for right angles, squares, rectangles, trapezia, and area-preserving transformations (such as transforming a square into a circle of equal area).",
        "historical_background": "Dated between c. 800 and 500 BCE, the major Śulba Sūtras are attributed to Baudhāyana, Āpastamba, Kātyāyana, and Mānava. Baudhāyana's sutra explicitly states the diagonal property of rectangles (the Pythagorean relation) and gives a remarkably accurate rational approximation for √2 (1 + 1/3 + 1/(3×4) - 1/(3×4×34) ≈ 1.4142156).",
        "important_concepts": [
            {"term": "Rajju / Śulba (रज्जु / शुल्व)", "meaning": "Measuring rope or cord used to lay out geometric figures."},
            {"term": "Akṣṇayā-rajju", "meaning": "Diagonal cord of a rectangle or square."},
            {"term": "Citi (चिति)", "meaning": "Multi-layered brick altar constructed in falcon, chariot, or tortoise shapes of equal area."}
        ],
        "major_contributors": [
            {"name": "Baudhāyana", "era": "c. 800 BCE", "contribution": "Earliest extant Śulba Sūtra; general statement of the diagonal-square theorem and √2 approximation."},
            {"name": "George Thibaut", "era": "1875 CE", "contribution": "First modern critical edition and English translation of Baudhāyana Śulba Sūtra."}
        ],
        "important_texts": [
            {"title": "Baudhāyana Śulba Sūtra", "author": "Baudhāyana", "period": "c. 800 BCE"},
            {"title": "Līlāvatī (Kṣetravyavahāra section)", "author": "Bhāskara II", "period": "1150 CE"}
        ],
        "practical_applications": [
            "Surveying, land mensuration, and civil construction",
            "Geometric transformations and irrational number approximation",
            "Historical pedagogy for constructive geometry"
        ],
        "references": [REF_INSA, REF_ARCHIVE],
        "linked_resource_ids": [3, 2, 31]
    },
    "infinite-series-analysis": {
        "sanskrit_name": "Ananta-śreṇī (अनन्तश्रेणी)",
        "introduction": "Infinite series and early calculus concepts in India reached their zenith in the Kerala School of Astronomy and Mathematics (14th–16th century CE), alongside earlier trigonometric work by Āryabhaṭa and Bhāskara II.",
        "detailed_explanation": "Building on geometric summations and finite differences, Mādhava of Saṅgamagrāma derived infinite power series for π (Gregory-Leibniz series), sine, cosine, and arctangent—centuries before similar developments in Europe—using end-correction terms (Antya-saṁskāra) to accelerate convergence.",
        "historical_background": "While early ideas of instantaneous motion appear in Bhāskara II's Siddhāntaśiromaṇi (1150 CE), Mādhava (c. 1340–1425 CE) and his successors Nīlakaṇṭha Somayājī (Tantrasaṅgraha, 1500 CE) and Jyeṣṭhadeva (Yuktibhāṣā, c. 1530 CE) provided rigorous proofs and rationales.",
        "important_concepts": [
            {"term": "Jya & Kojya (ज्या / कोज्या)", "meaning": "Half-chord (sine) and cosine functions pioneered in Indian trigonometry."},
            {"term": "Antya-saṁskāra", "meaning": "Remainder correction terms used to speed convergence of infinite series for π."},
            {"term": "Tātkālika-gati", "meaning": "Instantaneous planetary velocity analogous to the derivative of sine."}
        ],
        "major_contributors": [
            {"name": "Āryabhaṭa", "era": "499 CE", "contribution": "First sine-difference table and π approximation."},
            {"name": "Mādhava of Saṅgamagrāma", "era": "c. 1340–1425 CE", "contribution": "Power series for sin x, cos x, arctan x, and π."},
            {"name": "Jyeṣṭhadeva", "era": "c. 1530 CE", "contribution": "Yuktibhāṣā, containing complete prose derivations of infinite series."}
        ],
        "important_texts": [
            {"title": "Āryabhaṭīya", "author": "Āryabhaṭa", "period": "499 CE"},
            {"title": "A Concise History of Science in India", "author": "Bose, Sen & Subbarayappa", "period": "1971 CE"}
        ],
        "practical_applications": [
            "High-precision trigonometric tables for astronomy",
            "Numerical approximation of π and transcendental functions",
            "Foundational ideas of integration and series convergence"
        ],
        "references": [REF_INSA, REF_MOE_IKS],
        "linked_resource_ids": [1, 31, 32]
    },

    # =========================================================================
    # 2. ASTRONOMY AND COSMOLOGY (1 + 3 subcategories = 4)
    # =========================================================================
    "astronomy-and-cosmology": {
        "sanskrit_name": "Jyotiṣa (ज्योतिष)",
        "introduction": "Indian Astronomy (Jyotiṣa, literally 'science of luminous bodies') spans Vedic calendrical astronomy, mathematical Siddhāntas, planetary models, eclipse prediction, and monumental masonry observatories.",
        "detailed_explanation": "As one of the six Vedāṅgas ('limbs of the Veda'), Jyotiṣa began with tracking solstices, lunar phases, and the 27/28 Nakṣatras for ritual timing, later evolving into sophisticated trigonometric and epicyclic planetary models in the Siddhānta era.",
        "historical_background": "Lagadha's Vedāṅga Jyotiṣa (c. 1st millennium BCE) codifies a 5-year lunisolar Yuga. From the 5th century CE onward, Āryabhaṭa (499 CE), Varāhamihira, Brahmagupta, and Bhāskara II transformed astronomy into a quantitative mathematical science using spherical trigonometry. In the 18th century, Sawai Jai Singh II built large stone observatories (Jantar Mantar).",
        "important_concepts": [
            {"term": "Nakṣatra (नक्षत्र)", "meaning": "27 (or 28) lunar mansions dividing the ecliptic into ~13°20' segments."},
            {"term": "Tithi (तिथि)", "meaning": "Lunar day defined by a 12° elongation between Moon and Sun."},
            {"term": "Graha-gaṇita", "meaning": "Mathematical computation of true planetary longitudes and eclipses."}
        ],
        "major_contributors": [
            {"name": "Lagadha", "era": "c. 1st millennium BCE", "contribution": "Author of Vedāṅga Jyotiṣa, earliest extant Indian astronomical manual."},
            {"name": "Āryabhaṭa", "era": "499 CE", "contribution": "Proposed Earth's axial rotation and scientific explanation of solar/lunar eclipses."},
            {"name": "Sawai Jai Singh II", "era": "1688–1743 CE", "contribution": "Built the Jantar Mantar observatories in Delhi, Jaipur, Ujjain, and Varanasi."}
        ],
        "important_texts": [
            {"title": "Sūrya Siddhānta", "author": "Traditional / Siddhāntic school", "period": "c. 4th–10th century CE"},
            {"title": "Vedāṅga Jyotiṣa", "author": "Lagadha", "period": "c. 1st millennium BCE"},
            {"title": "Āryabhaṭīya (Golapāda & Kālakriyā)", "author": "Āryabhaṭa", "period": "499 CE"}
        ],
        "practical_applications": [
            "Lunisolar calendrics (Pañcāṅga) and festival/agricultural timing",
            "Eclipse prediction and celestial timekeeping",
            "Spherical trigonometry and orbital calculation"
        ],
        "references": [REF_INSA, REF_NDLI, REF_MOE_IKS],
        "linked_resource_ids": [4, 5, 1, 31]
    },
    "siddhantic-astronomy": {
        "sanskrit_name": "Siddhānta-jyotiṣa (सिद्धान्तज्योतिष)",
        "introduction": "Siddhāntic Astronomy represents the mathematical golden age of Indian astronomy, employing epicycles, eccentric circles, and trigonometry to model planetary motion and eclipses.",
        "detailed_explanation": "A 'Siddhānta' ('established conclusion') begins with cosmic cycles (Mahāyuga / Kalpa), derives mean planetary motions, applies corrections (Equation of Center / Manda-saṁskāra and Śīghra-saṁskāra), and computes eclipses and planetary conjunctions.",
        "historical_background": "Key treatises include the Sūrya Siddhānta (preserved in its classical form c. 4th–10th century CE), Āryabhaṭa's Āryabhaṭīya (499 CE), Varāhamihira's Pañcasiddhāntikā (6th century CE), and Brahmagupta's Brahmasphuṭasiddhānta (628 CE).",
        "important_concepts": [
            {"term": "Manda & Śīghra", "meaning": "Apogee (equation of center) and conjunction (annual parallax) epicyclic corrections."},
            {"term": "Rāhu-Ketu (lunar nodes)", "meaning": "Ascending and descending nodes where the Moon's orbit intersects the ecliptic, causing eclipses."},
            {"term": "Ahargaṇa (अहर्गण)", "meaning": "Count of elapsed civil days since an astronomical epoch."}
        ],
        "major_contributors": [
            {"name": "Āryabhaṭa", "era": "499 CE", "contribution": "Explained eclipses via Earth's and Moon's shadows and Earth's daily rotation."},
            {"name": "Ebenezer Burgess & W. D. Whitney", "era": "1860 CE", "contribution": "Landmark English translation and mathematical commentary on Sūrya Siddhānta."}
        ],
        "important_texts": [
            {"title": "Sūrya Siddhānta", "author": "Burgess & Whitney (Trans.)", "period": "1860 CE edition"},
            {"title": "Āryabhaṭīya", "author": "Āryabhaṭa", "period": "499 CE"}
        ],
        "practical_applications": [
            "Computing planetary ephemerides and eclipse circumstances",
            "Determining local latitude, meridian, and solar declination"
        ],
        "references": [REF_INSA, REF_ARCHIVE],
        "linked_resource_ids": [4, 1, 31]
    },
    "observational-instruments": {
        "sanskrit_name": "Yantra-vidyā (यन्त्रविद्या)",
        "introduction": "Observational Instruments (Yantras) in Indian astronomy range from portable gnomons, water clocks, and armillary spheres to monumental masonry sundials.",
        "detailed_explanation": "Classical texts describe the Śaṅku (gnomon), Ghaṭikā-yantra (sinking-bowl water clock), Cakra-yantra (graduated wheel), Phalaka-yantra (astrolabe-like board), and Golayantra (armillary sphere). These culminated in Sawai Jai Singh II's masonry instruments.",
        "historical_background": "Detailed chapters on Yantras appear in the Sūrya Siddhānta, Brahmagupta's Brahmasphuṭasiddhānta, Bhāskara II's Siddhāntaśiromaṇi, and Mahendra Sūri's Yantrarāja (1370 CE). Between 1724 and 1734 CE, Sawai Jai Singh II built five Jantar Mantar observatories, including Jaipur's Samrāṭ Yantra.",
        "important_concepts": [
            {"term": "Śaṅku (शङ्कु)", "meaning": "Vertical gnomon stick used to measure solar shadow length and cardinal directions."},
            {"term": "Ghaṭikā (घटिका)", "meaning": "24-minute time unit measured by a perforated copper bowl sinking in water."},
            {"term": "Samrāṭ Yantra", "meaning": "Equinoctial sundial with a 27-meter gnomon aligned to Earth's axis, accurate to ~2 seconds."}
        ],
        "major_contributors": [
            {"name": "Bhāskara II", "era": "12th century CE", "contribution": "Described the Phalaka-yantra and Yaṣṭi-yantra in Yantrādhyāya."},
            {"name": "Sawai Jai Singh II", "era": "18th century CE", "contribution": "Designed large-scale masonry astronomical instruments at Jaipur and Delhi."}
        ],
        "important_texts": [
            {"title": "Sūrya Siddhānta (Chapter XIII: Armillary & Instruments)", "author": "Burgess (Trans.)", "period": "Classical / 1860 CE"},
            {"title": "A Concise History of Science in India", "author": "Bose, Sen & Subbarayappa", "period": "1971 CE"}
        ],
        "practical_applications": [
            "Solar timekeeping and meridian determination",
            "Measuring celestial altitude, azimuth, and declination"
        ],
        "references": [REF_INSA, REF_NDLI],
        "linked_resource_ids": [4, 31]
    },
    "calendrical-systems": {
        "sanskrit_name": "Pañcāṅga & Kālagaṇanā (पञ्चाङ्ग)",
        "introduction": "Indian Calendrical Systems harmonize lunar months with the solar year through the Pañcāṅga ('five limbs': Tithi, Vāra, Nakṣatra, Yoga, and Karaṇa).",
        "detailed_explanation": "Because 12 lunar synodic months (~354.37 days) fall ~10.87 days short of a solar year (~365.24 days), Indian calendars insert an intercalary month (Adhika-māsa) roughly every 32.5 months to keep seasons and festivals aligned.",
        "historical_background": "Lagadha's Vedāṅga Jyotiṣa (c. 1st millennium BCE) established the 5-year Yuga with 62 lunar months and 2 intercalary months. Subsequent Siddhāntic reforms aligned the Saka (78 CE) and Vikrama (57 BCE) eras with astronomical observations.",
        "important_concepts": [
            {"term": "Pañcāṅga (पञ्चाङ्ग)", "meaning": "Traditional almanac tracking five daily astronomical elements."},
            {"term": "Adhika-māsa (अधिकमास)", "meaning": "Intercalary ('extra') lunar month synchronizing lunar and solar years."},
            {"term": "Uttarayana & Dakṣiṇāyana", "meaning": "Northward (winter-to-summer solstice) and southward solar courses."}
        ],
        "major_contributors": [
            {"name": "Lagadha", "era": "c. 1st millennium BCE", "contribution": "Codified the earliest mathematical lunisolar calendar in Vedāṅga Jyotiṣa."},
            {"name": "T. S. Kuppanna Sastry & K. V. Sarma", "era": "20th century CE", "contribution": "Critical modern edition and translation of Vedāṅga Jyotiṣa."}
        ],
        "important_texts": [
            {"title": "Vedāṅga Jyotiṣa of Lagadha", "author": "Lagadha (Ed. Sastry & Sarma)", "period": "Ancient / 1985 CE"},
            {"title": "Sūrya Siddhānta", "author": "Classical Tradition", "period": "Classical"}
        ],
        "practical_applications": [
            "Indian National Calendar (Saka) and regional agricultural almanacs",
            "Predicting monsoon onset windows and seasonal cycles"
        ],
        "references": [REF_INSA, REF_MOE_IKS],
        "linked_resource_ids": [5, 4, 31]
    },

    # =========================================================================
    # 3. AYURVEDA AND TRADITIONAL MEDICINE (1 + 4 subcategories = 5)
    # =========================================================================
    "ayurveda-and-traditional-medicine": {
        "sanskrit_name": "Āyurveda (आयुर्वेद)",
        "introduction": "Āyurveda ('Science of Life') is India's classical medical system integrating anatomy, pathology, pharmacology, surgery, dietetics, and preventive hygiene.",
        "detailed_explanation": "Organized traditionally into eight clinical branches (Aṣṭāṅga Āyurveda), it views health (Svāsthya) as the dynamic equilibrium of three physiological principles (Vāta, Pitta, Kapha), seven bodily tissues (Dhātus), digestive fire (Agni), and mental clarity.",
        "historical_background": "Rooted in the Atharvaveda's healing traditions, Āyurveda was systematized in the Bṛhat-trayī ('Great Trio'): Caraka Saṁhitā (internal medicine, c. 1st–2nd century CE redaction of Agniveśa), Suśruta Saṁhitā (surgery, c. early centuries CE), and Vāgbhaṭa's Aṣṭāṅga Hṛdaya (c. 6th–7th century CE).",
        "important_concepts": [
            {"term": "Tridoṣa (त्रिदोष)", "meaning": "Vāta (motion/nervous regulation), Pitta (metabolism/heat), and Kapha (structure/cohesion)."},
            {"term": "Prakṛti (प्रकृति)", "meaning": "Individual psychosomatic constitution guiding personalized diet and therapy."},
            {"term": "Aṣṭāṅga Āyurveda", "meaning": "Eight classical medical specialties including internal medicine (Kāyacikitsā) and surgery (Śalya)."}
        ],
        "major_contributors": [
            {"name": "Agniveśa & Caraka", "era": "c. 2nd century BCE – 2nd century CE", "contribution": "Foundational compendium on internal medicine, diagnostics, and medical ethics."},
            {"name": "Suśruta", "era": "c. early centuries CE", "contribution": "Pioneer of surgical instrumentation, rhinoplasty, and cataract couching."}
        ],
        "important_texts": [
            {"title": "Caraka Saṁhitā", "author": "Agniveśa / Caraka / Dṛḍhabala", "period": "Classical"},
            {"title": "Suśruta Saṁhitā", "author": "Suśruta", "period": "Classical"}
        ],
        "practical_applications": [
            "Preventive lifestyle medicine and seasonal dietetics",
            "Phytopharmacology and integrative clinical care",
            "Reconstructive surgical history"
        ],
        "references": [REF_NDLI, REF_MOE_IKS, REF_INSA],
        "linked_resource_ids": [6, 7, 31, 32]
    },
    "classical-samhitas": {
        "sanskrit_name": "Bṛhat-trayī (बृहत्त्रयी)",
        "introduction": "The Classical Saṁhitās form the foundational canon of Āyurveda, preserving comprehensive treatises on clinical diagnosis, therapeutics, ethics, and surgery.",
        "detailed_explanation": "These encyclopedic Sanskrit texts combine prose and verse across structured sections (Sthānas) covering basic principles (Sūtrasthāna), pathology (Nidānasthāna), anatomy (Śārīrasthāna), therapeutics (Cikitsāsthāna), and pharmaceutics (Kalpasthāna).",
        "historical_background": "The Caraka Saṁhitā was redacted by Caraka and completed by Dṛḍhabala (Kashmir, c. 4th–5th century CE), while the Suśruta Saṁhitā was redacted by Nāgārjuna. Critical editions by Vaidya Jadavji Trikamji Acharya and translations by K. L. Bhishagratna made them accessible worldwide.",
        "important_concepts": [
            {"term": "Sūtrasthāna", "meaning": "Opening section of a Saṁhitā laying out core medical axioms and ethics."},
            {"term": "Nidāna-pañcaka", "meaning": "Five-fold diagnostic framework from etiology to prognosis."}
        ],
        "major_contributors": [
            {"name": "Caraka & Dṛḍhabala", "era": "Classical", "contribution": "Authored and completed the Caraka Saṁhitā."},
            {"name": "Vaidya Jadavji Trikamji Acharya", "era": "20th century CE", "contribution": "Standard critical Sanskrit edition of Caraka Saṁhitā."}
        ],
        "important_texts": [
            {"title": "The Charaka-Samhita of Agnivesha", "author": "Charaka (Ed. J.T. Acharya)", "period": "Classical"},
            {"title": "The Sushruta Samhita", "author": "Sushruta (Trans. Bhishagratna)", "period": "Classical"}
        ],
        "practical_applications": [
            "Standard curriculum in BAMS (Āyurveda) medical education",
            "Clinical reference for classical formulations and medical ethics"
        ],
        "references": [REF_NDLI, REF_ARCHIVE],
        "linked_resource_ids": [6, 7]
    },
    "dravyaguna-medicinal-plants": {
        "sanskrit_name": "Dravyaguṇa (द्रव्यगुण)",
        "introduction": "Dravyaguṇa is the Ayurvedic science of materia medica and pharmacology—studying medicinal plants, minerals, their taste (Rasa), potency (Vīrya), and post-digestive effect (Vipāka).",
        "detailed_explanation": "Rather than isolating single synthetic molecules, Dravyaguṇa classifies over 700 botanicals by their systemic physiological actions, ecological habitat, harvesting season, and synergistic combinations.",
        "historical_background": "Both the Caraka Saṁhitā (mentioning ~600 plant-based drugs) and Suśruta Saṁhitā (~700 plants in 37 Gaṇas) systematically categorize medicinal flora, later expanded in medieval Nighaṇṭus (lexicons) such as Bhāvaprakāśa Nighaṇṭu.",
        "important_concepts": [
            {"term": "Rasa (रस)", "meaning": "Six tastes (sweet, sour, salty, pungent, bitter, astringent) predicting physiological action."},
            {"term": "Vīrya & Vipāka", "meaning": "Thermal potency (heating/cooling) and post-digestive metabolic transformation."}
        ],
        "major_contributors": [
            {"name": "Caraka & Suśruta", "era": "Classical", "contribution": "Systematized hundreds of botanicals into therapeutic groups (Mahākaṣāya and Gaṇa)."},
            {"name": "Surapala", "era": "c. 1000 CE", "contribution": "Documented plant health, grafting, and botanical care in Vṛkṣāyurveda."}
        ],
        "important_texts": [
            {"title": "The Charaka-Samhita (Sūtrasthāna Ch. 4 & 27)", "author": "Charaka", "period": "Classical"},
            {"title": "Vrikshayurveda", "author": "Surapala", "period": "c. 1000 CE"}
        ],
        "practical_applications": [
            "Ethnobotanical drug discovery and herbal pharmacopeia",
            "Sustainable cultivation of medicinal flora"
        ],
        "references": [REF_INSA, REF_NDLI],
        "linked_resource_ids": [6, 7, 8]
    },
    "surgery-shalya-tantra": {
        "sanskrit_name": "Śalya-tantra (शल्यतन्त्र)",
        "introduction": "Śalya-tantra is the ancient Indian surgical tradition codified in the Suśruta Saṁhitā, renowned for its systematic classification of surgical instruments and reconstructive procedures.",
        "detailed_explanation": "Suśruta describes 101 blunt instruments (Yantras), 20 sharp instruments (Śastras), eight fundamental surgical techniques (excision, incision, scraping, probing, extraction, suturing, etc.), pre-operative preparation, and anatomical dissection.",
        "historical_background": "The Suśruta Saṁhitā documents pedicle-flap rhinoplasty (reconstructive nasal surgery), cataract couching, lithotomy (bladder stone removal), fracture setting, and the use of non-absorbable sutures and ants' heads for intestinal anastomosis.",
        "important_concepts": [
            {"term": "Yantra & Śastra", "meaning": "Blunt surgical forceps/specula (101 types) and sharp scalpels/needles (20 types)."},
            {"term": "Aṣṭavidha Śastrakarma", "meaning": "Eight canonical surgical procedures (Chedya, Bhedya, Lekhya, Vedhya, Eṣya, Āhārya, Viśrāvya, Sīvya)."}
        ],
        "major_contributors": [
            {"name": "Suśruta", "era": "c. early centuries CE", "contribution": "Authored Suśruta Saṁhitā, earning recognition as a pioneer of plastic and ophthalmic surgery."}
        ],
        "important_texts": [
            {"title": "An English Translation of the Sushruta Samhita", "author": "Sushruta (Trans. K. L. Bhishagratna)", "period": "Classical / 1907 CE"}
        ],
        "practical_applications": [
            "Foundations of reconstructive flap surgery (Indian forehead flap rhinoplasty)",
            "History of surgical sterilization, suturing, and anatomical pedagogy"
        ],
        "references": [REF_INSA, REF_ARCHIVE],
        "linked_resource_ids": [7, 31]
    },
    "preventive-health": {
        "sanskrit_name": "Svasthavṛtta (स्वस्थवृत्त)",
        "introduction": "Svasthavṛtta focuses on preventive healthcare, daily hygiene (Dinacaryā), seasonal regimens (Ṛtucaryā), sleep, exercise, and mental equilibrium.",
        "detailed_explanation": "Rather than treating disease only after onset, Āyurveda prescribes individualized routines aligned with circadian and seasonal rhythms, alongside Rasāyana (rejuvenation) and Ācāra Rasāyana (ethical social conduct).",
        "historical_background": "Chapters 5–8 of the Caraka Saṁhitā Sūtrasthāna provide one of the world's earliest detailed manuals on preventive public and personal health, emphasizing clean water, balanced nutrition, and moderation.",
        "important_concepts": [
            {"term": "Dinacaryā (दिनचर्या)", "meaning": "Daily regimen aligned with biological/circadian rhythms."},
            {"term": "Ṛtucaryā (ऋतुचर्या)", "meaning": "Seasonal adaptation of diet and activity across India's six seasons."}
        ],
        "major_contributors": [
            {"name": "Caraka", "era": "Classical", "contribution": "Codified Dinacaryā, Ṛtucaryā, and Sadvṛtta (ethical conduct) in Caraka Saṁhitā."},
            {"name": "Patañjali", "era": "c. 2nd century BCE – 4th century CE", "contribution": "Integrated breath regulation (Prāṇāyāma) and ethical discipline (Yama-Niyama)."}
        ],
        "important_texts": [
            {"title": "The Charaka-Samhita", "author": "Charaka", "period": "Classical"},
            {"title": "The Yoga-System of Patanjali", "author": "Patanjali", "period": "Classical"}
        ],
        "practical_applications": [
            "Circadian wellness and lifestyle disease prevention",
            "Integrative stress management and nutrition"
        ],
        "references": [REF_MOE_IKS, REF_NDLI],
        "linked_resource_ids": [6, 9]
    },

    # =========================================================================
    # 4. YOGA AND PHILOSOPHY (1 + 4 subcategories = 5)
    # =========================================================================
    "yoga-and-philosophy": {
        "sanskrit_name": "Darśana & Yoga (दर्शन)",
        "introduction": "Indian Philosophy (Darśana, 'vision of truth') encompasses the six orthodox (Āstika) schools—Sāṁkhya, Yoga, Nyāya, Vaiśeṣika, Mīmāṁsā, and Vedānta—alongside Jain, Buddhist, and Cārvāka traditions.",
        "detailed_explanation": "Each Darśana examines epistemology (Pramāṇa — valid means of knowledge such as perception, inference, and testimony), metaphysics, causality, ethics, and liberation (Mokṣa/Kaivalya) through rigorous logical debate.",
        "historical_background": "Emerging from Upaniṣadic inquiry (c. 800–400 BCE), philosophical systems were codified into concise Sūtras between c. 400 BCE and 400 CE (e.g., Patañjali's Yoga Sūtras, Īśvarakṛṣṇa's Sāṁkhya Kārikā), followed by centuries of commentary by Vyāsa, Śaṅkara, Vācaspati Miśra, and Rāmānuja.",
        "important_concepts": [
            {"term": "Pramāṇa (प्रमाण)", "meaning": "Valid means of acquiring true knowledge (Pratyakṣa, Anumāna, Śabda)."},
            {"term": "Puruṣa & Prakṛti", "meaning": "Pure conscious awareness and dynamic primordial nature in Sāṁkhya-Yoga."}
        ],
        "major_contributors": [
            {"name": "Patañjali", "era": "c. 2nd century BCE – 4th century CE", "contribution": "Systematized Aṣṭāṅga Yoga in 195 aphorisms."},
            {"name": "Īśvarakṛṣṇa", "era": "c. 4th century CE", "contribution": "Authored Sāṁkhya Kārikā, the foundational text of classical Sāṁkhya."}
        ],
        "important_texts": [
            {"title": "Yoga Sūtras of Patañjali", "author": "Patañjali (Trans. J. H. Woods)", "period": "Classical / 1914 CE"},
            {"title": "Sāṁkhya Kārikā", "author": "Īśvarakṛṣṇa (Trans. Colebrooke & Wilson)", "period": "c. 4th century CE"}
        ],
        "practical_applications": [
            "Mindfulness, mental health, and cognitive focus",
            "Formal Indian logic and debate methodology (Vāda)"
        ],
        "references": [REF_IGNCA, REF_NDLI, REF_ARCHIVE],
        "linked_resource_ids": [9, 10, 30, 32]
    },
    "classical-yoga": {
        "sanskrit_name": "Aṣṭāṅga Yoga (अष्टाङ्गयोग)",
        "introduction": "Classical Yoga (Rāja Yoga) as codified by Patañjali defines yoga as the intentional calming of the fluctuations of the mind (Yogaś citta-vṛtti-nirodhaḥ).",
        "detailed_explanation": "Patañjali's eight-limbed path (Aṣṭāṅga) progresses from ethical restraints (Yama) and personal observances (Niyama) through posture (Āsana), breath regulation (Prāṇāyāma), sensory withdrawal (Pratyāhāra), concentration (Dhāraṇā), meditation (Dhyāna), and absorption (Samādhi).",
        "historical_background": "Compiled in the Yoga Sūtras with the authoritative commentary (Bhāṣya) of Vyāsa and later sub-commentary (Tattvavaiśāradī) of Vācaspati Miśra (9th century CE), translated critically in James Haughton Woods' Harvard Oriental Series volume (1914).",
        "important_concepts": [
            {"term": "Citta-vṛtti-nirodha", "meaning": "Stillness of mental modifications leading to clarity of awareness."},
            {"term": "Yama & Niyama", "meaning": "Ethical foundations (non-violence, truthfulness, contentment, self-study)."}
        ],
        "major_contributors": [
            {"name": "Patañjali", "era": "Classical", "contribution": "Composed the 195 Yoga Sūtras."},
            {"name": "Vyāsa & Vācaspati Miśra", "era": "c. 5th–9th century CE", "contribution": "Standard commentaries on Yoga psychology and practice."}
        ],
        "important_texts": [
            {"title": "The Yoga-System of Patanjali", "author": "Patanjali (Trans. J. H. Woods)", "period": "1914 CE"}
        ],
        "practical_applications": [
            "Global physical and mental wellness practices",
            "Attention regulation, breathwork, and stress reduction"
        ],
        "references": [REF_ARCHIVE, REF_MOE_IKS],
        "linked_resource_ids": [9, 32]
    },
    "samkhya-cosmology": {
        "sanskrit_name": "Sāṁkhya (सांख्य)",
        "introduction": "Sāṁkhya is one of India's oldest rationalist philosophical systems, analyzing all existence through 25 evolutionary principles (Tattvas) emerging from Puruṣa and Prakṛti.",
        "detailed_explanation": "Sāṁkhya explains natural transformation via three constituent qualities (Guṇas): Sattva (luminosity/harmony), Rajas (activity/energy), and Tamas (inertia/mass), and introduces Satkāryavāda—the doctrine that an effect pre-exists in potential form within its material cause.",
        "historical_background": "Traditionally attributed to sage Kapila, Sāṁkhya's earliest complete surviving manual is Īśvarakṛṣṇa's Sāṁkhya Kārikā (72 verses, c. 4th century CE), accompanied by Gauḍapāda's and Vācaspati Miśra's commentaries.",
        "important_concepts": [
            {"term": "Triguṇa (त्रिगुण)", "meaning": "Sattva, Rajas, and Tamas—the three dynamic strands of nature."},
            {"term": "Satkāryavāda", "meaning": "Theory of causation holding that effects pre-exist within their material cause."}
        ],
        "major_contributors": [
            {"name": "Īśvarakṛṣṇa", "era": "c. 4th century CE", "contribution": "Authored Sāṁkhya Kārikā."},
            {"name": "H. T. Colebrooke & H. H. Wilson", "era": "1837 CE", "contribution": "Classical English translation and commentary."}
        ],
        "important_texts": [
            {"title": "The Sankhya Karika", "author": "Ishvarakrishna (Trans. Colebrooke & Wilson)", "period": "c. 4th century CE / 1837 CE"}
        ],
        "practical_applications": [
            "Theoretical foundation of Āyurveda and Classical Yoga",
            "Philosophical models of consciousness and natural evolution"
        ],
        "references": [REF_ARCHIVE, REF_IGNCA],
        "linked_resource_ids": [10, 9]
    },
    "nyaya-vaisheshika": {
        "sanskrit_name": "Nyāya-Vaiśeṣika (न्याय-वैशेषिक)",
        "introduction": "Nyāya (logic and epistemology) and Vaiśeṣika (atomistic natural philosophy) form twin realist schools analyzing valid reasoning, debate, and physical categories.",
        "detailed_explanation": "Nyāya formalizes a 5-step syllogism (Pañcāvayava) and rules for valid inference (Anumāna) and fallacies (Hetvābhāsa), while Vaiśeṣika classifies reality into six/seven categories (Padārthas) and proposes indivisible atoms (Paramāṇu).",
        "historical_background": "Founded by Gautama (Nyāya Sūtras) and Kaṇāda (Vaiśeṣika Sūtras, c. 2nd century BCE – 2nd century CE), these schools merged into a unified syncretic tradition (Navya-Nyāya) in medieval Mithila and Navadvipa.",
        "important_concepts": [
            {"term": "Anumāna (अनुमान)", "meaning": "Logical inference grounded in invariable concomitance (Vyāpti)."},
            {"term": "Paramāṇu (परमाणु)", "meaning": "Indivisible elementary particles combining to form macroscopic matter."}
        ],
        "major_contributors": [
            {"name": "Gautama & Kaṇāda", "era": "Ancient", "contribution": "Founders of Nyāya logic and Vaiśeṣika atomism."},
            {"name": "D. M. Bose, S. N. Sen & B. V. Subbarayappa", "era": "1971 CE", "contribution": "Documented Vaiśeṣika physical theories in A Concise History of Science in India."}
        ],
        "important_texts": [
            {"title": "A Concise History of Science in India", "author": "Bose, Sen & Subbarayappa", "period": "1971 CE"},
            {"title": "Selected Readings in Indian Knowledge Systems", "author": "IKS Division, Ministry of Education", "period": "2023 CE"}
        ],
        "practical_applications": [
            "Formal argumentation, legal reasoning, and scientific method",
            "Early atomic and physical classification frameworks"
        ],
        "references": [REF_INSA, REF_MOE_IKS],
        "linked_resource_ids": [31, 32]
    },
    "vedanta-metaphysics": {
        "sanskrit_name": "Vedānta (वेदान्त)",
        "introduction": "Vedānta ('End/Culmination of the Vedas') investigates the relationship between ultimate reality (Brahman), the individual self (Ātman), and the phenomenal universe.",
        "detailed_explanation": "Grounded in the Prasthāna-trayī (Upaniṣads, Bhagavad Gītā, and Brahma Sūtras), Vedānta branched into Advaita (non-dualism, Śaṅkara), Viśiṣṭādvaita (qualified non-dualism, Rāmānuja), and Dvaita (dualism, Madhva).",
        "historical_background": "Emerging from the Upaniṣads (c. 800–400 BCE) and Bādarāyaṇa's Brahma Sūtras, Vedānta deeply influenced linguistics (Bhartṛhari's Śabda-advaita in Vākyapadīya) and modern Indian philosophical thought.",
        "important_concepts": [
            {"term": "Brahman & Ātman", "meaning": "Absolute reality and the innermost conscious self."},
            {"term": "Prasthāna-trayī", "meaning": "Three canonical pillars of Vedānta: Upaniṣads, Bhagavad Gītā, and Brahma Sūtras."}
        ],
        "major_contributors": [
            {"name": "Bhartṛhari", "era": "c. 5th century CE", "contribution": "Developed linguistic non-dualism (Śabda-brahman) in Vākyapadīya."},
            {"name": "Sāyaṇācārya", "era": "14th century CE", "contribution": "Monumental Vedic commentary preserving traditional Vedāntic exegesis."}
        ],
        "important_texts": [
            {"title": "The Vakyapadiya of Bhartrihari", "author": "Bhartrihari", "period": "c. 5th century CE"},
            {"title": "Selected Readings in Indian Knowledge Systems", "author": "IKS Division, Ministry of Education", "period": "2023 CE"}
        ],
        "practical_applications": [
            "Comparative metaphysics and philosophy of consciousness",
            "Ethical humanism and environmental interconnectedness"
        ],
        "references": [REF_IGNCA, REF_MOE_IKS],
        "linked_resource_ids": [30, 32, 11]
    },

    # =========================================================================
    # 5. VEDIC LITERATURE (1 + 4 subcategories = 5)
    # =========================================================================
    "vedic-literature": {
        "sanskrit_name": "Veda-vāṅmaya (वेदवाङ्मय)",
        "introduction": "Vedic Literature comprises the four Saṁhitās—Ṛgveda, Sāmaveda, Yajurveda, and Atharvaveda—along with their Brāhmaṇas, Āraṇyakas, and Upaniṣads, preserved through UNESCO-recognized oral recitation traditions.",
        "detailed_explanation": "Transmitted with extraordinary phonetic accuracy via eleven recitation modes (Pāṭhas such as Pada-pāṭha, Krama-pāṭha, and Ghana-pāṭha), Vedic texts preserve hymns, cosmology, music, ritual geometry, and early medicine.",
        "historical_background": "Composed in Vedic Sanskrit during the 2nd–1st millennium BCE, the Vedic corpus was documented in manuscripts and commented upon extensively by Sāyaṇācārya (14th century CE) and edited in critical modern editions in the 19th–20th centuries.",
        "important_concepts": [
            {"term": "Śruti (श्रुति)", "meaning": "Canonical Vedic texts 'heard' and transmitted orally across generations."},
            {"term": "Ṛta (ऋत)", "meaning": "Cosmic, natural, and moral order governing the universe."}
        ],
        "major_contributors": [
            {"name": "Sāyaṇācārya", "era": "14th century CE", "contribution": "Comprehensive Sanskrit commentary on all four Vedas."},
            {"name": "F. Max Müller & W. D. Whitney", "era": "19th–20th century CE", "contribution": "Critical editions and translations of the Ṛgveda and Atharvaveda."}
        ],
        "important_texts": [
            {"title": "Rig-Veda-Sanhita", "author": "Ed. F. Max Müller / Comm. Sāyaṇa", "period": "Ancient / 1890 CE"},
            {"title": "The Hymns of the Samaveda", "author": "Trans. R. T. H. Griffith", "period": "Ancient / 1893 CE"},
            {"title": "White Yajurveda (Vājasaneyi Saṁhitā)", "author": "Trans. R. T. H. Griffith", "period": "Ancient / 1899 CE"},
            {"title": "Atharva-Veda Samhita", "author": "Trans. W. D. Whitney & C. R. Lanman", "period": "Ancient / 1905 CE"}
        ],
        "practical_applications": [
            "Comparative Indo-European philology and historical linguistics",
            "UNESCO Intangible Cultural Heritage oral-memory preservation"
        ],
        "references": [REF_VEDIC_HERITAGE, REF_IGNCA, REF_BORI],
        "linked_resource_ids": [11, 12, 13, 14]
    },
    "rigveda-traditions": {
        "sanskrit_name": "Ṛgveda (ऋग्वेद)",
        "introduction": "The Ṛgveda is the oldest extant Vedic Saṁhitā, consisting of 1,028 hymns (Sūktas) and 10,552 verses organized into ten books (Maṇḍalas).",
        "detailed_explanation": "Composed in metrical Vedic Sanskrit (Gāyatrī, Triṣṭubh, Jagatī), the hymns explore cosmology (Nāsadīya Sūkta), natural forces, ethics, and early astronomical and poetic imagery.",
        "historical_background": "Preserved in the Śākala recension with Sāyaṇācārya's 14th-century Bhāṣya, and critically edited by F. Max Müller (1849–1874; 2nd ed. 1890–1892).",
        "important_concepts": [
            {"term": "Maṇḍala & Sūkta", "meaning": "Ten structural book divisions containing hymns composed by Ṛṣi families."},
            {"term": "Pada-pāṭha", "meaning": "Word-by-word recitation method preventing textual corruption."}
        ],
        "major_contributors": [
            {"name": "Sāyaṇācārya", "era": "14th century CE", "contribution": "Authoritative grammatical and ritual commentary on the Ṛgveda."},
            {"name": "F. Max Müller", "era": "1890 CE", "contribution": "Critical edition of the Ṛgveda Saṁhitā with Sāyaṇa's commentary."}
        ],
        "important_texts": [
            {"title": "Rig-Veda-Sanhita: The Sacred Hymns of the Brahmans", "author": "F. Max Müller & Sāyaṇācārya", "period": "1890 CE"}
        ],
        "practical_applications": [
            "Foundational source for Sanskrit grammar and Indo-European linguistics",
            "Study of early Indian cosmology and poetic meters"
        ],
        "references": [REF_VEDIC_HERITAGE, REF_BORI],
        "linked_resource_ids": [11]
    },
    "samaveda-traditions": {
        "sanskrit_name": "Sāmaveda (सामवेद)",
        "introduction": "The Sāmaveda ('Veda of Melodies') sets Vedic verses—mostly drawn from the Ṛgveda—to musical chants (Sāman), forming the earliest documented foundation of Indian classical music.",
        "detailed_explanation": "It contains the Ārcika (verse collections) and Gāna (melodic notation manuals) using a seven-note scale (Svara) and rhythmic phrasing.",
        "historical_background": "Preserved primarily in the Kauthuma, Rāṇāyanīya, and Jaiminīya Śākhās, the Sāmaveda directly inspired later Nāṭyaśāstra and Saṅgīta treatises.",
        "important_concepts": [
            {"term": "Sāman (सामन्)", "meaning": "Chanted melody applied to a Ṛgvedic verse."},
            {"term": "Saptasvara", "meaning": "Seven-note tonal framework underlying Indian music."}
        ],
        "major_contributors": [
            {"name": "Ralph T. H. Griffith", "era": "1893 CE", "contribution": "Complete English translation of the Kauthuma Sāmaveda."}
        ],
        "important_texts": [
            {"title": "The Hymns of the Samaveda", "author": "R. T. H. Griffith", "period": "1893 CE"},
            {"title": "Sangitaratnakara", "author": "Śārṅgadeva", "period": "13th century CE"}
        ],
        "practical_applications": [
            "Historical origin of Hindustani and Carnatic rāga/svara traditions",
            "Acoustic and prosodic studies of Vedic chant"
        ],
        "references": [REF_VEDIC_HERITAGE, REF_IGNCA],
        "linked_resource_ids": [12, 25]
    },
    "yajurveda-traditions": {
        "sanskrit_name": "Yajurveda (यजुर्वेद)",
        "introduction": "The Yajurveda ('Veda of Ritual Formulas') preserves prose mantras (Yajus) and verses detailing Vedic liturgical procedures, altar geometry, and social ethics.",
        "detailed_explanation": "Transmitted in two major branches—Śukla (White, e.g., Vājasaneyi Saṁhitā) and Kṛṣṇa (Black, e.g., Taittirīya Saṁhitā)—it provides the ritual context out of which the Śulba Sūtra geometry developed.",
        "historical_background": "The Śukla Yajurveda (Mādhyandina and Kāṇva recensions) separates mantras from prose Brāhmaṇa explanations (Śatapatha Brāhmaṇa) and ends with the Īśāvāsya Upaniṣad.",
        "important_concepts": [
            {"term": "Śukla & Kṛṣṇa Yajurveda", "meaning": "Two primary recensional traditions (separating vs. combining mantras and prose explanations)."},
            {"term": "Yajña (यज्ञ)", "meaning": "Structured ritual offering symbolizing cosmic interdependence."}
        ],
        "major_contributors": [
            {"name": "Yājñavalkya (tradition)", "era": "Ancient", "contribution": "Associated with the Śukla Yajurveda and Śatapatha Brāhmaṇa."},
            {"name": "Ralph T. H. Griffith", "era": "1899 CE", "contribution": "English translation of the Vājasaneyi Saṁhitā."}
        ],
        "important_texts": [
            {"title": "The Texts of the White Yajurveda", "author": "R. T. H. Griffith", "period": "1899 CE"},
            {"title": "Baudhayana Sulba-Sutra", "author": "Baudhāyana", "period": "c. 800 BCE"}
        ],
        "practical_applications": [
            "Historical source for large decimal number names and altar geometry",
            "Comparative ritual and cultural history"
        ],
        "references": [REF_VEDIC_HERITAGE, REF_IGNCA],
        "linked_resource_ids": [13, 3]
    },
    "atharvaveda-traditions": {
        "sanskrit_name": "Atharvaveda (अथर्ववेद)",
        "introduction": "The Atharvaveda ('Veda of the Atharvans') is a rich treasury of early Indian medicine (Bhaiṣajya), botany, statecraft, marriage hymns, and the celebrated Hymn to the Earth (Bhūmi Sūkta).",
        "detailed_explanation": "Divided into 20 Kāṇḍas (~730 hymns), it reflects everyday life in ancient India—documenting herbal remedies, anatomical terms, community harmony, and ecological reverence.",
        "historical_background": "Preserved in Śaunaka and Paippalāda recensions, it is explicitly cited by Caraka and Suśruta as the Vedic root of Āyurveda. Critically translated by W. D. Whitney and C. R. Lanman (1905).",
        "important_concepts": [
            {"term": "Bhūmi Sūkta (भूमि सूक्त)", "meaning": "Hymn to Earth (AV 12.1) celebrating biodiversity and ecological stewardship."},
            {"term": "Bhaiṣajya (भैषज्य)", "meaning": "Early herbal and therapeutic healing hymns precursor to Āyurveda."}
        ],
        "major_contributors": [
            {"name": "W. D. Whitney & C. R. Lanman", "era": "1905 CE", "contribution": "Critical English translation and textual commentary of the Atharvaveda."}
        ],
        "important_texts": [
            {"title": "Atharva-Veda Samhita", "author": "Whitney & Lanman", "period": "1905 CE"},
            {"title": "The Charaka-Samhita", "author": "Charaka", "period": "Classical"}
        ],
        "practical_applications": [
            "Historical roots of Āyurvedic botany and public health",
            "Ecological ethics and cultural anthropology"
        ],
        "references": [REF_VEDIC_HERITAGE, REF_ARCHIVE],
        "linked_resource_ids": [14, 6]
    },

    # =========================================================================
    # 6. SANSKRIT AND CLASSICAL LITERATURE (1 + 3 subcategories = 4)
    # =========================================================================
    "sanskrit-and-classical-literature": {
        "sanskrit_name": "Saṁskṛta Sāhitya (संस्कृत साहित्य)",
        "introduction": "Sanskrit and Classical Literature encompasses Pāṇinian grammar (Vyākaraṇa), poetic epics (Mahākāvya), lyrical poetry (Khaṇḍakāvya), drama (Nāṭaka), and aesthetic theory (Rasa & Dhvani).",
        "detailed_explanation": "Characterized by extraordinary structural precision and expressive richness, classical Sanskrit literature achieved global acclaim through Kālidāsa, Bhavabhūti, and Bāṇabhaṭṭa, underpinned by Pāṇini's generative grammar.",
        "historical_background": "Following Pāṇini's Aṣṭādhyāyī (c. 5th–4th century BCE) and Bharata's Nāṭyaśāstra, classical Sanskrit drama and poetry flourished under Gupta-era patronage (4th–5th century CE), notably through Kālidāsa's Abhijñānaśākuntalam and Meghadūta.",
        "important_concepts": [
            {"term": "Rasa (रस)", "meaning": "Aesthetic emotional essence evoked in the audience through drama and poetry."},
            {"term": "Kāvya & Nāṭaka", "meaning": "Classical literary poetry and dramatic performance."}
        ],
        "major_contributors": [
            {"name": "Kālidāsa", "era": "c. 4th–5th century CE", "contribution": "Foremost Sanskrit poet and dramatist; author of Śākuntala and Meghadūta."},
            {"name": "Pāṇini", "era": "c. 5th–4th century BCE", "contribution": "Codified classical Sanskrit in the 3,959 sūtras of Aṣṭādhyāyī."}
        ],
        "important_texts": [
            {"title": "Abhijñānaśākuntalam (Sakuntala)", "author": "Kālidāsa", "period": "c. 4th–5th century CE"},
            {"title": "Meghadūta", "author": "Kālidāsa", "period": "c. 4th–5th century CE"},
            {"title": "Aṣṭādhyāyī", "author": "Pāṇini", "period": "c. 5th–4th century BCE"}
        ],
        "practical_applications": [
            "Comparative world literature and literary aesthetics",
            "Computational linguistics and formal grammar models"
        ],
        "references": [REF_IGNCA, REF_NDLI, REF_BORI],
        "linked_resource_ids": [15, 16, 17, 18]
    },
    "paninian-vyakarana": {
        "sanskrit_name": "Vyākaraṇa (व्याकरण)",
        "introduction": "Pāṇinian Vyākaraṇa is the world's oldest and most complete formal generative grammar, describing Sanskrit morphology, phonology, and syntax in ~4,000 algebraic rules.",
        "detailed_explanation": "Using meta-rules (Paribhāṣā), technical markers (It-saṁjñā), and compact phoneme groupings (Pratyāhāras from the Śiva Sūtras), Pāṇini's Aṣṭādhyāyī generates valid Sanskrit words and sentences with rule-based precision comparable to Backus-Naur Form (BNF).",
        "historical_background": "Composed by Pāṇini (c. 5th–4th century BCE, Gandhāra), expanded by Kātyāyana's Vārttikas and Patañjali's Mahābhāṣya (c. 2nd century BCE), and translated into English by Srisa Chandra Vasu (1891).",
        "important_concepts": [
            {"term": "Pratyāhāra (प्रत्याहार)", "meaning": "Abbreviated sound-class notations derived from the 14 Māheśvara Sūtras."},
            {"term": "Kāraka (कारक)", "meaning": "Semantic-syntactic roles linking verbs to participants in an action."}
        ],
        "major_contributors": [
            {"name": "Pāṇini", "era": "c. 5th–4th century BCE", "contribution": "Author of Aṣṭādhyāyī."},
            {"name": "Srisa Chandra Vasu", "era": "1891 CE", "contribution": "First complete English translation of the Aṣṭādhyāyī."}
        ],
        "important_texts": [
            {"title": "The Ashtadhyayi of Panini", "author": "Panini (Trans. S. C. Vasu)", "period": "1891 CE"},
            {"title": "The Vakyapadiya", "author": "Bhartṛhari", "period": "c. 5th century CE"}
        ],
        "practical_applications": [
            "Natural Language Processing (NLP) and morphological analyzers",
            "Formal language theory and compiler grammar design"
        ],
        "references": [REF_MOE_IKS, REF_ARCHIVE],
        "linked_resource_ids": [18, 30]
    },
    "classical-kavya-nataka": {
        "sanskrit_name": "Kāvya & Nāṭaka (काव्य-नाटक)",
        "introduction": "Classical Kāvya (poetry) and Nāṭaka (drama) represent the pinnacle of Sanskrit literary art, blending intricate meter, simile (Upamā), nature imagery, and psychological depth.",
        "detailed_explanation": "Dramas combine Sanskrit prose and verse for noble characters with regional Prakrit dialects for everyday dialogue, illustrating vibrant multilingual literary culture.",
        "historical_background": "From Aśvaghoṣa and Bhāsa to Kālidāsa (c. 4th–5th century CE), Sanskrit drama reached Europe in 1789 via Sir William Jones' translation of Śākuntala, inspiring Goethe and the European Romantic movement.",
        "important_concepts": [
            {"term": "Upamā (उपमा)", "meaning": "Poetic simile, for which Kālidāsa is famously celebrated (Upamā Kālidāsasya)."},
            {"term": "Mandākrāntā Meter", "meaning": "Slow, stately 17-syllable poetic meter used throughout Meghadūta."}
        ],
        "major_contributors": [
            {"name": "Kālidāsa", "era": "c. 4th–5th century CE", "contribution": "Author of Abhijñānaśākuntalam and Meghadūta."},
            {"name": "Sir Monier Monier-Williams & E. Hultzsch", "era": "19th–20th century CE", "contribution": "Critical editions and translations of Kālidāsa's works."}
        ],
        "important_texts": [
            {"title": "Sakuntala: A Sanskrit Drama in Seven Acts", "author": "Kalidasa (Ed. Monier-Williams)", "period": "1876 CE"},
            {"title": "The Meghaduta of Kalidasa", "author": "Kalidasa (Ed. E. Hultzsch)", "period": "1911 CE"}
        ],
        "practical_applications": [
            "World literature curricula and comparative poetics",
            "Classical theatre adaptation and cultural heritage"
        ],
        "references": [REF_IGNCA, REF_ARCHIVE],
        "linked_resource_ids": [15, 16]
    },
    "natyashastra-aesthetics": {
        "sanskrit_name": "Rasa-śāstra / Nāṭyaśāstra (रसशास्त्र)",
        "introduction": "Nāṭyaśāstra Aesthetics explores Bharata Muni's theory of Rasa—the systematic analysis of how drama, poetry, music, and gesture evoke universalized emotional experience in spectators.",
        "detailed_explanation": "According to Bharata's Rasa Sūtra, aesthetic relish (Rasa) arises from the union of determinants (Vibhāva), physical expressions (Anubhāva), and transient states (Vyabhicāribhāva), organized into eight (later nine) primary Rasas.",
        "historical_background": "Codified in Bharata Muni's Nāṭyaśāstra (c. 200 BCE – 200 CE) and famously elucidated by Abhinavagupta (10th–11th century CE) in the Abhinavabhāratī.",
        "important_concepts": [
            {"term": "Navarasa (नवरस)", "meaning": "Nine aesthetic emotions: Śṛṅgāra, Hāsya, Karuṇa, Raudra, Vīra, Bhayānaka, Bībhatsa, Adbhuta, Śānta."},
            {"term": "Abhinaya (अभिनय)", "meaning": "Four modes of dramatic expression: bodily, vocal, costume, and subtle emotional."}
        ],
        "major_contributors": [
            {"name": "Bharata Muni", "era": "c. 200 BCE – 200 CE", "contribution": "Authored Nāṭyaśāstra, foundational encyclopedia of Indian aesthetics."},
            {"name": "Manomohan Ghosh", "era": "1951 CE", "contribution": "Complete critical English translation of Nāṭyaśāstra."}
        ],
        "important_texts": [
            {"title": "The Natyashastra", "author": "Bharata Muni (Trans. Manomohan Ghosh)", "period": "Classical / 1951 CE"}
        ],
        "practical_applications": [
            "Theory of Indian classical dance, theatre, and cinema",
            "Emotion and reception theory in aesthetics"
        ],
        "references": [REF_IGNCA, REF_NDLI],
        "linked_resource_ids": [17, 15]
    },

    # =========================================================================
    # 7. ARCHITECTURE AND ENGINEERING (1 + 3 subcategories = 4)
    # =========================================================================
    "architecture-and-engineering": {
        "sanskrit_name": "Vāstu-śāstra & Śilpa (वास्तुशास्त्र)",
        "introduction": "Indian Architecture and Engineering (Vāstu Śāstra and Śilpa Śāstra) codifies site selection, orientation, structural geometry, temple architecture, residential design, and urban planning.",
        "detailed_explanation": "Treatises like Mānasāra, Mayamata, and King Bhoja's Samarāṅgaṇa-Sūtradhāra combine practical civil engineering (soil testing, joinery, foundations, water drainage) with proportional modular grids (Vāstu-puruṣa-maṇḍala).",
        "historical_background": "Rooted in Indus-Sarasvati urban engineering and Śulba geometry, Vāstu texts matured between the 6th and 12th centuries CE across Drāviḍa, Nāgara, and Vesara architectural traditions.",
        "important_concepts": [
            {"term": "Vāstu-puruṣa-maṇḍala", "meaning": "Geometric modular grid (often 8×8 or 9×9) governing spatial layout and proportions."},
            {"term": "Tāla-māna (तालमान)", "meaning": "Proportional measurement system for pillars, shrines, and sculptures."}
        ],
        "major_contributors": [
            {"name": "King Bhoja of Dhārā", "era": "11th century CE", "contribution": "Authored Samarāṅgaṇa-Sūtradhāra covering architecture, town planning, and mechanical devices."},
            {"name": "Prasanna Kumar Acharya & Bruno Dagens", "era": "20th century CE", "contribution": "Standard translations and encyclopedias of Mānasāra and Mayamata."}
        ],
        "important_texts": [
            {"title": "Mayamata", "author": "Ed./Trans. Bruno Dagens", "period": "Medieval / 1994 CE"},
            {"title": "Architecture of Manasara", "author": "Trans. P. K. Acharya", "period": "Classical / 1934 CE"},
            {"title": "Samarangana-Sutradhara", "author": "King Bhoja", "period": "11th century CE"}
        ],
        "practical_applications": [
            "Passive solar orientation, natural ventilation, and climate-responsive building",
            "Heritage conservation of stone temples and stepwells"
        ],
        "references": [REF_IGNCA, REF_NDLI, REF_MOE_IKS],
        "linked_resource_ids": [19, 20, 21]
    },
    "vastu-shastra-design": {
        "sanskrit_name": "Vāstu-vidyā (वास्तुविद्या)",
        "introduction": "Vāstu-vidyā covers residential design, spatial orientation, soil assessment, material selection, and proportional harmony for human dwellings.",
        "detailed_explanation": "Both Mayamata and Mānasāra devote systematic chapters to evaluating soil fertility and load-bearing capacity, aligning courtyards (Catuḥśālā) for daylight and cross-ventilation, and timber/stone joinery.",
        "historical_background": "Preserved in South Indian Āgama-linked treatises (Mayamata, c. 9th–12th century CE) and northern encyclopedias (Samarāṅgaṇa-Sūtradhāra, 11th century CE).",
        "important_concepts": [
            {"term": "Bhū-parīkṣā (भूपरीक्षा)", "meaning": "Empirical soil testing for color, odor, slope, and water retention before construction."},
            {"term": "Catuḥśālā", "meaning": "Four-winged courtyard house maximizing natural light and passive cooling."}
        ],
        "major_contributors": [
            {"name": "Maya (tradition) / Bruno Dagens", "era": "Medieval / 1994 CE", "contribution": "Preserved and translated the Mayamata residential architecture manual."}
        ],
        "important_texts": [
            {"title": "Mayamata: An Indian Treatise on Housing Architecture", "author": "Bruno Dagens (Trans.)", "period": "1994 CE"},
            {"title": "Samarangana-Sutradhara", "author": "King Bhoja", "period": "11th century CE"}
        ],
        "practical_applications": [
            "Sustainable vernacular courtyard housing",
            "Bioclimatic architectural design in tropical climates"
        ],
        "references": [REF_IGNCA, REF_MOE_IKS],
        "linked_resource_ids": [19, 21]
    },
    "temple-architecture": {
        "sanskrit_name": "Prāsāda-vāstu (प्रासादवास्तु)",
        "introduction": "Temple Architecture in India evolved three major structural styles—Nāgara (northern curvilinear Śikhara), Drāviḍa (southern stepped Vimāna), and Vesara (hybrid)—governed by strict modular geometry.",
        "detailed_explanation": "Treatises detail every component from the foundation (Adhiṣṭhāna) and sanctum (Garbhagṛha) to column orders, corbelled domes, and tower superstructures using interlocking stone masonry without mortar.",
        "historical_background": "Codified in Mānasāra, Mayamata, and Samarāṅgaṇa-Sūtradhāra, and exemplified by surviving monuments from Mahabalipuram, Pattadakal, Khajuraho, and Thanjavur.",
        "important_concepts": [
            {"term": "Garbhagṛha & Śikhara", "meaning": "Sanctum sanctorum and rising superstructure tower."},
            {"term": "Nāgara, Drāviḍa, Vesara", "meaning": "Three canonical regional temple architectural traditions."}
        ],
        "major_contributors": [
            {"name": "P. K. Acharya", "era": "1934 CE", "contribution": "Translated the complete 70-chapter Mānasāra."}
        ],
        "important_texts": [
            {"title": "Architecture of Manasara", "author": "P. K. Acharya (Trans.)", "period": "1934 CE"},
            {"title": "Mayamata", "author": "Bruno Dagens (Trans.)", "period": "1994 CE"}
        ],
        "practical_applications": [
            "Structural conservation and restoration of historic monuments",
            "Dry-stone seismic-resilient interlocking masonry studies"
        ],
        "references": [REF_IGNCA, REF_ARCHIVE],
        "linked_resource_ids": [20, 19, 21]
    },
    "town-planning-civil": {
        "sanskrit_name": "Nagara-vinyāsa (नगरविन्यास)",
        "introduction": "Town Planning and Civil Engineering in classical India detailed fortified city layouts, road hierarchies, zoning, drainage, and civic waterworks.",
        "detailed_explanation": "Mānasāra describes eight classical town-plan typologies (Daṇḍaka, Sarvatobhadra, Nandyāvarta, Padmaka, Swastika, Prastara, Kārmuka, Caturmukha) tailored to riverbanks, hills, or trade crossroads.",
        "historical_background": "Urban planning rules appear in Kauṭilya's Arthaśāstra (4th century BCE–3rd century CE), Mānasāra, and Samarāṅgaṇa-Sūtradhāra, alongside archaeological cities such as Dholavira, Pāṭaliputra, and Jaipur.",
        "important_concepts": [
            {"term": "Sarvatobhadra & Daṇḍaka", "meaning": "Grid-iron and radial civic town plans with dedicated market, residential, and garden zones."},
            {"term": "Rājamārga", "meaning": "Broad primary royal thoroughfare intersecting civic quarters."}
        ],
        "major_contributors": [
            {"name": "King Bhoja", "era": "11th century CE", "contribution": "Detailed civic layout, fortifications, and water engineering in Samarāṅgaṇa-Sūtradhāra."},
            {"name": "Kauṭilya", "era": "Ancient", "contribution": "Codified urban zoning and civic infrastructure in Arthaśāstra Book II."}
        ],
        "important_texts": [
            {"title": "Architecture of Manasara", "author": "P. K. Acharya", "period": "1934 CE"},
            {"title": "Samarangana-Sutradhara", "author": "King Bhoja", "period": "11th century CE"},
            {"title": "Kautilya's Arthashastra", "author": "Kautilya", "period": "Ancient"}
        ],
        "practical_applications": [
            "Walkable mixed-use urban design and civic sanitation history",
            "Heritage city conservation"
        ],
        "references": [REF_IGNCA, REF_MOE_IKS],
        "linked_resource_ids": [20, 21, 27]
    },

    # =========================================================================
    # 8. AGRICULTURE AND ECOLOGY (1 + 3 subcategories = 4)
    # =========================================================================
    "agriculture-and-ecology": {
        "sanskrit_name": "Kṛṣi & Vṛkṣāyurveda (कृषि-वृक्षायुर्वेद)",
        "introduction": "Indian Agriculture and Ecology unites agronomy (Kṛṣi-śāstra), plant pathology and arboriculture (Vṛkṣāyurveda), monsoon forecasting, organic manuring, and water harvesting.",
        "detailed_explanation": "Classical treatises treat soil, seed, water, livestock, and forest biodiversity as an integrated agro-ecological system, emphasizing seed preservation, crop rotation, and botanical pest control.",
        "historical_background": "From Vedic agricultural hymns to Kauṭilya's Superintendent of Agriculture (Sītādhyakṣa), Parāśara's Kṛṣi-Parāśara (c. 4th–10th century CE), and Surapāla's Vṛkṣāyurveda (c. 1000 CE), India sustained multi-crop farming for millennia.",
        "important_concepts": [
            {"term": "Kuṇapajala (कुणपजल)", "meaning": "Fermented organic liquid bio-fertilizer described in Vṛkṣāyurveda."},
            {"term": "Bīja-saṁskāra", "meaning": "Pre-sowing seed treatment using ash, milk, and botanicals."}
        ],
        "major_contributors": [
            {"name": "Parāśara", "era": "c. 4th–10th century CE", "contribution": "Authored Kṛṣi-Parāśara on monsoon prediction, plowing, and cattle care."},
            {"name": "Surapāla", "era": "c. 1000 CE", "contribution": "Authored Vṛkṣāyurveda on horticulture, grafting, and plant pathology."}
        ],
        "important_texts": [
            {"title": "Vrikshayurveda", "author": "Surapala (Trans. N. Sadhale)", "period": "c. 1000 CE"},
            {"title": "Krishi-Parashara", "author": "Parashara (Trans. N. Sadhale)", "period": "Early Medieval"}
        ],
        "practical_applications": [
            "Organic and regenerative farming (Kuṇapajala bio-inputs)",
            "Agroforestry and traditional seed conservation"
        ],
        "references": [REF_AAHF, REF_NDLI, REF_MOE_IKS],
        "linked_resource_ids": [8, 22, 27]
    },
    "krishi-shastra": {
        "sanskrit_name": "Kṛṣi-śāstra (कृषिशास्त्र)",
        "introduction": "Kṛṣi-śāstra is the classical science of agronomy—covering rainfall forecasting, soil preparation, plow design, sowing calendars, harvesting, and grain storage.",
        "detailed_explanation": "Parāśara's Kṛṣi-Parāśara provides 243 verses detailing astronomical rainfall indicators, bullock health, compost preparation, and precise sowing windows tied to lunar Nakṣatras.",
        "historical_background": "Edited and translated with scientific commentary by Nalini Sadhale and Y. L. Nene under the Asian Agri-History Foundation (1999), demonstrating remarkable alignment with modern agro-meteorology.",
        "important_concepts": [
            {"term": "Megha-lakṣaṇa", "meaning": "Atmospheric and astronomical observation methods for monsoon forecasting."},
            {"term": "Kṛṣi-yantra", "meaning": "Traditional wooden plow (Hala) components and draught-animal management."}
        ],
        "major_contributors": [
            {"name": "Parāśara", "era": "Early Medieval", "contribution": "Composed Kṛṣi-Parāśara."},
            {"name": "Nalini Sadhale & Y. L. Nene", "era": "1999 CE", "contribution": "Critical translation and agronomic validation."}
        ],
        "important_texts": [
            {"title": "Krishi-Parashara (Agriculture by Parashara)", "author": "Parashara (Trans. Sadhale)", "period": "1999 CE"}
        ],
        "practical_applications": [
            "Rain-fed sustainable agriculture and soil moisture conservation",
            "Indigenous agro-meteorological wisdom"
        ],
        "references": [REF_AAHF, REF_NDLI],
        "linked_resource_ids": [22, 8]
    },
    "vrikshayurveda-plant-science": {
        "sanskrit_name": "Vṛkṣāyurveda (वृक्षायुर्वेद)",
        "introduction": "Vṛkṣāyurveda ('Science of Plant Life') applies the Tridoṣa framework of Āyurveda to botany, horticulture, grafting, soil nutrition, and plant disease management.",
        "detailed_explanation": "Surapāla's 325-verse treatise classifies soils (arid, marshy, balanced), details 170+ plant species, explains seed soaking and propagation by cuttings/grafts, and diagnoses plant ailments caused by Vāta, Pitta, and Kapha imbalances.",
        "historical_background": "Written by Surapāla (c. 1000 CE, court scholar of Bhīmapāla) from a Bodleian Library manuscript, and translated by Nalini Sadhale (1996).",
        "important_concepts": [
            {"term": "Kuṇapajala", "meaning": "Nutrient-rich liquid manure tested in modern organic farming trials."},
            {"term": "Vṛkṣa-cikitsā", "meaning": "Botanical plant therapy using neem, turmeric, milk, and honey pastes."}
        ],
        "major_contributors": [
            {"name": "Surapāla", "era": "c. 1000 CE", "contribution": "Author of Vṛkṣāyurveda."},
            {"name": "Y. L. Nene & Nalini Sadhale", "era": "1996 CE", "contribution": "Modern agronomic commentary and experimental validation."}
        ],
        "important_texts": [
            {"title": "Vrikshayurveda (The Science of Plant Life)", "author": "Surapala (Trans. Sadhale)", "period": "c. 1000 CE / 1996 CE"}
        ],
        "practical_applications": [
            "Chemical-free organic horticulture and pest management",
            "Urban forestry and ecological restoration"
        ],
        "references": [REF_AAHF, REF_MOE_IKS],
        "linked_resource_ids": [8, 22]
    },
    "water-harvesting": {
        "sanskrit_name": "Jala-saṁvardhana (जलसंवर्धन)",
        "introduction": "Traditional Indian Water Harvesting encompasses community-managed tanks (Eri/Kere), stepwells (Vāv/Bāolī), check-dams, inundation canals, and groundwater recharge.",
        "detailed_explanation": "Classical texts—from Kauṭilya's Arthaśāstra and Kṛṣi-Parāśara (construction of bunds/water-retaining ridges) to Vāstu works—codified irrigation taxation, silt clearance, and gravity-fed canal networks.",
        "historical_background": "Archaeological sites like Dholavira (Harappan reservoirs), Sudarśana Lake (Junagadh, Mauryan-Gupta periods), and medieval Tamil Eri cascades showcase millennia of decentralized hydrological engineering.",
        "important_concepts": [
            {"term": "Setubandha (सेतुबन्ध)", "meaning": "Water-retaining embankments, reservoirs, and check-dams described in Arthaśāstra."},
            {"term": "Bāolī / Kuṇḍa", "meaning": "Stepped subterranean wells accessing deep aquifers while minimizing evaporation."}
        ],
        "major_contributors": [
            {"name": "Kauṭilya", "era": "Ancient", "contribution": "Codified reservoir construction and irrigation management in Arthaśāstra."},
            {"name": "Parāśara", "era": "Early Medieval", "contribution": "Emphasized bunding and seasonal water retention for paddy."}
        ],
        "important_texts": [
            {"title": "Krishi-Parashara", "author": "Parashara", "period": "Early Medieval"},
            {"title": "Kautilya's Arthashastra", "author": "Kautilya", "period": "Ancient"},
            {"title": "Vrikshayurveda (Water & Soil chapters)", "author": "Surapala", "period": "c. 1000 CE"}
        ],
        "practical_applications": [
            "Decentralized rainwater harvesting and drought resilience",
            "Revival of traditional lakes, johads, and stepwells"
        ],
        "references": [REF_AAHF, REF_MOE_IKS],
        "linked_resource_ids": [22, 8, 27]
    },

    # =========================================================================
    # 9. METALLURGY AND MATERIAL SCIENCE (1 + 3 subcategories = 4)
    # =========================================================================
    "metallurgy-and-material-science": {
        "sanskrit_name": "Dhātuvāda & Rasaśāstra (धातुवाद)",
        "introduction": "Indian Metallurgy and Material Science spans ancient zinc distillation at Zawar, high-carbon Wootz crucible steel, corrosion-resistant iron pillars, bronze lost-wax casting, and Rasaśāstra alchemy.",
        "detailed_explanation": "Combining empirical furnace engineering with alchemical/chemical treatises (Rasaśāstra), Indian metallurgists mastered temperature-controlled reduction, alloying, and herbo-mineral purification.",
        "historical_background": "Archaeometallurgical evidence includes the 4th–5th century CE Delhi Iron Pillar, Zawar's downward-distillation zinc retorts (earliest industrial zinc production in the world), and medieval texts like Rasaratnasamuccaya (13th–14th century CE).",
        "important_concepts": [
            {"term": "Dhātu & Upadhātu", "meaning": "Primary metals (gold, silver, copper, iron, tin, lead, zinc) and secondary minerals."},
            {"term": "Puṭa & Mūṣā", "meaning": "Controlled calcination heating cycles and specialized clay crucibles."}
        ],
        "major_contributors": [
            {"name": "Vāgbhaṭa (Rasavāgbhaṭa)", "era": "c. 13th–14th century CE", "contribution": "Authored Rasaratnasamuccaya on laboratory apparatus, crucibles, and minerals."},
            {"name": "Prof. R. Balasubramaniam", "era": "2002–2008 CE", "contribution": "Materials science elucidation of the Delhi Iron Pillar's passive corrosion film."}
        ],
        "important_texts": [
            {"title": "Rasaratnasamuccaya", "author": "Vāgbhaṭa (Trans. D. Joshi)", "period": "c. 13th–14th century CE"},
            {"title": "Delhi Iron Pillar: New Insights", "author": "Prof. R. Balasubramaniam", "period": "2005 CE"}
        ],
        "practical_applications": [
            "Corrosion-resistant iron alloying and phosphate passive coatings",
            "High-purity metal extraction and Ayurvedic herbo-mineral pharmaceutics"
        ],
        "references": [REF_INSA, REF_NDLI, REF_MOE_IKS],
        "linked_resource_ids": [23, 24, 31]
    },
    "rasa-shastra": {
        "sanskrit_name": "Rasaśāstra (रसशास्त्र)",
        "introduction": "Rasaśāstra is the classical Indian chemical and iatrochemical tradition focused on mercury (Pārada), minerals, gems, laboratory apparatus (Yantras), and micro-purified therapeutic preparations (Bhasmas).",
        "detailed_explanation": "Texts like Rasaratnasamuccaya systematically classify 8 Mahārasas, 8 Uparasas, 7 metals, crucibles (Mūṣā), furnaces (Koṣṭhī), and distillation/sublimation devices (Pātana-yantra).",
        "historical_background": "Evolving from early Indian alchemy (8th–11th century CE, Rasārṇava) into a standardized pharmaceutical chemistry by the 13th–14th century CE (Rasaratnasamuccaya), critically translated by Prof. D. Joshi for INSA.",
        "important_concepts": [
            {"term": "Yantra-prakaraṇa", "meaning": "Detailed designs for distillation (Tiryak-pātana), sublimation, and steam-bath apparatus."},
            {"term": "Bhasma (भस्म)", "meaning": "Calcined herbo-mineral preparations processed through repeated incineration and trituration."}
        ],
        "major_contributors": [
            {"name": "Vāgbhaṭa", "era": "c. 13th–14th century CE", "contribution": "Systematized laboratory design, furnaces, and mineral classification in Rasaratnasamuccaya."},
            {"name": "Prof. Damodar Joshi", "era": "1987 CE", "contribution": "INSA English translation and chemical commentary."}
        ],
        "important_texts": [
            {"title": "Rasaratnasamuccaya of Vagbhata", "author": "Vagbhata (Trans. D. Joshi)", "period": "1987 CE"}
        ],
        "practical_applications": [
            "History of chemical apparatus, distillation, and metallurgy",
            "Standardization and safety validation of traditional mineral formulations"
        ],
        "references": [REF_INSA, REF_NDLI],
        "linked_resource_ids": [23, 31]
    },
    "wootz-steel-iron": {
        "sanskrit_name": "Ukku / Kṛṣṇāyas (उक्कु / कृष्णायास)",
        "introduction": "Indian Iron and Wootz Steel represents world-renowned ancient metallurgical mastery—producing both ultra-pure high-phosphorus wrought iron (like the Delhi Iron Pillar) and ultra-high-carbon crucible steel (Wootz).",
        "detailed_explanation": "Forge-welded wrought iron pillars resisted rust for over 1,600 years due to a protective crystalline iron-hydrogen-phosphate hydrate passive layer, while South Indian Wootz steel (from Tamil/Kannada *ukku*) was exported globally to craft Damascus blades.",
        "historical_background": "The 7.2-meter, 6-ton Delhi Iron Pillar was erected during Chandragupta II's reign (c. 402 CE). Prof. R. Balasubramaniam (IIT Kanpur) scientifically established its composition and corrosion-resistance mechanism.",
        "important_concepts": [
            {"term": "Misawite Passive Film", "meaning": "Protective amorphous oxyhydroxide and phosphate barrier preventing rust on the Delhi Iron Pillar."},
            {"term": "Wootz Crucible Steel", "meaning": "High-carbon (~1.5% C) steel produced by carburizing iron in sealed clay crucibles."}
        ],
        "major_contributors": [
            {"name": "Prof. R. Balasubramaniam", "era": "2002–2005 CE", "contribution": "Revealed the metallurgical science behind the Delhi Iron Pillar's corrosion resistance."}
        ],
        "important_texts": [
            {"title": "Delhi Iron Pillar: New Insights on its Metallurgy and Corrosion Resistance", "author": "R. Balasubramaniam", "period": "2005 CE"},
            {"title": "A Concise History of Science in India", "author": "Bose, Sen & Subbarayappa", "period": "1971 CE"}
        ],
        "practical_applications": [
            "Corrosion engineering and phosphate-treated structural steels",
            "Archaeometallurgy and materials characterization"
        ],
        "references": [REF_INSA, REF_MOE_IKS],
        "linked_resource_ids": [24, 31]
    },
    "non-ferrous-alloys": {
        "sanskrit_name": "Tāmra-Kāṁsya-Yaśada (ताम्र-कांस्य-यशद)",
        "introduction": "Non-Ferrous Alloys in India cover copper, high-tin bronze (bell metal), brass (Pītala), Pañcaloha ('five-metal' sacred alloy), and the pioneering Zawar zinc distillation process.",
        "detailed_explanation": "Because zinc vaporizes below its ore reduction temperature, Indian metallurgists invented downward-condensation clay retorts (Koṣṭhī) at Zawar (Rajasthan) to condense pure metallic zinc centuries before Europe.",
        "historical_background": "Documented in Rasaratnasamuccaya (describing zinc extraction from Rasaka/calamine) and verified by archaeological excavations at Zawar dating back to at least the 12th century CE (with earlier traces from 1st millennium BCE).",
        "important_concepts": [
            {"term": "Tiryak-pātana / Adhaḥ-pātana", "meaning": "Downward distillation technique used to condense zinc vapor without re-oxidation."},
            {"term": "Madhūcchiṣṭa-vidhāna", "meaning": "Lost-wax casting process for high-precision Chola bronze sculptures."}
        ],
        "major_contributors": [
            {"name": "Vāgbhaṭa", "era": "c. 13th–14th century CE", "contribution": "Described extraction of Yaśada-sattva (zinc) from calamine in Rasaratnasamuccaya."},
            {"name": "D. M. Bose, S. N. Sen & B. V. Subbarayappa", "era": "1971 CE", "contribution": "Synthesized archaeological and textual evidence of copper, bronze, and zinc."}
        ],
        "important_texts": [
            {"title": "Rasaratnasamuccaya", "author": "Vagbhata (Trans. D. Joshi)", "period": "1987 CE"},
            {"title": "A Concise History of Science in India", "author": "Bose, Sen & Subbarayappa", "period": "1971 CE"}
        ],
        "practical_applications": [
            "Pyrometallurgical distillation design",
            "Traditional bell-metal (Kāṁsya) and sculptural bronze craftsmanship"
        ],
        "references": [REF_INSA, REF_NDLI],
        "linked_resource_ids": [23, 31]
    },

    # =========================================================================
    # 10. ARTS, MUSIC AND PERFORMING TRADITIONS (1 + 3 subcategories = 4)
    # =========================================================================
    "arts-music-and-performing-traditions": {
        "sanskrit_name": "Saṅgīta & Kalā (सङ्गीत-कला)",
        "introduction": "Indian Arts, Music, and Performing Traditions unite musicology (Saṅgīta), classical dance and dramaturgy (Nāṭya/Nṛtya), and visual iconography (Śilpa).",
        "detailed_explanation": "Classical Indian treatises define Saṅgīta as the triad of vocal music (Gīta), instrumental music (Vādya), and dance (Nṛtya), governed by microtonal intervals (Śruti), melodic frameworks (Rāga), and rhythmic cycles (Tāla).",
        "historical_background": "Beginning with Bharata's Nāṭyaśāstra (c. 200 BCE – 200 CE), Mataṅga's Bṛhaddeśī (c. 6th–8th century CE, first major treatise defining Rāga), and Śārṅgadeva's Saṅgītaratnākara (13th century CE), these works bridge both Hindustani and Carnatic traditions.",
        "important_concepts": [
            {"term": "Rāga (राग)", "meaning": "Melodic framework of notes, ornaments, and phrases designed to evoke a specific mood."},
            {"term": "Tāla (ताल)", "meaning": "Cyclic rhythmic structure organizing beats and accents."}
        ],
        "major_contributors": [
            {"name": "Bharata Muni", "era": "c. 200 BCE – 200 CE", "contribution": "Author of Nāṭyaśāstra."},
            {"name": "Mataṅga Muni", "era": "c. 6th–8th century CE", "contribution": "Author of Bṛhaddeśī; first systematic exposition of Rāga."},
            {"name": "Śārṅgadeva", "era": "13th century CE", "contribution": "Author of Saṅgītaratnākara, foundational to both northern and southern music."}
        ],
        "important_texts": [
            {"title": "The Natyashastra", "author": "Bharata Muni", "period": "Classical"},
            {"title": "Sangitaratnakara", "author": "Śārṅgadeva", "period": "13th century CE"},
            {"title": "Brihaddesi", "author": "Matanga Muni", "period": "c. 6th–8th century CE"}
        ],
        "practical_applications": [
            "Hindustani and Carnatic classical music pedagogy",
            "Classical dance preservation (Bharatanatyam, Kathak, Odissi, etc.)"
        ],
        "references": [REF_IGNCA, REF_NDLI, REF_MOE_IKS],
        "linked_resource_ids": [17, 25, 26]
    },
    "musicology-sangita": {
        "sanskrit_name": "Saṅgīta-śāstra (सङ्गीतशास्त्र)",
        "introduction": "Saṅgīta-śāstra is the mathematical and aesthetic science of Indian music—analyzing the 22 microtones (Śrutis), seven notes (Svaras), scales (Grāma-Mūrchanā), and Rāga grammar.",
        "detailed_explanation": "Treatises examine acoustic vibration (Nāda), vocal production, string/wind/percussion organology, and hundreds of classical and regional Rāgas and Tālas.",
        "historical_background": "Mataṅga's Bṛhaddeśī (c. 6th–8th century CE) introduced the formal definition of Rāga, while Śārṅgadeva's 7-chapter Saṅgītaratnākara (c. 1210–1247 CE, Devagiri) became the universal reference text prior to the Hindustani-Carnatic divergence.",
        "important_concepts": [
            {"term": "22 Śrutis (श्रुति)", "meaning": "Microtonal pitch intervals dividing the octave."},
            {"term": "Mārga & Deśī", "meaning": "Classical pan-Indian sacred music vs. vibrant regional melodic traditions."}
        ],
        "major_contributors": [
            {"name": "Mataṅga Muni", "era": "c. 6th–8th century CE", "contribution": "Defined Rāga and regional Deśī traditions in Bṛhaddeśī."},
            {"name": "Śārṅgadeva", "era": "13th century CE", "contribution": "Synthesized Indian musicology and dance in Saṅgītaratnākara."}
        ],
        "important_texts": [
            {"title": "Sangitaratnakara of Sarngadeva", "author": "Sarangadeva (Trans. C. Kunhan Raja)", "period": "13th century CE"},
            {"title": "Brihaddesi of Sri Matanga Muni", "author": "Matanga Muni (Ed. Prem Lata Sharma)", "period": "c. 6th–8th century CE"}
        ],
        "practical_applications": [
            "Acoustic analysis of microtonal scales",
            "Performance and conservatory training in Indian classical music"
        ],
        "references": [REF_IGNCA, REF_ARCHIVE],
        "linked_resource_ids": [25, 26]
    },
    "dance-dramatic-expression": {
        "sanskrit_name": "Nāṭya & Nṛtya (नाट्य-नृत्य)",
        "introduction": "Dance and Dramatic Expression (Nāṭya, Nṛtya, and Nṛtta) codifies classical movement vocabulary, hand gestures (Mudrās/Hastas), eye/neck movements, and stagecraft.",
        "detailed_explanation": "Bharata's Nāṭyaśāstra defines 108 Karaṇas (coordinated dance units), 24/28 single- and double-hand Mudrās, and 8 Sāttvika Bhāvas, while Saṅgītaratnākara's 7th chapter (Nartanādhyāya) expands regional dance styles.",
        "historical_background": "Preserved across temple sculptures (e.g., Chidambaram's 108 Karaṇa reliefs) and living guru-śiṣya lineages underlying India's recognized classical dance forms.",
        "important_concepts": [
            {"term": "Karaṇa (करण)", "meaning": "108 fundamental sculptural/kinetic dance transitions combining stance and hand gesture."},
            {"term": "Mudrā / Hasta", "meaning": "Codified hand gestures conveying narrative, objects, and emotion."}
        ],
        "major_contributors": [
            {"name": "Bharata Muni", "era": "Classical", "contribution": "Codified Karaṇas, Aṅgahāras, and Abhinaya in Nāṭyaśāstra."},
            {"name": "Śārṅgadeva", "era": "13th century CE", "contribution": "Documented medieval dance forms in Nartanādhyāya."}
        ],
        "important_texts": [
            {"title": "The Natyashastra", "author": "Bharata Muni (Trans. M. Ghosh)", "period": "Classical"},
            {"title": "Sangitaratnakara (Chapter 7)", "author": "Sarangadeva", "period": "13th century CE"}
        ],
        "practical_applications": [
            "Choreography and classical dance reconstruction",
            "Non-verbal gesture and storytelling pedagogy"
        ],
        "references": [REF_IGNCA, REF_NDLI],
        "linked_resource_ids": [17, 25]
    },
    "shilpa-iconography": {
        "sanskrit_name": "Śilpa-vidyā (शिल्पविद्या)",
        "introduction": "Śilpa and Iconography (Pratimā-lakṣaṇa) governs sculptural proportions, iconometry, relief composition, painting (Citra-sūtra), and sacred symbolism in stone, wood, and bronze.",
        "detailed_explanation": "Treatises specify proportional canons (Tālamāna—such as Daśatāla for deities), posture bends (Tribhaṅga), attributes (Āyudhas), and surface pigments for murals.",
        "historical_background": "Detailed across the Mānasāra, Mayamata, Samarāṅgaṇa-Sūtradhāra, and Viṣṇudharmottara Purāṇa (Citrasūtra), guiding classical sculpture from Gupta art to Chola bronzes.",
        "important_concepts": [
            {"term": "Daśatāla (दशताल)", "meaning": "Ten-fold facial-unit proportional canon for classical sculpture."},
            {"term": "Tribhaṅga", "meaning": "Graceful 'three-bend' sculptural posture."}
        ],
        "major_contributors": [
            {"name": "King Bhoja", "era": "11th century CE", "contribution": "Devoted chapters of Samarāṅgaṇa-Sūtradhāra to iconography and painting."},
            {"name": "Bruno Dagens & P. K. Acharya", "era": "20th century CE", "contribution": "Translated Mayamata and Mānasāra iconographic canons."}
        ],
        "important_texts": [
            {"title": "Mayamata: Housing Architecture and Iconography", "author": "Bruno Dagens", "period": "1994 CE"},
            {"title": "Architecture of Manasara", "author": "P. K. Acharya", "period": "1934 CE"},
            {"title": "Samarangana-Sutradhara", "author": "King Bhoja", "period": "11th century CE"}
        ],
        "practical_applications": [
            "Art history, museum curation, and iconographic identification",
            "Traditional stone-carving and bronze-casting apprenticeships"
        ],
        "references": [REF_IGNCA, REF_ARCHIVE],
        "linked_resource_ids": [19, 20, 21]
    },

    # =========================================================================
    # 11. GOVERNANCE AND ECONOMICS (1 + 3 subcategories = 4)
    # =========================================================================
    "governance-and-economics": {
        "sanskrit_name": "Arthaśāstra & Rājanīti (अर्थशास्त्र-राजनीति)",
        "introduction": "Indian Governance and Economics examines statecraft, diplomacy, public administration, jurisprudence, taxation, and trade regulation from the Mauryan period onward.",
        "detailed_explanation": "Rejecting purely idealistic models, texts like Kauṭilya's Arthaśāstra and Śukranīti integrate ethics (Dharma), economic prosperity (Artha), administrative auditing, and strategic diplomacy.",
        "historical_background": "Systematized in Kauṭilya's Arthaśāstra (composed/redacted c. 4th century BCE – 3rd century CE, rediscovered in 1905 by R. Shamasastry at Mysore) and later Nīti treatises such as Kāmandaka's Nītisāra and Śukranīti.",
        "important_concepts": [
            {"term": "Saptāṅga Theory (सप्ताङ्ग)", "meaning": "Seven constituent limbs of a state: King, Ministers, Territory/Population, Fort, Treasury, Army, Ally."},
            {"term": "Yogakṣema (योगक्षेम)", "meaning": "Security and welfare of citizens as the primary duty of the state."}
        ],
        "major_contributors": [
            {"name": "Kauṭilya (Cāṇakya)", "era": "Ancient", "contribution": "Authored Arthaśāstra, foundational treatise on statecraft, law, and economics."},
            {"name": "Dr. R. Shamasastry", "era": "1905–1915 CE", "contribution": "Rediscovered and translated the Arthaśāstra manuscript."}
        ],
        "important_texts": [
            {"title": "Kautilya's Arthashastra", "author": "Kautilya (Trans. R. Shamasastry)", "period": "Ancient / 1915 CE"},
            {"title": "The Sukraniti", "author": "Shukracharya (Trans. B. K. Sarkar)", "period": "1914 CE"}
        ],
        "practical_applications": [
            "Public policy, anti-corruption auditing, and strategic diplomacy",
            "History of economic thought and institutional governance"
        ],
        "references": [REF_NDLI, REF_MOE_IKS, REF_ARCHIVE],
        "linked_resource_ids": [27, 28, 32]
    },
    "arthashastra-statecraft": {
        "sanskrit_name": "Daṇḍanīti / Arthaśāstra (दण्डनीति)",
        "introduction": "Arthaśāstra Statecraft covers political administration, cabinet counsel (Mantripariṣad), intelligence networks, civil service accountability, and the Maṇḍala theory of foreign policy.",
        "detailed_explanation": "Kauṭilya details 30+ departmental superintendents (Adhyakṣas), crisis management, six-fold foreign policy (Ṣāḍguṇya), and the principle that the ruler's happiness lies in the welfare of the subjects.",
        "historical_background": "Codified in 15 Adhikaraṇas (Books) and 150 chapters of Kauṭilya's Arthaśāstra, alongside administrative maxims in Śukranīti.",
        "important_concepts": [
            {"term": "Maṇḍala Theory", "meaning": "Geopolitical circle of states analyzing alliances, neutrality, and balance of power."},
            {"term": "Ṣāḍguṇya (षाड्गुण्य)", "meaning": "Six diplomatic instruments: peace, war, neutrality, marching, alliance, dual policy."}
        ],
        "major_contributors": [
            {"name": "Kauṭilya", "era": "Ancient", "contribution": "Formulated systematic administrative and diplomatic doctrine."}
        ],
        "important_texts": [
            {"title": "Kautilya's Arthashastra", "author": "Kautilya (Trans. Shamasastry)", "period": "1915 CE"},
            {"title": "The Sukraniti", "author": "Trans. B. K. Sarkar", "period": "1914 CE"}
        ],
        "practical_applications": [
            "Strategic studies, international relations, and public administration",
            "Organizational leadership and risk management"
        ],
        "references": [REF_NDLI, REF_ARCHIVE],
        "linked_resource_ids": [27, 28]
    },
    "dharmashastra-jurisprudence": {
        "sanskrit_name": "Vyavahāra & Dharmaśāstra (व्यवहार)",
        "introduction": "Dharmaśāstra Jurisprudence (Vyavahāra) covers civil and criminal law, judicial procedure, witness evaluation, contracts, property rights, and proportionate penalties.",
        "detailed_explanation": "Books III and IV of Arthaśāstra (Dharmasthīya and Kaṇṭakaśodhana) and Chapter IV of Śukranīti distinguish civil disputes from public-safety offenses, requiring written evidence, impartial judges, and protection against judicial misconduct.",
        "historical_background": "Rooted in Dharmasūtras and Smṛtis (Manu, Yājñavalkya, Nārada) alongside practical state codes in Arthaśāstra and Śukranīti.",
        "important_concepts": [
            {"term": "Dharmasthīya & Kaṇṭakaśodhana", "meaning": "Civil courts (contracts, marriage, inheritance) vs. criminal/administrative courts."},
            {"term": "Vyavahāra-pāda", "meaning": "Classical 18 titles of legal litigation."}
        ],
        "major_contributors": [
            {"name": "Kauṭilya", "era": "Ancient", "contribution": "Codified empirical court procedures and consumer protection laws."},
            {"name": "Prof. Benoy Kumar Sarkar", "era": "1914 CE", "contribution": "Translated and analyzed Śukranīti's legal and sociological chapters."}
        ],
        "important_texts": [
            {"title": "Kautilya's Arthashastra (Books III–IV)", "author": "Kautilya", "period": "Ancient"},
            {"title": "The Sukraniti", "author": "Shukracharya (Trans. B. K. Sarkar)", "period": "1914 CE"}
        ],
        "practical_applications": [
            "Comparative legal history and contract/consumer-protection heritage",
            "Dispute resolution and judicial ethics"
        ],
        "references": [REF_ARCHIVE, REF_MOE_IKS],
        "linked_resource_ids": [27, 28]
    },
    "public-finance-trade": {
        "sanskrit_name": "Kośa & Vārttā (कोश-वार्त्ता)",
        "introduction": "Public Finance and Trade (Kośa and Vārttā) addresses treasury management, agricultural/mineral revenues, price regulation, weights and measures, guilds (Śreṇīs), and customs duties.",
        "detailed_explanation": "Kauṭilya's Arthaśāstra Book II establishes standardized weights and measures (Pautavādhyakṣa), market supervision against adulteration, anti-hoarding rules, and state accounting audits (Akṣapaṭala).",
        "historical_background": "Detailed fiscal and commercial regulations appear in Arthaśāstra and Śukranīti, reflecting thriving overland and maritime trade networks.",
        "important_concepts": [
            {"term": "Vārttā (वार्त्ता)", "meaning": "The productive economy: agriculture, animal husbandry, and trade."},
            {"term": "Śreṇī (श्रेणी)", "meaning": "Self-governing merchant and craft guilds with banking and legal standing."}
        ],
        "major_contributors": [
            {"name": "Kauṭilya", "era": "Ancient", "contribution": "Formulated treasury accounting, taxation principles, and trade regulation."}
        ],
        "important_texts": [
            {"title": "Kautilya's Arthashastra (Book II)", "author": "Kautilya", "period": "Ancient"},
            {"title": "The Sukraniti", "author": "Trans. B. K. Sarkar", "period": "1914 CE"}
        ],
        "practical_applications": [
            "Fiscal policy, market regulation, and consumer-protection history",
            "Auditing and public-expenditure accountability"
        ],
        "references": [REF_NDLI, REF_ARCHIVE],
        "linked_resource_ids": [27, 28]
    },

    # =========================================================================
    # 12. EDUCATION AND LINGUISTICS (1 + 3 subcategories = 4)
    # =========================================================================
    "education-and-linguistics": {
        "sanskrit_name": "Śikṣā, Nirukta & Vāk (शिक्षा-निरुक्त)",
        "introduction": "Indian Education and Linguistics unites ancient pedagogical traditions (Gurukul, Takṣaśilā, Nālandā), phonetics (Śikṣā), etymology (Nirukta), grammar (Vyākaraṇa), and philosophy of language (Vākyapadīya).",
        "detailed_explanation": "Indian linguistics analyzed speech from articulatory phonetics and word-derivation to sentence-level holistic meaning (Sphoṭa), while traditional education emphasized close mentorship, memory, debate (Vāda), and character formation.",
        "historical_background": "Spanning Yāska's Nirukta (c. 6th–5th century BCE), Pāṇini's Aṣṭādhyāyī, Bhartṛhari's Vākyapadīya (c. 5th century CE), and modern IKS curricular syntheses by the Ministry of Education.",
        "important_concepts": [
            {"term": "Śikṣā & Nirukta", "meaning": "Vedic phonetics/pronunciation and semantic etymology."},
            {"term": "Sphoṭa (स्फोट)", "meaning": "Bhartṛhari's theory of indivisible, instantaneous meaning-comprehension."}
        ],
        "major_contributors": [
            {"name": "Yāska", "era": "c. 6th–5th century BCE", "contribution": "Authored Nirukta, the oldest surviving treatise on etymology and semantics."},
            {"name": "Bhartṛhari", "era": "c. 5th century CE", "contribution": "Authored Vākyapadīya on philosophy of language and syntax."}
        ],
        "important_texts": [
            {"title": "The Nighantu and the Nirukta", "author": "Yaska (Trans. Lakshman Sarup)", "period": "1920 CE"},
            {"title": "The Vakyapadiya", "author": "Bhartrihari (Trans. K. A. S. Iyer)", "period": "1965 CE"},
            {"title": "The Ashtadhyayi", "author": "Panini", "period": "Ancient"},
            {"title": "Selected Readings in Indian Knowledge Systems", "author": "IKS Division, MoE", "period": "2023 CE"}
        ],
        "practical_applications": [
            "Modern phonetics, lexicography, and cognitive semantics",
            "NEP 2020 Indian Knowledge Systems higher-education curricula"
        ],
        "references": [REF_MOE_IKS, REF_NDLI, REF_BORI],
        "linked_resource_ids": [18, 29, 30, 32]
    },
    "vedic-pedagogy": {
        "sanskrit_name": "Gurukula & Śikṣā (गुरुकुल-शिक्षा)",
        "introduction": "Vedic Pedagogy encompasses the Gurukul mentorship model, phonetic training (Śikṣā), memorization techniques, and structured philosophical debate (Śāstrārtha / Vāda).",
        "detailed_explanation": "Education began with Upanayana and emphasized self-discipline, oral mastery of texts through analytical recitation (Pada, Krama, Jaṭā, Ghana), and multi-disciplinary study in residential centers like Takṣaśilā and Nālandā.",
        "historical_background": "Documented across Upaniṣads (Taittirīya Upaniṣad Śikṣāvallī), Vedāṅga Śikṣā texts, and modern institutional compilations by the Ministry of Education IKS Division.",
        "important_concepts": [
            {"term": "Svādhyāya (स्वाध्याय)", "meaning": "Lifelong self-study and reflective engagement with texts."},
            {"term": "Śāstrārtha (शास्त्रार्थ)", "meaning": "Structured scholarly debate testing arguments against logic and evidence."}
        ],
        "major_contributors": [
            {"name": "Pāṇini & Yāska", "era": "Ancient", "contribution": "Provided the phonetic and semantic curriculum foundational to Gurukul learning."},
            {"name": "IKS Division, Ministry of Education", "era": "2023 CE", "contribution": "Published modern academic readings integrating IKS into university education."}
        ],
        "important_texts": [
            {"title": "Selected Readings in Indian Knowledge Systems", "author": "IKS Division, Ministry of Education", "period": "2023 CE"},
            {"title": "The Ashtadhyayi of Panini", "author": "Panini", "period": "Ancient"}
        ],
        "practical_applications": [
            "Holistic competency-based and mentor-guided education",
            "Phonetic precision and memory-strengthening pedagogy"
        ],
        "references": [REF_MOE_IKS, REF_VEDIC_HERITAGE],
        "linked_resource_ids": [32, 18]
    },
    "nirukta-etymology": {
        "sanskrit_name": "Nirukta (निरुक्त)",
        "introduction": "Nirukta is the classical Indian science of etymology, lexicography, and hermeneutic semantics, systematically deriving word meanings from verbal roots (Dhātus).",
        "detailed_explanation": "Yāska's Nirukta is a commentary on the Nighaṇṭu (an ancient Vedic thesaurus), dividing all words into four parts of speech—noun (Nāma), verb (Ākhyāta), prefix (Upasarga), and particle (Nipāta)—and arguing that nouns derive from verbal actions.",
        "historical_background": "Composed by Yāska (c. 6th–5th century BCE), predating Pāṇini and representing one of the earliest works of theoretical linguistics anywhere in the world; critically edited and translated by Lakshman Sarup (1920–1927).",
        "important_concepts": [
            {"term": "Catvāri Padajātāni", "meaning": "Fourfold classification of words: Nāma, Ākhyāta, Upasarga, Nipāta."},
            {"term": "Dhātu-ja Theory", "meaning": "Semantic principle that nouns originate from dynamic verbal roots."}
        ],
        "major_contributors": [
            {"name": "Yāska", "era": "c. 6th–5th century BCE", "contribution": "Authored Nirukta, pioneering etymological and semantic analysis."},
            {"name": "Lakshman Sarup", "era": "1920 CE", "contribution": "Critical edition and English translation of Nighaṇṭu and Nirukta."}
        ],
        "important_texts": [
            {"title": "The Nighantu and the Nirukta", "author": "Yaska (Ed./Trans. Lakshman Sarup)", "period": "1920 CE"}
        ],
        "practical_applications": [
            "Historical linguistics, lexicography, and Sanskrit root analysis",
            "Vedic hermeneutics and textual interpretation"
        ],
        "references": [REF_ARCHIVE, REF_BORI],
        "linked_resource_ids": [29, 18]
    },
    "philosophy-of-language": {
        "sanskrit_name": "Śabda-tattva (शब्दतत्त्व)",
        "introduction": "Philosophy of Language in India investigates how sounds, words, and sentences convey meaning, culminating in Bhartṛhari's Vākyapadīya and his celebrated Sphoṭa theory.",
        "detailed_explanation": "Bhartṛhari argues that the primary unit of meaning is not an isolated word or syllable, but the whole sentence (Vākya) grasped as an undivided flash of insight (Sphoṭa / Pratibhā), uniting cognitive science, grammar, and metaphysics.",
        "historical_background": "Composed by Bhartṛhari (c. 5th century CE) in three Kāṇḍas (Brahma-kāṇḍa, Vākya-kāṇḍa, Pada-kāṇḍa), critically translated by K. A. Subramania Iyer (Deccan College, Pune).",
        "important_concepts": [
            {"term": "Sphoṭa (स्फोट)", "meaning": "Indivisible linguistic sign that 'bursts forth' as unified meaning in the listener's mind."},
            {"term": "Parā, Paśyantī, Madhyamā, Vaikharī", "meaning": "Four stages of speech from subtle thought-impulse to audible articulation."}
        ],
        "major_contributors": [
            {"name": "Bhartṛhari", "era": "c. 5th century CE", "contribution": "Authored Vākyapadīya, landmark treatise in philosophy of language."},
            {"name": "K. A. Subramania Iyer", "era": "1965 CE", "contribution": "Authoritative English translation and commentary on Vākyapadīya."}
        ],
        "important_texts": [
            {"title": "The Vakyapadiya of Bhartrihari", "author": "Bhartrihari (Trans. K. A. S. Iyer)", "period": "c. 5th century CE / 1965 CE"}
        ],
        "practical_applications": [
            "Cognitive linguistics, semiotics, and philosophy of mind",
            "Sentence-level semantic parsing in computational linguistics"
        ],
        "references": [REF_BORI, REF_NDLI],
        "linked_resource_ids": [30, 18, 29]
    }
}
