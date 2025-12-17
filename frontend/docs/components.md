---
sidebar_position: 3
---

# Components Guide

This page demonstrates various DaisyUI components that can be used in your documentation.

## Buttons

<div className="flex flex-wrap gap-2">
  <button className="btn">Button</button>
  <button className="btn btn-primary">Primary</button>
  <button className="btn btn-secondary">Secondary</button>
  <button className="btn btn-accent">Accent</button>
  <button className="btn btn-ghost">Ghost</button>
  <button className="btn btn-link">Link</button>
</div>

## Alerts

<div className="space-y-4">
  <div className="alert alert-info">
    <div>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="stroke-current flex-shrink-0 w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
      <span>Info: This is an info alert.</span>
    </div>
  </div>
  <div className="alert alert-success">
    <div>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="stroke-current flex-shrink-0 w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
      <span>Success: This is a success alert.</span>
    </div>
  </div>
  <div className="alert alert-warning">
    <div>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="stroke-current flex-shrink-0 w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
      <span>Warning: This is a warning alert.</span>
    </div>
  </div>
  <div className="alert alert-error">
    <div>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="stroke-current flex-shrink-0 w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
      <span>Error: This is an error alert.</span>
    </div>
  </div>
</div>

## Cards

<div className="grid grid-cols-1 md:grid-cols-2 gap-4">
  <div className="card bg-base-100 shadow-xl">
    <div className="card-body">
      <h2 className="card-title">Card Title</h2>
      <p>Rearrange your thoughts. You can do it with Docusaurus.</p>
      <div className="card-actions justify-end">
        <button className="btn btn-primary">Buy Now</button>
      </div>
    </div>
  </div>
  <div className="card bg-primary text-primary-content">
    <div className="card-body">
      <h2 className="card-title">Colored Card!</h2>
      <p>Rearrange your thoughts. You can do it with Docusaurus.</p>
      <div className="card-actions justify-end">
        <button className="btn">Try it</button>
      </div>
    </div>
  </div>
</div>