// Cybersecurity Background Effects JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Cybersecurity effects loading...');
    
    // Enhanced Virus Scanner
    function createVirusScan() {
        console.log('Creating virus scan effects...');
        const virusBg = document.querySelector('.bg-virus-scan');
        if (!virusBg) return;
        
        const existingElements = virusBg.querySelectorAll('.scan-beam, .virus-code, .threat-detected, .matrix-char');
        existingElements.forEach(el => el.remove());
        
        // Create multiple scan beams
        for (let i = 0; i < 3; i++) {
            const beam = document.createElement('div');
            beam.className = 'scan-beam';
            beam.style.animationDelay = (i * 1) + 's';
            beam.style.animationDuration = (3 + i * 0.5) + 's';
            virusBg.appendChild(beam);
        }
        
        // Create scrolling code
        const codeSnippets = [
            'SCANNING MEMORY... 47%', 
            'CHECKING REGISTRY...', 
            'ANALYZING NETWORK TRAFFIC',
            'VIRUS SIGNATURE UPDATED',
            'QUARANTINE: 3 THREATS', 
            'SYSTEM INTEGRITY: OK',
            'FIREWALL STATUS: ACTIVE',
            'REAL-TIME SHIELD: ON',
            'SCANNING C:\\WINDOWS\\',
            'HEURISTIC ANALYSIS...',
            'ROOTKIT SCAN COMPLETE',
            'BEHAVIORAL MONITORING',
            'CLOUD PROTECTION: ACTIVE',
            'THREAT INTELLIGENCE: UPDATED'
        ];
        
        // Create regular status codes
        for (let i = 0; i < 35; i++) {
            const code = document.createElement('div');
            code.className = 'virus-code';
            code.textContent = codeSnippets[Math.floor(Math.random() * codeSnippets.length)];
            code.style.left = Math.random() * 90 + '%';
            code.style.animationDelay = Math.random() * 6 + 's';
            code.style.animationDuration = (Math.random() * 3 + 4) + 's';
            virusBg.appendChild(code);
        }
        
        // Create matrix-style falling characters
        const matrixChars = '01ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ';
        for (let i = 0; i < 50; i++) {
            const matrixChar = document.createElement('div');
            matrixChar.className = 'matrix-char';
            matrixChar.textContent = matrixChars[Math.floor(Math.random() * matrixChars.length)];
            matrixChar.style.left = Math.random() * 100 + '%';
            matrixChar.style.animationDelay = Math.random() * 4 + 's';
            matrixChar.style.animationDuration = (Math.random() * 2 + 3) + 's';
            virusBg.appendChild(matrixChar);
        }
        
        // Create threat alerts
        const threats = [
            'THREAT DETECTED: TROJAN.WIN32',
            'MALWARE BLOCKED',
            'SUSPICIOUS ACTIVITY',
            'PHISHING ATTEMPT BLOCKED',
            'RANSOMWARE PREVENTED'
        ];
        
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                const threat = document.createElement('div');
                threat.className = 'threat-detected';
                threat.textContent = threats[Math.floor(Math.random() * threats.length)];
                threat.style.left = Math.random() * 70 + '%';
                threat.style.top = Math.random() * 80 + '%';
                virusBg.appendChild(threat);
                
                // Remove threat after 3 seconds
                setTimeout(() => {
                    if (threat.parentNode) {
                        threat.parentNode.removeChild(threat);
                    }
                }, 3000);
            }, i * 2000);
        }
    }

    // Initialize virus scan effects
    createVirusScan();
    
    // Restart virus scan animation every 15 seconds
    setInterval(() => {
        createVirusScan();
    }, 15000);
});
