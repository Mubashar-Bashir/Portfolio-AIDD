---
name: docusaurus
description: Comprehensive Docusaurus site development, configuration, and content management. Use when Claude needs to work with Docusaurus documentation sites for: (1) Creating new documentation sites, (2) Customizing themes and layouts, (3) Managing content structure, (4) Configuring plugins and features, (5) Deploying and maintaining sites
---

# Docusaurus Skill

## Purpose
This skill provides comprehensive support for Docusaurus site development, configuration, and content management. It enables efficient creation and maintenance of documentation sites with proper structure, theming, and functionality.

## When to Use This Skill
- Creating new Docusaurus documentation sites
- Customizing existing Docusaurus themes and layouts
- Managing documentation content structure and navigation
- Configuring Docusaurus plugins and features
- Troubleshooting Docusaurus site issues
- Optimizing Docusaurus sites for performance and SEO

## Core Capabilities

### Site Creation
- Initialize new Docusaurus projects with recommended configurations
- Set up proper directory structure for documentation content
- Configure essential plugins (search, sitemap, gtag, etc.)

### Theme Customization
- Modify CSS and styling to match brand requirements
- Create custom layout components
- Implement responsive design patterns

### Content Management
- Organize documentation in logical structure
- Create and maintain navigation sidebars
- Implement content versioning strategies

### Plugin Configuration
- Set up Algolia search or local search
- Configure Google Analytics and other tracking
- Add custom remark/rehype plugins

## Key Commands and Patterns

### Project Initialization
```bash
npx create-docusaurus@latest my-website classic
```

### Common Configuration Files
- `docusaurus.config.js` - Main site configuration
- `sidebars.js` - Navigation structure
- `static/` - Static assets
- `src/` - Custom components and pages

## Best Practices
- Use modular content organization
- Implement consistent navigation patterns
- Optimize for search engine visibility
- Ensure mobile-responsive design
- Maintain accessibility standards (WCAG)

## Common Use Cases

### Creating Documentation Pages
- Organize content in logical hierarchy
- Use appropriate markdown features (admonitions, code tabs, etc.)
- Link related documentation sections

### Custom Components
- Create reusable components in `src/components/`
- Use Docusaurus theme APIs for proper integration
- Ensure components work with swizzling

### Deployment Preparation
- Configure deployment settings in docusaurus.config.js
- Optimize for performance (code splitting, lazy loading)
- Set up custom domains and SSL certificates

## References
- See [DOCS_GUIDE.md](DOCS_GUIDE.md) for comprehensive documentation patterns
- See [THEME_CUSTOMIZATION.md](THEME_CUSTOMIZATION.md) for theme modification techniques
- See [PLUGIN_INTEGRATION.md](PLUGIN_INTEGRATION.md) for plugin configuration patterns