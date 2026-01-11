/* 
 * MEMOIR 3D Scene 
 * Three.js Implementation for Hero Background
 */

class MemoirScene {
    constructor() {
        this.container = document.getElementById('canvas-container');
        
        // Validate container exists before proceeding
        if (!this.container) {
            console.warn('MemoirScene: canvas-container element not found');
            return;
        }
        
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        
        this.init();
        this.createParticles();
        this.animate();
        
        window.addEventListener('resize', this.onResize.bind(this));
    }

    init() {
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.container.appendChild(this.renderer.domElement);
        
        this.camera.position.z = 5;
        
        // Fog for depth
        this.scene.fog = new THREE.FogExp2(0x000000, 0.05);
    }

    createParticles() {
        const geometry = new THREE.BufferGeometry();
        const count = 2000;
        
        const positions = new Float32Array(count * 3);
        const sizes = new Float32Array(count);
        
        for (let i = 0; i < count; i++) {
            positions[i * 3] = (Math.random() - 0.5) * 15; // x
            positions[i * 3 + 1] = (Math.random() - 0.5) * 15; // y
            positions[i * 3 + 2] = (Math.random() - 0.5) * 15; // z
            
            sizes[i] = Math.random() * 2;
        }
        
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));
        
        // Custom Shader Material for Golden Particles
        const material = new THREE.PointsMaterial({
            size: 0.05,
            color: 0xD4AF37, // Gold
            transparent: true,
            opacity: 0.8,
            blending: THREE.AdditiveBlending
        });
        
        this.particles = new THREE.Points(geometry, material);
        this.scene.add(this.particles);
    }

    animate() {
        requestAnimationFrame(this.animate.bind(this));
        
        const time = Date.now() * 0.0005;
        
        // Gentle rotation
        this.particles.rotation.y = time * 0.1;
        this.particles.rotation.x = time * 0.05;
        
        // Optional: Interactive mouse movement could be added here
        
        this.renderer.render(this.scene, this.camera);
    }

    onResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
}

// Initialize on load
window.addEventListener('load', () => {
    new MemoirScene();
});

