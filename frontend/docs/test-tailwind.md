---
sidebar_position: 2
---

# TailwindCSS Test

This page tests that TailwindCSS classes work properly in MDX documentation files.

## Card Component

<div className="card bg-base-100 shadow-xl">
  <div className="card-body">
    <h2 className="card-title">TailwindCSS Working!</h2>
    <p>This card is styled with TailwindCSS and DaisyUI classes.</p>
    <div className="card-actions justify-end">
      <button className="btn btn-primary">Try it</button>
      <button className="btn btn-ghost">Button</button>
    </div>
  </div>
</div>

## Responsive Grid

<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <div className="bg-primary text-primary-content p-4 rounded-lg">
    <h3>Column 1</h3>
    <p>This is responsive content.</p>
  </div>
  <div className="bg-secondary text-secondary-content p-4 rounded-lg">
    <h3>Column 2</h3>
    <p>This is responsive content.</p>
  </div>
  <div className="bg-accent text-accent-content p-4 rounded-lg">
    <h3>Column 3</h3>
    <p>This is responsive content.</p>
  </div>
</div>