import React from 'react';
import { Link } from 'react-router-dom';
import { BookMarked, ShieldCheck, Scale, Globe, ArrowUpRight } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-navy-950 text-ivory-300 border-t border-gold-500/30 pt-16 pb-12 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-10 pb-12 border-b border-navy-800">
          {/* Brand & Mandate */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-navy-900 border border-gold-500/40 flex items-center justify-center">
                <BookMarked className="w-5 h-5 text-gold-400" />
              </div>
              <div>
                <span className="font-serif text-lg font-bold text-white block">
                  IKS Digital Repository
                </span>
                <span className="text-[11px] text-gold-400/80 font-mono tracking-widest uppercase block">
                  Preservation • Categorisation • Open Access
                </span>
              </div>
            </div>
            <p className="text-xs text-ivory-400 leading-relaxed max-w-md">
              An academic digital repository prototype engineered to categorize, search, and legally govern open access resources and classical manuscripts across the multifaceted branches of Indian Knowledge Systems (IKS).
            </p>
            <div className="flex flex-wrap items-center gap-3 pt-2 text-xs text-gold-300/90 font-mono">
              <span className="flex items-center gap-1 bg-navy-900 px-2.5 py-1 rounded border border-navy-800">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
                Dublin Core Compliant
              </span>
              <span className="flex items-center gap-1 bg-navy-900 px-2.5 py-1 rounded border border-navy-800">
                <Scale className="w-3.5 h-3.5 text-gold-400" />
                Legally Verified Rights
              </span>
            </div>
          </div>

          {/* Quick Navigation */}
          <div>
            <h4 className="text-xs font-bold text-white uppercase tracking-widest font-mono mb-4">
              Repository Index
            </h4>
            <ul className="space-y-2.5 text-xs">
              <li>
                <Link to="/explore" className="hover:text-gold-300 transition-colors flex items-center gap-1">
                  Catalogue Explorer
                </Link>
              </li>
              <li>
                <Link to="/domains" className="hover:text-gold-300 transition-colors flex items-center gap-1">
                  12 Knowledge Domains
                </Link>
              </li>
              <li>
                <Link to="/about" className="hover:text-gold-300 transition-colors flex items-center gap-1">
                  Archival Methodology & Dublin Core
                </Link>
              </li>
              <li>
                <Link to="/admin/login" className="hover:text-gold-300 transition-colors flex items-center gap-1">
                  Curator / Admin Console
                </Link>
              </li>
            </ul>
          </div>

          {/* Institutional Partners */}
          <div>
            <h4 className="text-xs font-bold text-white uppercase tracking-widest font-mono mb-4">
              Source Archives
            </h4>
            <ul className="space-y-2 text-xs text-ivory-400">
              <li className="flex items-center gap-1.5">
                <Globe className="w-3 h-3 text-gold-500" />
                <span>IGNCA Cultural Archives</span>
              </li>
              <li className="flex items-center gap-1.5">
                <Globe className="w-3 h-3 text-gold-500" />
                <span>National Digital Library of India (NDLI)</span>
              </li>
              <li className="flex items-center gap-1.5">
                <Globe className="w-3 h-3 text-gold-500" />
                <span>Bhandarkar Oriental Research Institute (BORI)</span>
              </li>
              <li className="flex items-center gap-1.5">
                <Globe className="w-3 h-3 text-gold-500" />
                <span>Indian National Science Academy (INSA)</span>
              </li>
              <li className="flex items-center gap-1.5">
                <Globe className="w-3 h-3 text-gold-500" />
                <span>Rare Book Society of India (RBSI)</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="pt-8 flex flex-col md:flex-row items-center justify-between text-xs text-navy-400 gap-4">
          <p>© 2026 Digital Repository of Selected IKS Texts and Resources. Built for academic research and cultural heritage preservation.</p>
          <div className="flex items-center gap-4 text-ivory-400">
            <span>Powered by FastAPI & SQLite FTS5</span>
            <span>•</span>
            <Link to="/about#licensing" className="hover:text-gold-300 underline">
              Licensing Policy
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
};
