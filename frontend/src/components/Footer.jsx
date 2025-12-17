import React from 'react';
import Link from '@docusaurus/Link';

const Footer = () => {
  const footerLinks = {
    docs: [
      { label: 'Tutorial', path: '/docs/intro' },
      { label: 'Test Tailwind', path: '/docs/test-tailwind' },
    ],
    community: [
      { label: 'Stack Overflow', href: 'https://stackoverflow.com/questions/tagged/docusaurus' },
      { label: 'Discord', href: 'https://discordapp.com/invite/docusaurus' },
      { label: 'Twitter', href: 'https://twitter.com/docusaurus' },
    ],
    social: [
      { label: 'GitHub', href: 'https://github.com/facebook/docusaurus' },
      { label: 'LinkedIn', href: '#' },
    ],
  };

  return (
    <footer className="footer bg-base-200 text-base-content p-10">
      <div className="container mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <span className="footer-title">Docs</span>
            <ul>
              {footerLinks.docs.map((link, index) => (
                <li key={index}>
                  <Link to={link.path} className="link link-hover">
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <span className="footer-title">Community</span>
            <ul>
              {footerLinks.community.map((link, index) => (
                <li key={index}>
                  <a href={link.href} className="link link-hover" target="_blank" rel="noopener noreferrer">
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <span className="footer-title">Social</span>
            <ul>
              {footerLinks.social.map((link, index) => (
                <li key={index}>
                  <a href={link.href} className="link link-hover" target="_blank" rel="noopener noreferrer">
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <span className="footer-title">Legal</span>
            <ul>
              <li><a href="#" className="link link-hover">Terms of use</a></li>
              <li><a href="#" className="link link-hover">Privacy policy</a></li>
              <li><a href="#" className="link link-hover">Cookie policy</a></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-base-300 mt-10 pt-6 text-center">
          <p className="text-sm">
            Copyright © {new Date().getFullYear()} My Project, Inc. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;