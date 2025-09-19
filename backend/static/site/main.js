// Matrix Code Rain Animation
function initMatrixRain() {
  const canvas = document.getElementById('matrix-canvas');
  if (!canvas) {
    console.log('Matrix canvas not found, skipping matrix rain effect');
    return;
  }
  const ctx = canvas.getContext('2d');

  // Set canvas size
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // Matrix characters (mix of code symbols, binary, Japanese katakana, and programming symbols)
  const matrixChars = "01アカサタナハマヤラワガザダバパイキシチニヒミリギジヂビピウクスツヌフムユルグズヅブプエケセテネヘメレゲゼデベペオコソトノホモヨロゴゾドボポヴッン{}[]();,.<>=+-*/&|^~#@$%!?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  
  const fontSize = 14;
  const columns = Math.floor(canvas.width / fontSize);
  
  // Initialize drops array
  const drops = [];
  for (let i = 0; i < columns; i++) {
    drops[i] = Math.floor(Math.random() * canvas.height / fontSize);
  }

  // Draw matrix rain
  function drawMatrix() {
    // Much more transparent black background for very subtle trail effect
    ctx.fillStyle = 'rgba(0, 0, 0, 0.15)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Very subtle green, much more transparent
    ctx.fillStyle = 'rgba(0, 255, 65, 0.1)';
    ctx.font = fontSize + 'px monospace';

    // Draw characters - much fewer of them
    for (let i = 0; i < drops.length; i++) {
      // Only draw characters occasionally to make it very sparse
      if (Math.random() > 0.98) {
        const char = matrixChars[Math.floor(Math.random() * matrixChars.length)];
        ctx.fillText(char, i * fontSize, drops[i] * fontSize);
      }

      // Reset drop to top after reaching bottom, with much more random delay
      if (drops[i] * fontSize > canvas.height && Math.random() > 0.992) {
        drops[i] = 0;
      }
      
      // Move drop down slower
      if (Math.random() > 0.7) {
        drops[i]++;
      }
    }
  }

  // Start animation - slower refresh rate
  setInterval(drawMatrix, 100);
}

// Enhanced UI Elements & Animations
document.addEventListener('DOMContentLoaded', () => {
  // Initialize Matrix Rain
  initMatrixRain();

  // Initialize floating particles background if present
  const bgParticles = document.querySelector('.bg-particles');
  if (bgParticles) {
    const count = parseInt(bgParticles.getAttribute('data-count') || '30', 10);
    const w = window.innerWidth;
    const h = window.innerHeight;
    for (let i = 0; i < count; i++) {
      const dot = document.createElement('span');
      dot.className = 'bg-particle';
      dot.style.left = Math.random() * w + 'px';
      dot.style.top = Math.random() * h + 'px';
      dot.style.animationDuration = (8 + Math.random() * 12) + 's';
      dot.style.animationDelay = (-Math.random() * 10) + 's';
      dot.style.transform = `scale(${0.6 + Math.random()*1.2})`;
      bgParticles.appendChild(dot);
    }
  }
  // Create scroll progress indicator
  const scrollProgress = document.createElement('div');
  scrollProgress.className = 'scroll-progress';
  const progressBar = document.createElement('div');
  progressBar.className = 'scroll-progress-bar';
  scrollProgress.appendChild(progressBar);
  document.body.appendChild(scrollProgress);

  // Create floating action buttons
  const floatingActions = document.createElement('div');
  floatingActions.className = 'floating-actions';
  
  const scrollToTopBtn = document.createElement('button');
  scrollToTopBtn.className = 'floating-btn scroll-to-top';
  scrollToTopBtn.innerHTML = '<i class="uil uil-arrow-up"></i>';
  scrollToTopBtn.title = 'Scroll to Top';
  
  const themeToggle = document.createElement('button');
  themeToggle.className = 'floating-btn theme-toggle';
  themeToggle.innerHTML = '<i class="uil uil-moon"></i>';
  themeToggle.title = 'Toggle Theme';
  
  floatingActions.appendChild(scrollToTopBtn);
  floatingActions.appendChild(themeToggle);
  document.body.appendChild(floatingActions);

  // Create cursor elements
  const cursor = document.createElement('div');
  const cursorTrail = document.createElement('div');
  cursor.className = 'cursor';
  cursorTrail.className = 'cursor-trail';
  document.body.appendChild(cursor);
  document.body.appendChild(cursorTrail);

  // Mouse movement handler
  document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX - 10 + 'px';
    cursor.style.top = e.clientY - 10 + 'px';
    
    setTimeout(() => {
      cursorTrail.style.left = e.clientX - 4 + 'px';
      cursorTrail.style.top = e.clientY - 4 + 'px';
    }, 100);
  });

  // Hover effects
  const hoverElements = document.querySelectorAll('a, button, .work-card, .nav-link');
  hoverElements.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.style.transform = 'scale(1.5)';
      cursor.style.background = 'rgba(220, 38, 127, 1)';
    });
    el.addEventListener('mouseleave', () => {
      cursor.style.transform = 'scale(1)';
      cursor.style.background = 'rgba(220, 38, 127, 0.8)';
    });
  });
});

// Scroll Animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, observerOptions);

// Load skills data dynamically
async function loadSkillsData() {
  try {
    const response = await fetch('/api/skills/');
    if (!response.ok) {
      throw new Error('Failed to fetch skills data');
    }
    const skillsData = await response.json();

    const skillsTabs = document.getElementById('skills-tabs');
    const skillsContent = document.getElementById('skills-content');
    
    if (!skillsTabs || !skillsContent) return;

    // Group skills by category
    const skillsByCategory = {};
    skillsData.forEach(skill => {
      if (!skillsByCategory[skill.category]) {
        skillsByCategory[skill.category] = [];
      }
      skillsByCategory[skill.category].push(skill);
    });

    // Clear existing content
    skillsTabs.innerHTML = '';
    skillsContent.innerHTML = '';

    // Create tabs and content for each category
    let isFirst = true;
    Object.entries(skillsByCategory).forEach(([category, skills]) => {
      // Create tab
      const tab = document.createElement('div');
      tab.className = `skills-header ${isFirst ? 'skills-active' : ''}`;
      tab.setAttribute('data-target', `#${category}`);
      
      // Set icon based on category
      let iconClass = 'uil uil-cog';
      if (category === 'language') iconClass = 'uil uil-brackets-curly';
      else if (category === 'framework') iconClass = 'uil uil-server-network';
      else if (category === 'tool') iconClass = 'uil uil-swatchbook';
      
      tab.innerHTML = `
        <i class="${iconClass} skills-icon"></i>
        <div>
          <h1 class="skills-title">${category.charAt(0).toUpperCase() + category.slice(1)}</h1>
          <span class="skills-subtitle">${skills.length} skills</span>
        </div>
        <i class="uil uil-angle-down skills-arrow"></i>
      `;
      
      skillsTabs.appendChild(tab);

      // Create content
      const content = document.createElement('div');
      content.className = `skills-group ${isFirst ? 'skills-active' : ''}`;
      content.setAttribute('data-content', '');
      content.id = category;
      
      const skillsList = document.createElement('div');
      skillsList.className = 'skills-list grid';
      
      skills.forEach(skill => {
        const skillItem = document.createElement('div');
        skillItem.className = 'skills-data';
        skillItem.innerHTML = `
          <div class="skills-titles">
            <h3 class="skills-name">${skill.name}</h3>
            <span class="skills-number">${skill.level}%</span>
          </div>
          <div class="skills-bar">
            <span class="skills-percentage" style="width: ${skill.level}%"></span>
          </div>
        `;
        skillsList.appendChild(skillItem);
      });
      
      content.appendChild(skillsList);
      skillsContent.appendChild(content);
      
      isFirst = false;
    });

    // Add click event listeners to tabs
    const tabs = skillsTabs.querySelectorAll('.skills-header');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target);
        skillsContent.querySelectorAll('.skills-group').forEach(c => c.classList.remove('skills-active'));
        if (target) target.classList.add('skills-active');
        tabs.forEach(t => t.classList.remove('skills-active'));
        tab.classList.add('skills-active');
      });
    });

  } catch (error) {
    console.error('Error loading skills data:', error);
    const skillsTabs = document.getElementById('skills-tabs');
    const skillsContent = document.getElementById('skills-content');
    if (skillsTabs && skillsContent) {
      skillsTabs.innerHTML = '<div class="skills-header skills-active"><h1 class="skills-title">Skills</h1><span class="skills-subtitle">Loading...</span></div>';
      skillsContent.innerHTML = '<div class="skills-group skills-active"><div class="skills-list grid"><p>Unable to load skills data. Please try again later.</p></div></div>';
    }
  }
}

// Observe elements for scroll animations - Enhanced for entire site
document.addEventListener('DOMContentLoaded', () => {
  // Load dynamic data
  loadSkillsData();
  const animateElements = document.querySelectorAll(
    '.work-card, .skills-data, .section-title, .about-box, .about-img, .about-heading, .about-description, ' +
    '.timeline-item, .services-content, .testimonial-card, .contact-card, .contact-form, ' +
    '.footer-title, .footer-subtitle, .footer-links, .qualification-title, .skills-header'
  );
  
  animateElements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(50px)';
    el.style.transition = `opacity 0.8s ease ${index * 0.1}s, transform 0.8s ease ${index * 0.1}s`;
    observer.observe(el);
  });

  // Add stagger animation delay for elements in the same section
  const sections = document.querySelectorAll('.section');
  sections.forEach(section => {
    const sectionElements = section.querySelectorAll('.work-card, .skills-data, .about-box');
    sectionElements.forEach((el, index) => {
      el.style.transitionDelay = `${index * 0.2}s`;
    });
  });
});

// Enhanced scrolling effects with progress indicator
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const scrollPercentage = (scrolled / maxScroll) * 100;

  // Update scroll progress bar
  const progressBar = document.querySelector('.scroll-progress-bar');
  if (progressBar) {
    progressBar.style.width = scrollPercentage + '%';
  }

  // Show/hide scroll to top button
  const scrollToTopBtn = document.querySelector('.scroll-to-top');
  if (scrollToTopBtn) {
    if (scrolled > 300) {
      scrollToTopBtn.style.opacity = '1';
      scrollToTopBtn.style.visibility = 'visible';
    } else {
      scrollToTopBtn.style.opacity = '0';
      scrollToTopBtn.style.visibility = 'hidden';
    }
  }

  // Parallax scrolling effect
  const parallaxElements = document.querySelectorAll('.section::before, .section::after');
  parallaxElements.forEach((element, index) => {
    const speed = 0.5 + (index * 0.1);
    element.style.transform = `translateY(${scrolled * speed}px)`;
  });

  // Keep sidebar fixed - remove floating effect
  // Sidebar should stay static for better UX

  // Subtle navigation links animation based on scroll
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach((link, index) => {
    link.style.transform = `translateY(${Math.sin(scrolled * 0.01 + index) * 2}px)`;
  });

  // Add active section highlighting
  const sections = document.querySelectorAll('.section');
  const navItems = document.querySelectorAll('.nav-link');
  
  sections.forEach((section, index) => {
    const rect = section.getBoundingClientRect();
    if (rect.top <= 100 && rect.bottom >= 100) {
      navItems.forEach(item => item.classList.remove('active-link'));
      if (navItems[index]) {
        navItems[index].classList.add('active-link');
      }
    }
  });
});

// Add dynamic background particles that respond to mouse movement
document.addEventListener('mousemove', (e) => {
  const mouseX = e.clientX / window.innerWidth;
  const mouseY = e.clientY / window.innerHeight;
  
  const backgroundElements = document.querySelectorAll('.section::after');
  backgroundElements.forEach((element, index) => {
    const moveX = (mouseX - 0.5) * 20 * (index + 1);
    const moveY = (mouseY - 0.5) * 20 * (index + 1);
    element.style.transform += ` translate(${moveX}px, ${moveY}px)`;
  });
});

// Enhanced typing effect for titles
function typeWriter(element, text, speed = 100) {
  let i = 0;
  element.innerHTML = '';
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  type();
}

// Apply typing effect to main title when page loads
document.addEventListener('DOMContentLoaded', () => {
  const mainTitle = document.querySelector('.home-title');
  if (mainTitle) {
    const originalText = mainTitle.textContent;
    setTimeout(() => typeWriter(mainTitle, originalText, 80), 1000);
  }

  // Floating button functionality
  const scrollToTopBtn = document.querySelector('.scroll-to-top');
  const themeToggleBtn = document.querySelector('.theme-toggle');
  
  if (scrollToTopBtn) {
    scrollToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
    // Initially hide scroll to top button
    scrollToTopBtn.style.opacity = '0';
    scrollToTopBtn.style.visibility = 'hidden';
    scrollToTopBtn.style.transition = 'all 0.3s ease';
  }
  
  if (themeToggleBtn) {
    let isDarkMode = true;
    themeToggleBtn.addEventListener('click', () => {
      document.body.classList.toggle('light-theme');
      isDarkMode = !isDarkMode;
      themeToggleBtn.innerHTML = isDarkMode ? 
        '<i class="uil uil-moon"></i>' : 
        '<i class="uil uil-sun"></i>';
    });
  }

  // Add gradient text effect to titles
  const titles = document.querySelectorAll('.home-title, .about-heading');
  titles.forEach(title => {
    title.classList.add('gradient-text');
  });
});

// Toggling Skill Tabs
const tabs = document.querySelectorAll('[data-target]');
const tabContent = document.querySelectorAll('[data-content]');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(tab.dataset.target);
    tabContent.forEach(c => c.classList.remove('skills-active'));
    if (target) target.classList.add('skills-active');
    tabs.forEach(t => t.classList.remove('skills-active'));
    tab.classList.add('skills-active');
  });
});

// MixItUp Sorting
if (window.mixitup) {
  window.mixitup('.work-container', {
    selectors: { target: '.work-card' },
    animation: { duration: 300 },
  });
}

// Active link changing
const linkWork = document.querySelectorAll('.work-item');
function activeWork() { linkWork.forEach(l => l.classList.remove('active-work')); this.classList.add('active-work'); }
linkWork.forEach(l => l.addEventListener('click', activeWork));

// Portfolio Popup
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('work-button')) {
    togglePortfolioPopup();
    portfolioItemDetails(e.target.parentElement);
  }
});
function togglePortfolioPopup() { document.querySelector('.portfolio-popup').classList.toggle('open'); }
const popupClose = document.querySelector('.portfolio-popup-close');
if (popupClose) popupClose.addEventListener('click', togglePortfolioPopup);
function portfolioItemDetails(portfolioItem) {
  const thumb = document.querySelector('.pp-thumbnail img');
  const subtitle = document.querySelector('.portfolio-popup-subtitle span');
  const body = document.querySelector('.portfolio-popup-body');
  if (!portfolioItem || !thumb || !subtitle || !body) return;
  const img = portfolioItem.querySelector('.work-img');
  const title = portfolioItem.querySelector('.work-title');
  const details = portfolioItem.querySelector('.portfolio-item-details');
  if (img) thumb.src = img.src;
  if (title) subtitle.innerHTML = title.innerHTML;
  if (details) body.innerHTML = details.innerHTML;
}

// Services Popup
const modalViews = document.querySelectorAll('.services-modal');
const modelBtns = document.querySelectorAll('.services-button');
const modalCloses = document.querySelectorAll('.services-modal-close');
const openModal = (i) => modalViews[i].classList.add('active-modal');
modelBtns.forEach((btn, i) => btn.addEventListener('click', () => openModal(i)));
modalCloses.forEach((close) => close.addEventListener('click', () => modalViews.forEach((v) => v.classList.remove('active-modal'))));

// Swiper Testimonial
if (window.Swiper) {
  new Swiper('.testimonials-container', {
    spaceBetween: 24,
    loop: true,
    grabCursor: true,
    pagination: { el: '.swiper-pagination', clickable: true },
    breakpoints: { 576: { slidesPerView: 2 }, 768: { slidesPerView: 2, spaceBetween: 48 } },
  });
}

// Input Animation
const inputs = document.querySelectorAll('.input');
function focusFunc() { this.parentNode.classList.add('focus'); }
function blurFunc() { if (this.value === '') this.parentNode.classList.remove('focus'); }
inputs.forEach((input) => { input.addEventListener('focus', focusFunc); input.addEventListener('blur', blurFunc); });


// Activating Sidebar
const navMenu = document.getElementById('sidebar');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');
if (navToggle) navToggle.addEventListener('click', () => navMenu.classList.add('show-sidebar'));
if (navClose) navClose.addEventListener('click', () => navMenu.classList.remove('show-sidebar'));

// Scroll Section Active Link
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  const scrollY = window.pageYOffset;
  sections.forEach((current) => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 50;
    const sectionId = current.getAttribute('id');
    const link = document.querySelector('.nav-menu a[href*=' + CSS.escape(sectionId) + ']');
    if (!link) return;
    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) link.classList.add('active-link');
    else link.classList.remove('active-link');
  });
});
