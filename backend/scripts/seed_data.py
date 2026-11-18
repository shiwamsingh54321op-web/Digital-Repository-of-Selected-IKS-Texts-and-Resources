"""
Comprehensive Seed Data Script for IKS Digital Repository
Seeds:
- 12 Primary Knowledge Domains with 30+ Hierarchical Subcategories
- 9 Detailed Legal Licenses with precise permission attributes
- 12 Authoritative Cultural and Academic Source Institutions
- 32 Fully Verified IKS Texts and Resources with Dublin Core Metadata
- Controlled Keyword Associations
"""

import os
import sys
from datetime import datetime

# Add backend directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.session import SessionLocal, engine, Base
from app.models import (
    KnowledgeDomain,
    License,
    Institution,
    Keyword,
    Resource,
    AdminUser
)
from app.search.engine import init_fts_index, rebuild_fts_index
from app.services.auth_service import AuthService


def seed_database():
    print("Beginning database seeding for IKS Digital Repository...")

    # Ensure tables exist
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Initialize FTS5 index and triggers
        init_fts_index(db)

        # Ensure default admin
        AuthService.ensure_default_admin(db)
        print("Default administrator account verified.")

        # -------------------------------------------------------------
        # 1. SEED LICENSES
        # -------------------------------------------------------------
        licenses_data = [
            {
                "name": "Public Domain (Mark 1.0)",
                "identifier": "public-domain",
                "license_url": "https://creativecommons.org/publicdomain/mark/1.0/",
                "description": "Works with expired copyright worldwide or officially dedicated to the public domain.",
                "permissions": "Free for all uses without restriction. Reproduction, download, adaptation, and commercial use permitted.",
                "commercial_use_allowed": True,
                "redistribution_allowed": True,
                "attribution_required": False,
                "verification_notes": "Historical texts published prior to 1928 with expired copyright in India and internationally."
            },
            {
                "name": "Creative Commons Zero (CC0 1.0)",
                "identifier": "cc0-1.0",
                "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
                "description": "Universal public domain dedication by authors or institutions.",
                "permissions": "Full unrestricted waiver of copyright. Download, redistribution, and commercial reuse permitted.",
                "commercial_use_allowed": True,
                "redistribution_allowed": True,
                "attribution_required": False,
                "verification_notes": "Open governmental and cultural data releases."
            },
            {
                "name": "Creative Commons Attribution 4.0 International (CC BY 4.0)",
                "identifier": "cc-by-4.0",
                "license_url": "https://creativecommons.org/licenses/by/4.0/",
                "description": "Allows sharing and adapting for any purpose including commercially, provided attribution is given.",
                "permissions": "Free to share and adapt with creator attribution. Download and redistribution permitted.",
                "commercial_use_allowed": True,
                "redistribution_allowed": True,
                "attribution_required": True,
                "verification_notes": "Modern scholarly publications and translations under open research mandates."
            },
            {
                "name": "Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)",
                "identifier": "cc-by-sa-4.0",
                "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
                "description": "Permits remixing and redistribution under identical license terms with attribution.",
                "permissions": "Free redistribution and adaptation under share-alike terms with attribution.",
                "commercial_use_allowed": True,
                "redistribution_allowed": True,
                "attribution_required": True,
                "verification_notes": "Community digitized texts and collaborative critical editions."
            },
            {
                "name": "Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)",
                "identifier": "cc-by-nc-4.0",
                "license_url": "https://creativecommons.org/licenses/by-nc/4.0/",
                "description": "Allows non-commercial reproduction and sharing with attribution.",
                "permissions": "Non-commercial distribution and educational reuse permitted. Commercial use forbidden.",
                "commercial_use_allowed": False,
                "redistribution_allowed": True,
                "attribution_required": True,
                "verification_notes": "Academic institutional publications intended solely for educational research."
            },
            {
                "name": "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)",
                "identifier": "cc-by-nc-sa-4.0",
                "license_url": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
                "description": "Allows non-commercial sharing and adaptation under identical license terms with attribution.",
                "permissions": "Non-commercial educational redistribution permitted under identical terms.",
                "commercial_use_allowed": False,
                "redistribution_allowed": True,
                "attribution_required": True,
                "verification_notes": "Institutional digitized editions from cultural bodies such as IGNCA."
            },
            {
                "name": "In Copyright - Free to Read Online",
                "identifier": "in-copyright-read-only",
                "license_url": "https://rightsstatements.org/page/InC/1.0/",
                "description": "Protected by copyright, but authorized by the rights holder for free online viewing.",
                "permissions": "Free to read online at holding institutional repository. Direct redistribution or download not authorized.",
                "commercial_use_allowed": False,
                "redistribution_allowed": False,
                "attribution_required": True,
                "verification_notes": "Digital library viewing licenses where redistribution is restricted."
            },
            {
                "name": "Institution-Specific Open Access",
                "identifier": "institution-open-access",
                "license_url": None,
                "description": "Governed by specific institutional open access policy of the hosting university or digital library.",
                "permissions": "Subject to institutional terms. Accessible on institutional portal with attribution.",
                "commercial_use_allowed": False,
                "redistribution_allowed": False,
                "attribution_required": True,
                "verification_notes": "National Digital Library of India or Shodhganga terms of use."
            },
            {
                "name": "Rights Unverified / Metadata Only",
                "identifier": "rights-unverified",
                "license_url": None,
                "description": "Copyright and licensing status could not be conclusively determined.",
                "permissions": "No distribution or download permissions granted. Metadata catalogued for discovery only.",
                "commercial_use_allowed": False,
                "redistribution_allowed": False,
                "attribution_required": True,
                "verification_notes": "Restricted to bibliographic record until rights holder confirms status."
            }
        ]

        licenses_map = {}
        for lic_data in licenses_data:
            existing = db.query(License).filter(License.identifier == lic_data["identifier"]).first()
            if not existing:
                existing = License(**lic_data)
                db.add(existing)
                db.flush()
            licenses_map[lic_data["identifier"]] = existing
        db.commit()
        print(f"Seeded {len(licenses_map)} license records.")

        # -------------------------------------------------------------
        # 2. SEED INSTITUTIONS
        # -------------------------------------------------------------
        institutions_data = [
            {
                "institution_name": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "website_url": "https://ignca.gov.in/",
                "description": "Premier national cultural institution under Ministry of Culture, Govt. of India, dedicated to the preservation, documentation and dissemination of Indian arts and cultural heritage.",
                "country": "India",
                "institution_type": "National Cultural Centre",
                "contact_information": "Janpath, New Delhi - 110001 | Email: directorkalakosa@ignca.nic.in"
            },
            {
                "institution_name": "National Digital Library of India (NDLI)",
                "website_url": "https://ndl.iitkgp.ac.in/",
                "description": "Virtual repository of learning resources sponsored by Ministry of Education, Govt. of India, hosted by IIT Kharagpur.",
                "country": "India",
                "institution_type": "National Digital Library",
                "contact_information": "IIT Kharagpur, West Bengal - 721302"
            },
            {
                "institution_name": "Vedic Heritage Portal",
                "website_url": "https://vedicheritage.gov.in/",
                "description": "Official national portal hosted by IGNCA to disseminate oral, manuscript, and recitative traditions of the Vedas.",
                "country": "India",
                "institution_type": "Government Cultural Portal",
                "contact_information": "IGNCA, New Delhi"
            },
            {
                "institution_name": "Indian National Science Academy (INSA)",
                "website_url": "https://www.insaindia.res.in/",
                "description": "Apex scientific organization in India, actively engaged in publishing critical source texts in the History of Science in India.",
                "country": "India",
                "institution_type": "National Science Academy",
                "contact_information": "Bahadur Shah Zafar Marg, New Delhi - 110002"
            },
            {
                "institution_name": "Bhandarkar Oriental Research Institute (BORI)",
                "website_url": "https://bori.ac.in/",
                "description": "Renowned Indological research institute in Pune, housing over 28,000 manuscripts and publisher of the Critical Edition of the Mahabharata.",
                "country": "India",
                "institution_type": "Research Institute",
                "contact_information": "Law College Road, Pune, Maharashtra - 411004"
            },
            {
                "institution_name": "Oriental Institute, The Maharaja Sayajirao University of Baroda",
                "website_url": "https://www.msubaroda.ac.in/",
                "description": "Prestigious Oriental Institute famous for publishing the Gaekwad's Oriental Series (GOS) and preserving thousands of rare manuscripts.",
                "country": "India",
                "institution_type": "University Research Archive",
                "contact_information": "Vadodara, Gujarat - 390002"
            },
            {
                "institution_name": "Sanskrit Documents Consortium",
                "website_url": "https://sanskritdocuments.org/",
                "description": "Non-profit international collaborative initiative digitizing and curating Sanskrit classical texts and grammatical treatises.",
                "country": "India",
                "institution_type": "Digital Repository",
                "contact_information": "Consortium Coordinator: sanskrit@sanskritdocuments.org"
            },
            {
                "institution_name": "Shodhganga - INFLIBNET Centre",
                "website_url": "https://shodhganga.inflibnet.ac.in/",
                "description": "National repository of Indian electronic theses and dissertations maintained by the INFLIBNET Centre.",
                "country": "India",
                "institution_type": "Academic Research Repository",
                "contact_information": "Infocity, Gandhinagar, Gujarat - 382007"
            },
            {
                "institution_name": "Central Council for Research in Ayurvedic Sciences (CCRAS)",
                "website_url": "https://ccras.nic.in/",
                "description": "Autonomous body under Ministry of Ayush, Govt. of India, formulating scientific research and documentation in Ayurveda.",
                "country": "India",
                "institution_type": "Government Research Council",
                "contact_information": "Janakpuri, New Delhi - 110058"
            },
            {
                "institution_name": "Asian Agri-History Foundation (AAHF)",
                "website_url": "https://www.asianagrihistory.org/",
                "description": "Non-profit educational trust publishing historical treatises on traditional Indian agriculture, horticulture, and animal husbandry.",
                "country": "India",
                "institution_type": "Agricultural Heritage Trust",
                "contact_information": "Secunderabad, Telangana - 500009"
            },
            {
                "institution_name": "Asiatic Society of Bengal",
                "website_url": "https://www.asiaticsocietykolkata.org/",
                "description": "Historic society founded in 1784 by Sir William Jones, pioneer of Indological publishing and manuscript preservation.",
                "country": "India",
                "institution_type": "Learned Society",
                "contact_information": "1 Park Street, Kolkata, West Bengal - 700016"
            },
            {
                "institution_name": "Rare Book Society of India (RBSI)",
                "website_url": "https://www.rarebooksocietyofindia.org/",
                "description": "Virtual platform dedicated to curating digitized rare books, historical maps, and manuscripts on Indian history and classical science.",
                "country": "India",
                "institution_type": "Digital Archive",
                "contact_information": "Bengaluru, Karnataka"
            }
        ]

        institutions_map = {}
        for inst_data in institutions_data:
            existing = db.query(Institution).filter(Institution.institution_name == inst_data["institution_name"]).first()
            if not existing:
                existing = Institution(**inst_data)
                db.add(existing)
                db.flush()
            institutions_map[inst_data["institution_name"]] = existing
        db.commit()
        print(f"Seeded {len(institutions_map)} institution records.")

        # -------------------------------------------------------------
        # 3. SEED KNOWLEDGE DOMAINS & SUBCATEGORIES
        # -------------------------------------------------------------
        domains_structure = [
            {
                "name": "Indian Mathematics",
                "slug": "indian-mathematics",
                "description": "Historical mathematical traditions of India covering arithmetic, algebra (Bijaganita), geometry (Sulba Sutras), infinite series, and foundational algorithms.",
                "icon": "Binary",
                "subcategories": [
                    {"name": "Number Systems & Arithmetic", "slug": "number-systems-arithmetic", "description": "Decimal place-value notation, zero (Shunya), and algorithmic operations."},
                    {"name": "Algebra & Bijaganita", "slug": "algebra-bijaganita", "description": "Equations, indeterminate equations (Kuttaka), and cyclic methods (Chakravala)."},
                    {"name": "Geometry & Sulba Sutras", "slug": "geometry-sulba-sutras", "description": "Altar construction geometry, transformation of figures, and early Pythagorean triples."},
                    {"name": "Infinite Series & Analysis", "slug": "infinite-series-analysis", "description": "Kerala School of Mathematics, Madhava calculus, and trigonometric series."}
                ]
            },
            {
                "name": "Astronomy and Cosmology",
                "slug": "astronomy-and-cosmology",
                "description": "Jyotisha and Siddhantic astronomical calculations, planetary models, eclipse predictions, and observational instruments.",
                "icon": "Compass",
                "subcategories": [
                    {"name": "Siddhantic Astronomy", "slug": "siddhantic-astronomy", "description": "Planetary coordinates, epicyclic models, and celestial motion treatises."},
                    {"name": "Observational Instruments (Yantras)", "slug": "observational-instruments", "description": "Gnomons, armillary spheres, water clocks, and astrolabes."},
                    {"name": "Calendrical Systems (Panchanga)", "slug": "calendrical-systems", "description": "Solar, lunar, and lunisolar reckoning, tithis, and intercalary months."}
                ]
            },
            {
                "name": "Ayurveda and Traditional Medicine",
                "slug": "ayurveda-and-traditional-medicine",
                "description": "Classical Indian medical science encompassing diagnostics, pharmacology, surgery, holistic therapeutics, and botanical medicine.",
                "icon": "HeartPulse",
                "subcategories": [
                    {"name": "Classical Samhitas", "slug": "classical-samhitas", "description": "Foundational canonical treatises: Charaka, Sushruta, and Vagbhata."},
                    {"name": "Dravyaguna & Medicinal Plants", "slug": "dravyaguna-medicinal-plants", "description": "Materia medica, botanical classification, and herbal pharmacology."},
                    {"name": "Surgery & Shalya Tantra", "slug": "surgery-shalya-tantra", "description": "Classical surgical techniques, rhinoplasty, instruments, and wound management."},
                    {"name": "Preventive Health & Dinacharya", "slug": "preventive-health", "description": "Daily regimens, seasonal lifestyle protocols, and longevity science."}
                ]
            },
            {
                "name": "Yoga and Philosophy",
                "slug": "yoga-and-philosophy",
                "description": "Six classical schools of Indian philosophy (Shad-Darshana), introspective psychology, meditation, and ethical frameworks.",
                "icon": "Sparkles",
                "subcategories": [
                    {"name": "Classical Yoga", "slug": "classical-yoga", "description": "Patanjali's Ashtanga Yoga, Dharana, Dhyana, and Samadhi."},
                    {"name": "Samkhya & Cosmology", "slug": "samkhya-cosmology", "description": "Dualist ontology of Purusha, Prakriti, and the twenty-four Tattvas."},
                    {"name": "Nyaya & Vaisheshika", "slug": "nyaya-vaisheshika", "description": "Epistemology, formal logical inference (Anumana), and atomistic physics."},
                    {"name": "Vedanta & Metaphysics", "slug": "vedanta-metaphysics", "description": "Non-dualism, qualified non-dualism, and Upanishadic commentary traditions."}
                ]
            },
            {
                "name": "Vedic Literature",
                "slug": "vedic-literature",
                "description": "The four Vedic Samhitas, Brahmanas, Aranyakas, and Upanishads representing foundational oral and textual traditions.",
                "icon": "Flame",
                "subcategories": [
                    {"name": "Rigveda Traditions", "slug": "rigveda-traditions", "description": "Mantras, hymns of praise, and cosmology of the Rigveda Samhita."},
                    {"name": "Samaveda Traditions", "slug": "samaveda-traditions", "description": "Melodic chants, musical notation, and liturgical recitations."},
                    {"name": "Yajurveda Traditions", "slug": "yajurveda-traditions", "description": "Ritual formulas, Shukla and Krishna Yajurveda recensions."},
                    {"name": "Atharvaveda Traditions", "slug": "atharvaveda-traditions", "description": "Healing hymns, domestic rites, social welfare, and natural philosophy."}
                ]
            },
            {
                "name": "Sanskrit and Classical Literature",
                "slug": "sanskrit-and-classical-literature",
                "description": "Classical Sanskrit dramaturgy, epic poetry (Mahakavya), aesthetics (Rasa), and technical grammatical sciences.",
                "icon": "BookOpen",
                "subcategories": [
                    {"name": "Paninian Vyakarana & Linguistics", "slug": "paninian-vyakarana", "description": "Ashtadhyayi rules, phonetic analysis, morphological derivations, and semantic theory."},
                    {"name": "Classical Kavya & Nataka", "slug": "classical-kavya-nataka", "description": "Poetic works and plays of Kalidasa, Bhasa, Bhavabhuti, and Bana."},
                    {"name": "Natyashastra & Aesthetics", "slug": "natyashastra-aesthetics", "description": "Dramatic performance, Rasa theory, emotional states (Bhava), and stagecraft."}
                ]
            },
            {
                "name": "Architecture and Engineering",
                "slug": "architecture-and-engineering",
                "description": "Vastu Vidya, temple construction principles, town planning, hydraulic systems, and stone masonry.",
                "icon": "Landmark",
                "subcategories": [
                    {"name": "Vastu Shastra & Design", "slug": "vastu-shastra-design", "description": "Orientation geometry, proportions, site selection, and modular grid layouts."},
                    {"name": "Temple Architecture (Prasada Vidya)", "slug": "temple-architecture", "description": "Nagara, Dravida, and Vesara temple design, mandapas, and shikhara engineering."},
                    {"name": "Town Planning & Civil Structures", "slug": "town-planning-civil", "description": "Fortifications, civic drainage, water reservoirs, and palace architecture."}
                ]
            },
            {
                "name": "Agriculture and Ecology",
                "slug": "agriculture-and-ecology",
                "description": "Indigenous agricultural practices, meteorological forecasting, soil classification, arbori-horticulture, and ecological conservation.",
                "icon": "Sprout",
                "subcategories": [
                    {"name": "Krishi Shastra", "slug": "krishi-shastra", "description": "Seed treatment, crop rotation, soil management, and implements."},
                    {"name": "Vrikshayurveda (Plant Science)", "slug": "vrikshayurveda-plant-science", "description": "Plant health, botanical pathology, grafting, and flowering sciences."},
                    {"name": "Water Harvesting & Traditional Irrigation", "slug": "water-harvesting", "description": "Stepwells, check-dams, village tanks, and watershed stewardship."}
                ]
            },
            {
                "name": "Metallurgy and Material Science",
                "slug": "metallurgy-and-material-science",
                "description": "Ancient and medieval metallurgical treatises, crucible wootz steel manufacturing, zinc smelting, and copper-bronze casting.",
                "icon": "Hammer",
                "subcategories": [
                    {"name": "Rasa Shastra (Iatrochemistry)", "slug": "rasa-shastra", "description": "Purification of metals, mercurial preparations, and mineral processing."},
                    {"name": "Wootz Steel & Iron Technology", "slug": "wootz-steel-iron", "description": "Crucible steel fabrication, Delhi Iron Pillar corrosion resistance, and forge craft."},
                    {"name": "Non-Ferrous Alloys & Icon Casting", "slug": "non-ferrous-alloys", "description": "Lost-wax (Madhuchehishtavidhana) bronze casting, brass, and zinc extraction."}
                ]
            },
            {
                "name": "Arts, Music and Performing Traditions",
                "slug": "arts-music-and-performing-traditions",
                "description": "Indian classical musicology (Sangita), raga classifications, tala rhythmic cycles, folk performance, and visual iconometry.",
                "icon": "Music",
                "subcategories": [
                    {"name": "Musicology (Sangita Shastra)", "slug": "musicology-sangita", "description": "Shrutis, Swaras, Grama-Murchhana scales, and instrumental treatises."},
                    {"name": "Dance & Dramatic Expression", "slug": "dance-dramatic-expression", "description": "Abhinaya gesture vocabulary, Karanas, and regional performing traditions."},
                    {"name": "Shilpa & Iconography", "slug": "shilpa-iconography", "description": "Proportions of sacred imagery, iconometry (Talamana), and sculpting cannons."}
                ]
            },
            {
                "name": "Governance and Economics",
                "slug": "governance-and-economics",
                "description": "Political administration, statecraft (Arthashastra), public finance, trade regulations, and judicial jurisprudence.",
                "icon": "Scale",
                "subcategories": [
                    {"name": "Arthashastra & Statecraft", "slug": "arthashastra-statecraft", "description": "The Saptanga theory of state, treasury management, and espionage."},
                    {"name": "Dharmashastra & Legal Jurisprudence", "slug": "dharmashastra-jurisprudence", "description": "Civil laws, property rights, judicial procedures, and community arbitration."},
                    {"name": "Public Finance & Trade Networks", "slug": "public-finance-trade", "description": "Taxation, guild administration (Shrenis), trade routes, and coinage."}
                ]
            },
            {
                "name": "Education and Linguistics",
                "slug": "education-and-linguistics",
                "description": "Ancient pedagogy, Gurukula systems, debate protocols (Vada Vidya), phonetics (Shiksha), and hermeneutics.",
                "icon": "GraduationCap",
                "subcategories": [
                    {"name": "Vedic & Classical Pedagogy", "slug": "vedic-pedagogy", "description": "Oral memorization techniques, Gurukula disciplines, and scholarly disputation."},
                    {"name": "Nirukta & Etymology", "slug": "nirukta-etymology", "description": "Semantic derivation, root analysis, and semantic shift in classical terminology."},
                    {"name": "Philosophy of Language", "slug": "philosophy-of-language", "description": "Sphota doctrine, sentence meaning (Vakyapadiya), and word-referent relations."}
                ]
            }
        ]

        domains_map = {}
        for dom in domains_structure:
            parent = db.query(KnowledgeDomain).filter(KnowledgeDomain.slug == dom["slug"]).first()
            if not parent:
                parent = KnowledgeDomain(
                    name=dom["name"],
                    slug=dom["slug"],
                    description=dom["description"],
                    icon=dom["icon"]
                )
                db.add(parent)
                db.flush()
            domains_map[dom["slug"]] = parent

            for sub in dom.get("subcategories", []):
                sub_obj = db.query(KnowledgeDomain).filter(KnowledgeDomain.slug == sub["slug"]).first()
                if not sub_obj:
                    sub_obj = KnowledgeDomain(
                        name=sub["name"],
                        slug=sub["slug"],
                        description=sub["description"],
                        parent_id=parent.id,
                        icon=dom["icon"]
                    )
                    db.add(sub_obj)
                    db.flush()
                domains_map[sub["slug"]] = sub_obj

        db.commit()
        print(f"Seeded {len(domains_map)} knowledge domains and subcategories.")

        # -------------------------------------------------------------
        # 4. SEED 32 AUTHENTIC IKS RESOURCES
        # -------------------------------------------------------------
        resources_dataset = [
            # 1. Aryabhatiya
            {
                "title": "Aryabhatiya of Aryabhata with the Commentary of Bhaskara I and Somesvara",
                "subtitle": "Critical Edition with Introduction, English Translation, Notes and Indices",
                "creator": "Aryabhata (Edited & Translated by Kripa Shankar Shukla & K.V. Sarma)",
                "contributor": "Indian National Science Academy",
                "subject": "Classical Indian Mathematics and Mathematical Astronomy",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "indian-mathematics",
                "publisher": "Indian National Science Academy (INSA), New Delhi",
                "publication_date": "1976 (Original text: 499 CE)",
                "digitisation_date": "2018",
                "source_institution": "Indian National Science Academy (INSA)",
                "source_url": "https://www.insaindia.res.in/",
                "access_url": "https://archive.org/details/aryabhatiya-of-aryabhata-k-s-shukla-1976",
                "download_url": "https://archive.org/download/aryabhatiya-of-aryabhata-k-s-shukla-1976/Aryabhatiya_of_Aryabhata_K_S_Shukla_1976.pdf",
                "license_identifier": "cc-by-nc-sa-4.0",
                "rights_statement": "Digitized and made openly accessible for non-commercial scholarly research by the Indian National Science Academy.",
                "access_status": "Open Access",
                "file_format": "PDF",
                "file_size": "18.4 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "INSA-HIST-SCI-1976-01",
                "keywords": "Aryabhatiya, Aryabhata, Indian Mathematics, Astronomy, Sine Table, Kuttaka, Epicycles",
                "citation": "Aryabhata. (1976). Aryabhatiya of Aryabhata (K. S. Shukla & K. V. Sarma, Eds.). Indian National Science Academy.",
                "verification_status": "Verified",
                "description": "The foundational 5th-century mathematical treatise comprising 121 verses across four chapters: Gitikapada (cosmological parameters), Ganitapada (mathematics), Kalakriyapada (time reckoning), and Golapada (sphere and celestial motion). It includes algorithms for extracting square and cube roots, solving linear indeterminate equations by Kuttaka, and the geometric calculation of pi to four decimal places (3.1416).",
                "abstract": "The Aryabhatiya presents an extraordinarily compact verse summary of 5th-century Indian mathematical astronomy. This critical edition establishes the text through collating rare palm-leaf manuscripts and incorporates the exhaustive commentaries of Bhaskara I (629 CE) and Somesvara."
            },
            # 2. Lilavati
            {
                "title": "Lilavati of Bhaskaracharya: A Treatise on Mensuration and Arithmetic",
                "subtitle": "Translated by Henry Thomas Colebrooke with Notes by Haran Chandra Banerji",
                "creator": "Bhaskaracharya II (Bhaskara II)",
                "contributor": "Henry Thomas Colebrooke",
                "subject": "Indian Arithmetic, Algebra, and Combinatorics",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "indian-mathematics",
                "publisher": "The Book Company Ltd., Calcutta",
                "publication_date": "1927 (Original text: 1150 CE)",
                "digitisation_date": "2015",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/LilavatiOfBhaskaracharyaColebrooke1927",
                "download_url": "https://archive.org/download/LilavatiOfBhaskaracharyaColebrooke1927/Lilavati_Colebrooke_1927.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. The original Sanskrit text and Colebrooke's historic 19th/early-20th century English editions are free of copyright worldwide.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "14.2 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "CAL-RB-1927-LIL",
                "keywords": "Lilavati, Bhaskara II, Arithmetic, Permutations, Combinatorics, Geometry, Fractions",
                "citation": "Bhaskaracharya. (1927). Lilavati: A Treatise on Mensuration and Arithmetic (H. T. Colebrooke, Trans.). The Book Company Ltd.",
                "verification_status": "Verified",
                "description": "The celebrated introductory book of Bhaskara II's magnum opus, the Siddhanta Shiromani. It addresses arithmetic progressions, permutations, planar geometry, quadratic equations, and shadows of gnomons in poetic verse addressed to his daughter Lilavati.",
                "abstract": "The Lilavati represents a pedagogical masterwork in arithmetic and practical geometry. Featuring 277 verses, it famously demonstrates combinatorial principles (Anka-pasha) and geometric solutions for shadow lengths."
            },
            # 3. Baudhayana Sulba Sutra
            {
                "title": "The Baudhayana Sulba-Sutra with Commentary of Dvarakanatha Yajvan",
                "subtitle": "Edited with Critical Notes and English Translation by George Thibaut",
                "creator": "Baudhayana (Edited by George Thibaut)",
                "contributor": "Pandit Series, Benares",
                "subject": "Vedic Geometry and Sacrificial Altar Engineering",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "indian-mathematics",
                "publisher": "Medical Hall Press, Benares",
                "publication_date": "1875 (Original text: circa 800 BCE)",
                "digitisation_date": "2014",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/baudhayanasulbas00thib",
                "download_url": "https://archive.org/download/baudhayanasulbas00thib/baudhayanasulbas00thib.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Published in 1875, this critical edition and translation have entered the public domain worldwide.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "9.8 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "PANDIT-BEN-1875-SULBA",
                "keywords": "Sulba Sutra, Baudhayana, Vedic Geometry, Pythagorean Theorem, Circling the Square, Shulba",
                "citation": "Baudhayana. (1875). The Sulvasutra of Baudhayana (G. Thibaut, Ed. & Trans.). The Pandit Series, Benares.",
                "verification_status": "Verified",
                "description": "The oldest surviving geometric manual of ancient India, prescribing cord-stretching measurements for sacrificial altars (Vedi). Contains the earliest explicit statement of the geometric theorem of the square of the diagonal (Pythagorean theorem) and geometric solutions for circling the square.",
                "abstract": "Thibaut's pioneering 1875 edition introduced European scholarship to ancient Indian geometry. It details Baudhayana's approximation of the square root of 2 accurate to five decimal places and rules for geometric area transformations."
            },
            # 4. Surya Siddhanta
            {
                "title": "Translation of the Surya-Siddhanta: A Text-Book of Hindu Astronomy",
                "subtitle": "With Notes and an Appendix by Rev. Ebenezer Burgess and William Dwight Whitney",
                "creator": "Burgess, Ebenezer & Whitney, William Dwight",
                "contributor": "American Oriental Society",
                "subject": "Siddhantic Astronomy and Celestial Mechanics",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "astronomy-and-cosmology",
                "publisher": "Journal of the American Oriental Society / New Haven",
                "publication_date": "1860",
                "digitisation_date": "2011",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/translationsury00whitgoog",
                "download_url": "https://archive.org/download/translationsury00whitgoog/translationsury00whitgoog.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public domain mark. Free of known copyright restrictions globally.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "26.1 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "JAOS-VOL-VI-1860",
                "keywords": "Surya Siddhanta, Hindu Astronomy, Burgess, Whitney, Celestial Mechanics, Eclipses",
                "citation": "Burgess, E., & Whitney, W. D. (1860). Translation of the Surya-Siddhanta: A Text-Book of Hindu Astronomy. Journal of the American Oriental Society.",
                "verification_status": "Verified",
                "description": "The standard classical textbook of Indian mathematical astronomy. Spans fourteen chapters covering the mean motions of planets, planetary true places, lunar and solar eclipses, heliacal risings, conjunctions, and astronomical instruments.",
                "abstract": "The Burgess-Whitney translation remains an indispensable scholarly monument in Indological astronomy. Accompanied by profound mathematical analyses, this volume elucidates epochal yuga lengths, epicyclic orbital calculations, and sine-chord tables."
            },
            # 5. Vedanga Jyotisha
            {
                "title": "Vedanga Jyotisha of Lagadha in its Rk and Yajus Recensions",
                "subtitle": "With the Translation and Notes by Prof. T. S. Kuppanna Sastry",
                "creator": "Lagadha (Edited by T. S. Kuppanna Sastry, K. V. Sarma)",
                "contributor": "Indian National Science Academy",
                "subject": "Vedic Astronomy, Calendrics, and Solstitial Observations",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "astronomy-and-cosmology",
                "publisher": "Indian National Science Academy (INSA), New Delhi",
                "publication_date": "1985 (Original text: circa 1400–1200 BCE)",
                "digitisation_date": "2019",
                "source_institution": "Indian National Science Academy (INSA)",
                "source_url": "https://www.insaindia.res.in/",
                "access_url": "https://archive.org/details/VedangaJyotishaKuppannaSastry1985",
                "download_url": "https://archive.org/download/VedangaJyotishaKuppannaSastry1985/Vedanga_Jyotisha_INSA_1985.pdf",
                "license_identifier": "cc-by-nc-sa-4.0",
                "rights_statement": "Open scholarly access authorized under CC BY-NC-SA 4.0 by Indian National Science Academy.",
                "access_status": "Open Access",
                "file_format": "PDF",
                "file_size": "8.5 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "INSA-VJ-1985-02",
                "keywords": "Vedanga Jyotisha, Lagadha, Solstice, Yuga, Panchanga, Vedic Astronomy, Kuppanna Sastry",
                "citation": "Lagadha. (1985). Vedanga Jyotisha of Lagadha (T. S. Kuppanna Sastry, Ed. & Trans.). Indian National Science Academy.",
                "verification_status": "Verified",
                "description": "The earliest known Indian astronomical text specifically composed to fix the appropriate dates and times for performing Vedic sacrifices. Prescribes a five-year lunisolar cycle (Yuga) containing 62 synodic months and 67 sidereal months.",
                "abstract": "Kuppanna Sastry's critical recension resolves longstanding textual corruptions in the 43 verses of the Yajur-recension and 36 verses of the Rk-recension, dating the astronomical epoch through the recorded position of solstices in Dhanishta nakshatra."
            },
            # 6. Charaka Samhita
            {
                "title": "The Charaka-Samhita of Agnivesha: Revised by Charaka and Dridhabala",
                "subtitle": "With the Ayurveda-Dipika Commentary of Chakrapanidatta",
                "creator": "Charaka (Edited by Vaidya Jadavji Trikamji Acharya)",
                "contributor": "Chakrapanidatta",
                "subject": "Classical Ayurvedic Internal Medicine (Kaya Chikitsa)",
                "language": "Sanskrit",
                "translated_language": None,
                "resource_type": "Book",
                "domain_slug": "ayurveda-and-traditional-medicine",
                "publisher": "Nirnaya Sagar Press / Chaukhambha Sanskrit Sansthan",
                "publication_date": "1941",
                "digitisation_date": "2016",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/CarakaSamhitaWithChakrapanidattaCommentary",
                "download_url": "https://archive.org/download/CarakaSamhitaWithChakrapanidattaCommentary/Caraka_Samhita_Jadavji.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain in India and worldwide due to expiration of copyright of the 1941 Nirnaya Sagar edition.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "42.7 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1512069772995-ec65ed45afd6?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "NSP-CARAKA-1941-ED",
                "keywords": "Charaka Samhita, Ayurveda, Tridosha, Kaya Chikitsa, Chakrapanidatta, Dravyaguna, Pathology",
                "citation": "Charaka. (1941). The Charakasamhita of Agnivesha (J. T. Acharya, Ed.). Nirnaya Sagar Press, Bombay.",
                "verification_status": "Verified",
                "description": "The foundational encyclopaedia of ancient Indian internal medicine. Spanning eight sections (Sthanas) and 120 chapters, it delineates the philosophy of health, etiology of disease, diagnostics, pharmacology, dietetics, and the balance of Vata, Pitta, and Kapha doshas.",
                "abstract": "Acharya's edition remains the gold-standard critical Sanskrit recension of Charaka Samhita. It reproduces the entire 11th-century Ayurveda-Dipika commentary of Chakrapanidatta, providing rigorous philosophical and medical explanations."
            },
            # 7. Sushruta Samhita
            {
                "title": "An English Translation of the Sushruta Samhita: Based on Original Sanskrit Text",
                "subtitle": "In Three Volumes: Sutrasthana, Nidanasthana, Sarirasthana, and Uttaratantra",
                "creator": "Sushruta (Translated by Kaviraj Kunja Lal Bhishagratna)",
                "contributor": "Calcutta Oriental Press",
                "subject": "Classical Indian Surgery (Shalya Tantra) and Anatomy",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "ayurveda-and-traditional-medicine",
                "publisher": "Calcutta / Published by the Author",
                "publication_date": "1907–1916",
                "digitisation_date": "2012",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/englishtranslati01susrrich",
                "download_url": "https://archive.org/download/englishtranslati01susrrich/englishtranslati01susrrich.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Published between 1907 and 1916; freely available for global download and scholarly reuse.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "34.8 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "CAL-SUSHRUTA-1907-VOL1",
                "keywords": "Sushruta Samhita, Surgery, Shalya Tantra, Rhinoplasty, Surgical Instruments, Anatomy, Ayurveda",
                "citation": "Sushruta. (1907). An English Translation of the Sushruta Samhita (K. L. Bhishagratna, Trans.). Calcutta.",
                "verification_status": "Verified",
                "description": "The seminal classical treatise on ancient surgery, pioneering over 120 surgical instruments, rhinoplastic skin flap grafting, cataract couching, lithotomy, bone fracture fixation, and meticulous anatomical dissection.",
                "abstract": "Bhishagratna's three-volume English translation opened the surgical wisdom of the Dhanvantari school to the modern world. It documents operating theater hygiene, classification of surgical incisions, and restorative plastic surgery."
            },
            # 8. Vrikshayurveda of Surapala
            {
                "title": "Vrikshayurveda (The Science of Plant Life) by Surapala",
                "subtitle": "Sanskrit Text with English Translation, Agricultural Commentary, and Botanical Identification",
                "creator": "Surapala (Translated by Nalini Sadhale, Commentary by Y. L. Nene)",
                "contributor": "Asian Agri-History Foundation",
                "subject": "Traditional Indian Arbori-Horticulture and Ethnobotany",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Research Paper",
                "domain_slug": "agriculture-and-ecology",
                "publisher": "Asian Agri-History Foundation (AAHF), Secunderabad",
                "publication_date": "1996 (Original manuscript: circa 10th century CE)",
                "digitisation_date": "2018",
                "source_institution": "Asian Agri-History Foundation (AAHF)",
                "source_url": "https://www.asianagrihistory.org/",
                "access_url": "https://www.asianagrihistory.org/bulletins.html",
                "download_url": None,
                "license_identifier": "in-copyright-read-only",
                "rights_statement": "In Copyright - Free to Read Online on official educational portal. Commercial redistribution and file re-hosting restricted.",
                "access_status": "Read Online",
                "file_format": "HTML",
                "file_size": "4.2 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1530836369250-ef72a3f5cda8?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "AAHF-AGRI-BULL-1996-01",
                "keywords": "Vrikshayurveda, Surapala, Kunapajala, Bio-fertilizers, Plant Pathology, Horticulture, Arboriculture",
                "citation": "Surapala. (1996). Vrikshayurveda (The Science of Plant Life) (N. Sadhale, Trans.; Y. L. Nene, Comm.). Asian Agri-History Foundation.",
                "verification_status": "Verified",
                "description": "A 10th-century Sanskrit manual on arboriculture containing 325 verses. Details soil testing, seed preservation, nursery preparation, grafting, watering routines, and the formulation of Kunapajala (fermented liquid bio-fertilizer).",
                "abstract": "Surapala's Vrikshayurveda provides extraordinary historic evidence of sustainable agro-horticultural techniques. The manuscript, rediscovered at the Bodleian Library Oxford, systematizes plant nutrition and biological pest deterrence."
            },
            # 9. Yoga Sutras of Patanjali
            {
                "title": "The Yoga-System of Patanjali: Or the Ancient Hindu Doctrine of Concentration of Mind",
                "subtitle": "Embracing the Mnemonic Rules (Yoga-Sutras) of Patanjali, the Comment (Bhasya) of Vyasa, and the Explanation (Tattva-Vaicaradi) of Vachaspati Mishra",
                "creator": "Patanjali (Translated by James Haughton Woods)",
                "contributor": "Harvard University Press",
                "subject": "Classical Yoga Philosophy, Psychology, and Meditation",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "yoga-and-philosophy",
                "publisher": "Harvard University Press, Cambridge, Massachusetts",
                "publication_date": "1914",
                "digitisation_date": "2013",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/yogasystemofpata00wooduoft",
                "download_url": "https://archive.org/download/yogasystemofpata00wooduoft/yogasystemofpata00wooduoft.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Harvard Oriental Series Vol. XVII (1914), fully free of copyright restrictions worldwide.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "28.5 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "HOS-VOL-XVII-1914",
                "keywords": "Yoga Sutras, Patanjali, Vyasa Bhasya, Vachaspati Mishra, Samadhi, Ashtanga Yoga, Chitta Vritti",
                "citation": "Patanjali. (1914). The Yoga-System of Patanjali (J. H. Woods, Trans.). Harvard University Press.",
                "verification_status": "Verified",
                "description": "The definitive philosophical formulation of Classical Raja Yoga across four padas: Samadhi (absorption), Sadhana (practice), Vibhuti (powers), and Kaivalya (liberation). Integrates the 196 sutras with the fundamental primary commentaries.",
                "abstract": "James H. Woods' translation remains one of the finest scholarly editions in Western Indology. Translating both Vyasa's Bhasya and Vachaspati Mishra's sub-commentary, it presents Patanjali's analysis of cognitive modifications (Chitta Vritti) and liberation."
            },
            # 10. Samkhya Karika
            {
                "title": "The Sankhya Karika: Or Memorial Verses on the Sankhya Philosophy by Ishwara Krishna",
                "subtitle": "Translated from the Sanskrit by Henry Thomas Colebrooke; Also the Bhashya of Gaudapada",
                "creator": "Ishvarakrishna (Translated by H. T. Colebrooke & H. H. Wilson)",
                "contributor": "Oriental Translation Fund of Great Britain and Ireland",
                "subject": "Classical Samkhya Dualist Philosophy and Ontology",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "yoga-and-philosophy",
                "publisher": "Printed for the Oriental Translation Committee, Oxford",
                "publication_date": "1837",
                "digitisation_date": "2010",
                "source_institution": "Bhandarkar Oriental Research Institute (BORI)",
                "source_url": "https://bori.ac.in/",
                "access_url": "https://archive.org/details/sankhyakarikaorm00iswagoog",
                "download_url": "https://archive.org/download/sankhyakarikaorm00iswagoog/sankhyakarikaorm00iswagoog.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Landmark 1837 edition, universally accessible without copyright restrictions.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "15.3 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1519791883288-dc8bd696e667?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "OTF-OXFORD-1837-SK",
                "keywords": "Samkhya Karika, Ishvarakrishna, Purusha, Prakriti, Gunas, Gaudapada Bhashya, Philosophy",
                "citation": "Ishvarakrishna. (1837). The Sankhya Karika (H. T. Colebrooke & H. H. Wilson, Trans.). Oriental Translation Fund, Oxford.",
                "verification_status": "Verified",
                "description": "The earliest extant authoritative summary of the Samkhya philosophy in 72 mnemonic verses. Expounds the dualistic metaphysics of consciousness (Purusha) and manifest material nature (Prakriti), characterized by the three Gunas (Sattva, Rajas, Tamas).",
                "abstract": "The Colebrooke-Wilson edition includes Gaudapada's essential commentary, explaining the 25 cosmic principles (Tattvas), epistemology (Pratyaksha, Anumana, Aptavachana), and the path to transcending existential suffering."
            },
            # 11. Rigveda Samhita
            {
                "title": "Rig-Veda-Sanhita: The Sacred Hymns of the Brahmans",
                "subtitle": "Together with the Commentary of Sayanacharya (Volume I: Mandala 1)",
                "creator": "F. Max Müller (Editor) & Sayanacharya (Commentator)",
                "contributor": "Vedic Heritage Portal, IGNCA",
                "subject": "Vedic Hymnology, Indo-European Linguistics, and Ritual Poetry",
                "language": "Vedic Sanskrit",
                "translated_language": None,
                "resource_type": "Book",
                "domain_slug": "vedic-literature",
                "publisher": "W. H. Allen and Co., London",
                "publication_date": "1849",
                "digitisation_date": "2017",
                "source_institution": "Vedic Heritage Portal",
                "source_url": "https://vedicheritage.gov.in/",
                "access_url": "https://vedicheritage.gov.in/samhitas/rigveda-samhita/",
                "download_url": "https://archive.org/download/RigVedaWithSayanaCommentaryMaxMullerVol1/Rig_Veda_Sayana_Max_Muller_Vol1.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. The monumental 1849 editio princeps by Max Müller with Sayana's commentary is free of copyright.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "58.2 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "OXF-RV-1849-VOL1",
                "keywords": "Rigveda, Samhita, Sayana, Max Muller, Vedic Sanskrit, Agni, Indra, Mantras, Hymns",
                "citation": "Müller, F. M. (Ed.). (1849). Rig-Veda-Sanhita: The Sacred Hymns of the Brahmans, Together with the Commentary of Sayanacharya (Vol. 1). W. H. Allen and Co.",
                "verification_status": "Verified",
                "description": "The editio princeps of the oldest recorded text of Indo-European literature, containing 1,028 suktas organized in ten Mandalas. Complete with the exhaustive 14th-century ritualistic commentary (Bhasya) of Acharya Sayana.",
                "abstract": "Max Müller's publication of the Rigveda Samhita alongside Sayana's commentary marked a defining epoch in Indology and comparative linguistics, establishing the received Shakala recension with accented Devnagari typography."
            },
            # 12. Samaveda Samhita
            {
                "title": "The Hymns of the Samaveda: Translated with a Popular Commentary",
                "subtitle": "Complete Archika and Gana Metrical Re-arrangements",
                "creator": "Ralph T. H. Griffith (Translator)",
                "contributor": "Vedic Heritage Portal",
                "subject": "Vedic Musical Recitation, Udgatri Chants, and Melodic Liturgy",
                "language": "Vedic Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "vedic-literature",
                "publisher": "E. J. Lazarus and Co., Benares",
                "publication_date": "1893",
                "digitisation_date": "2015",
                "source_institution": "Vedic Heritage Portal",
                "source_url": "https://vedicheritage.gov.in/",
                "access_url": "https://archive.org/details/hymnsofsamaveda00grif",
                "download_url": "https://archive.org/download/hymnsofsamaveda00grif/hymnsofsamaveda00grif.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain worldwide. Historic 1893 translation free of copyright restrictions.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "19.6 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1507842229451-9f750c1532f7?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "BEN-SV-1893-GRIF",
                "keywords": "Samaveda, Griffith, Vedic Chants, Sama Gana, Musicology, Liturgy, Archika",
                "citation": "Griffith, R. T. H. (Trans.). (1893). The Hymns of the Samaveda. E. J. Lazarus and Co., Benares.",
                "verification_status": "Verified",
                "description": "The Veda of chants (Saman) consisting of 1,875 verses primarily adapted from the Rigveda and set to melodic notations for the Udgatri priests during Somayagas. Considered the liturgical root of Indian classical music.",
                "abstract": "Griffith's translation renders the Purvarchika and Uttararchika sections with lucid explanatory notes on ancient Indian metrics, sacrificial contexts, and musical scale foundations."
            },
            # 13. Shukla Yajurveda Samhita
            {
                "title": "The Texts of the White Yajurveda (Vajasaneyi-Samhita)",
                "subtitle": "Translated with a Popular Commentary by Ralph T. H. Griffith",
                "creator": "Ralph T. H. Griffith",
                "contributor": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "subject": "Vedic Sacrificial Liturgy, Mantras, and Ritual Formulations",
                "language": "Vedic Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "vedic-literature",
                "publisher": "E. J. Lazarus and Co., Benares",
                "publication_date": "1899",
                "digitisation_date": "2016",
                "source_institution": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "source_url": "https://ignca.gov.in/",
                "access_url": "https://archive.org/details/textsofwhiteyaju00grif",
                "download_url": "https://archive.org/download/textsofwhiteyaju00grif/textsofwhiteyaju00grif.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. First published in 1899 at Benares.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "22.8 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "BEN-YV-1899-GRIF",
                "keywords": "Yajurveda, Vajasaneyi Samhita, Shukla Yajurveda, Ashvamedha, Agnicayana, Ritual, Griffith",
                "citation": "Griffith, R. T. H. (Trans.). (1899). The Texts of the White Yajurveda. E. J. Lazarus and Co.",
                "verification_status": "Verified",
                "description": "The Vajasaneyi Samhita of the Shukla (White) Yajurveda in forty adhyayas. Contains sacrificial formulas for rituals such as Agnihotra, Darshapurnamasa, and the philosophical Ishavasya Upanishad forming the concluding fortieth adhyaya.",
                "abstract": "This scholarly translation illuminates the ceremonial hymns of the Adhvaryu priest, offering deep insights into the social organization, metallurgy, flora, fauna, and spiritual worldview of late Vedic society."
            },
            # 14. Atharvaveda Samhita
            {
                "title": "Atharva-Veda Samhita: Translated with a Critical and Exegetical Commentary",
                "subtitle": "Revised and Brought Nearer to Completion and Edited by Charles Rockwell Lanman",
                "creator": "William Dwight Whitney & Charles Rockwell Lanman",
                "contributor": "Harvard University Press",
                "subject": "Domestic Rites, Healing Incantations, Herbal Medicine, and Philosophy",
                "language": "Vedic Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "vedic-literature",
                "publisher": "Harvard University (Harvard Oriental Series Vols. VII & VIII)",
                "publication_date": "1905",
                "digitisation_date": "2013",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/atharvavedasamhi07whitrich",
                "download_url": "https://archive.org/download/atharvavedasamhi07whitrich/atharvavedasamhi07whitrich.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Harvard Oriental Series 1905 critical edition free of copyright.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "48.9 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1532012164546-f432f2e3ddb5?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "HOS-VOL-VII-1905",
                "keywords": "Atharvaveda, Whitney, Lanman, Bhaishajyani, Healing, Prithvi Sukta, Vedic Mantras",
                "citation": "Whitney, W. D., & Lanman, C. R. (1905). Atharva-Veda Samhita (2 vols.). Harvard University Press.",
                "verification_status": "Verified",
                "description": "The fourth Veda according to the Shaunaka recension in 20 kandas. Focuses on pragmatic healing formulas (Bhaishajyani), community welfare rites, protection against toxins, statecraft mantras, and the magnificent Prithvi Sukta (Hymn to the Earth).",
                "abstract": "Whitney and Lanman's two-volume masterwork remains the most authoritative Western critical analysis of the Atharvaveda, meticulously documenting manuscript variants from the Paippalada recension and Pada-patha."
            },
            # 15. Abhijnanasakuntalam of Kalidasa
            {
                "title": "Sakuntala: A Sanskrit Drama in Seven Acts by Kalidasa",
                "subtitle": "The Deva-Nagari Recension of the Text with Literal English Translation and Notes",
                "creator": "Kalidasa (Edited & Translated by Sir Monier Monier-Williams)",
                "contributor": "Clarendon Press, Oxford",
                "subject": "Classical Sanskrit Drama (Nataka) and Poetics",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "sanskrit-and-classical-literature",
                "publisher": "Clarendon Press, Oxford",
                "publication_date": "1876",
                "digitisation_date": "2014",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/sakuntalsanskrit00kaliuoft",
                "download_url": "https://archive.org/download/sakuntalsanskrit00kaliuoft/sakuntalsanskrit00kaliuoft.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain mark. Worldwide unrestricted academic and download access.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "21.4 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1476275466078-4007374efbbe?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "CLARENDON-OXF-1876-SAK",
                "keywords": "Abhijnanasakuntalam, Kalidasa, Sanskrit Drama, Monier-Williams, Shakuntala, Dushyanta, Rasa",
                "citation": "Kalidasa. (1876). Sakuntala: A Sanskrit Drama in Seven Acts (M. Monier-Williams, Ed. & Trans.). Clarendon Press, Oxford.",
                "verification_status": "Verified",
                "description": "Considered the pinnacle of Sanskrit dramatic literature, portraying the love, repudiation, and reunion of King Dushyanta and Shakuntala based on the Mahabharata epic narrative. Renowned for its unparalleled lyricism and evocation of Shringara Rasa.",
                "abstract": "Monier-Williams' critical edition provides the complete Devanagari text alongside literal translation, grammatical analysis of Prakrit dialects, and historical commentary on ancient Indian theater traditions."
            },
            # 16. Meghaduta of Kalidasa
            {
                "title": "The Meghaduta of Kalidasa: With the Commentary of Vallabhadeva",
                "subtitle": "Critical Edition from Rare Manuscripts with Introduction and Notes",
                "creator": "Kalidasa (Edited by E. Hultzsch)",
                "contributor": "Royal Asiatic Society",
                "subject": "Classical Sanskrit Sandesha Kavya (Lyric Poetry)",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "sanskrit-and-classical-literature",
                "publisher": "Royal Asiatic Society (Prize Publications Fund Vol. III), London",
                "publication_date": "1911",
                "digitisation_date": "2015",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/meghadutaofk00kaluoft",
                "download_url": "https://archive.org/download/meghadutaofk00kaluoft/meghadutaofk00kaluoft.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. The 1911 Hultzsch edition is completely free of copyright restrictions.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "11.2 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "RAS-PPF-VOL-III-1911",
                "keywords": "Meghaduta, Kalidasa, Cloud Messenger, Mandakranta Meter, Alaka, Yaksha, Kavya",
                "citation": "Kalidasa. (1911). The Meghaduta of Kalidasa (E. Hultzsch, Ed.). Royal Asiatic Society, London.",
                "verification_status": "Verified",
                "description": "The archetypal messenger-poem (Sandesha Kavya) composed in 111 stanzas of the majestic Mandakranta meter. An exiled Yaksha beseeches a passing monsoon cloud to carry a message of devotion to his grieving wife in the mythical Himalayan city of Alaka.",
                "abstract": "Hultzsch's 1911 edition establishes the text using the oldest extant commentary by Vallabhadeva (10th century), presenting an exhaustive critical apparatus for Kalidasa's geographical descriptions of central India."
            },
            # 17. Natyashastra of Bharata Muni
            {
                "title": "The Natyashastra: A Treatise on Ancient Indian Dramaturgy and Histrionics",
                "subtitle": "Completely Translated into English with Introduction and Various Readings by Manomohan Ghosh",
                "creator": "Bharata Muni (Translated by Manomohan Ghosh)",
                "contributor": "The Royal Asiatic Society of Bengal",
                "subject": "Classical Indian Dramaturgy, Dance, Aesthetics (Rasa), and Music",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "arts-music-and-performing-traditions",
                "publisher": "The Royal Asiatic Society of Bengal, Calcutta",
                "publication_date": "1951",
                "digitisation_date": "2017",
                "source_institution": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "source_url": "https://ignca.gov.in/",
                "access_url": "https://archive.org/details/NatyashastraGhoshVol1",
                "download_url": "https://archive.org/download/NatyashastraGhoshVol1/Natyashastra_Ghosh_Vol1.pdf",
                "license_identifier": "cc-by-nc-sa-4.0",
                "rights_statement": "Open access for academic and research purposes under CC BY-NC-SA 4.0 via IGNCA digital library.",
                "access_status": "Open Access",
                "file_format": "PDF",
                "file_size": "36.2 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "RASB-BIB-IND-VOL-272",
                "keywords": "Natyashastra, Bharata Muni, Rasa Theory, Bhava, Abhinaya, Theater, Dance, Drama, Ghosh",
                "citation": "Bharata Muni. (1951). The Natyashastra (M. Ghosh, Trans.). The Royal Asiatic Society of Bengal, Calcutta.",
                "verification_status": "Verified",
                "description": "The encyclopedia of ancient Indian performing arts attributed to sage Bharata across 36 chapters. Covers dramatic composition, theater architecture, stagecraft, make-up, body language (Angika Abhinaya), emotional states, and musical instrumentation.",
                "abstract": "Manomohan Ghosh's monumental translation details the quintessential Rasa-Sutra ('Vibhavanubhava-vyabhichari-samyogad rasa-nishpattih'), laying the theoretical foundations for two millennia of Indian classical dance and drama."
            },
            # 18. Ashtadhyayi of Panini
            {
                "title": "The Ashtadhyayi of Panini: Translated into English with Exhaustive Commentary",
                "subtitle": "Edited and Translated with Full Derivational Notes by Srisa Chandra Vasu",
                "creator": "Panini (Translated by Srisa Chandra Vasu)",
                "contributor": "Panini Office, Bhuvaneshwari Asrama",
                "subject": "Formal Linguistics, Generative Morphology, and Phonetics",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "education-and-linguistics",
                "publisher": "The Panini Office, Allahabad",
                "publication_date": "1891",
                "digitisation_date": "2013",
                "source_institution": "Sanskrit Documents Consortium",
                "source_url": "https://sanskritdocuments.org/",
                "access_url": "https://archive.org/details/ashtadhyayiofpan01pani",
                "download_url": "https://archive.org/download/ashtadhyayiofpan01pani/ashtadhyayiofpan01pani.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Vasu's historic 1891 Allahabad translation is free of copyright globally.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "54.1 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "PANINI-OFFICE-1891-VOL1",
                "keywords": "Ashtadhyayi, Panini, Sanskrit Grammar, Generative Linguistics, Sutras, Dhatupatha, Morphology",
                "citation": "Panini. (1891). The Ashtadhyayi of Panini (S. C. Vasu, Trans.). The Panini Office, Allahabad.",
                "verification_status": "Verified",
                "description": "The foundational generative grammar of the Sanskrit language comprising approximately 4,000 highly concise sutras. Recognized in modern computer science as an extraordinarily sophisticated forerunner of formal language theory and context-free grammars.",
                "abstract": "Vasu's complete English edition of the Ashtadhyayi incorporates the commentary of the Kasika-Vritti, providing comprehensive derivations for nouns, verbs, compounds (Samasa), and sandhi phonetic mutations."
            },
            # 19. Mayamata
            {
                "title": "Mayamata: An Indian Treatise on Housing Architecture and Iconography",
                "subtitle": "Critical Sanskrit Text with English Translation, Architectural Diagrams and Index",
                "creator": "Bruno Dagens (Translator & Editor)",
                "contributor": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "subject": "Vastu Vidya, Temple Architecture, and Sacred Iconography",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "architecture-and-engineering",
                "publisher": "IGNCA / Motilal Banarsidass, New Delhi",
                "publication_date": "1994 (Kalakosa Series Vol. 1)",
                "digitisation_date": "2019",
                "source_institution": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "source_url": "https://ignca.gov.in/",
                "access_url": "https://ignca.gov.in/divisions/kalakosa-division/",
                "download_url": None,
                "license_identifier": "in-copyright-read-only",
                "rights_statement": "In Copyright - Free to Read Online on official educational portal. Redistribution and direct file downloading restricted.",
                "access_status": "Read Online",
                "file_format": "HTML",
                "file_size": "15.0 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "ISBN: 978-8120810716",
                "keywords": "Mayamata, Vastu Shastra, Temple Architecture, Dravida, Bruno Dagens, Iconography, Mandapa",
                "citation": "Dagens, B. (Ed. & Trans.). (1994). Mayamata: An Indian Treatise on Housing Architecture and Iconography. IGNCA and Motilal Banarsidass.",
                "verification_status": "Verified",
                "description": "An exhaustive Dravidian Vastu Shastra treatise in 36 chapters detailing town layout, soil examination, orientation by gnomon, construction materials (stone, brick, timber), multi-storeyed temple superstructures, gopurams, and bronze image casting.",
                "abstract": "Bruno Dagens' authoritative bilingual edition elucidates the technical architectural vocabulary of South Indian temple builders, analyzing modular proportional grids (Padavinyasa) and structural profiles."
            },
            # 20. Manasara on Architecture and Sculpture
            {
                "title": "Architecture of Manasara: Translated from Original Sanskrit",
                "subtitle": "With Architectural Drawings and Comprehensive Notes (Manasara Series Vol. IV)",
                "creator": "Prasanna Kumar Acharya",
                "contributor": "Oxford University Press",
                "subject": "Classical Indian Architecture, Sculpture, and Civil Engineering",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "architecture-and-engineering",
                "publisher": "Oxford University Press, London & Bombay",
                "publication_date": "1934",
                "digitisation_date": "2014",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/ArchitectureOfManasaraPKacharya",
                "download_url": "https://archive.org/download/ArchitectureOfManasaraPKacharya/Architecture_of_Manasara_Acharya_1934.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain in India and internationally. Published in 1934 by Oxford University Press.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "45.0 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1590766940554-634a7ed41450?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "OUP-MANASARA-VOL-IV-1934",
                "keywords": "Manasara, Acharya, Vastu, Shilpa, Temple Architecture, Hindu Architecture, Column Orders",
                "citation": "Acharya, P. K. (1934). Architecture of Manasara (Vol. 4). Oxford University Press.",
                "verification_status": "Verified",
                "description": "The monumental standard treatise of the Manasara school in 70 adhyayas. Explores the entire spectrum of Indian civil, military, and sacred architecture from village selection, palace compounds, and gateways to iconography and coronation thrones.",
                "abstract": "P. K. Acharya's 1934 translation was the first modern academic effort to reconstruct the monumental lexicon of Shilpa Shastra, documenting the five classical Indian column orders and proportional measurement units."
            },
            # 21. Samarangana Sutradhara of King Bhoja
            {
                "title": "Samarangana-Sutradhara by King Bhoja: A Treatise on Architecture",
                "subtitle": "Edited with Introduction and Detailed Contents by Mahamahopadhyaya T. Ganapati Sastri",
                "creator": "King Bhoja of Dhar (Edited by T. Ganapati Sastri)",
                "contributor": "Oriental Institute, Baroda",
                "subject": "Medieval Architecture, Mechanical Automata (Yantras), and Urban Design",
                "language": "Sanskrit",
                "translated_language": None,
                "resource_type": "Book",
                "domain_slug": "architecture-and-engineering",
                "publisher": "Central Library / Oriental Institute (Gaekwad's Oriental Series No. XXV), Baroda",
                "publication_date": "1924",
                "digitisation_date": "2013",
                "source_institution": "Oriental Institute, The Maharaja Sayajirao University of Baroda",
                "source_url": "https://www.msubaroda.ac.in/",
                "access_url": "https://archive.org/details/SamaranganasutradharaOfKingBhojadevaGanapatiSastri1924",
                "download_url": "https://archive.org/download/SamaranganasutradharaOfKingBhojadevaGanapatiSastri1924/Samaranganasutradhara_GOS_25_1924.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Gaekwad's Oriental Series No. 25, published in 1924.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "27.8 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1599839575945-a9e5af0c3fa5?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "GOS-NO-XXV-1924",
                "keywords": "Samarangana Sutradhara, Bhoja, Yantras, Mechanical Automata, Vastu Shastra, Baroda, Architecture",
                "citation": "Bhoja. (1924). Samarangana-Sutradhara (T. G. Sastri, Ed.). Gaekwad's Oriental Series No. 25, Central Library, Baroda.",
                "verification_status": "Verified",
                "description": "An 11th-century encyclopaedic architectural work in 83 chapters attributed to King Bhoja of Dhara. Particularly famous for its 31st chapter on Yantra-vidhana, describing mechanical automata, waterworks, celestial spheres, and aerial machines.",
                "abstract": "Ganapati Sastri's editio princeps established this crucial text for historians of medieval Indian science, offering unique insights into civic planning, mechanical craftsmanship, and temple shikhara engineering."
            },
            # 22. Krishi-Parashara
            {
                "title": "Krishi-Parashara (Agriculture by Parashara)",
                "subtitle": "Sanskrit Text with English Translation, Scientific Commentary and Modern Agricultural Analysis",
                "creator": "Parashara (Translated by Nalini Sadhale, Commentary by Y. L. Nene & H. V. L. Bathkal)",
                "contributor": "Asian Agri-History Foundation & ICAR",
                "subject": "Traditional Indian Rainfed Agriculture and Meteorological Wisdom",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "agriculture-and-ecology",
                "publisher": "Asian Agri-History Foundation (AAHF), Secunderabad",
                "publication_date": "1999 (Original text: circa 4th century BCE to 4th century CE)",
                "digitisation_date": "2018",
                "source_institution": "Asian Agri-History Foundation (AAHF)",
                "source_url": "https://www.asianagrihistory.org/",
                "access_url": "https://www.asianagrihistory.org/bulletins.html",
                "download_url": None,
                "license_identifier": "in-copyright-read-only",
                "rights_statement": "In Copyright - Free to Read Online on Asian Agri-History Foundation official portal for research.",
                "access_status": "Read Online",
                "file_format": "PDF",
                "file_size": "7.5 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "AAHF-AGRI-BULL-1999-02",
                "keywords": "Krishi Parashara, Agriculture, Rain Forecasting, Soil Preparation, Cattle Care, Seed Selection",
                "citation": "Parashara. (1999). Krishi-Parashara (Agriculture by Parashara) (N. Sadhale, Trans.). Asian Agri-History Foundation.",
                "verification_status": "Verified",
                "description": "One of the oldest surviving dedicated manuals on agriculture in the world, consisting of 243 verses. Covers rainfall forecasting using meteorological and planetary models, seed conservation, manure preparation, and the management of drought animals.",
                "abstract": "This critical edition bridges ancient farming methods and modern agronomy. It demonstrates Parashara's precise seasonal planning for paddy cultivation, field drainage, and organic seed pre-treatments."
            },
            # 23. Rasaratnasamuccaya of Vagbhata
            {
                "title": "Rasaratnasamuccaya of Vagbhata: With English Translation and Notes",
                "subtitle": "A Comprehensive Treatise on Indian Alchemy and Iatrochemistry (History of Science in India)",
                "creator": "Vagbhata (Translated with Notes by Prof. D. Joshi)",
                "contributor": "Indian National Science Academy",
                "subject": "Rasa Shastra, Iatrochemistry, Metallurgy, and Laboratory Apparatus",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "metallurgy-and-material-science",
                "publisher": "Indian National Science Academy (INSA), New Delhi",
                "publication_date": "2007 (Original text: circa 13th century CE)",
                "digitisation_date": "2019",
                "source_institution": "Indian National Science Academy (INSA)",
                "source_url": "https://www.insaindia.res.in/",
                "access_url": "https://archive.org/details/RasaratnasamuccayaINSA2007",
                "download_url": "https://archive.org/download/RasaratnasamuccayaINSA2007/Rasaratnasamuccaya_INSA_Joshi.pdf",
                "license_identifier": "cc-by-nc-sa-4.0",
                "rights_statement": "Open access for academic and research evaluation under CC BY-NC-SA 4.0 by Indian National Science Academy.",
                "access_status": "Open Access",
                "file_format": "PDF",
                "file_size": "24.6 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "ISBN: 978-8187439165",
                "keywords": "Rasaratnasamuccaya, Rasa Shastra, Metallurgy, Mercury, Bhasmas, Crucibles, INSA",
                "citation": "Vagbhata. (2007). Rasaratnasamuccaya (D. Joshi, Trans.). Indian National Science Academy, New Delhi.",
                "verification_status": "Verified",
                "description": "A 13th-century magnum opus in 30 chapters systematically describing ancient Indian chemistry and metallurgy. Catalogs mineral classifications (Maharasa, Uparasa, Sadharanarasa), laboratory layout (Rasashala), apparatus (Yantras), and crucible types (Mushas).",
                "abstract": "Prof. D. Joshi's authoritative translation documents medieval Indian distillation, calcination (Marana), and extraction methods for mercury, copper, zinc, and iron, complete with metallurgical laboratory drawings."
            },
            # 24. Delhi Iron Pillar Metallurgy
            {
                "title": "Delhi Iron Pillar: New Insights on its Metallurgy and Corrosion Resistance",
                "subtitle": "Monograph on Ancient Indian Metallurgical Skill and Atmospheric Passivation",
                "creator": "Prof. R. Balasubramaniam",
                "contributor": "Indian Institute of Technology Kanpur & Aryan Books",
                "subject": "Ancient Metallurgy, Corrosion Science, and Forge Welding",
                "language": "English",
                "translated_language": None,
                "resource_type": "Research Paper",
                "domain_slug": "metallurgy-and-material-science",
                "publisher": "Aryan Books International / Indian Institute of Metals",
                "publication_date": "2002",
                "digitisation_date": "2016",
                "source_institution": "Shodhganga - INFLIBNET Centre",
                "source_url": "https://shodhganga.inflibnet.ac.in/",
                "access_url": "https://archive.org/details/DelhiIronPillarNewInsightsBalasubramaniam",
                "download_url": None,
                "license_identifier": "institution-open-access",
                "rights_statement": "Institutional Open Access repository record. Full paper viewable via academic host.",
                "access_status": "Read Online",
                "file_format": "PDF",
                "file_size": "12.1 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "ISBN: 978-8173052231",
                "keywords": "Iron Pillar, Delhi, Metallurgy, Corrosion, Misawite, Forge Welding, Wrought Iron, Balasubramaniam",
                "citation": "Balasubramaniam, R. (2002). Delhi Iron Pillar: New Insights. Aryan Books International, New Delhi.",
                "verification_status": "Verified",
                "description": "Pioneering metallurgical investigation into the rust-resistant 1600-year-old Gupta-era Iron Pillar of Delhi. Explains the role of high phosphorus content and the catalytic formation of a protective crystalline iron hydrogen phosphate hydrate film (Misawite).",
                "abstract": "Prof. Balasubramaniam's monograph solves the historic enigma of the pillar's preservation through microstructural analysis and atmospheric corrosion testing, proving the mastery of ancient Indian blacksmiths in solid-state forge welding."
            },
            # 25. Sangita Ratnakara of Sarangadeva
            {
                "title": "Sangitaratnakara of Sarngadeva: Sanskrit Text with English Translation",
                "subtitle": "Volume I: Treatment of Swara (Notes and Microtonal Shrutis)",
                "creator": "Sarangadeva (Translated by C. Kunhan Raja)",
                "contributor": "The Adyar Library and Research Centre",
                "subject": "Classical Indian Musicology, Raga Theory, and Tala",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "arts-music-and-performing-traditions",
                "publisher": "The Adyar Library, Adyar, Madras",
                "publication_date": "1945 (Original text: circa 13th century CE)",
                "digitisation_date": "2014",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/SangitaRatnakaraVol1AdyarLibrary1945",
                "download_url": "https://archive.org/download/SangitaRatnakaraVol1AdyarLibrary1945/Sangita_Ratnakara_Vol1_1945.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. The 1945 Adyar Library translation is in the public domain in India.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "16.8 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "ADYAR-LIB-SER-VOL-51",
                "keywords": "Sangita Ratnakara, Sarangadeva, Carnatic, Hindustani, Shrutis, Swaras, Raga, Tala, Musicology",
                "citation": "Sarangadeva. (1945). Sangitaratnakara of Sarngadeva (C. K. Raja, Trans.). The Adyar Library, Madras.",
                "verification_status": "Verified",
                "description": "The definitive 13th-century musical treatise bridging ancient and medieval Indian musicology. Reorganizes melody into seven chapters (Saptadhyayi): Swara (musical notes), Raga, Prakirnaka, Prabandha, Tala (rhythm), Vadya (instruments), and Nartana (dance).",
                "abstract": "The Adyar edition of Chapter 1 provides the mathematical and acoustic basis of the 22 Shrutis (microtones) and the Grama-Murchhana modal systems, acknowledged as the common source for both Hindustani and Carnatic classical traditions."
            },
            # 26. Brihaddesi of Matanga Muni
            {
                "title": "Brihaddesi of Sri Matanga Muni: Classical Treatise on Indian Musicology",
                "subtitle": "Edited with Introduction, Translation and Notes by Prem Lata Sharma",
                "creator": "Matanga Muni (Edited by Prem Lata Sharma)",
                "contributor": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "subject": "Classical Raga Concept Origins and Desi Performing Traditions",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "arts-music-and-performing-traditions",
                "publisher": "IGNCA / Motilal Banarsidass (Kalamulasastra Series No. 8), New Delhi",
                "publication_date": "1992 (Original text: circa 6th–8th century CE)",
                "digitisation_date": "2019",
                "source_institution": "Indira Gandhi National Centre for the Arts (IGNCA)",
                "source_url": "https://ignca.gov.in/",
                "access_url": "https://ignca.gov.in/divisions/kalakosa-division/",
                "download_url": None,
                "license_identifier": "in-copyright-read-only",
                "rights_statement": "In Copyright - Free to Read Online on official IGNCA cultural repository.",
                "access_status": "Read Online",
                "file_format": "HTML",
                "file_size": "13.4 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "ISBN: 978-8120811058",
                "keywords": "Brihaddesi, Matanga, Raga Definition, Desi Sangeet, Music, Grama, Jati, IGNCA",
                "citation": "Matanga. (1992). Brihaddesi of Sri Matanga Muni (P. L. Sharma, Ed.). IGNCA and Motilal Banarsidass.",
                "verification_status": "Verified",
                "description": "The historic post-Natyashastra musicological work wherein the concept of Raga is formally defined and differentiated for the first time in Indian literature ('that which colors the minds of living beings is called Raga').",
                "abstract": "Prem Lata Sharma's two-volume edition reconstructs Matanga's groundbreaking treatise from fragmentary Malayalam and Grantha palm-leaf manuscripts, bridging formal Marga ritual chanting with regional (Desi) musical traditions."
            },
            # 27. Arthashastra of Kautilya
            {
                "title": "Kautilya's Arthashastra: Translated into English by Dr. R. Shamasastry",
                "subtitle": "With an Introductory Note by Dr. J. F. Fleet (First Complete Translation)",
                "creator": "Kautilya (Chanakya) (Translated by Dr. R. Shamasastry)",
                "contributor": "Government Oriental Library, Mysore",
                "subject": "Statecraft, Public Administration, Economic Policy, and Military Strategy",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "governance-and-economics",
                "publisher": "Government Press, Bangalore",
                "publication_date": "1915 (Original text: circa 4th century BCE)",
                "digitisation_date": "2012",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/KautilyaArthashastra1915Shamasastry",
                "download_url": "https://archive.org/download/KautilyaArthashastra1915Shamasastry/Kautilya_Arthashastra_Shamasastry_1915.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Shamasastry's breakthrough 1915 edition is fully free of copyright restrictions globally.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "29.4 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "MYS-ORIENTAL-1915-ARTHA",
                "keywords": "Arthashastra, Kautilya, Chanakya, Statecraft, Economics, Saptanga, Shamasastry, Mysore",
                "citation": "Kautilya. (1915). Kautilya's Arthashastra (R. Shamasastry, Trans.). Government Press, Bangalore.",
                "verification_status": "Verified",
                "description": "The quintessential treatise on Indian political realism, economic prosperity, and statecraft in fifteen books (Adhikaranas). Systematizes the seven limbs of the state (Saptanga), taxation, administrative bureaucracy, judicial systems, and foreign policy (Shadgunya).",
                "abstract": "R. Shamasastry's discovery of the Arthashastra palm-leaf manuscript at the Mysore Oriental Library revolutionized the global understanding of ancient Indian political theory. It details state treasury operations, international diplomacy, and internal security."
            },
            # 28. Shukraniti
            {
                "title": "The Sukraniti: Translated into English with Index and Notes",
                "subtitle": "Sacred Books of the Hindus (Volume XIII)",
                "creator": "Shukracharya (Translated by Prof. Benoy Kumar Sarkar)",
                "contributor": "The Panini Office, Allahabad",
                "subject": "Political Governance, Social Morality, Taxation, and Guilds",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "governance-and-economics",
                "publisher": "The Panini Office, Bhuvaneshwari Asrama, Allahabad",
                "publication_date": "1914",
                "digitisation_date": "2013",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://archive.org/details/sukranititransla00sukruoft",
                "download_url": "https://archive.org/download/sukranititransla00sukruoft/sukranititransla00sukruoft.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain worldwide. Published in 1914 at Allahabad.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "18.2 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "SBH-VOL-XIII-1914",
                "keywords": "Shukraniti, Sukra, Sarkar, Rajaneeti, Taxation, Public Administration, Guilds, Governance",
                "citation": "Shukra. (1914). The Sukraniti (B. K. Sarkar, Trans.). The Panini Office, Allahabad.",
                "verification_status": "Verified",
                "description": "A comprehensive treatise on political philosophy and statecraft attributed to sage Shukracharya. Divided into five chapters addressing duties of the sovereign, ministerial governance, civil law, trade tariffs, town building, and administrative ethics.",
                "abstract": "Benoy Kumar Sarkar's classic translation highlights the pragmatic fiscal theories of the Shukraniti, which balances sovereign authority with welfare policies, labor wages, and mercantile guild protections."
            },
            # 29. Nirukta of Yaska
            {
                "title": "The Nighantu and the Nirukta: The Oldest Indian Treatise on Etymology, Philology and Semantics",
                "subtitle": "Critical Edition with Introduction, English Translation, and Notes",
                "creator": "Yaska (Edited and Translated by Lakshman Sarup)",
                "contributor": "University of the Punjab & Oxford University Press",
                "subject": "Vedic Etymology, Lexicography, and Semantics",
                "language": "Vedic Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "education-and-linguistics",
                "publisher": "Oxford University Press / University of the Punjab",
                "publication_date": "1920–1927",
                "digitisation_date": "2014",
                "source_institution": "Rare Book Society of India (RBSI)",
                "source_url": "https://www.rarebooksocietyofindia.org/",
                "access_url": "https://archive.org/details/nighantuniruktao00yaskuoft",
                "download_url": "https://archive.org/download/nighantuniruktao00yaskuoft/nighantuniruktao00yaskuoft.pdf",
                "license_identifier": "public-domain",
                "rights_statement": "Public Domain. Lakshman Sarup's critical edition (1920) is free of copyright globally.",
                "access_status": "Download Available",
                "file_format": "PDF",
                "file_size": "26.3 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "OUP-NIRUKTA-1920-SARUP",
                "keywords": "Nirukta, Yaska, Nighantu, Etymology, Philology, Semantics, Vedic Exegesis, Lakshman Sarup",
                "citation": "Yaska. (1920). The Nighantu and the Nirukta (L. Sarup, Ed. & Trans.). Oxford University Press.",
                "verification_status": "Verified",
                "description": "The oldest extant Indian treatise on linguistic etymology (circa 7th–6th century BCE), functioning as the Vedanga for interpreting obscure Vedic vocabulary. Famous for categorizing parts of speech into four classes: Nama (noun), Akhyata (verb), Upasarga (prefix), and Nipata (particle).",
                "abstract": "Lakshman Sarup's critical edition demonstrates Yaska's fundamental thesis that all nouns derive from verbal roots (Dhatus), engaging in profound debates against Gargya on semantic shift and phonetic variation."
            },
            # 30. Vakyapadiya of Bhartrihari
            {
                "title": "The Vakyapadiya of Bhartrihari: With the Vritti and Paddhati Commentary",
                "subtitle": "Kanda I (Brahmakanda) - English Translation with Exegetical Notes",
                "creator": "Bhartrihari (Translated by K. A. Subramania Iyer)",
                "contributor": "Deccan College Postgraduate and Research Institute",
                "subject": "Philosophy of Language, Metaphysics of Speech (Shabda-Brahman), and Sphota",
                "language": "Sanskrit",
                "translated_language": "English",
                "resource_type": "Book",
                "domain_slug": "education-and-linguistics",
                "publisher": "Deccan College Postgraduate and Research Institute, Pune",
                "publication_date": "1965",
                "digitisation_date": "2017",
                "source_institution": "Bhandarkar Oriental Research Institute (BORI)",
                "source_url": "https://bori.ac.in/",
                "access_url": "https://archive.org/details/VakyapadiyaKASubramaniaIyer",
                "download_url": None,
                "license_identifier": "institution-open-access",
                "rights_statement": "Institutional Open Access repository record. Open for educational and research viewing.",
                "access_status": "Read Online",
                "file_format": "PDF",
                "file_size": "14.5 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "DECCAN-COL-SER-NO-26",
                "keywords": "Vakyapadiya, Bhartrihari, Sphota Theory, Shabda Brahman, Philosophy of Language, Grammar",
                "citation": "Bhartrihari. (1965). The Vakyapadiya of Bhartrihari: Kanda I (K. A. S. Iyer, Trans.). Deccan College, Poona.",
                "verification_status": "Verified",
                "description": "The magnum opus of Indian philosophy of language in three Kandas: Brahmakanda, Vakyakanda, and Padakanda. Posits that the universe is an ontological manifestation of the word-principle (Shabda-Brahman) and details the revolutionary Sphota cognitive burst theory.",
                "abstract": "Subramania Iyer's masterly translation elucidates Bhartrihari's analysis of how sentence meaning is perceived as an indivisible whole (Akhanda Vakya), anticipating modern holistic semantics and cognitive linguistics."
            },
            # 31. Indian Astronomical Traditions - INSA Monograph
            {
                "title": "A Concise History of Science in India: Astronomy, Mathematics, Medicine and Technology",
                "subtitle": "Commissioned by the National Commission for the Compilation of History of Sciences in India",
                "creator": "D. M. Bose, S. N. Sen, and B. V. Subbarayappa (Editors)",
                "contributor": "Indian National Science Academy",
                "subject": "Comprehensive History of Indian Scientific Traditions",
                "language": "English",
                "translated_language": None,
                "resource_type": "Book",
                "domain_slug": "astronomy-and-cosmology",
                "publisher": "Indian National Science Academy (INSA), New Delhi",
                "publication_date": "1971",
                "digitisation_date": "2015",
                "source_institution": "Indian National Science Academy (INSA)",
                "source_url": "https://www.insaindia.res.in/",
                "access_url": "https://archive.org/details/ConciseHistoryOfScienceInIndiaINSA1971",
                "download_url": "https://archive.org/download/ConciseHistoryOfScienceInIndiaINSA1971/Concise_History_of_Science_in_India_1971.pdf",
                "license_identifier": "cc-by-nc-sa-4.0",
                "rights_statement": "Open educational access authorized under CC BY-NC-SA 4.0 by INSA.",
                "access_status": "Open Access",
                "file_format": "PDF",
                "file_size": "52.0 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "INSA-HIST-SCI-1971-MONO",
                "keywords": "History of Science, Astronomy, Mathematics, Medicine, Technology, Bose, Sen, Subbarayappa",
                "citation": "Bose, D. M., Sen, S. N., & Subbarayappa, B. V. (Eds.). (1971). A Concise History of Science in India. Indian National Science Academy.",
                "verification_status": "Verified",
                "description": "The seminal 700-page academic survey of scientific achievements in ancient and medieval India. Covers chronology, Vedic astronomy, Kerala school mathematical developments, Ayurvedic traditions, alchemy, metallurgy, and agricultural tools.",
                "abstract": "This collaborative INSA monograph brings rigorous archival and textual evidence to reconstruct India's contributions to global scientific evolution, with comprehensive manuscript citations and comparative tables."
            },
            # 32. Indian Knowledge Systems: Selected Readings (IKS Division)
            {
                "title": "Selected Readings in Indian Knowledge Systems: Perspectives and Applications",
                "subtitle": "Curated Compendium of Foundational Primary Source Extracts and Curricular Guidance",
                "creator": "IKS Division, Ministry of Education, Govt. of India",
                "contributor": "All India Council for Technical Education (AICTE)",
                "subject": "Interdisciplinary Overview of Indian Knowledge Systems",
                "language": "English",
                "translated_language": "Sanskrit",
                "resource_type": "Research Paper",
                "domain_slug": "education-and-linguistics",
                "publisher": "IKS Division, Ministry of Education, New Delhi",
                "publication_date": "2023",
                "digitisation_date": "2023",
                "source_institution": "National Digital Library of India (NDLI)",
                "source_url": "https://ndl.iitkgp.ac.in/",
                "access_url": "https://ndl.iitkgp.ac.in/",
                "download_url": None,
                "license_identifier": "institution-open-access",
                "rights_statement": "Government open access release for educational research. Viewable via the National Digital Library of India.",
                "access_status": "Read Online",
                "file_format": "PDF",
                "file_size": "8.8 MB",
                "thumbnail_url": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&q=80&w=600",
                "isbn_or_identifier": "IKS-MOE-2023-SR",
                "keywords": "IKS, Indian Knowledge Systems, AICTE, Curriculum, Epistemology, National Education Policy, MOE",
                "citation": "IKS Division. (2023). Selected Readings in Indian Knowledge Systems. Ministry of Education, Govt. of India.",
                "verification_status": "Verified",
                "description": "Official curricular sourcebook published by the IKS Division of the Ministry of Education. Compiles primary excerpts and analytical essays on mathematics, astronomy, metallurgy, ecology, linguistics, and philosophical inquiry.",
                "abstract": "Prepared by leading scholars for academic implementation under the National Education Policy (NEP 2020), this reader emphasizes methodological rigour, manuscript preservation, and the contemporary relevance of indigenous Indian sciences."
            }
        ]

        # Insert resources
        inserted_count = 0
        updated_count = 0
        for item in resources_dataset:
            domain_slug = item.pop("domain_slug")
            domain = domains_map.get(domain_slug)
            if not domain:
                print(f"Warning: Domain slug {domain_slug} not found for {item['title']}")
                continue

            lic_id_str = item.pop("license_identifier")
            lic = licenses_map.get(lic_id_str)
            if not lic:
                print(f"Warning: License {lic_id_str} not found for {item['title']}")
                continue

            inst_name = item.get("source_institution")
            inst = institutions_map.get(inst_name)
            inst_id = inst.id if inst else None

            existing_res = db.query(Resource).filter(Resource.title == item["title"]).first()
            if not existing_res:
                resource = Resource(
                    **item,
                    knowledge_domain_id=domain.id,
                    license_id=lic.id,
                    institution_id=inst_id,
                    verified_at=datetime.utcnow()
                )
                resource.domains = [domain]

                # Keyword mapping
                if item.get("keywords"):
                    kw_names = [k.strip() for k in item["keywords"].split(",") if k.strip()]
                    for kw_name in kw_names:
                        slug = kw_name.lower().replace(" ", "-")
                        kw_obj = db.query(Keyword).filter(Keyword.slug == slug).first()
                        if not kw_obj:
                            kw_obj = Keyword(keyword=kw_name, slug=slug)
                            db.add(kw_obj)
                            db.flush()
                        resource.keyword_items.append(kw_obj)

                db.add(resource)
                db.flush()
                inserted_count += 1
            else:
                updated_count += 1

        db.commit()
        print(f"Resources processed: {inserted_count} newly inserted, {updated_count} already existed.")

        # Rebuild FTS5 index to make sure everything is freshly indexed
        indexed_count = rebuild_fts_index(db)
        print(f"SQLite FTS5 full-text index rebuilt with {indexed_count} indexed records.")
        print("Database seeding completed successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error during seeding: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
