# Data Model: Docusaurus Basic Structure for Demo

## Entities

### Documentation Site
- **name**: string - The name/title of the documentation site
- **tagline**: string - Brief description of the site
- **url**: string - Base URL for the site
- **baseUrl**: string - Base path for the site
- **favicon**: string - Path to favicon
- **organizationName**: string - GitHub organization/user name
- **projectName**: string - GitHub repository name
- **themeConfig**: object - Configuration for the site theme

### Navigation Items
- **label**: string - Display text for navigation item
- **to**: string - Destination path
- **position**: string - Position in navigation (left/right)
- **activeBasePath**: string - Base path to determine active state

### Documentation Pages
- **id**: string - Unique identifier for the document
- **title**: string - Title of the document
- **sidebar_label**: string - Label used in sidebar
- **description**: string - Meta description for SEO
- **slug**: string - Custom URL slug (optional)
- **tags**: array - List of tags for the document

### Sidebar Categories
- **type**: string - Type of sidebar item (category or link)
- **label**: string - Display label for the category
- **items**: array - List of child items in the category
- **link**: object - Optional link for the category itself

### Theme Configuration
- **navbar**: object - Navigation bar configuration
- **footer**: object - Footer configuration
- **prism**: object - Code block syntax highlighting configuration
- **colorMode**: object - Color mode settings (light/dark)

## Relationships
- Documentation Site contains multiple Navigation Items
- Documentation Site contains multiple Documentation Pages
- Documentation Pages are organized in Sidebar Categories
- Theme Configuration applies to Documentation Site