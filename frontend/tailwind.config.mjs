/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
    theme: {
        extend: {
            colors: {
                'primary-dark': '#2b2d42',
                'primary-light': '#8d99ae',
                'accent': '#ef233c',
                'accent-secondary': '#ff6b35',
            },
            backgroundImage: {
                'gradient-primary': 'linear-gradient(135deg, #2b2d42 0%, #1a1b2e 100%)',
                'gradient-accent': 'linear-gradient(135deg, #ef233c 0%, #ff6b35 100%)',
            }
        }
    },
    plugins: [require('@tailwindcss/typography'), require('daisyui')],
    daisyui: {
        themes: [
            {
                dark: {
                    "primary": "#ef233c",
                    "secondary": "#ff6b35",
                    "accent": "#2b2d42",
                    "neutral": "#1a1b2e",
                    "base-100": "#2b2d42",
                    "base-200": "#1a1b2e",
                    "base-300": "#16171f",
                    "info": "#3b82f6",
                    "success": "#10b981",
                    "warning": "#f59e0b",
                    "error": "#ef4444",
                },
            },
            {
                light: {
                    "primary": "#ef233c",
                    "secondary": "#ff6b35",
                    "accent": "#2b2d42",
                    "neutral": "#f3f4f6",
                    "base-100": "#ffffff",
                    "base-200": "#f3f4f6",
                    "base-300": "#e5e7eb",
                    "info": "#3b82f6",
                    "success": "#10b981",
                    "warning": "#f59e0b",
                    "error": "#ef4444",
                },
            },
        ],
    },
}