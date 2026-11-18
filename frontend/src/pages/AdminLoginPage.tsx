import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Shield, Lock, User, AlertCircle, ArrowRight, CheckCircle2 } from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';

export const AdminLoginPage: React.FC = () => {
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('Admin@IKS2026!');
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
      const authResponse = await api.login(username, password);
      const user = await api.getMe();
      login(authResponse.access_token, user);
      navigate('/admin/dashboard');
    } catch (err: any) {
      setError(err.message || 'Invalid administrator credentials. Access denied.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-[75vh] flex items-center justify-center px-4 sm:px-6 lg:px-8 py-12">
      <div className="max-w-md w-full bg-white border border-ivory-300 rounded-2xl p-8 shadow-parchment-lg space-y-6">
        <div className="text-center space-y-2">
          <div className="w-12 h-12 rounded-xl bg-navy-950 text-gold-400 border border-gold-500/30 flex items-center justify-center mx-auto shadow-sm">
            <Shield className="w-6 h-6" />
          </div>
          <h1 className="font-serif text-2xl font-bold text-navy-950">
            Curator & Admin Portal
          </h1>
          <p className="text-xs text-navy-600">
            Sign in with authorized academic credentials to manage Dublin Core records, audit verification, and export metadata.
          </p>
        </div>

        {error && (
          <div className="p-3 bg-rose-50 border border-rose-200 rounded-xl flex items-center gap-2.5 text-xs text-rose-800">
            <AlertCircle className="w-4 h-4 flex-shrink-0 text-rose-600" />
            <span>{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-mono uppercase tracking-wider font-semibold text-navy-700 mb-1">
              Username
            </label>
            <div className="relative">
              <User className="w-4 h-4 text-navy-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full pl-9 pr-3 py-2.5 bg-ivory-50 border border-ivory-300 rounded-lg text-sm text-navy-950 focus:outline-none focus:ring-2 focus:ring-gold-500/40"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-mono uppercase tracking-wider font-semibold text-navy-700 mb-1">
              Password
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 text-navy-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full pl-9 pr-3 py-2.5 bg-ivory-50 border border-ivory-300 rounded-lg text-sm text-navy-950 focus:outline-none focus:ring-2 focus:ring-gold-500/40"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full mt-2 py-3 bg-navy-950 hover:bg-navy-900 text-gold-300 rounded-xl text-sm font-semibold transition-all flex items-center justify-center gap-2 shadow-sm disabled:opacity-50"
          >
            {isLoading ? (
              <div className="w-4 h-4 border-2 border-gold-400 border-t-transparent rounded-full animate-spin" />
            ) : (
              <>
                <span>Sign In to Admin Console</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </form>

        {/* Development Seed Account Hint */}
        <div className="p-4 bg-ivory-100/70 border border-ivory-200 rounded-xl text-xs space-y-1">
          <div className="flex items-center gap-1.5 font-semibold text-navy-800">
            <CheckCircle2 className="w-3.5 h-3.5 text-gold-600" />
            <span>Default Seed Credentials</span>
          </div>
          <p className="text-navy-600 font-mono text-[11px]">
            User: <code className="bg-white px-1.5 py-0.5 rounded border border-ivory-300 text-navy-900 font-bold">admin</code>
            {' '} | Password: <code className="bg-white px-1.5 py-0.5 rounded border border-ivory-300 text-navy-900 font-bold">Admin@IKS2026!</code>
          </p>
        </div>
      </div>
    </div>
  );
};
