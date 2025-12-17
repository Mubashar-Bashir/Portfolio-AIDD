# Quickstart Guide: Docusaurus ChatKit Integration Package

## Overview
This package provides a ready-made Docusaurus setup with integrated ChatKit UI component, combining book content structure with chatbot functionality in a single frontend application.

## Prerequisites
- Node.js (v16 or higher)
- npm or yarn package manager
- Basic knowledge of Docusaurus and React

## Installation

### 1. Clone or Download the Package
```bash
# If using as a template
npx create-docusaurus@latest my-book-site classic
cd my-book-site

# Install ChatKit dependencies
npm install @creativecode/chatkit
# Or if using a different ChatKit library, install accordingly
```

### 2. Set up the Project Structure
The package includes the following structure:
```
my-book-site/
├── docs/                 # Book content in markdown format
├── src/
│   ├── components/       # Custom React components
│   │   ├── ChatKit/      # ChatKit UI components
│   │   └── BookContent/  # Book-specific components
│   ├── pages/            # Custom pages
│   └── theme/            # Docusaurus theme customization
├── static/               # Static assets
├── docusaurus.config.js  # Docusaurus configuration
└── package.json          # Project dependencies
```

### 3. Install Dependencies
```bash
npm install
```

## Configuration

### 1. Docusaurus Configuration
Update `docusaurus.config.js` with your site details:

```javascript
// docusaurus.config.js
module.exports = {
  title: 'My Book Title',
  tagline: 'A comprehensive guide',
  url: 'https://your-book-site.com',
  baseUrl: '/',
  organizationName: 'your-org',
  projectName: 'your-book-site',
  // ... other Docusaurus config
};
```

### 2. ChatKit Integration
The ChatKit component is already integrated in the layout. You can customize it by modifying:

- `src/components/ChatKit/ChatKitContainer.jsx` - Main chat container
- `src/components/ChatKit/ChatInterface.jsx` - Chat interface UI
- `src/components/ChatKit/MessageDisplay.jsx` - Message display component

### 3. Book Content Structure
Add your book content to the `docs/` directory following Docusaurus conventions:

```
docs/
├── intro.md
├── chapter-1/
│   ├── getting-started.md
│   └── basic-concepts.md
└── chapter-2/
    ├── advanced-topics.md
    └── conclusion.md
```

Each markdown file should include frontmatter:

```markdown
---
title: Getting Started
sidebar_position: 1
---

# Getting Started

Your book content here...
```

## Running the Development Server

```bash
npm start
```

This command starts a local development server and opens your site in a browser at `http://localhost:3000`.

## Building for Production

```bash
npm run build
```

This command creates a `build/` directory with the static files ready for deployment.

## Deployment

### To GitHub Pages:
```bash
GIT_USER=<your-github-username> npm run deploy
```

### To Vercel:
1. Push your code to a GitHub repository
2. Connect your repository to Vercel
3. Set build command to `npm run build`
4. Set output directory to `build`

### To Netlify:
1. Push your code to a GitHub repository
2. Connect your repository to Netlify
3. Set build command to `npm run build`
4. Set publish directory to `build`

## Customization

### Adding New Book Sections
1. Create new markdown files in the `docs/` directory
2. Add them to the sidebar configuration in `sidebars.js`

### Customizing the ChatKit UI
1. Modify components in `src/components/ChatKit/`
2. Update styles in `src/css/custom.css`
3. Adjust the chat window position and behavior in the component state

### Theming
Customize the look and feel by:
1. Modifying `src/css/custom.css`
2. Adjusting theme settings in `docusaurus.config.js`
3. Overriding Docusaurus theme components in `src/theme/`

## Testing

Run the test suite:
```bash
npm test
```

## Troubleshooting

### ChatKit Component Not Loading
- Ensure all ChatKit dependencies are installed
- Check browser console for JavaScript errors
- Verify component imports in the layout files

### Book Content Not Displaying
- Confirm markdown files are in the correct `docs/` subdirectory
- Check that frontmatter is properly formatted
- Verify sidebar configuration includes your content

### Build Issues
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`
- Ensure Node.js version meets requirements

## Next Steps

1. Add your book content to the `docs/` directory
2. Customize the ChatKit integration for your specific use case
3. Configure the navigation and sidebar in `sidebars.js`
4. Update the site metadata in `docusaurus.config.js`
5. Test the chat functionality with your content