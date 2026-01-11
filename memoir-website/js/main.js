/* 
 * MEMOIR Main Application Logic 
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // Initialize Locomotive Scroll
    const scroll = new LocomotiveScroll({
        el: document.querySelector('[data-scroll-container]'),
        smooth: true,
        multiplier: 1,
        lerp: 0.1, // Linear interpolation (smoothness)
        tablet: { smooth: true },
        smartphone: { smooth: true }
    });

    // GSAP ScrollTrigger Proxy for Locomotive Scroll
    gsap.registerPlugin(ScrollTrigger);

    scroll.on('scroll', ScrollTrigger.update);

    ScrollTrigger.scrollerProxy('[data-scroll-container]', {
        scrollTop(value) {
            return arguments.length ? scroll.scrollTo(value, 0, 0) : scroll.scroll.instance.scroll.y;
        },
        getBoundingClientRect() {
            return {top: 0, left: 0, width: window.innerWidth, height: window.innerHeight};
        },
        pinType: document.querySelector('[data-scroll-container]').style.transform ? "transform" : "fixed"
    });

    // Refresh ScrollTrigger when window updates
    ScrollTrigger.addEventListener('refresh', () => scroll.update());
    ScrollTrigger.refresh();

    // Navigation Logic
    const navLinks = document.querySelectorAll('[data-scroll-to]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const target = document.querySelector(targetId);
            if (target) {
                scroll.scrollTo(target);
            }
        });
    });

    // Navbar transparency on scroll
    scroll.on('scroll', (args) => {
        const nav = document.querySelector('.main-nav');
        if (args.scroll.y > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // Button interactions
    const buttons = document.querySelectorAll('.btn-primary, .btn-secondary, .btn-black');
    buttons.forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            gsap.to(btn, { scale: 1.05, duration: 0.3, ease: 'power1.out' });
        });
        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, { scale: 1, duration: 0.3, ease: 'power1.out' });
        });
    });

    // Hero CTA - scroll to pricing section
    const heroCta = document.getElementById('hero-cta');
    if (heroCta) {
        heroCta.addEventListener('click', () => {
            const pricingSection = document.getElementById('pricing');
            if (pricingSection) {
                scroll.scrollTo(pricingSection);
            }
        });
    }

    // Gallery Modal (Simplified for prototype)
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            // Future implementation: Open modal with full details
            console.log('Open gallery item details');
        });
    });
});

