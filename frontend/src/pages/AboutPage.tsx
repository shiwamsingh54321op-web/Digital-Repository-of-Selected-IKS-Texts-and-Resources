import React from 'react';
import {
  BookOpen,
  Scale,
  Search,
  Database,
  Building,
  ShieldCheck,
  CheckCircle2,
  FileText,
  Award
} from 'lucide-react';

export const AboutPage: React.FC = () => {
  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12">
      {/* Title Section */}
      <div className="text-center max-w-3xl mx-auto space-y-4">
        <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-gold-100 border border-gold-300 text-gold-900 text-xs font-mono uppercase tracking-widest">
          <Award className="w-3.5 h-3.5 text-gold-700" />
          <span>Academic Repository Project</span>
        </div>
        <h1 className="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-navy-950">
          About the IKS Digital Repository
        </h1>
        <p className="text-sm sm:text-base text-navy-600 leading-relaxed font-light">
          An institutional-grade prototype built to categorize, search, retrieve, and legally govern open access resources and classical treatises of the Indian Knowledge Systems.
        </p>
      </div>

      {/* Assignment Mandate Callout */}
      <div className="bg-navy-950 text-white rounded-2xl p-6 sm:p-8 border border-gold-500/30 shadow-parchment-lg">
        <div className="flex items-start gap-4">
          <div className="w-10 h-10 rounded-lg bg-navy-900 border border-gold-400/40 flex items-center justify-center flex-shrink-0 text-gold-400 mt-1">
            <BookOpen className="w-5 h-5" />
          </div>
          <div className="space-y-2">
            <h2 className="font-serif text-lg sm:text-xl font-bold text-gold-300">
              Project Assignment Mandate
            </h2>
            <p className="text-xs sm:text-sm text-ivory-200 leading-relaxed italic">
              "Build a prototype repository with metadata, categorisation, search, and retrieval facilities for legally usable/open IKS resources."
            </p>
            <p className="text-xs text-ivory-400 leading-relaxed pt-1">
              This system delivers the complete triad of <strong>Database Architecture</strong> (SQLAlchemy/SQLite relational schema with composite indexes), <strong>Information Retrieval Engine</strong> (SQLite FTS5 with BM25 ranking and Unicode diacritic normalisation), and <strong>Web Interface</strong> (React, TypeScript, Tailwind, REST API).
            </p>
          </div>
        </div>
      </div>

      {/* Visual Heritage Context */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {[
          {
            img: '/images/iks-gurukul.jpg',
            title: 'Ancient Centers of Learning',
            caption: 'Universities such as Takṣaśilā and Nālandā housed vast manuscript libraries and fostered interdisciplinary scholarship across Asia.'
          },
          {
            img: '/images/iks-astronomy.jpg',
            title: 'Empirical Observation',
            caption: 'From Vedic calendars to Jaipur’s Jantar Mantar, Indian astronomy paired mathematical Siddhāntas with precision instruments.'
          },
          {
            img: '/images/iks-architecture.jpg',
            title: 'Engineering & Heritage',
            caption: 'Śilpa and Vāstu texts codified geometry, acoustics, and sustainable water conservation still visible in India’s heritage monuments.'
          }
        ].map((card, idx) => (
          <div key={idx} className="bg-white border border-ivory-300 rounded-xl overflow-hidden shadow-parchment">
            <div className="aspect-[16/9] w-full overflow-hidden bg-ivory-100 border-b border-ivory-200">
              <img
                src={card.img}
                alt={card.title}
                loading="lazy"
                decoding="async"
                className="w-full h-full object-cover"
              />
            </div>
            <div className="p-4 space-y-1">
              <h3 className="font-serif text-sm font-bold text-navy-950">{card.title}</h3>
              <p className="text-xs text-navy-600 leading-relaxed">{card.caption}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Core Architectural Components */}
      <div className="space-y-6">
        <h2 className="font-serif text-2xl font-bold text-navy-950 border-b border-ivory-300 pb-2">
          Methodological Standards
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Dublin Core */}
          <div className="bg-white border border-ivory-300 rounded-xl p-6 shadow-parchment space-y-3">
            <div className="flex items-center gap-2 text-gold-700">
              <Database className="w-5 h-5" />
              <h3 className="font-serif text-base font-bold text-navy-900">
                1. Dublin Core Metadata Standard (ISO 15836)
              </h3>
            </div>
            <p className="text-xs text-navy-600 leading-relaxed">
              Every cataloged record implements all 15 elements of the Dublin Core standard: Title, Creator, Subject, Description, Publisher, Contributor, Date, Type, Format, Identifier (DOI / ISBN / Archive Accession), Source, Language, Relation, Coverage, and Rights.
            </p>
            <div className="flex flex-wrap gap-1.5 pt-2 text-[10px] font-mono text-navy-600">
              <span className="bg-ivory-100 px-2 py-0.5 rounded border border-ivory-200">dc:title</span>
              <span className="bg-ivory-100 px-2 py-0.5 rounded border border-ivory-200">dc:creator</span>
              <span className="bg-ivory-100 px-2 py-0.5 rounded border border-ivory-200">dc:subject</span>
              <span className="bg-ivory-100 px-2 py-0.5 rounded border border-ivory-200">dc:rights</span>
              <span className="bg-ivory-100 px-2 py-0.5 rounded border border-ivory-200">dc:identifier</span>
            </div>
          </div>

          {/* Full Text Search */}
          <div className="bg-white border border-ivory-300 rounded-xl p-6 shadow-parchment space-y-3">
            <div className="flex items-center gap-2 text-gold-700">
              <Search className="w-5 h-5" />
              <h3 className="font-serif text-base font-bold text-navy-900">
                2. Information Retrieval & BM25 Scoring
              </h3>
            </div>
            <p className="text-xs text-navy-600 leading-relaxed">
              Full-text information retrieval uses a native SQLite FTS5 virtual table synchronized via database triggers (`AFTER INSERT`, `UPDATE`, `DELETE`). Queries are weighted across title, subject, creator, and keywords, ranking results by BM25 probabilistic relevance.
            </p>
            <p className="text-xs text-navy-500 italic">
              Tokenized with `unicode61 remove_diacritics 2` and Porter stemming, allowing queries in English, Sanskrit transliteration (IAST), and diacritic variants.
            </p>
          </div>

          {/* Legal Rights Framework */}
          <div className="bg-white border border-ivory-300 rounded-xl p-6 shadow-parchment space-y-3">
            <div className="flex items-center gap-2 text-gold-700">
              <Scale className="w-5 h-5" />
              <h3 className="font-serif text-base font-bold text-navy-900">
                3. Legal Rights & Controlled Downloads
              </h3>
            </div>
            <p className="text-xs text-navy-600 leading-relaxed">
              Strict legal differentiation governs every resource. Open access and public domain materials permit file downloads; in-copyright or research-only materials provide verified metadata and institutional access links while disabling unauthorized file redistribution.
            </p>
            <div className="flex items-center gap-2 text-xs text-emerald-800 font-medium">
              <ShieldCheck className="w-4 h-4 text-emerald-600" />
              <span>Protects cultural copyright while preserving research access</span>
            </div>
          </div>

          {/* Taxonomy Hierarchy */}
          <div className="bg-white border border-ivory-300 rounded-xl p-6 shadow-parchment space-y-3">
            <div className="flex items-center gap-2 text-gold-700">
              <BookOpen className="w-5 h-5" />
              <h3 className="font-serif text-base font-bold text-navy-900">
                4. 52-Domain Taxonomic Hierarchy
              </h3>
            </div>
            <p className="text-xs text-navy-600 leading-relaxed">
              A comprehensive 2-tier classification system representing the disciplines of classical India: Mathematics (*Ganita*), Astronomy (*Jyotisha*), Medicine (*Ayurveda*), Philosophy (*Darshana*), Vedic Literature, Linguistics (*Vyakarana*), Architecture (*Vastu*), Agriculture (*Krishi*), Metallurgy, Economics (*Arthashastra*), and the Arts.
            </p>
          </div>
        </div>
      </div>

      {/* Institutional Source Archives */}
      <div className="bg-white border border-ivory-300 rounded-2xl p-6 sm:p-8 shadow-parchment space-y-6">
        <h2 className="font-serif text-xl font-bold text-navy-950 flex items-center gap-2">
          <Building className="w-5 h-5 text-gold-600" />
          <span>Recognized Source Archives & Repositories</span>
        </h2>
        <p className="text-xs sm:text-sm text-navy-600 leading-relaxed">
          The records in this digital repository are curated and cross-referenced with premier national, academic, and cultural manuscript repositories across India and internationally:
        </p>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 text-xs">
          {[
            'Indira Gandhi National Centre for the Arts (IGNCA)',
            'National Digital Library of India (NDLI, IIT Kharagpur)',
            'Bhandarkar Oriental Research Institute (BORI, Pune)',
            'Indian National Science Academy (INSA, New Delhi)',
            'Saraswathi Mahal Library (Thanjavur)',
            'Oriental Research Institute (Mysore)',
            'The Asiatic Society of Mumbai',
            'Asian Agri-History Foundation (AAHF)',
            'Rare Book Society of India (RBSI)',
            'Sanskrit Documents Consortium',
            'Vedic Heritage Portal (IGNCA)',
            'Shodhganga - INFLIBNET Centre'
          ].map((inst, idx) => (
            <div key={idx} className="flex items-center gap-2 p-3 bg-ivory-50 rounded-lg border border-ivory-200">
              <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
              <span className="font-medium text-navy-900">{inst}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
