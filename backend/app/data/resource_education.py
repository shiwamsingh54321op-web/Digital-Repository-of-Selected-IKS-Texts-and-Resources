"""
Verified educational study guides, authentic chapter/section breakdowns, Sanskrit
terminology with simple meanings, learning objectives, examples, and recommended
reading for all 32 canonical resources in the IKS Digital Repository.
"""

from typing import Dict, Any

RESOURCE_EDUCATION: Dict[int, Dict[str, Any]] = {
    1: {
        "subject_introduction": "The Āryabhaṭīya (499 CE) is one of the foundational works of classical Indian mathematics and mathematical astronomy, condensing arithmetic, algebra, trigonometry, timekeeping, and planetary astronomy into 121 concise Sanskrit Āryā verses.",
        "historical_context": "Composed by Āryabhaṭa I at Kusumapura (Pāṭaliputra) at age 23, and elucidated by Bhāskara I's detailed 629 CE prose commentary and Someśvara's gloss, this work shaped astronomy across India and the Islamic world.",
        "learning_objectives": [
            "Understand Āryabhaṭa's alphabetic place-value notation (Varga/Avarga consonants).",
            "Trace the derivation of the 24 sine-difference values (Jya) and π ≈ 3.1416.",
            "Learn how Āryabhaṭa explained Earth's axial rotation and solar/lunar eclipses scientifically."
        ],
        "chapters_and_topics": [
            {"section": "1. Gītikāpāda (13 verses)", "topics": "Alphabetic numerical system, cosmological revolutions, and the 24 half-chord sine differences."},
            {"section": "2. Gaṇitapāda (33 verses)", "topics": "Square/cube roots, mensuration, π approximation (62832/20000), arithmetic progressions, and Kuṭṭaka (linear indeterminate equations)."},
            {"section": "3. Kālakriyāpāda (25 verses)", "topics": "Time units (Yuga, Māsa, Dina), planetary conjunctions, and epicyclic eccenter models."},
            {"section": "4. Golapāda (50 verses)", "topics": "Celestial sphere, Earth's rotation causing apparent westward star motion, and geometric eclipse shadow calculations."}
        ],
        "sanskrit_terminology": [
            {"term": "Āryā (आर्या)", "meaning": "Moraic Sanskrit verse meter used for compact mathematical encoding."},
            {"term": "Jya (ज्या)", "meaning": "Half-chord (R·sin θ), foundational to modern trigonometry."},
            {"term": "Kuṭṭaka (कुट्टक)", "meaning": "'Pulverizer' algorithm for solving linear Diophantine equations."},
            {"term": "Bhū-bhramaṇa", "meaning": "Apparent rotation of the sky explained by Earth's daily spin on its axis."}
        ],
        "examples": [
            "Approximation of π (Gaṇitapāda v.10): Add 4 to 100, multiply by 8, and add 62,000 — giving 62,832 as circumference for diameter 20,000 (π ≈ 3.1416, noted as āsanna / 'approximate')."
        ],
        "recommended_reading": [
            "K. S. Shukla & K. V. Sarma (1976), Āryabhaṭīya of Āryabhaṭa, Indian National Science Academy (INSA).",
            "K. Plofker (2009), Mathematics in India, Princeton University Press."
        ]
    },
    2: {
        "subject_introduction": "Līlāvatī (1150 CE) is the first part of Bhāskarācārya's magnum opus Siddhāntaśiromaṇi, serving for centuries as India's premier textbook on arithmetic, proportions, mensuration, and combinatorics.",
        "historical_context": "Written by Bhāskara II (b. 1114 CE, Vijjadavida), Līlāvatī blends poetic word-problems—many addressed playfully to a young learner named Līlāvatī—with rigorous step-by-step computational procedures.",
        "learning_objectives": [
            "Master traditional Indian algorithms for arithmetic, fractions, and root extraction.",
            "Apply the Rule of Three (Trairāśika) and inverse/compound proportions.",
            "Explore permutations, combinations (Aṅkapāśa), and right-triangle mensuration."
        ],
        "chapters_and_topics": [
            {"section": "Paribhāṣā & Parikarma", "topics": "Units of weight/currency/length, positional notation, eight basic operations, and operations with zero (Śūnya)."},
            {"section": "Prakīrṇaka & Vyavahāra", "topics": "Rule of Three/Five/Seven, interest, mixtures, progressions, and cistern/pipe problems."},
            {"section": "Kṣetra & Khāta", "topics": "Areas of triangles, cyclic quadrilaterals, circles, spheres, and excavation volumes."},
            {"section": "Kuṭṭaka & Aṅkapāśa", "topics": "Linear indeterminate equations and combinatorics (permutations of digits/meters)."}
        ],
        "sanskrit_terminology": [
            {"term": "Pāṭīgaṇita", "meaning": "Arithmetic written on a dust-covered calculation board."},
            {"term": "Trairāśika", "meaning": "Rule of Three relating three known quantities to one unknown."},
            {"term": "Aṅkapāśa", "meaning": "Combinatorial permutations and combinations."}
        ],
        "examples": [
            "Swarm of Bees Problem: One-fifth of a swarm flew to a kadamba flower, one-third to a śilīndhra, three times their difference to a kuṭaja, and one remained hovering — find the total number of bees (15)."
        ],
        "recommended_reading": [
            "K. S. Patwardhan, S. A. Naimpally & S. L. Singh (2001), Līlāvatī of Bhāskarācārya, Motilal Banarsidass.",
            "H. T. Colebrooke (1817), Algebra, with Arithmetic and Mensuration, from the Sanscrit of Brahmegupta and Bháscara."
        ]
    },
    3: {
        "subject_introduction": "The Baudhāyana Śulba Sūtra (c. 800 BCE) is the oldest surviving Indian geometric manual, detailing cord-and-peg constructions for Vedic fire altars (Vedi and Citi).",
        "historical_context": "Part of the Baudhāyana Kalpa Sūtra attached to the Kṛṣṇa Yajurveda, it preserves the earliest explicit verbal statement of the diagonal property of rectangles (Pythagorean relation) in the Indian tradition.",
        "learning_objectives": [
            "Understand how Vedic altar geometry motivated area-preserving transformations.",
            "Read Baudhāyana's general statement of the diagonal-square theorem.",
            "Examine the rational series approximation for √2."
        ],
        "chapters_and_topics": [
            {"section": "Paribhāṣā & Units", "topics": "Linear measures (Aṅgula, Pada, Vyāyāma, Puruṣa) and perpendicular construction using a cord."},
            {"section": "Geometric Theorems & Transformations", "topics": "Diagonal of square/rectangle, combining/subtracting squares, and transforming a square into a circle and vice versa."},
            {"section": "Altars (Agni-citi)", "topics": "Falcon-shaped (Śyenaciti), chariot-wheel, and tortoise-shaped multi-layer brick altars."}
        ],
        "sanskrit_terminology": [
            {"term": "Śulba / Rajju", "meaning": "Measuring cord or rope."},
            {"term": "Akṣṇayā-rajju", "meaning": "Diagonal cord of a rectangle."},
            {"term": "Saviśeṣa", "meaning": "Approximation of √2 as 1 + 1/3 + 1/(3×4) - 1/(3×4×34)."}
        ],
        "examples": [
            "Diagonal Theorem (BSS 1.12): 'The diagonal cord of a rectangle produces both (areas) which the flank and the horizontal side produce separately.'"
        ],
        "recommended_reading": [
            "George Thibaut (1875), 'On the Śulvasūtras', Journal of the Asiatic Society of Bengal.",
            "S. N. Sen & A. K. Bag (1983), The Śulbasūtras, Indian National Science Academy."
        ]
    },
    4: {
        "subject_introduction": "The Sūrya Siddhānta is one of the most influential classical textbooks of Indian mathematical astronomy, presenting spherical geometry, planetary longitudes, eclipses, and astronomical instruments.",
        "historical_context": "While an earlier version was summarized by Varāhamihira in the 6th century CE, the extant 14-chapter recension was translated and mathematically annotated by Rev. Ebenezer Burgess and W. D. Whitney in 1860.",
        "learning_objectives": [
            "Understand mean vs. true planetary motion using Manda and Śīghra corrections.",
            "Learn how solar and lunar eclipses are predicted geometrically.",
            "Explore classical astronomical instruments described in Chapter 13."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–2: Mean & True Motions", "topics": "Kalpa/Mahāyuga cycles, sine tables, and epicyclic equations of center."},
            {"section": "Ch. 3: Direction, Place & Time", "topics": "Gnomon shadows, equinoctial shadow, latitude, and solar declination."},
            {"section": "Ch. 4–6: Lunar & Solar Eclipses", "topics": "Angular diameters, shadow cones, parallax, and eclipse projection."},
            {"section": "Ch. 12–14: Cosmography & Instruments", "topics": "Armillary sphere (Golayantra), water clocks, and calendrical epochs."}
        ],
        "sanskrit_terminology": [
            {"term": "Mahāyuga", "meaning": "4,320,000-year astronomical cycle used to express integer planetary revolution counts."},
            {"term": "Lambana & Nati", "meaning": "Longitudinal and latitudinal lunar parallax in solar eclipses."}
        ],
        "examples": [
            "Chapter 3 gnomon method: Measuring the noon shadow of a 12-aṅgula vertical Śaṅku on the equinox day determines local terrestrial latitude."
        ],
        "recommended_reading": [
            "Ebenezer Burgess (1860), Translation of the Sūrya-Siddhānta, Journal of the American Oriental Society."
        ]
    },
    5: {
        "subject_introduction": "Lagadha's Vedāṅga Jyotiṣa is the earliest surviving Indian treatise on mathematical calendrics, linking lunar Nakṣatras and solar solstices into a 5-year lunisolar cycle.",
        "historical_context": "Preserved in two recensions—Ṛk-jyotiṣa (36 verses) and Yajus-jyotiṣa (43/44 verses)—its observational winter-solstice marker (Śraviṣṭhā/Dhaniṣṭhā) reflects an astronomical epoch around c. 1400–1100 BCE, with textual redaction in the 1st millennium BCE.",
        "learning_objectives": [
            "Understand the 5-year Yuga (Pañcavarṣa-yuga) of 1,830 civil days and 62 synodic months.",
            "Learn how intercalary months (Adhimāsa) synchronize lunar and solar calendars.",
            "Examine early linear rules for daylight duration between solstices."
        ],
        "chapters_and_topics": [
            {"section": "Yuga & Solstices", "topics": "5-year cycle, 67 sidereal lunar months, 62 synodic months, and 2 intercalary months."},
            {"section": "Nakṣatra & Tithi Algorithms", "topics": "Computing the Moon's Nakṣatra, Parvan (New/Full Moon), and Viṣuva (equinox)."},
            {"section": "Daylight Variation", "topics": "Linear interpolation of day-length between 12 Muhūrtas (winter solstice) and 18 Muhūrtas (summer solstice)."}
        ],
        "sanskrit_terminology": [
            {"term": "Yuga (युग)", "meaning": "Here, a 5-year luni-solar calendrical cycle."},
            {"term": "Muhūrta (मुहूर्त)", "meaning": "Traditional time unit equal to 1/30th of a 24-hour day (48 minutes)."}
        ],
        "examples": [
            "Daylight rule: Between winter and summer solstice (183 days), daytime increases by 6 Muhūrtas (144 minutes total, or ~47 seconds per day)."
        ],
        "recommended_reading": [
            "T. S. Kuppanna Sastry & K. V. Sarma (1985), Vedāṅga Jyotiṣa of Lagadha, INSA."
        ]
    },
    6: {
        "subject_introduction": "The Caraka Saṁhitā is the foundational compendium of Ayurvedic internal medicine (Kāyacikitsā), integrating clinical diagnostics, pharmacology, dietetics, and physician ethics.",
        "historical_context": "Originally taught by Ātreya Punarvasu and recorded by Agniveśa, later revised by Caraka and completed by Dṛḍhabala (c. 4th–5th century CE). Vaidya Jadavji Trikamji Acharya's critical edition is the global academic standard.",
        "learning_objectives": [
            "Learn the Tridoṣa model (Vāta, Pitta, Kapha) and Saptadhātu physiology.",
            "Understand Caraka's emphasis on Dinacaryā (daily routine) and Hitāhāra (wholesome diet).",
            "Examine the Caraka Śapatha (physician's ethical oath) and clinical reasoning (Yukti)."
        ],
        "chapters_and_topics": [
            {"section": "1. Sūtrasthāna (30 chapters)", "topics": "Fundamental axioms, Tridoṣa, 50 Mahākaṣāya herb groups, dietetics, and daily hygiene."},
            {"section": "2. Nidāna & Vimānasthāna (16 chapters)", "topics": "Pathology of eight major diseases, epidemiology (Janapadoddhvaṁsa), and medical education."},
            {"section": "3. Śārīra & Indriyasthāna (20 chapters)", "topics": "Embryology, anatomy, consciousness, and prognostic signs."},
            {"section": "4. Cikitsā, Kalpa & Siddhisthāna (54 chapters)", "topics": "Clinical therapeutics, Rasāyana rejuvenation, pharmaceutics, and Pañcakarma purification."}
        ],
        "sanskrit_terminology": [
            {"term": "Prakṛti (प्रकृति)", "meaning": "Innate constitutional balance of Vāta, Pitta, and Kapha."},
            {"term": "Agni (अग्नि)", "meaning": "Digestive and metabolic transformation capacity."},
            {"term": "Yukti (युक्ति)", "meaning": "Rational clinical synthesis of multiple diagnostic factors."}
        ],
        "examples": [
            "Preventive maxim (Sūtrasthāna 1.53): 'Health is the supreme foundation of Dharma, Artha, Kāma, and Mokṣa.'"
        ],
        "recommended_reading": [
            "P. V. Sharma (1981–1994), Caraka-Saṁhitā (Text with English Translation), Chaukhambha Orientalia."
        ]
    },
    7: {
        "subject_introduction": "The Suśruta Saṁhitā is the premier classical treatise of Indian surgery (Śalya-tantra), renowned for its systematic classification of surgical instruments, anatomical dissection, and reconstructive procedures.",
        "historical_context": "Associated with Dhanvantari's surgical school at Vārāṇasī and redacted by Suśruta and Nāgārjuna; Kaviraj Kunja Lal Bhishagratna's 3-volume translation (1907–1916) introduced its surgical descriptions worldwide.",
        "learning_objectives": [
            "Identify Suśruta's 101 blunt (Yantra) and 20 sharp (Śastra) surgical instruments.",
            "Understand the eight canonical surgical techniques (Aṣṭavidha Śastrakarma).",
            "Study classical pedicle-flap rhinoplasty and wound-healing protocols."
        ],
        "chapters_and_topics": [
            {"section": "Sūtrasthāna (46 chapters)", "topics": "Training on vegetables/models, instruments, cautery (Kṣāra/Agni), leech therapy, and wound care."},
            {"section": "Nidāna & Śārīrasthāna (26 chapters)", "topics": "Surgical pathology, Marma vital points (107), and cadaveric dissection methodology."},
            {"section": "Cikitsā & Kalpasthāna (48 chapters)", "topics": "Fractures, lithotomy, fistulas, ophthalmic surgery, and toxicology (Agadatantra)."},
            {"section": "Uttaratantra (66 chapters)", "topics": "Ophthalmology (76 eye diseases including cataract), ENT, pediatrics, and internal medicine."}
        ],
        "sanskrit_terminology": [
            {"term": "Śalya (शल्य)", "meaning": "Foreign body or surgical intervention."},
            {"term": "Marma (मर्म)", "meaning": "107 vital anatomical junctions of muscles, vessels, nerves, bones, and joints."},
            {"term": "Nāsā-sandhāna", "meaning": "Surgical reconstruction of a severed nose using a cheek/forehead skin flap."}
        ],
        "examples": [
            "Surgical Simulation (Sūtrasthāna Ch. 9): Students practiced incisions on gourds, probing on worm-eaten wood, and suturing on leather before operating on patients."
        ],
        "recommended_reading": [
            "K. L. Bhishagratna (1907), The Sushruta Samhita, Calcutta.",
            "G. D. Singhal (2007), Ancient Indian Surgery Series, Chaukhamba Sanskrit Pratishthan."
        ]
    },
    8: {
        "subject_introduction": "Surapāla's Vṛkṣāyurveda (c. 1000 CE) is a comprehensive Sanskrit treatise on arboriculture, horticulture, soil classification, seed treatment, grafting, and organic plant protection.",
        "historical_context": "Preserved in a rare manuscript at the Bodleian Library, Oxford, and translated with modern agricultural validation by Nalini Sadhale and Y. L. Nene (Asian Agri-History Foundation, 1996).",
        "learning_objectives": [
            "Understand how Ayurvedic Tridoṣa principles were adapted to diagnose plant disorders.",
            "Learn the preparation and benefits of Kuṇapajala fermented organic bio-fertilizer.",
            "Explore ancient grafting, seed soaking, and companion-planting methods."
        ],
        "chapters_and_topics": [
            {"section": "Soil & Seed Selection", "topics": "Three soil types (Jāṅgala, Anūpa, Sādhāraṇa) and pre-sowing seed treatments."},
            {"section": "Planting & Propagation", "topics": "Optimal spacing, pit preparation, cuttings, and grafting techniques."},
            {"section": "Nourishment (Kuṇapajala)", "topics": "Fermented organic liquid manures for vigorous flowering and fruiting."},
            {"section": "Plant Pathology & Therapy", "topics": "Vāta/Pitta/Kapha plant disorders and botanical pest remedies (neem, viḍaṅga, mustard)."}
        ],
        "sanskrit_terminology": [
            {"term": "Kuṇapajala", "meaning": "Fermented organic nutrient solution used as a bio-stimulant."},
            {"term": "Dohada (दोहद)", "meaning": "Specialized horticultural treatments to induce timely flowering and fruiting."}
        ],
        "examples": [
            "Seed Treatment: Seeds soaked in milk, rubbed with cow-dung and viḍaṅga (Embelia ribes) show improved germination and fungal resistance."
        ],
        "recommended_reading": [
            "Nalini Sadhale (1996), Surapala's Vrikshayurveda, Asian Agri-History Foundation."
        ]
    },
    9: {
        "subject_introduction": "Patañjali's Yoga Sūtras form the foundational text of Classical Rāja Yoga, presenting a systematic psychology of attention, ethics, meditation, and inner freedom.",
        "historical_context": "Compiled between c. 200 BCE and 400 CE, accompanied by Vyāsa's Yoga-bhāṣya and Vācaspati Miśra's Tattvavaiśāradī; translated rigorously by James Haughton Woods (Harvard Oriental Series, 1914).",
        "learning_objectives": [
            "Distinguish the five types of mental fluctuations (Citta-vṛtti) and five afflictions (Kleśas).",
            "Trace the eight limbs of Aṣṭāṅga Yoga from ethical conduct to Samādhi.",
            "Understand Abhyāsa (steady practice) and Vairāgya (non-attachment)."
        ],
        "chapters_and_topics": [
            {"section": "1. Samādhipāda (51 sūtras)", "topics": "Definition of Yoga, mental modifications, Abhyāsa-Vairāgya, and levels of meditative absorption."},
            {"section": "2. Sādhanapāda (55 sūtras)", "topics": "Kriyā Yoga, five Kleśas, Karma, and the first five external limbs (Yama to Pratyāhāra)."},
            {"section": "3. Vibhūtipāda (56 sūtras)", "topics": "Internal limbs (Dhāraṇā, Dhyāna, Samādhi / Saṁyama) and subtle perceptual capacities."},
            {"section": "4. Kaivalyapāda (34 sūtras)", "topics": "Nature of mind, liberation (Kaivalya), and freedom from conditioned habits."}
        ],
        "sanskrit_terminology": [
            {"term": "Citta-vṛtti", "meaning": "Cognitive patterns: valid knowledge, error, imagination, sleep, and memory."},
            {"term": "Saṁyama", "meaning": "Combined mastery of concentration (Dhāraṇā), meditation (Dhyāna), and absorption (Samādhi)."}
        ],
        "examples": [
            "YS 1.2 & 1.12: 'Yoga is the calming of the fluctuations of the mind' — achieved through steady practice (Abhyāsa) and non-attachment (Vairāgya)."
        ],
        "recommended_reading": [
            "J. H. Woods (1914), The Yoga-System of Patañjali, Harvard University Press.",
            "Edwin F. Bryant (2009), The Yoga Sūtras of Patañjali, North Point Press."
        ]
    },
    10: {
        "subject_introduction": "Īśvarakṛṣṇa's Sāṁkhya Kārikā (72 verses) is the oldest complete surviving text of the Sāṁkhya philosophical school, mapping reality into 25 evolutionary principles (Tattvas).",
        "historical_context": "Composed c. 4th century CE and commented on by Gauḍapāda and Vācaspati Miśra; translated by H. T. Colebrooke and H. H. Wilson (1837), forming a cornerstone of comparative Indian philosophy.",
        "learning_objectives": [
            "Understand the dualism of conscious Puruṣa and dynamic Prakṛti.",
            "Analyze the three Guṇas (Sattva, Rajas, Tamas) and the 25 Tattvas.",
            "Examine Satkāryavāda (pre-existence of effect in cause) and Pramāṇas."
        ],
        "chapters_and_topics": [
            {"section": "Verses 1–21: Epistemology & Cause", "topics": "Threefold suffering, three Pramāṇas, Satkāryavāda, and proofs for Puruṣa and Prakṛti."},
            {"section": "Verses 22–52: Evolution of 25 Tattvas", "topics": "Buddhi (intellect), Ahaṁkāra (ego), Manas, 10 sense/action organs, 5 Tanmātras, and 5 gross elements."},
            {"section": "Verses 53–72: Liberation", "topics": "Discriminative discernment (Viveka-khyāti) freeing Puruṣa from misidentification."}
        ],
        "sanskrit_terminology": [
            {"term": "Tattva (तत्त्व)", "meaning": "25 fundamental ontological categories of consciousness, mind, and matter."},
            {"term": "Viveka (विवेक)", "meaning": "Clear discrimination between conscious awareness (Puruṣa) and mental-material nature (Prakṛti)."}
        ],
        "examples": [
            "Blind & Lame Analogy (Kārikā 21): Prakṛti (active but non-conscious) and Puruṣa (conscious but non-acting) cooperate like a blind person carrying a lame person to reach a destination."
        ],
        "recommended_reading": [
            "G. J. Larson (1979), Classical Sāṁkhya, Motilal Banarsidass."
        ]
    },
    11: {
        "subject_introduction": "The Ṛgveda Saṁhitā (1,028 hymns in 10 Maṇḍalas) is the oldest surviving Vedic text, preserving early Indian cosmology, poetic meter, ethics, and philosophical inquiry.",
        "historical_context": "Edited critically by F. Max Müller alongside Sāyaṇācārya's 14th-century Sanskrit commentary (Bhāṣya), capturing both ancient Vedic Sanskrit and medieval exegetical tradition.",
        "learning_objectives": [
            "Explore the 10-Maṇḍala organization and Family Books (Maṇḍalas II–VII).",
            "Study philosophical hymns such as Nāsadīya Sūkta (10.129) and Puruṣa Sūkta (10.90).",
            "Appreciate the role of Sāyaṇa's Bhāṣya and oral Pāṭha preservation."
        ],
        "chapters_and_topics": [
            {"section": "Maṇḍalas II–VII (Family Books)", "topics": "Hymns by Gṛtsamada, Viśvāmitra, Vāmadeva, Atri, Bharadvāja, and Vasiṣṭha lineages."},
            {"section": "Maṇḍalas I, VIII, IX", "topics": "Poetic hymns, Soma Pavamāna hymns (Maṇḍala IX), and cosmic riddles (Asya Vāmīya 1.164)."},
            {"section": "Maṇḍala X", "topics": "Cosmological, philosophical, dialogue, and social hymns (Nāsadīya, Hiraṇyagarbha, Saṁjñāna)."}
        ],
        "sanskrit_terminology": [
            {"term": "Sūkta (सूक्त)", "meaning": "'Well-spoken' Vedic hymn composed of metrical Ṛc verses."},
            {"term": "Ṛta (ऋत)", "meaning": "Universal cosmic order and truth."}
        ],
        "examples": [
            "Rigveda 1.89.1 (Ā no bhadrāḥ): 'Let noble thoughts come to us from every direction.'"
        ],
        "recommended_reading": [
            "Stephanie W. Jamison & Joel P. Brereton (2014), The Rigveda: The Earliest Religious Poetry of India, Oxford University Press."
        ]
    },
    12: {
        "subject_introduction": "The Sāmaveda ('Veda of Melodies') adapts Ṛgvedic hymns into chanted musical melodies (Sāmans), preserving the earliest musical notation and tonal system of India.",
        "historical_context": "Translated by Ralph T. H. Griffith (1893) from the Kauthuma recension, this corpus is the recognized Vedic root of Indian classical music.",
        "learning_objectives": [
            "Understand the relationship between textual Ṛc verses and musical Sāman melodies.",
            "Examine the Ārcika and Gāna divisions of Sāmavedic chant."
        ],
        "chapters_and_topics": [
            {"section": "Pūrvārcika", "topics": "585 single stanzas arranged by deity (Agni, Indra, Soma) serving as melodic templates."},
            {"section": "Uttarārcika", "topics": "400 three-verse triplets (Tṛcas) chanted in Soma rituals."},
            {"section": "Gāna Manuals", "topics": "Grāmageya and Āraṇyageya melodic notations."}
        ],
        "sanskrit_terminology": [
            {"term": "Sāman", "meaning": "Sacred chant melody with prolonged vowels and musical syllables (Stobha)."},
            {"term": "Svara", "meaning": "Musical pitch/tone (seven Vedic Svaras corresponding to later classical notes)."}
        ],
        "examples": [
            "Stobha syllables (such as 'hau', 'hāyi', 'oṁ') inserted during Sāman chanting for rhythmic and melodic balance."
        ],
        "recommended_reading": [
            "Wayne Howard (1977), Samavedic Chant, Yale University Press."
        ]
    },
    13: {
        "subject_introduction": "The White Yajurveda (Vājasaneyi Saṁhitā) compiles 40 Adhyāyas of ritual formulas, civic prayers, and early philosophical hymns—concluding with the Īśāvāsya Upaniṣad.",
        "historical_context": "Transmitted in Mādhyandina and Kāṇva recensions and translated by R. T. H. Griffith (1899), it also records decimal number names up to 10^12 (Parārdha) in Chapter 17.",
        "learning_objectives": [
            "Distinguish Śukla (White) and Kṛṣṇa (Black) Yajurveda traditions.",
            "Locate early decimal numeration (Adhyāya 17) and the Īśā Upaniṣad (Adhyāya 40)."
        ],
        "chapters_and_topics": [
            {"section": "Adhyāyas 1–18", "topics": "New/Full Moon rituals, Agnicayana altar chants, and large decimal number lists (Adhyāya 17.2)."},
            {"section": "Adhyāyas 19–39", "topics": "Rājasūya, Aśvamedha, and Śatarudriya hymns."},
            {"section": "Adhyāya 40", "topics": "Īśāvāsya Upaniṣad—earliest Upaniṣad embedded directly in a Saṁhitā."}
        ],
        "sanskrit_terminology": [
            {"term": "Yajus (यजुस्)", "meaning": "Prose sacrificial formula."},
            {"term": "Parārdha (परार्ध)", "meaning": "Decimal number 10^12 listed in Vājasaneyi Saṁhitā 17.2."}
        ],
        "examples": [
            "Īśāvāsya Upaniṣad v.1 (VS 40.1): 'All this universe is pervaded by the Supreme; enjoy with detachment, do not covet another's wealth.'"
        ],
        "recommended_reading": [
            "Frits Staal (2008), Discovering the Vedas, Penguin Books."
        ]
    },
    14: {
        "subject_introduction": "The Atharvaveda Saṁhitā (20 Kāṇḍas, ~730 hymns) preserves ancient Indian healing remedies, botany, household rites, statecraft, and ecological hymns such as the Bhūmi Sūkta.",
        "historical_context": "Translated with critical text-notes by William Dwight Whitney and edited posthumously by Charles Rockwell Lanman (Harvard Oriental Series, 1905), it provides unmatched insight into everyday Vedic society.",
        "learning_objectives": [
            "Explore early Vedic healing traditions (Bhaiṣajya) linking to Āyurveda.",
            "Read the Bhūmi Sūkta (Book 12, Hymn 1) as an ancient ecological charter."
        ],
        "chapters_and_topics": [
            {"section": "Books 1–7", "topics": "Short hymns on healing fevers, wounds, herbs, longevity, and harmony."},
            {"section": "Books 8–12", "topics": "Philosophical hymns, Skambha, Kāla (Time), and Bhūmi Sūkta (12.1)."},
            {"section": "Books 13–20", "topics": "Marriage hymns (Book 14), Vrātya (Book 15), and funerary/royal hymns."}
        ],
        "sanskrit_terminology": [
            {"term": "Oṣadhi (ओषधि)", "meaning": "Medicinal healing herb."},
            {"term": "Mātā Bhūmiḥ", "meaning": "'Earth is my mother, and I am her child' (AV 12.1.12)."}
        ],
        "examples": [
            "Atharvaveda 12.1.11–12 celebrates Earth's mountains, rivers, diverse languages, and ecosystems, praying that whatever we dig from her may regenerate swiftly."
        ],
        "recommended_reading": [
            "Maurice Bloomfield (1897), Hymns of the Atharva-Veda, Sacred Books of the East Vol. 42."
        ]
    },
    15: {
        "subject_introduction": "Kālidāsa's Abhijñānaśākuntalam ('The Recognition of Śakuntalā') is universally acclaimed as the masterpiece of classical Sanskrit drama, weaving human emotion, nature, and dharma across seven acts.",
        "historical_context": "Composed c. 4th–5th century CE during the Gupta era; Sir Monier Monier-Williams' 1876 critical edition with Devanagari text and notes remains a classic pedagogical resource.",
        "learning_objectives": [
            "Analyze the seven-act dramatic structure (Sandhis) and Rasa evocation.",
            "Observe the bilingual interplay of Sanskrit and Prakrit in classical theatre."
        ],
        "chapters_and_topics": [
            {"section": "Acts I–III", "topics": "King Duṣyanta meets Śakuntalā in Kaṇva's forest hermitage; mutual love."},
            {"section": "Act IV (Celebrated Act)", "topics": "Durvāsas' curse and Śakuntalā's poignant farewell from the forest."},
            {"section": "Acts V–VII", "topics": "Rejection at court, recovery of the signet ring, and celestial reunion."}
        ],
        "sanskrit_terminology": [
            {"term": "Abhijñāna (अभिज्ञान)", "meaning": "Token of recognition (the royal signet ring)."},
            {"term": "Śṛṅgāra & Karuṇa Rasa", "meaning": "Aesthetic sentiments of love and pathos."}
        ],
        "examples": [
            "Act IV: Even the forest deer, creepers, and trees grieve as Śakuntalā departs Kaṇva's āśrama—illustrating Kālidāsa's ecological empathy."
        ],
        "recommended_reading": [
            "Chandra Rajan (1989), Kālidāsa: The Loom of Time, Penguin Classics."
        ]
    },
    16: {
        "subject_introduction": "Kālidāsa's Meghadūta ('The Cloud Messenger') is a 115-stanza lyrical masterpiece (Khaṇḍakāvya) in Mandākrāntā meter, tracing an exiled Yakṣa's message across the geography of classical India.",
        "historical_context": "Edited with Vallabhadeva's 10th-century Kashmirian commentary by E. Hultzsch (1911), Meghadūta founded the 'Dūta-kāvya' (messenger-poem) genre in Indian literature.",
        "learning_objectives": [
            "Appreciate the musical cadence of the 17-syllable Mandākrāntā meter.",
            "Trace the cultural geography of India from Rāmagiri to Ujjayinī and the Himalayas."
        ],
        "chapters_and_topics": [
            {"section": "Pūrvamegha (Part I)", "topics": "The exiled Yakṣa begs a monsoon cloud to travel north across Central India, Ujjain, and Kurukṣetra."},
            {"section": "Uttaramegha (Part II)", "topics": "Description of mythical Alakāpurī in the Himalayas and the message of hope to his spouse."}
        ],
        "sanskrit_terminology": [
            {"term": "Mandākrāntā", "meaning": "'Slow-stepping' 17-syllable meter evoking yearning and majesty."},
            {"term": "Vipralambha Śṛṅgāra", "meaning": "Aesthetic sentiment of love in separation."}
        ],
        "examples": [
            "Stanza 14–25: Vivid poetic geography describing the Narmadā, Vidisha, and the temple bells of Mahākāla in Ujjayinī."
        ],
        "recommended_reading": [
            "Mallinātha's Sañjīvanī commentary; Leonard Nathan (1976), The Transport of Love: The Meghadūta of Kālidāsa."
        ]
    },
    17: {
        "subject_introduction": "Bharata Muni's Nāṭyaśāstra (36 chapters, ~6,000 verses) is the encyclopedic foundational treatise of Indian performing arts—covering theatre architecture, acting, dance, music, poetics, and Rasa theory.",
        "historical_context": "Compiled c. 200 BCE – 200 CE and translated critically by Manomohan Ghosh (1951), it is often termed the 'Fifth Veda' (Nāṭyaveda) accessible to all sections of society.",
        "learning_objectives": [
            "Master the Rasa Sūtra (Vibhāva, Anubhāva, Vyabhicāribhāva → Rasa).",
            "Explore the 4 Abhinayas, 108 dance Karaṇas, and classical stage construction."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–5: Origin, Theatre & Preliminaries", "topics": "Construction of rectangular/square playhouses (Vikṛṣṭa, Caturasra) and Pūrvaraṅga."},
            {"section": "Ch. 6–7: Rasa & Bhāva", "topics": "Eight Rasas, eight Sthāyibhāvas, and 33 transitory emotional states."},
            {"section": "Ch. 8–13: Āṅgika Abhinaya", "topics": "Movements of eyes, neck, hands (Mudrās), and 108 Karaṇas."},
            {"section": "Ch. 28–33: Music & Instruments", "topics": "22 Śrutis, Grāma scales, string, wind, and percussion instruments."}
        ],
        "sanskrit_terminology": [
            {"term": "Rasa (रस)", "meaning": "Distilled aesthetic relish experienced by a perceptive spectator (Sahr̥daya)."},
            {"term": "Abhinaya", "meaning": "Fourfold dramatic communication (bodily, verbal, costume/makeup, subtle emotion)."}
        ],
        "examples": [
            "Ch. 6: Bharata compares Rasa to culinary taste—just as spices and ingredients combine to create a unified flavor, emotions and gestures combine to evoke Rasa."
        ],
        "recommended_reading": [
            "Kapila Vatsyayan (1996), Bharata: The Nāṭyaśāstra, Sahitya Akademi."
        ]
    },
    18: {
        "subject_introduction": "Pāṇini's Aṣṭādhyāyī ('Eight Chapters') is a 3,959-sūtra formal generative grammar of Sanskrit, celebrated globally for its algorithmic economy, recursion, and meta-linguistic precision.",
        "historical_context": "Composed c. 5th–4th century BCE in Śalātura (Gandhāra), commented on by Kātyāyana and Patañjali, and translated in full by Srisa Chandra Vasu (1891–1898).",
        "learning_objectives": [
            "Understand how the 14 Śiva Sūtras generate compact Pratyāhāra sound classes.",
            "Learn how Sūtra brevity (Lāghava) works via Anuvṛtti (context inheritance) and Kāraka theory."
        ],
        "chapters_and_topics": [
            {"section": "Śiva Sūtras & Adhyāya 1", "topics": "14 phonetic aphorisms, technical definitions (Saṁjñā), meta-rules (Paribhāṣā), and Kāraka syntax."},
            {"section": "Adhyāyas 2–5", "topics": "Compounds (Samāsa), verbal roots (Dhātupāṭha), primary (Kṛt) and secondary (Taddhita) suffixes."},
            {"section": "Adhyāyas 6–8", "topics": "Phonological Sandhi rules, reduplication, accentuation, and Asiddha rule-ordering."}
        ],
        "sanskrit_terminology": [
            {"term": "Pratyāhāra", "meaning": "Compact abbreviation denoting a range of phonemes (e.g., 'ac' = all vowels)."},
            {"term": "Anuvṛtti", "meaning": "Carry-over of terms from earlier sūtras into subsequent sūtras to avoid repetition."}
        ],
        "examples": [
            "Rule 6.1.77 (iko yaṇ aci): 'i, u, ṛ, ḷ' become 'y, v, r, l' when followed by a vowel—generating Sandhi forms like prati + eka → pratyeka."
        ],
        "recommended_reading": [
            "George Cardona (1997), Pāṇini: His Work and Its Traditions, Motilal Banarsidass."
        ]
    },
    19: {
        "subject_introduction": "Mayamata is a premier South Indian Sanskrit treatise on Vāstu Śāstra, providing systematic instructions for site selection, residential architecture, temples, town planning, and iconography.",
        "historical_context": "Composed between the 9th and 12th centuries CE in the Śaiva Āgama tradition; critically edited and translated by Bruno Dagens (IGNCA / Motilal Banarsidass, 1994).",
        "learning_objectives": [
            "Examine traditional soil-testing, site orientation, and modular grid (Pada-vinyāsa) rules.",
            "Understand courtyard housing design (Śālā / Catuḥśālā) and proportion systems."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–8: Site & Grid", "topics": "Site examination, linear measurements, Vāstupuruṣa-maṇḍala grids (1 to 1,024 squares), and village/town layouts."},
            {"section": "Ch. 9–25: Temples & Towers", "topics": "Foundations, plinths (Adhiṣṭhāna), pillars, entablatures, and tiered Vimāna superstructures."},
            {"section": "Ch. 26–36: Housing & Iconography", "topics": "Residential courtyard homes, pavilions, joinery, and sculptural proportions."}
        ],
        "sanskrit_terminology": [
            {"term": "Āyādi-ṣaḍvarga", "meaning": "Six proportional arithmetic checks ensuring structural and harmonic balance."},
            {"term": "Adhiṣṭhāna", "meaning": "Molded stone plinth elevating and protecting the superstructure from moisture."}
        ],
        "examples": [
            "Site Testing (Ch. 4): Digging a 1-cubit pit, refilling it, and checking whether the soil overflows (dense/ideal), matches, or settles below level."
        ],
        "recommended_reading": [
            "Bruno Dagens (1994), Mayamata: An Indian Treatise on Housing Architecture and Iconography, IGNCA."
        ]
    },
    20: {
        "subject_introduction": "Mānasāra ('Essence of Measurement') is the most comprehensive surviving encyclopedia of Indian architecture and sculpture, spanning 70 chapters from town planning to temple engineering and iconography.",
        "historical_context": "Translated in full with an accompanying architectural dictionary by Prasanna Kumar Acharya (Oxford University Press, 1934), serving as a foundational reference for South Asian art and architectural history.",
        "learning_objectives": [
            "Identify the eight classical town-planning patterns described in Mānasāra.",
            "Understand the proportional Tālamāna system used across architecture and sculpture."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–10: Measurement & Town Planning", "topics": "Units from atom (Paramāṇu) to Daṇḍa, soil/orientation, and 8 city layouts."},
            {"section": "Ch. 11–40: Buildings & Temples", "topics": "Multi-storeyed buildings (1–12 storeys), pillars, doors, and gateways (Gopuras)."},
            {"section": "Ch. 41–70: Furniture, Vehicles & Icons", "topics": "Thrones, chariots, and iconometric proportions (Daśatāla, Navatāla)."}
        ],
        "sanskrit_terminology": [
            {"term": "Māna-sāra", "meaning": "Canonical standard of proportional measurement."},
            {"term": "Gopura", "meaning": "Monumental gateway tower framing a temple complex."}
        ],
        "examples": [
            "Ch. 9 describes the Sarvatobhadra town plan: a square/oblong fortified city with four cardinal gates, central civic pavilion, and peripheral gardens."
        ],
        "recommended_reading": [
            "P. K. Acharya (1934), Architecture of Mānasāra, Oxford University Press (reprint IGNCA)."
        ]
    },
    21: {
        "subject_introduction": "Samarāṅgaṇa-Sūtradhāra ('Architect of Human Dwellings') by King Bhoja of Dhārā (11th century CE) is a monumental 83-chapter treatise covering northern Nāgara architecture, town planning, painting, and mechanical automata (Yantras).",
        "historical_context": "Composed by the Paramāra polymath King Bhoja (r. c. 1010–1055 CE) and edited by T. Ganapati Sastri (Gaekwad's Oriental Series, 1924–1925).",
        "learning_objectives": [
            "Compare northern Nāgara temple engineering with southern Drāviḍa treatises.",
            "Explore Chapter 31's descriptions of mechanical automata (Yantras) and hydraulic fountains."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–30: Geography, Cities & Homes", "topics": "Urban planning, royal palaces, and multi-courtyard residential design."},
            {"section": "Ch. 31: Yantravidhāna (Machines)", "topics": "Water-driven fountains, mechanical puppets, timekeepers, and lifting devices."},
            {"section": "Ch. 49–83: Nāgara Temples & Painting", "topics": "Temple typologies, stone joinery, iconography, and Ṣaḍaṅga canons of painting."}
        ],
        "sanskrit_terminology": [
            {"term": "Yantra-bīja", "meaning": "Mechanical prime movers (earth, water, fire, air) analyzed in Chapter 31."},
            {"term": "Nāgara", "meaning": "North Indian temple architecture marked by a curvilinear Śikhara."}
        ],
        "examples": [
            "Chapter 31 describes hydraulic garden fountains (Dhārā-gṛha) powered by elevated water tanks and concealed pipes for summer cooling."
        ],
        "recommended_reading": [
            "S. K. Shukla (1960), Vāstuśāstra: Hindu Science of Architecture (Study of Samarāṅgaṇa-Sūtradhāra)."
        ]
    },
    22: {
        "subject_introduction": "Kṛṣi-Parāśara ('Agriculture by Parāśara') is a 243-verse Sanskrit manual covering monsoon prediction, plowing, bullock care, seed storage, water retention, and harvesting.",
        "historical_context": "Composed between c. 4th and 10th century CE in eastern India; critically translated and evaluated agronomically by Nalini Sadhale, Y. L. Nene, and H. V. L. Bathkal (Asian Agri-History Foundation, 1999).",
        "learning_objectives": [
            "Understand traditional astro-meteorological indicators used to forecast seasonal rainfall.",
            "Examine soil tilth, organic manuring, and water-bunding techniques for rice cultivation."
        ],
        "chapters_and_topics": [
            {"section": "Verses 1–78: Weather & Rainfall", "topics": "Planetary ruler of the year, cloud types (Āvarta, Saṁvarta, Puṣkara, Droṇa), and wind vanes."},
            {"section": "Verses 79–156: Livestock & Plowing", "topics": "Care of draught bullocks, wooden plow (Hala) anatomy, and manure preparation."},
            {"section": "Verses 157–243: Sowing, Water & Harvest", "topics": "Seed preservation, transplanting, water-retaining bunds, and grain storage."}
        ],
        "sanskrit_terminology": [
            {"term": "Hala (हल)", "meaning": "Traditional wooden plow whose eight components are named and dimensioned."},
            {"term": "Puṣyābhiṣeka", "meaning": "Festive post-harvest community thanksgiving."}
        ],
        "examples": [
            "Seed Rule (v. 158): Seeds must be dried thoroughly in the sun, kept away from moisture and salt, and never mixed with leftover weeds."
        ],
        "recommended_reading": [
            "Nalini Sadhale (1999), Krishi-Parashara (Agriculture by Parashara), Asian Agri-History Foundation."
        ]
    },
    23: {
        "subject_introduction": "Vāgbhaṭa's Rasaratnasamuccaya (13th–14th century CE) is the most authoritative Sanskrit manual of Rasaśāstra—covering laboratory architecture, furnaces, distillation apparatus, minerals, and metal extraction.",
        "historical_context": "Translated with detailed chemical commentary by Prof. Damodar Joshi (INSA, 1987), it bridges medieval Indian metallurgy, pharmacy, and chemical engineering.",
        "learning_objectives": [
            "Identify classical Indian chemical apparatus (Pātana, Dolā, Vālukā, and Tiryaṅ-pātana Yantras).",
            "Understand how zinc (Yaśada) was extracted from calamine (Rasaka) by downward distillation."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–5: Minerals & Metals", "topics": "Mahārasas, Uparasas, gems, and extraction of seven metals including zinc from Rasaka."},
            {"section": "Ch. 6–11: Rasaśālā (Laboratory) & Apparatus", "topics": "Design of the chemical lab, 30+ Yantras, crucibles (Mūṣā), furnaces (Koṣṭhī), and Puṭa heating cycles."},
            {"section": "Ch. 12–30: Clinical Formulations", "topics": "Purification (Śodhana) and calcination (Māraṇa) for safe therapeutic Bhasmas."}
        ],
        "sanskrit_terminology": [
            {"term": "Rasaśālā", "meaning": "Well-ventilated, directional chemical laboratory described in Chapter 7."},
            {"term": "Mūṣā (मूषा)", "meaning": "Specialized heat-resistant clay/charcoal crucibles."}
        ],
        "examples": [
            "Chapter 2 (v. 157–164): Heating calamine (Rasaka) with turmeric, chebulic myrobalan, resin, and borax in a brinjal-shaped retort yields metallic zinc—matching archaeological retorts at Zawar."
        ],
        "recommended_reading": [
            "D. Joshi (1987), Rasaratnasamuccaya of Vāgbhaṭa, Indian National Science Academy."
        ]
    },
    24: {
        "subject_introduction": "Prof. R. Balasubramaniam's landmark materials-science monograph explains how the 1,600-year-old Delhi Iron Pillar resists atmospheric rusting despite open-air exposure.",
        "historical_context": "Published in collaboration with IIT Kanpur and INSA (2005), this study integrates Gupta-era epigraphy, forge-welding metallurgy, and X-ray diffraction surface chemistry.",
        "learning_objectives": [
            "Explain the role of high phosphorus (~0.25%) and low sulfur/manganese in forming a passive protective film.",
            "Understand the forge-welding technique used to build the 6-ton pillar."
        ],
        "chapters_and_topics": [
            {"section": "Historical & Epigraphic Context", "topics": "Gupta-era Brāhmī inscription of King Candra (Chandragupta II) and original Viṣṇupada location."},
            {"section": "Metallurgical Structure", "topics": "Alternating ferrite/slag microstructure from bloomery iron lumps forge-welded with hammers."},
            {"section": "Corrosion Science", "topics": "Formation of crystalline iron hydrogen phosphate hydrate passive barrier film."}
        ],
        "sanskrit_terminology": [
            {"term": "Viṣṇudhvaja", "meaning": "Original Gupta-period monumental standard designation in the pillar's Sanskrit inscription."}
        ],
        "examples": [
            "Electrochemical finding: Phosphorus in the slag-metal matrix catalyzes rapid formation of a dense, self-healing crystalline phosphate layer during wet-dry monsoon cycles."
        ],
        "recommended_reading": [
            "R. Balasubramaniam (2002), Delhi Iron Pillar: New Insights, Indian Institute of Advanced Study & Aryan Books."
        ]
    },
    25: {
        "subject_introduction": "Śārṅgadeva's Saṅgītaratnākara ('Ocean of Music and Dance', 13th century CE) is the monumental 7-chapter synthesis of Indian musicology, acoustics, organology, and dance.",
        "historical_context": "Composed at the Yādava court of Devagiri (Maharashtra) and translated into English by C. Kunhan Raja (Adyar Library, 1945), it is revered by both Hindustani and Carnatic traditions.",
        "learning_objectives": [
            "Understand the seven-chapter architecture (Saptādhyāyī) covering pitch, rāga, composition, rhythm, instruments, and dance.",
            "Explore the 22 Śruti microtonal scale and classification of musical instruments."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–2: Svara & Rāga", "topics": "Nāda (sound), 22 Śrutis, 7 Svaras, Grāmas, Mūrchanās, and 264 Rāgas."},
            {"section": "Ch. 3–5: Prakīrṇaka, Prabandha & Tāla", "topics": "Vocal techniques, compositional forms (Prabandha), and 120 Deśī Tālas."},
            {"section": "Ch. 6–7: Vādya & Nartana", "topics": "Fourfold instrument classification (Tata, Suṣira, Avanaddha, Ghana) and classical dance."}
        ],
        "sanskrit_terminology": [
            {"term": "Nāda (नाद)", "meaning": "Resonant musical sound divided into Āhata (struck) and Anāhata (unstruck)."},
            {"term": "Caturvidha Vādya", "meaning": "Chordophones (Tata), aerophones (Suṣira), membranophones (Avanaddha), idiophones (Ghana)."}
        ],
        "examples": [
            "Śārṅgadeva's 4-fold instrument classification anticipates the modern Hornbostel–Sachs system by seven centuries."
        ],
        "recommended_reading": [
            "R. K. Shringy & Prem Lata Sharma (1978–1989), Saṅgītaratnākara of Śārṅgadeva, Motilal Banarsidass."
        ]
    },
    26: {
        "subject_introduction": "Mataṅga Muni's Bṛhaddeśī (c. 6th–8th century CE) is the earliest surviving musicological treatise to define and systematically classify Rāga alongside regional Deśī melodies.",
        "historical_context": "Critically edited and translated by Dr. Prem Lata Sharma (IGNCA Kalāmūlaśāstra Series, 1992–1994), bridging Bharata's Nāṭyaśāstra and medieval musicology.",
        "learning_objectives": [
            "Understand Mataṅga's landmark definition of Rāga ('that which colors the mind').",
            "Distinguish classical Mārga scales from regional Deśī musical traditions."
        ],
        "chapters_and_topics": [
            {"section": "Nāda & Śruti", "topics": "Origin of musical sound and 22-microtone tuning."},
            {"section": "Grāma, Mūrchanā & Jāti", "topics": "Modal scales and twelve-tone Mūrchanā frameworks."},
            {"section": "Rāga-lakṣaṇa", "topics": "Formal characterization of Grāma-rāgas and Bhāṣā melodies."}
        ],
        "sanskrit_terminology": [
            {"term": "Rāga (राग)", "meaning": "Defined by Mataṅga from √rañj ('to color'): a tonal configuration that delights and colors the listener's heart."},
            {"term": "Deśī (देशी)", "meaning": "Regional musical idioms thriving across India's provinces."}
        ],
        "examples": [
            "Bṛhaddeśī v.280: 'That distinctive sound-arrangement adorned with notes and melodic movements which delights the minds of people is called Rāga.'"
        ],
        "recommended_reading": [
            "Prem Lata Sharma (1992), Bṛhaddeśī of Śrī Mataṅga Muni, IGNCA."
        ]
    },
    27: {
        "subject_introduction": "Kauṭilya's Arthaśāstra (15 Books, 150 Chapters) is India's classical encyclopedia of statecraft, public administration, economics, law, taxation, and strategic diplomacy.",
        "historical_context": "Rediscovered in 1905 by Dr. R. Shamasastry at the Mysore Oriental Library and published in English in 1915, reflecting administrative institutions from the Mauryan era through early centuries CE.",
        "learning_objectives": [
            "Understand the Saptāṅga (seven-limb) model of the state and Yogakṣema welfare duty.",
            "Analyze Kauṭilya's administrative departments, anti-corruption audits, and Maṇḍala diplomacy."
        ],
        "chapters_and_topics": [
            {"section": "Books I–II: Training & Departments", "topics": "Royal education, cabinet counsel, and 30+ superintendents (treasury, mines, agriculture, weights, markets)."},
            {"section": "Books III–V: Law & Crisis Finance", "topics": "Civil courts, criminal enforcement, consumer protection, and emergency revenues."},
            {"section": "Books VI–XV: Foreign Policy & Strategy", "topics": "Saptāṅga statecraft, Circle of Kings (Maṇḍala), six-fold diplomacy, and defense."}
        ],
        "sanskrit_terminology": [
            {"term": "Yogakṣema", "meaning": "Protection of what is earned and provision of citizen welfare."},
            {"term": "Ānvīkṣikī", "meaning": "Critical rational inquiry (Sāṁkhya, Yoga, Lokāyata) foundational to policy."}
        ],
        "examples": [
            "Book I, Ch. 19: 'In the happiness of his subjects lies the king's happiness; in their welfare his welfare.'"
        ],
        "recommended_reading": [
            "L. N. Rangarajan (1992), Kautilya: The Arthashastra, Penguin Classics.",
            "Patrick Olivelle (2013), King, Governance, and Law in Ancient India, Oxford University Press."
        ]
    },
    28: {
        "subject_introduction": "The Śukranīti (translated by Prof. Benoy Kumar Sarkar, 1914) is a comprehensive Sanskrit Nīti-śāstra treatise covering constitutional ethics, public finance, salaries, judicial procedures, and civic duties.",
        "historical_context": "Attributed traditionally to Śukrācārya and preserved in late-medieval manuscripts; Sarkar's 1914 edition includes detailed comparative notes on Indian political sociology.",
        "learning_objectives": [
            "Examine Śukranīti's principles of ministerial counsel and accountability.",
            "Explore classical guidelines on fair wages, taxation, and judicial evidence."
        ],
        "chapters_and_topics": [
            {"section": "Ch. 1–2: Ruler & Ministers", "topics": "Qualifications of rulers, council of 8–10 ministers (Prakṛtis), and departmental duties."},
            {"section": "Ch. 3–4: Ethics, Finance & Law", "topics": "Civic conduct, treasury reserves, public works, judicial procedure, and defense."},
            {"section": "Ch. 5: Supplementary Polity", "topics": "Treaties, alliances, and governance maxims."}
        ],
        "sanskrit_terminology": [
            {"term": "Nīti-śāstra", "meaning": "Science of ethical polity, governance, and practical wisdom."},
            {"term": "Prakṛtis", "meaning": "Ministerial portfolios forming the administrative cabinet."}
        ],
        "examples": [
            "Ch. 1.71: 'The king is made by the Creator to be the servant of the people, receiving his revenue as his wage.'"
        ],
        "recommended_reading": [
            "Benoy Kumar Sarkar (1914), The Sukraniti (Sacred Books of the Hindus Vol. 13)."
        ]
    },
    29: {
        "subject_introduction": "Yāska's Nirukta (c. 6th–5th century BCE) is the oldest surviving Indian treatise on etymology, semantics, and Vedic interpretation, commenting on the Nighaṇṭu lexicon.",
        "historical_context": "Predating Pāṇini, Nirukta laid the foundations for Indian lexicography and theoretical linguistics; critically edited and translated by Lakshman Sarup (1920–1927).",
        "learning_objectives": [
            "Learn Yāska's fourfold classification of parts of speech.",
            "Understand the debate between Yāska and Gārgya on whether all nouns derive from verbal roots."
        ],
        "chapters_and_topics": [
            {"section": "Naighaṇṭuka Kāṇḍa (Ch. 1–3)", "topics": "Four parts of speech, grammatical theories, and synonyms for natural phenomena."},
            {"section": "Naigama Kāṇḍa (Ch. 4–6)", "topics": "Homonyms and obscure Vedic words."},
            {"section": "Daivata Kāṇḍa (Ch. 7–12)", "topics": "Etymology and classification of Vedic deities across Earth, Atmosphere, and Heaven."}
        ],
        "sanskrit_terminology": [
            {"term": "Nāma, Ākhyāta, Upasarga, Nipāta", "meaning": "Noun, verb, preverb/prefix, and indeclinable particle."}
        ],
        "examples": [
            "Nirukta 1.1: 'A verb has becoming (Bhāva) as its predominant notion, whereas a noun has being (Sattva) as its predominant notion.'"
        ],
        "recommended_reading": [
            "Lakshman Sarup (1920), The Nighantu and the Nirukta, Oxford University Press (reprint Motilal Banarsidass)."
        ]
    },
    30: {
        "subject_introduction": "Bhartṛhari's Vākyapadīya (c. 5th century CE) is a landmark philosophical treatise on linguistics, cognition, and the nature of meaning—famously formulating the Sphoṭa theory.",
        "historical_context": "Composed in three Kāṇḍas (~2,000 kārikās) and critically translated by K. A. Subramania Iyer (Deccan College, Pune, 1965–1977), it links Pāṇinian grammar with philosophy of mind.",
        "learning_objectives": [
            "Understand Sphoṭa—the holistic, indivisible flash of sentence-meaning.",
            "Explore Bhartṛhari's four levels of speech (Parā, Paśyantī, Madhyamā, Vaikharī)."
        ],
        "chapters_and_topics": [
            {"section": "1. Brahmakāṇḍa", "topics": "Śabda-tattva, Sphoṭa vs. Dhvani (uttered sound), and levels of speech."},
            {"section": "2. Vākyakāṇḍa", "topics": "Primacy of the whole sentence over isolated words; Pratibhā (intuitive grasp of meaning)."},
            {"section": "3. Padakāṇḍa", "topics": "Detailed semantic analysis of universals (Jāti), substance, time, space, and Kāraka."}
        ],
        "sanskrit_terminology": [
            {"term": "Sphoṭa (स्फोट)", "meaning": "The unified linguistic meaning that 'bursts forth' in cognition."},
            {"term": "Pratibhā (प्रतिभा)", "meaning": "Holistic flash of understanding uniting a sentence's meaning."}
        ],
        "examples": [
            "Vākyapadīya 1.123: 'There is no cognition in the world that does not follow language; all knowledge shines as though pierced by speech.'"
        ],
        "recommended_reading": [
            "K. A. Subramania Iyer (1969), Bhartṛhari: A Study of the Vākyapadīya, Deccan College."
        ]
    },
    31: {
        "subject_introduction": "A Concise History of Science in India (INSA, 1971) is the landmark peer-reviewed scholarly survey synthesizing India's scientific contributions across astronomy, mathematics, medicine, chemistry, agriculture, and metallurgy.",
        "historical_context": "Edited by D. M. Bose, S. N. Sen, and B. V. Subbarayappa under the Indian National Science Academy (New Delhi), relying strictly on primary Sanskrit/Prakrit/Persian manuscripts and archaeological findings.",
        "learning_objectives": [
            "Gain an evidence-based interdisciplinary overview of Indian scientific traditions.",
            "Compare textual evidence with archaeological findings in metallurgy, astronomy, and medicine."
        ],
        "chapters_and_topics": [
            {"section": "Astronomy & Mathematics", "topics": "Vedic calendrics, Siddhāntic astronomy, zero, algebra, and Kerala series."},
            {"section": "Medicine & Botany", "topics": "Caraka, Suśruta, botanical classification, and agricultural treatises."},
            {"section": "Chemistry, Metallurgy & Physics", "topics": "Rasaśāstra apparatus, zinc distillation, Wootz steel, and Nyāya-Vaiśeṣika atomism."}
        ],
        "sanskrit_terminology": [
            {"term": "Śāstra & Prayoga", "meaning": "Theoretical scientific treatise paired with empirical craft/experimentation."}
        ],
        "examples": [
            "Documents the continuity from Zawar zinc retorts and Delhi Iron Pillar metallurgy to Siddhāntic planetary trigonometry."
        ],
        "recommended_reading": [
            "D. M. Bose, S. N. Sen & B. V. Subbarayappa (1971/2009), A Concise History of Science in India, Universities Press / INSA."
        ]
    },
    32: {
        "subject_introduction": "Selected Readings in Indian Knowledge Systems (IKS Division, Ministry of Education, Govt. of India) is a contemporary academic anthology introducing NEP 2020 students and educators to IKS foundations and modern applications.",
        "historical_context": "Prepared by the IKS Division (AICTE / Ministry of Education) and hosted via NDLI to provide verified, peer-reviewed introductory modules across disciplines.",
        "learning_objectives": [
            "Understand the NEP 2020 vision for integrating Indian Knowledge Systems into higher education.",
            "Connect classical treatises with contemporary STEM, humanities, management, and sustainability."
        ],
        "chapters_and_topics": [
            {"section": "Module 1: IKS Foundations", "topics": "Caturdaśa Vidyāsthānas, Pramāṇas, and Sanskrit linguistic architecture."},
            {"section": "Module 2: Science, Engineering & Technology", "topics": "Mathematics, astronomy, metallurgy, town planning, and water management."},
            {"section": "Module 3: Health, Ecology & Governance", "topics": "Āyurveda, Yoga, Vṛkṣāyurveda, Arthaśāstra, and aesthetics."}
        ],
        "sanskrit_terminology": [
            {"term": "Vidyāsthāna", "meaning": "Classical 14 or 18 branches of foundational Indian knowledge."}
        ],
        "examples": [
            "Demonstrates how Pāṇinian meta-rules inspire modern computational parsing and how Kuṇḍs inform urban water resilience."
        ],
        "recommended_reading": [
            "B. Mahadevan, Vinayak Rajat Bhat & Nagendra Pavana R. N. (2022), Introduction to Indian Knowledge Systems: Concepts and Applications, PHI Learning."
        ]
    }
}
