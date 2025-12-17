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
- Dark/light mode support
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