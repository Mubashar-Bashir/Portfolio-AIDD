import React from 'react';
import Link from '@docusaurus/Link';

const CTASection = () => {
  return (
    <section className="py-16 bg-primary text-primary-content">
      <div className="container mx-auto px-4 text-center">
        <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Get Started?</h2>
        <p className="text-xl mb-10 max-w-2xl mx-auto">
          Join thousands of developers who are already using our template to create beautiful documentation sites.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link to="/docs/intro" className="btn btn-accent btn-lg text-accent-content">
            View Documentation
          </Link>
          <Link to="https://github.com" className="btn btn-outline btn-lg text-accent-content border-accent-content/50 hover:bg-accent/10">
            View on GitHub
          </Link>
        </div>
      </div>
    </section>
  );
};

export default CTASection;