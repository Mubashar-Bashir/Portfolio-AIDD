import React from 'react';

const ExampleModal = ({ isOpen, onClose, title, children, size = 'modal-md' }) => {
  if (!isOpen) return null;

  return (
    <div className="modal modal-open">
      <div className={`modal-box ${size}`}>
        <div className="flex justify-between items-start mb-4">
          {title && <h3 className="font-bold text-lg">{title}</h3>}
          <button
            onClick={onClose}
            className="btn btn-sm btn-circle btn-ghost"
            aria-label="Close modal"
          >
            ✕
          </button>
        </div>
        <div className="py-4">
          {children}
        </div>
        <div className="modal-action">
          <button className="btn btn-ghost" onClick={onClose}>Close</button>
        </div>
      </div>
    </div>
  );
};

export default ExampleModal;