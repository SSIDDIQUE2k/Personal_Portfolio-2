// Enhanced Cybersecurity Background Effects

document.addEventListener('DOMContentLoaded', function() {
    console.log('🛡️ Cybersecurity System Initializing...');

    // Matrix Rain Effect
    function createMatrixRain() {
        const matrixChars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZ日本語αβγδεζηθικλμνξοπρστυφχψω';
        const numberOfColumns = Math.floor(window.innerWidth / 20);
        
        for (let i = 0; i < 10; i++) {
            setTimeout(() => {
                const matrixChar = document.createElement('div');
                matrixChar.className = 'matrix-char';
                matrixChar.textContent = matrixChars[Math.floor(Math.random() * matrixChars.length)];
                matrixChar.style.left = Math.random() * 100 + '%';
                matrixChar.style.animationDelay = Math.random() * 6 + 's';
                matrixChar.style.animationDuration = (Math.random() * 4 + 4) + 's';
                document.body.appendChild(matrixChar);
                
                // Remove element after animation
                setTimeout(() => {
                    if (matrixChar.parentNode) {
                        matrixChar.parentNode.removeChild(matrixChar);
                    }
                }, 8000);
            }, i * 200);
        }
    }

    // Threat Alert System
    function createThreatAlert() {
        const threats = [
            'THREAT DETECTED: TROJAN.WIN32',
            'MALWARE BLOCKED',
            'SUSPICIOUS ACTIVITY',
            'PHISHING ATTEMPT BLOCKED',
            'RANSOMWARE PREVENTED',
            'INTRUSION DETECTED',
            'FIREWALL BREACH ATTEMPT',
            'SQL INJECTION BLOCKED',
            'XSS ATTACK PREVENTED',
            'DDoS MITIGATION ACTIVE'
        ];
        
        const threat = document.createElement('div');
        threat.className = 'threat-alert';
        threat.textContent = threats[Math.floor(Math.random() * threats.length)];
        threat.style.left = Math.random() * 70 + '%';
        threat.style.top = Math.random() * 80 + 10 + '%';
        document.body.appendChild(threat);
        
        // Remove after 4 seconds
        setTimeout(() => {
            if (threat.parentNode) {
                threat.parentNode.removeChild(threat);
            }
        }, 4000);
    }

    // Update HUD Status
    function updateHudStatus() {
        const hud = document.querySelector('.cyber-hud');
        if (!hud) return;
        
        const statusMessages = [
            'SCANNING REGISTRY...',
            'ANALYZING NETWORK TRAFFIC',
            'VIRUS SIGNATURE UPDATED',
            'QUARANTINE: 3 THREATS',
            'SYSTEM INTEGRITY: OK',
            'HEURISTIC ANALYSIS...',
            'ROOTKIT SCAN COMPLETE',
            'BEHAVIORAL MONITORING',
            'CLOUD PROTECTION: ACTIVE',
            'THREAT INTELLIGENCE: UPDATED'
        ];
        
        const lastLine = hud.querySelector('.status-line:last-child');
        if (lastLine) {
            lastLine.textContent = statusMessages[Math.floor(Math.random() * statusMessages.length)];
        }
    }

    // Initialize Scanning Beam Animation
    function initScanBeam() {
        const beams = document.querySelectorAll('.scan-beam');
        beams.forEach((beam, index) => {
            beam.style.animationDelay = (index * 2) + 's';
        });
    }

    // Add Multiple Scanning Beams
    function createMultipleBeams() {
        for (let i = 1; i < 3; i++) {
            const beam = document.createElement('div');
            beam.className = 'scan-beam';
            beam.style.animationDelay = (i * 3) + 's';
            beam.style.animationDuration = (5 + i) + 's';
            document.body.appendChild(beam);
        }
    }

    // Add Glitch Effect to Main Title
    function addGlitchEffect() {
        const homeTitle = document.querySelector('.home-title');
        if (homeTitle) {
            homeTitle.classList.add('cyber-glitch');
            homeTitle.setAttribute('data-text', homeTitle.textContent);
        }
    }

    // Cyber Cursor Effect
    function initCyberCursor() {
        const cursor = document.createElement('div');
        cursor.className = 'cyber-cursor';
        cursor.style.cssText = `
            position: fixed;
            width: 20px;
            height: 20px;
            background: var(--primary);
            border-radius: 50%;
            pointer-events: none;
            z-index: 10000;
            mix-blend-mode: screen;
            transition: transform 0.1s;
            box-shadow: 0 0 20px var(--primary);
        `;
        document.body.appendChild(cursor);
        
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX - 10 + 'px';
            cursor.style.top = e.clientY - 10 + 'px';
        });
        
        // Pulse effect on click
        document.addEventListener('click', () => {
            cursor.style.transform = 'scale(2)';
            setTimeout(() => {
                cursor.style.transform = 'scale(1)';
            }, 150);
        });
    }

    // System Boot Sequence
    function systemBootSequence() {
        const bootMessages = [
            'INITIALIZING SECURITY PROTOCOLS...',
            'LOADING THREAT DATABASE...',
            'ACTIVATING REAL-TIME SHIELD...',
            'SYSTEM ONLINE'
        ];
        
        bootMessages.forEach((message, index) => {
            setTimeout(() => {
                console.log(`🔒 ${message}`);
            }, index * 1000);
        });
    }

    // Initialize all effects
    function initializeEffects() {
        systemBootSequence();
        createMultipleBeams();
        initScanBeam();
        addGlitchEffect();
        initCyberCursor();
        
        // Start matrix rain immediately
        createMatrixRain();
        
        // Set intervals for continuous effects (reduced frequency)
        setInterval(createMatrixRain, 15000);
        setInterval(createThreatAlert, 12000);
        setInterval(updateHudStatus, 5000);
        
        // Create initial threat alert
        setTimeout(createThreatAlert, 5000);
    }

    // Start everything
    initializeEffects();
    
    console.log('🛡️ Cybersecurity System Online');
});
