// // scripts.js

// document.addEventListener('DOMContentLoaded', () => {
//     const contactForm = document.getElementById('contact-form');
//     // const formResponse = document.getElementById('form-response');

//     contactForm.addEventListener('submit', function(e) {
//         e.preventDefault();

//         // Collect form data
//         const name = contactForm.name.value.trim();
//         const email = contactForm.email.value.trim();
//         const phone = contactForm.phone.value.trim();
//         // const subject = contactForm.subject.value.trim();
//         const message = contactForm.message.value.trim();

//         // Simple Validation
//         if (!name || !email || !message) {
//             formResponse.style.color = '#e74c3c';
//             formResponse.textContent = 'Please fill in all required fields.';
//             return;
//         }

//         // Email Validation
//         const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         if (!emailRegex.test(email)) {
//             formResponse.style.color = '#e74c3c';
//             formResponse.textContent = 'Please enter a valid email address.';
//             return;
//         }

//         // Simulate form submission (e.g., AJAX request)
//         // For demonstration, we'll use a timeout to mimic server response
//         // formResponse.style.color = '#27ae60';
//         // formResponse.textContent = 'Sending your message...';

//         setTimeout(() => {
//             // Assuming the submission is successful
//             formResponse.textContent = 'Your message has been sent successfully!';
//             contactForm.reset();
//         }, 2000);

//         // Remove the message after 5 seconds
//         setTimeout(() => {
//             formResponse.textContent = '';
//         }, 7000);
//     });
// });


//     document.addEventListener("DOMContentLoaded", function() {
//         const topImage = document.querySelector('.top-image');
//         topImage.addEventListener('load', function() {
//             topImage.classList.add('loaded');
//         });

//         // If the image is already cached, trigger the load event manually
//         if (topImage.complete) {
//             topImage.classList.add('loaded');
//         }
//     });
