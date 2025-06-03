#!/bin/zsh

# Create GitHub issues for Vagabond Engineer Development Plan

# Phase 1: MVP Website
gh issue create --title "Set up Wagtail project" --body "Create a new Wagtail project using \`wagtail start\`. Use \`uv\` for environment management and \`git init\` to initialize the repository."
gh issue create --title "Create HomePage model" --body "Define a HomePage model with introductory content."
gh issue create --title "Create AboutPage model" --body "Define an AboutPage model for static content."
gh issue create --title "Create ContactPage model" --body "Follow Wagtail's contact form tutorial to create a basic contact page."
gh issue create --title "Create BlogIndexPage model" --body "Create a BlogIndexPage model to serve as the blog landing page."
gh issue create --title "Create BlogPage model" --body "Create a BlogPage model with title, date, rich text body, tags, and categories."
gh issue create --title "Set up tags and categories" --body "Create a Category model and add ClusterTaggableManager for tags on BlogPage."
gh issue create --title "Add sample blog posts" --body "Write at least two blog posts with text and inline images using the RichTextField."
gh issue create --title "Add content to Home, About, and Contact pages" --body "Populate initial page content for testing."
gh issue create --title "Test site locally" --body "Run the local development server and test all pages."
gh issue create --title "Prepare for deployment to Fly.io" --body "Set up Dockerfile, fly.toml, and PostgreSQL configuration."
gh issue create --title "Deploy site to Fly.io" --body "Deploy the Wagtail site to Fly.io and verify it's online."

# Phase 2: Tailwind CSS Integration
gh issue create --title "Install Tailwind CSS via npm" --body "Install Tailwind and PostCSS via npm for styling."
gh issue create --title "Configure Tailwind and PostCSS" --body "Create tailwind.config.js and postcss.config.js for processing CSS."
gh issue create --title "Create base Tailwind CSS file" --body "Add @tailwind directives in a static CSS file."
gh issue create --title "Set up build script in package.json" --body "Add a script to build the Tailwind CSS output."
gh issue create --title "Generate and link styles.css in templates" --body "Ensure generated CSS is linked in templates."
gh issue create --title "Refine blog layout and typography" --body "Apply Tailwind classes for better typography and layout."
gh issue create --title "Style navigation, footer, and page sections" --body "Use Tailwind to style header, footer, and page sections."
gh issue create --title "Add responsive design features" --body "Use Tailwind's responsive utilities for mobile-friendly layout."

# Phase 3: Enhancements
gh issue create --title "Add structured content with StreamField" --body "Create ImageWithCaptionBlock for blog posts and migrate as needed."
gh issue create --title "Add SEO improvements" --body "Add meta tags, Open Graph data, and improve SEO."
gh issue create --title "Add branding (favicon, logo)" --body "Add a favicon and a custom logo for the site."
gh issue create --title "Optimize performance (minify CSS, caching)" --body "Set up CSS minification and caching strategies."
gh issue create --title "Add analytics (Plausible or Google Analytics)" --body "Integrate analytics tracking."