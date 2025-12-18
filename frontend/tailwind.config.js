/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./docs/**/*.{md,mdx}",
    "./blog/**/*.{md,mdx}",
    "./pages/**/*.{md,mdx}",
    "./node_modules/daisyui/dist/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui")
  ],
  safelist: [
    // Classes for the floating chat component
    'fixed',
    'bottom-5', 'right-5',
    'z-\\[9999\\]',
    'bg-gradient-to-r',
    'from-violet-600', 'to-purple-600',
    'text-white',
    'rounded-full',
    'w-16', 'h-16', 'w-14', 'h-14',
    'flex', 'items-center', 'justify-center',
    'cursor-pointer',
    'shadow-xl', 'hover:shadow-2xl',
    'transition-all', 'duration-300',
    'animate-pulse',
    'flex-shrink-0',
    'w-8', 'h-8', 'w-6', 'h-6', 'w-4', 'h-4',
    'w-3', 'h-3',
    'p-1', 'p-4',
    'space-x-2',
    'bg-green-400',
    'border-2',
    'border-white',
    'absolute',
    'top-1', 'right-1',
    'bg-gradient-to-b',
    'from-violet-50', 'to-purple-50',
    'backdrop-blur-sm',
    'whitespace-nowrap',
    'flex-shrink-0',
    'overflow-x-auto',
    'pb-2'
  ],
  daisyui: {
    themes: ["light", "dark", "cupcake", "bumblebee", "emerald", "corporate", "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"],
  },
}