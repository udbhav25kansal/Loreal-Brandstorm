/* 
 * MEMOIR GSAP Animations 
 */

gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', () => {
    
    // Animate Hero Content
    gsap.from('.hero-content', {
        duration: 1.5,
        y: 50,
        opacity: 0,
        ease: 'power3.out',
        delay: 0.5
    });

    // Animate Section Titles
    gsap.utils.toArray('.section-title').forEach(title => {
        gsap.from(title, {
            scrollTrigger: {
                trigger: title,
                start: 'top 80%',
                scroller: '[data-scroll-container]' // For Locomotive Scroll compatibility
            },
            y: 30,
            opacity: 0,
            duration: 1,
            ease: 'power2.out'
        });
    });

    // Staggered Animation for Pillars
    gsap.from('.pillar-card', {
        scrollTrigger: {
            trigger: '.pillars-grid',
            start: 'top 75%',
            scroller: '[data-scroll-container]'
        },
        y: 50,
        opacity: 0,
        duration: 1,
        stagger: 0.2,
        ease: 'back.out(1.7)'
    });

    // Process Steps
    gsap.from('.step-card', {
        scrollTrigger: {
            trigger: '.process-steps',
            start: 'top 70%',
            scroller: '[data-scroll-container]'
        },
        y: 50,
        opacity: 0,
        duration: 1,
        stagger: 0.3,
        ease: 'power2.out'
    });

    // Product Visual Parallax
    // Note: data-scroll-speed handles most of this via Locomotive, 
    // but we can add specific triggers here if needed.
});

