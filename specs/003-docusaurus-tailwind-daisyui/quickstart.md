# Quickstart Guide: Docusaurus v3 with TailwindCSS v4 and DaisyUI Template

## Prerequisites
- Node.js 18+ installed
- npm or yarn package manager

## Setup Instructions

### 1. Clone or Create Project
```bash
# If using as template
npx create-docusaurus@latest my-website classic
cd my-website
```

### 2. Install Dependencies
```bash
npm install -D tailwindcss postcss autoprefixer daisyui
npx tailwindcss init -p
```

### 3. Configure TailwindCSS
Update `tailwind.config.js`:
```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./docs/**/*.{md,mdx}",
    "./blog/**/*.{md,mdx}",
    "./pages/**/*.{md,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "cupcake", "bumblebee", "emerald", "corporate", "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"],
  },
};
```

### 4. Configure PostCSS
Ensure `postcss.config.js` includes:
```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

### 5. Import TailwindCSS
In `src/css/custom.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Additional custom styles can go here */
```

### 6. Configure Docusaurus
Update `docusaurus.config.js` to include the CSS file:
```js
module.exports = {
  // ... other config
  stylesheets: [
    {
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap',
      type: 'text/css',
    },
  ],
  themes: ['@docusaurus/theme-classic'],
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  // ... rest of config
};
```

### 7. Start Development Server
```bash
npm start
```

Your site will start at `http://localhost:3000`.

## Customization

### Adding Components
- Create new components in `src/components/`
- Use DaisyUI classes for styling
- Follow React best practices

### Changing Themes
- Modify the themes array in `tailwind.config.js`
- Use DaisyUI's theme classes in components
- Implement theme toggle functionality

### Adding Pages
- Create new pages in `src/pages/`
- Use Tailwind and DaisyUI classes
- Follow responsive design principles

## Deployment
- Build for production: `npm run build`
- Deploy the `build/` folder to your hosting platform (GitHub Pages, Vercel, etc.)