import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BookMarked, Compass, Layers, Info, Shield, LogOut, Menu, X, Landmark } from 'lucide-react';
import { useAuth } from '../../context/AuthContext';

export const Navbar: React.FC = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const { admin, isAuthenticated, logout } = useAuth();
  const location = useLocation();

  const isActive = (path: string) => {
    if (path === '/' && location.pathname === '/') return true;
    if (path !== '/' && location.pathname.startsWith(path)) return true;
    return false;
  };

  const navLinks = [
    { label: 'Home', path: '/', icon: Landmark },
    { label: 'Explore Catalog', path: '/explore', icon: Compass },
    { label: 'Knowledge Domains', path: '/domains', icon: Layers },
    { label: 'About Repository', path: '/about', icon: Info },
  ];

  return (
    <header className="sticky top-0 z-40 bg-navy-950/95 backdrop-blur-md border-b border-gold-500/30 text-ivory-50 shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Repository Branding */}
          <Link to="/" className="flex items-center gap-3 group">
            <div className="w-11 h-11 rounded-lg bg-navy-900 border border-gold-400/40 flex items-center justify-center shadow-inner group-hover:border-gold-400 transition-colors">
              <BookMarked className="w-6 h-6 text-gold-400 group-hover:scale-105 transition-transform" />
            </div>
            <div>
              <span className="font-serif text-lg md:text-xl font-bold tracking-tight text-white block leading-tight">
                IKS Digital Repository
              </span>
              <span className="text-[11px] text-gold-300/80 uppercase tracking-widest font-mono block">
                Indian Knowledge Systems • Academic Archive
              </span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-1">
            {navLinks.map((link) => {
              const Icon = link.icon;
              const active = isActive(link.path);
              return (
                <Link
                  key={link.path}
                  to={link.path}
                  className={`px-3.5 py-2 rounded-lg text-sm font-medium transition-all flex items-center gap-2 ${
                    active
                      ? 'bg-navy-850 text-gold-300 border border-gold-500/30'
                      : 'text-ivory-200 hover:text-white hover:bg-navy-900'
                  }`}
                >
                  <Icon className={`w-4 h-4 ${active ? 'text-gold-400' : 'text-ivory-400'}`} />
                  <span>{link.label}</span>
                </Link>
              );
            })}
          </nav>

          {/* Admin / Actions Portal */}
          <div className="hidden md:flex items-center gap-3">
            {isAuthenticated ? (
              <div className="flex items-center gap-2">
                <Link
                  to="/admin/dashboard"
                  className="px-3.5 py-1.5 rounded-lg bg-gold-500/20 hover:bg-gold-500/30 text-gold-300 border border-gold-500/40 text-xs font-medium transition-colors flex items-center gap-1.5"
                >
                  <Shield className="w-3.5 h-3.5 text-gold-400" />
                  <span>Curator Panel</span>
                </Link>
                <button
                  onClick={logout}
                  title="Sign Out"
                  className="p-1.5 text-ivory-400 hover:text-rose-300 hover:bg-navy-900 rounded-lg transition-colors"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            ) : (
              <Link
                to="/admin/login"
                className="px-3.5 py-1.5 rounded-lg bg-navy-900 hover:bg-navy-850 border border-ivory-300/20 text-ivory-200 hover:text-white text-xs font-medium transition-colors flex items-center gap-1.5"
              >
                <Shield className="w-3.5 h-3.5 text-gold-400" />
                <span>Admin Login</span>
              </Link>
            )}
          </div>

          {/* Mobile Menu Toggle */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden p-2 text-ivory-300 hover:text-white rounded-lg hover:bg-navy-900"
            aria-label="Toggle Navigation"
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="md:hidden bg-navy-950 border-b border-gold-500/30 px-4 pt-2 pb-6 space-y-2">
          {navLinks.map((link) => {
            const Icon = link.icon;
            const active = isActive(link.path);
            return (
              <Link
                key={link.path}
                to={link.path}
                onClick={() => setMobileMenuOpen(false)}
                className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium ${
                  active ? 'bg-navy-850 text-gold-300' : 'text-ivory-200 hover:bg-navy-900'
                }`}
              >
                <Icon className="w-4 h-4 text-gold-400" />
                <span>{link.label}</span>
              </Link>
            );
          })}

          <div className="pt-4 border-t border-navy-800 flex items-center justify-between">
            {isAuthenticated ? (
              <>
                <Link
                  to="/admin/dashboard"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2 text-xs font-medium text-gold-300"
                >
                  <Shield className="w-4 h-4" />
                  <span>Admin Dashboard ({admin?.username})</span>
                </Link>
                <button
                  onClick={() => {
                    logout();
                    setMobileMenuOpen(false);
                  }}
                  className="text-xs text-rose-300 flex items-center gap-1"
                >
                  <LogOut className="w-4 h-4" />
                  <span>Sign Out</span>
                </button>
              </>
            ) : (
              <Link
                to="/admin/login"
                onClick={() => setMobileMenuOpen(false)}
                className="flex items-center gap-2 text-xs font-medium text-ivory-300 hover:text-white"
              >
                <Shield className="w-4 h-4 text-gold-400" />
                <span>Curator / Admin Access</span>
              </Link>
            )}
          </div>
        </div>
      )}
    </header>
  );
};
