import React from 'react';
import Link from '@docusaurus/Link';

const HeroSection = () => {
  return (
    <section className="hero min-h-screen bg-base-200 py-16">
      <div className="container mx-auto px-4 py-16">
        <div className="hero-content text-center">
          <div className="max-w-3xl">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Welcome to Our Documentation
            </h1>
            <p className="text-xl mb-10 text-base-content/80">
              Build modern, accessible, and responsive documentation sites with our Docusaurus template integrated with TailwindCSS and DaisyUI.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/docs/intro" className="btn btn-primary btn-lg">
                Get Started
              </Link>
              <Link to="/docs/test-tailwind" className="btn btn-outline btn-lg">
                View Components
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;