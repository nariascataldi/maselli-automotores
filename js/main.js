/* =============================================
   MASELLI AUTOMOTORES - JavaScript Principal
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {

  // --- Theme Toggle (Day/Night) ---
  const themeToggle = document.querySelectorAll('.theme-toggle');
  const savedTheme = localStorage.getItem('theme') || 'dark';

  function updateThemeColor(theme) {
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = theme === 'dark' ? '#0A1628' : '#ffffff';
  }

  document.body.setAttribute('data-theme', savedTheme);
  updateThemeColor(savedTheme);

  function toggleTheme() {
    const current = document.body.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeColor(next);
  }

  themeToggle.forEach(btn => {
    btn.addEventListener('click', toggleTheme);
  });

  // --- Intro / Preloader ---
  const intro = document.querySelector('.intro');
  if (intro) {
    setTimeout(() => {
      intro.classList.add('hidden');
    }, 1500);
  }

  // --- Mobile Drawer ---
  const hamburger = document.querySelector('.hamburger');
  const drawer = document.querySelector('.mobile-drawer');
  const drawerClose = document.querySelector('.mobile-drawer__close');
  const drawerLinks = document.querySelectorAll('.mobile-drawer__links a');

  if (hamburger && drawer) {
    hamburger.addEventListener('click', () => {
      drawer.classList.add('open');
    });

    drawerClose?.addEventListener('click', () => {
      drawer.classList.remove('open');
    });

    drawerLinks.forEach(link => {
      link.addEventListener('click', () => {
        drawer.classList.remove('open');
      });
    });
  }

  // --- Header scroll effect ---
  const header = document.querySelector('.header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.style.background = 'var(--color-header-bg-scroll)';
      } else {
        header.style.background = 'var(--color-header-bg)';
      }
    });
  }

  // --- Smooth scroll para links internos ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

});
