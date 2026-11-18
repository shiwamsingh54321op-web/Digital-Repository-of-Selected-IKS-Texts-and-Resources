import React from 'react';

interface BadgeProps {
  variant?: 'access' | 'verification' | 'domain' | 'type' | 'language' | 'default';
  label: string;
  className?: string;
}

export const Badge: React.FC<BadgeProps> = ({ variant = 'default', label, className = '' }) => {
  let colorStyles = 'bg-ivory-200 text-navy-800 border-ivory-300';

  if (variant === 'access') {
    switch (label.toLowerCase()) {
      case 'open access':
      case 'download available':
        colorStyles = 'bg-emerald-50 text-emerald-800 border-emerald-200 font-medium';
        break;
      case 'read online':
        colorStyles = 'bg-amber-50 text-amber-800 border-amber-200 font-medium';
        break;
      case 'restricted access':
        colorStyles = 'bg-rose-50 text-rose-800 border-rose-200 font-medium';
        break;
      case 'metadata only':
      case 'rights unverified':
        colorStyles = 'bg-slate-100 text-slate-700 border-slate-300 font-medium';
        break;
      default:
        colorStyles = 'bg-ivory-200 text-navy-800 border-ivory-300';
    }
  } else if (variant === 'verification') {
    switch (label.toLowerCase()) {
      case 'verified':
        colorStyles = 'bg-emerald-50 text-emerald-700 border-emerald-300';
        break;
      case 'pending':
        colorStyles = 'bg-amber-50 text-amber-700 border-amber-300';
        break;
      case 'rejected':
        colorStyles = 'bg-rose-50 text-rose-700 border-rose-300';
        break;
    }
  } else if (variant === 'domain') {
    colorStyles = 'bg-gold-50 text-gold-700 border-gold-200';
  } else if (variant === 'type') {
    colorStyles = 'bg-navy-900 text-gold-300 border-navy-800';
  } else if (variant === 'language') {
    colorStyles = 'bg-ivory-100 text-navy-700 border-ivory-300';
  }

  return (
    <span
      className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs border tracking-wide ${colorStyles} ${className}`}
    >
      {label}
    </span>
  );
};
