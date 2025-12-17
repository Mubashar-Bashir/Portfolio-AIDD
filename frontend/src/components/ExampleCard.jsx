import React from 'react';

const ExampleCard = ({ title, children, image, actions, bordered = true, compact = false }) => {
  const cardClasses = `card ${bordered ? 'border border-base-200' : ''} bg-base-100 shadow-xl`;
  const bodyClasses = `card-body ${compact ? 'p-4' : 'p-6'}`;

  return (
    <div className={cardClasses}>
      {image && (
        <figure className="px-4 pt-4">
          <img src={image} alt={title} className="rounded-xl object-cover w-full" />
        </figure>
      )}
      <div className={bodyClasses}>
        {title && <h2 className="card-title">{title}</h2>}
        <div className="card-content">
          {children}
        </div>
        {actions && (
          <div className="card-actions justify-end">
            {actions}
          </div>
        )}
      </div>
    </div>
  );
};

export default ExampleCard;