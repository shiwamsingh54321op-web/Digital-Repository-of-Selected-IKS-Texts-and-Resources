/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#060E1A',
          900: '#0B192C',
          850: '#0F223D',
          800: '#142C4E',
          700: '#1E3E6B',
          600: '#2A528A',
        },
        gold: {
          50: '#FCF9F2',
          100: '#F7F0E1',
          200: '#EBDCB9',
          300: '#DEC48E',
          400: '#C5A880',
          500: '#B8860B',
          600: '#946B08',
          700: '#735205',
        },
        ivory: {
          50: '#FDFBF7',
          100: '#F8F4EB',
          200: '#EFE7D5',
          300: '#E4D7BE',
          400: '#CFC0A0',
          500: '#8C7E60',
          800: '#3D3627',
          900: '#262117',
        },
      },
      fontFamily: {
        serif: ['Cinzel', 'Merriweather', 'Georgia', 'serif'],
        sans: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      boxShadow: {
        'parchment': '0 4px 20px -2px rgba(11, 25, 44, 0.06), 0 2px 6px -1px rgba(11, 25, 44, 0.04)',
        'parchment-lg': '0 10px 30px -4px rgba(11, 25, 44, 0.1), 0 4px 12px -2px rgba(11, 25, 44, 0.06)',
      }
    },
  },
  plugins: [],
}
