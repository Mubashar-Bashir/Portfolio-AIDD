import React from 'react';

const TestimonialsSection = () => {
  const testimonials = [
    {
      quote: "This template has saved us countless hours in setup and configuration. The integration between Docusaurus, TailwindCSS, and DaisyUI is seamless.",
      author: "Alex Johnson",
      role: "Senior Developer",
      avatar: "/img/placeholder-avatar.jpg"
    },
    {
      quote: "The responsive design and dark mode support are perfect for our documentation needs. Our users love the clean, modern interface.",
      author: "Sarah Williams",
      role: "Tech Lead",
      avatar: "/img/placeholder-avatar.jpg"
    },
    {
      quote: "Finally, a documentation template that's both beautiful and functional. The accessibility features are top-notch.",
      author: "Michael Chen",
      role: "Product Manager",
      avatar: "/img/placeholder-avatar.jpg"
    }
  ];

  return (
    <section className="py-16 bg-base-200">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">What People Say</h2>
          <p className="text-xl text-base-content/80 max-w-2xl mx-auto">
            Don't just take our word for it - hear from our satisfied users
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="card bg-base-100 shadow-xl">
              <div className="card-body">
                <div className="rating mb-4">
                  {[...Array(5)].map((_, i) => (
                    <svg key={i} xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-yellow-400" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                  ))}
                </div>
                <p className="text-base-content/80 italic mb-4">"{testimonial.quote}"</p>
                <div className="flex items-center mt-auto">
                  <div className="avatar mr-4">
                    <div className="w-12 h-12 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
                      <img src={testimonial.avatar} alt={testimonial.author} />
                    </div>
                  </div>
                  <div>
                    <h4 className="font-bold">{testimonial.author}</h4>
                    <p className="text-sm text-base-content/60">{testimonial.role}</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TestimonialsSection;