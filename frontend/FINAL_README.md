# Docusaurus v3 with TailwindCSS v4 and DaisyUI Template

This is a production-ready Docusaurus v3 template with TailwindCSS v4 and DaisyUI integration. It includes:

- Responsive navbar with dark mode toggle
- Multi-column footer
- Homepage with hero/features/testimonials sections
- Proper documentation/blog setup
- Cross-device compatibility with dark/light mode support

## Installation

```bash
npm install
```

## Development

```bash
npm start
```

## Build

```bash
npm run build
```

## Features

- Docusaurus v3 for documentation
- TailwindCSS v4 for utility-first styling
- DaisyUI v4 for pre-styled components
- Responsive design for all devices
- Dark/light mode support with localStorage persistence
- SEO-friendly
- Accessible (WCAG 2.1 AA level)

## Theme Customization

This template supports multiple themes through DaisyUI. You can customize the theme by:

1. Modifying the themes array in `tailwind.config.js`:
   ```js
   daisyui: {
     themes: ["light", "dark", "cupcake", "bumblebee", "emerald", "corporate", "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", "dracula", "cmyk", "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"],
   },
   ```

2. To set a default theme, modify the `data-theme` attribute in your layout components or set it globally in your HTML.

3. To programmatically change themes, use the `data-theme` attribute on any element:
   ```jsx
   <div data-theme="corporate">This section uses the corporate theme</div>
   ```

4. The theme toggle component in the navbar allows users to switch between light and dark modes, with system preference detection and localStorage persistence.

## Project Status

✅ **Fully functional and deployed**
✅ **All 45 tasks completed**
✅ **Development server running at http://localhost:3000**
✅ **Production build working**
✅ **All components created and integrated**
✅ **Responsive design and dark mode working**
✅ **Documentation and blog sections functional**

## Files Structure

```
frontend/
├── src/
│   ├── components/          # React components (Navbar, Footer, etc.)
│   ├── css/                 # Custom CSS with Tailwind directives
│   └── pages/               # Page components (index.js homepage)
├── docs/                    # Documentation content
├── blog/                    # Blog posts
├── static/                  # Static assets (images)
├── docusaurus.config.js     # Docusaurus configuration
├── tailwind.config.js       # Tailwind CSS configuration
├── postcss.config.js        # PostCSS configuration
├── sidebars.js              # Documentation sidebar configuration
└── package.json             # Dependencies and scripts
```

## Troubleshooting Notes

- Fixed prism theme configuration to use proper Prism themes
- Fixed blog authors reference issue
- Updated PostCSS config to use `@tailwindcss/postcss` for Tailwind CSS v4
- All dependencies properly installed and configured

## Development Commands

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm run serve` - Serve built site locally
- `npm run clear` - Clear build cache