import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, X, Book, Tag, User, ArrowRight } from 'lucide-react';
import { api } from '../../api/client';
import { SearchSuggestionItem } from '../../types';

interface SearchBarProps {
  initialValue?: string;
  placeholder?: string;
  autoFocus?: boolean;
  className?: string;
  onSearchSubmit?: (query: string) => void;
}

export const SearchBar: React.FC<SearchBarProps> = ({
  initialValue = '',
  placeholder = 'Search treaties, authors, topics (e.g., Aryabhatiya, Sushruta, Vastu)...',
  autoFocus = false,
  className = '',
  onSearchSubmit,
}) => {
  const [query, setQuery] = useState(initialValue);
  const [suggestions, setSuggestions] = useState<SearchSuggestionItem[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    setQuery(initialValue);
  }, [initialValue]);

  // Handle outside click
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Fetch suggestions with debounce
  useEffect(() => {
    const trimmed = query.trim();
    if (trimmed.length < 2) {
      setSuggestions([]);
      setIsOpen(false);
      return;
    }

    const timer = setTimeout(async () => {
      setIsLoading(true);
      try {
        const results = await api.getSuggestions(trimmed, 7);
        setSuggestions(results);
        setIsOpen(results.length > 0);
      } catch (err) {
        console.error('Failed to fetch suggestions', err);
      } finally {
        setIsLoading(false);
      }
    }, 200);

    return () => clearTimeout(timer);
  }, [query]);

  const handleSubmit = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    const cleanQuery = query.trim();
    setIsOpen(false);
    if (onSearchSubmit) {
      onSearchSubmit(cleanQuery);
    } else {
      navigate(`/explore?q=${encodeURIComponent(cleanQuery)}`);
    }
  };

  const handleSelectSuggestion = (item: SearchSuggestionItem) => {
    setIsOpen(false);
    if (item.type === 'title' && item.matched_id) {
      navigate(`/resources/${item.matched_id}`);
    } else {
      setQuery(item.text);
      if (onSearchSubmit) {
        onSearchSubmit(item.text);
      } else {
        navigate(`/explore?q=${encodeURIComponent(item.text)}`);
      }
    }
  };

  const getIconForType = (type: string) => {
    switch (type) {
      case 'title':
        return <Book className="w-3.5 h-3.5 text-gold-600" />;
      case 'creator':
        return <User className="w-3.5 h-3.5 text-navy-600" />;
      case 'keyword':
      default:
        return <Tag className="w-3.5 h-3.5 text-emerald-600" />;
    }
  };

  return (
    <div ref={dropdownRef} className={`relative w-full ${className}`}>
      <form onSubmit={handleSubmit} className="relative flex items-center">
        <div className="absolute left-4 pointer-events-none text-navy-400">
          <Search className="w-5 h-5 text-gold-600" />
        </div>
        <input
          ref={inputRef}
          type="text"
          value={query}
          autoFocus={autoFocus}
          onChange={(e) => setQuery(e.target.value)}
          onFocus={() => query.trim().length >= 2 && suggestions.length > 0 && setIsOpen(true)}
          placeholder={placeholder}
          className="w-full pl-12 pr-28 py-3.5 bg-white border border-ivory-300 rounded-xl shadow-parchment text-navy-950 placeholder-navy-400 focus:outline-none focus:ring-2 focus:ring-gold-400/50 focus:border-gold-500 text-sm md:text-base transition-all"
        />

        {query && (
          <button
            type="button"
            onClick={() => {
              setQuery('');
              setSuggestions([]);
              setIsOpen(false);
              inputRef.current?.focus();
            }}
            className="absolute right-20 text-navy-400 hover:text-navy-700 p-1"
          >
            <X className="w-4 h-4" />
          </button>
        )}

        <button
          type="submit"
          className="absolute right-2 px-4 py-2 bg-navy-900 hover:bg-navy-800 text-gold-300 rounded-lg text-sm font-medium transition-colors shadow-sm flex items-center gap-1.5"
        >
          <span>Search</span>
          <ArrowRight className="w-3.5 h-3.5" />
        </button>
      </form>

      {/* Autocomplete Dropdown */}
      {isOpen && (
        <div className="absolute top-full left-0 right-0 mt-2 bg-white rounded-xl border border-ivory-300 shadow-xl overflow-hidden z-40 animate-fade-in">
          <div className="px-3 py-2 bg-ivory-100/70 border-b border-ivory-200 text-xs font-semibold text-navy-600 uppercase tracking-wider flex items-center justify-between">
            <span>Suggestions</span>
            {isLoading && <span className="text-[10px] lowercase italic text-navy-400">updating...</span>}
          </div>
          <ul className="py-1 divide-y divide-ivory-100 max-h-72 overflow-y-auto">
            {suggestions.map((item, idx) => (
              <li key={idx}>
                <button
                  type="button"
                  onClick={() => handleSelectSuggestion(item)}
                  className="w-full text-left px-4 py-2.5 hover:bg-gold-50/60 flex items-center justify-between transition-colors group"
                >
                  <div className="flex items-center gap-2.5 min-w-0">
                    <span className="p-1 rounded bg-ivory-100 group-hover:bg-gold-100 transition-colors">
                      {getIconForType(item.type)}
                    </span>
                    <span className="text-sm text-navy-900 truncate font-medium">{item.text}</span>
                  </div>
                  <span className="text-[11px] uppercase tracking-wider text-navy-600 ml-2 flex-shrink-0">
                    {item.type}
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
