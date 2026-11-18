import React, { useState } from 'react';
import { X, Copy, Check, Quote, BookOpen } from 'lucide-react';
import { Citations } from '../../types';

interface CitationModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  citations: Citations | null;
  isLoading?: boolean;
}

export const CitationModal: React.FC<CitationModalProps> = ({
  isOpen,
  onClose,
  title,
  citations,
  isLoading = false,
}) => {
  const [activeTab, setActiveTab] = useState<'apa' | 'mla' | 'chicago' | 'bibtex'>('apa');
  const [copied, setCopied] = useState<boolean>(false);

  if (!isOpen) return null;

  const getCitationText = () => {
    if (!citations) return '';
    return citations[activeTab] || '';
  };

  const handleCopy = () => {
    const text = getCitationText();
    if (text) {
      navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-navy-950/60 backdrop-blur-sm animate-fade-in">
      <div className="bg-ivory-50 border border-gold-300/40 rounded-xl max-w-2xl w-full shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="bg-navy-900 text-ivory-50 px-6 py-4 flex items-center justify-between border-b border-gold-500/30">
          <div className="flex items-center gap-2">
            <Quote className="w-5 h-5 text-gold-400" />
            <h3 className="font-serif text-lg font-medium tracking-wide">Scholarly Citation</h3>
          </div>
          <button
            onClick={onClose}
            className="text-ivory-300 hover:text-white transition-colors p-1 rounded-md hover:bg-navy-800"
            aria-label="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Resource Title Reference */}
        <div className="px-6 py-3 bg-ivory-100 border-b border-ivory-200 text-sm text-navy-800 flex items-center gap-2">
          <BookOpen className="w-4 h-4 text-gold-600 flex-shrink-0" />
          <span className="font-medium italic truncate">{title}</span>
        </div>

        {/* Style Tabs */}
        <div className="px-6 pt-4 flex gap-2 border-b border-ivory-200">
          {(['apa', 'mla', 'chicago', 'bibtex'] as const).map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`pb-2.5 px-3 text-xs font-semibold uppercase tracking-wider transition-all border-b-2 ${
                activeTab === tab
                  ? 'border-gold-500 text-navy-900 font-bold'
                  : 'border-transparent text-navy-600 hover:text-navy-900'
              }`}
            >
              {tab.toUpperCase()}
            </button>
          ))}
        </div>

        {/* Content Body */}
        <div className="p-6">
          {isLoading ? (
            <div className="py-12 flex justify-center items-center text-navy-600 text-sm">
              <div className="w-6 h-6 border-2 border-gold-500 border-t-transparent rounded-full animate-spin mr-3" />
              Generating academic citation formats...
            </div>
          ) : (
            <div>
              <div className="relative bg-white border border-ivory-300 rounded-lg p-4 font-mono text-xs text-navy-900 leading-relaxed shadow-inner overflow-x-auto min-h-[90px] whitespace-pre-wrap">
                {getCitationText() || 'Citation unavailable.'}
              </div>

              <div className="mt-4 flex items-center justify-between">
                <span className="text-xs text-navy-500 italic">
                  Format aligns with standard institutional reference manuals.
                </span>
                <button
                  onClick={handleCopy}
                  className="flex items-center gap-1.5 px-4 py-2 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-lg text-xs font-medium transition-colors shadow-sm"
                >
                  {copied ? (
                    <>
                      <Check className="w-3.5 h-3.5 text-emerald-400" />
                      <span>Copied to Clipboard</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3.5 h-3.5" />
                      <span>Copy Citation</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
