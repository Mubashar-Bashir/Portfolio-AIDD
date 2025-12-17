# Data Model: Docusaurus v3 with TailwindCSS v4 and DaisyUI Template

## Components

### Navbar Component
- **Props**:
  - `logo` (string): Path to logo image
  - `navItems` (array): Navigation items with label and URL
  - `darkMode` (boolean): Current theme state
- **State**:
  - `mobileMenuOpen` (boolean): Mobile menu visibility
  - `darkMode` (boolean): Theme state

### Footer Component
- **Props**:
  - `footerLinks` (object): Links grouped by category
  - `socialLinks` (array): Social media links
  - `copyrightText` (string): Copyright information
- **State**: None

### Hero Section Component
- **Props**:
  - `title` (string): Main headline
  - `subtitle` (string): Supporting text
  - `ctaButtons` (array): Call-to-action buttons
- **State**: None

### Features Section Component
- **Props**:
  - `features` (array): Feature items with title, description, and icon
- **State**: None

### Testimonials Section Component
- **Props**:
  - `testimonials` (array): Testimonial items with quote, author, and avatar
- **State**: None

## Configuration Files

### docusaurus.config.js
- **Site Metadata**: Title, tagline, URL, base URL
- **Themes**: Preset configuration for docs, blog, pages
- **Plugins**: Additional functionality
- **Theme Config**: Navigation, footer, color mode

### tailwind.config.js
- **Theme**: Color palette, spacing, typography
- **Plugins**: DaisyUI plugin with themes
- **Content**: File paths for Tailwind to scan

### postcss.config.js
- **Plugins**: TailwindCSS and autoprefixer

## Page Structure

### Homepage (index.js)
- **Sections**: Hero, Features, Testimonials, CTA
- **Layout**: Responsive grid using Tailwind classes
- **Components**: Imported modular components

### Documentation Pages
- **Structure**: MDX files in docs/ directory
- **Layout**: Docusaurus documentation layout
- **Styling**: Tailwind and DaisyUI classes

### Blog Pages
- **Structure**: MDX files in blog/ directory
- **Layout**: Docusaurus blog layout
- **Styling**: Tailwind and DaisyUI classes

## Theme System

### Dark Mode
- **Storage**: localStorage for theme persistence
- **Default**: System preference detection
- **Switching**: Toggle button with smooth transition
- **Themes**: Light, dark, and additional DaisyUI themes